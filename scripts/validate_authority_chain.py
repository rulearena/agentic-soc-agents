#!/usr/bin/env python3
"""validate_authority_chain.py — verify cross-agent schema consistency.

Checks (FAIL unless noted):
  C1   Frontmatter parseable
  C2   Required fields present: name, agent_id, seniority, escalates_to, escalates_from
  C2b  Frontmatter field types sane (response_authority dict, *_approval list, etc.)
  C3   agent_id == filename stem
  C4   agent_id unique across repo
  C5   escalates_to (if non-null) resolves to a loaded agent
  C6   escalates_from (if non-null) resolves to a loaded agent
  C7   Reverse consistency: A.escalates_to=B  =>  B.escalates_from==A
  C8   Authority mapping: requires_*_approval  ⊆  escalates_to target's can_approve
  C9   delegates_to forward refs (WARN only)

Exit: 0 = no FAIL; 1 = >=1 FAIL (or missing PyYAML dependency).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("FAIL: missing dependency PyYAML. Install with: python3 -m pip install pyyaml")
    sys.exit(1)

REPO_ROOT = Path(__file__).resolve().parent.parent
CATEGORIES = [
    "triage",
    "detection-engineering",
    "incident-response",
    "threat-intel",
    "governance",
    "purple-team",
]
REQUIRED_FIELDS = ["name", "agent_id", "seniority", "escalates_to", "escalates_from"]
REQUIRES_APPROVAL_RE = re.compile(r"^requires_.*_approval$")


def find_agent_files() -> list[Path]:
    files: list[Path] = []
    for cat in CATEGORIES:
        d = REPO_ROOT / cat
        if not d.exists():
            continue
        for f in sorted(d.glob("*.md")):
            if f.name == "README.md":
                continue
            files.append(f)
    return files


def read_frontmatter(path: Path):
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")
    if not lines or lines[0] != "---":
        raise ValueError("no frontmatter start marker")
    try:
        end = lines.index("---", 1)
    except ValueError:
        raise ValueError("no frontmatter end marker")
    return yaml.safe_load("\n".join(lines[1:end]))


def rel(p: Path) -> str:
    try:
        return str(p.relative_to(REPO_ROOT))
    except ValueError:
        return str(p)


def main() -> int:
    files = find_agent_files()
    agents: dict[str, tuple[Path, dict]] = {}
    fails: list[str] = []
    warns: list[str] = []

    # Pass 1: per-file checks
    for f in files:
        try:
            fm = read_frontmatter(f)
        except Exception as e:
            fails.append(f"{rel(f)}: [C1] frontmatter parse error: {e}")
            continue
        if not isinstance(fm, dict):
            fails.append(f"{rel(f)}: [C1] frontmatter is not a mapping")
            continue

        # C2: required fields present (key must exist; value may be null)
        missing = [k for k in REQUIRED_FIELDS if k not in fm]
        if missing:
            fails.append(f"{rel(f)}: [C2] missing required frontmatter fields: {missing}")

        # C2b: structural type sanity (avoid downstream crashes)
        ra = fm.get("response_authority")
        if ra is not None and not isinstance(ra, dict):
            fails.append(
                f"{rel(f)}: [C2b] response_authority must be a mapping, got {type(ra).__name__}"
            )
        if isinstance(ra, dict):
            for key, val in ra.items():
                if REQUIRES_APPROVAL_RE.match(key) and not isinstance(val, list):
                    fails.append(
                        f"{rel(f)}: [C2b] response_authority.{key} must be a list, "
                        f"got {type(val).__name__}"
                    )
            if "can_approve" in ra and not isinstance(ra["can_approve"], list):
                fails.append(
                    f"{rel(f)}: [C2b] response_authority.can_approve must be a list, "
                    f"got {type(ra['can_approve']).__name__}"
                )
            if "delegates_to" in ra and not isinstance(ra["delegates_to"], dict):
                fails.append(
                    f"{rel(f)}: [C2b] response_authority.delegates_to must be a mapping, "
                    f"got {type(ra['delegates_to']).__name__}"
                )

        # C3: agent_id == filename stem
        expected_id = f.stem
        aid = fm.get("agent_id")
        if aid != expected_id:
            fails.append(f"{rel(f)}: [C3] agent_id '{aid}' != filename stem '{expected_id}'")

        # C4: agent_id unique (index for Pass 2)
        if isinstance(aid, str):
            if aid in agents:
                fails.append(
                    f"{rel(f)}: [C4] duplicate agent_id '{aid}' "
                    f"(also in {rel(agents[aid][0])})"
                )
            else:
                agents[aid] = (f, fm)

    # Pass 2: cross-agent checks
    for aid, (path, fm) in sorted(agents.items()):
        eto = fm.get("escalates_to")
        efrom = fm.get("escalates_from")
        eto_resolved = isinstance(eto, str) and eto in agents

        # C5
        if eto is not None and not eto_resolved:
            fails.append(
                f"{rel(path)}: [C5] escalates_to '{eto}' not found among loaded agents"
            )
        # C6
        if efrom is not None and efrom not in agents:
            fails.append(
                f"{rel(path)}: [C6] escalates_from '{efrom}' not found among loaded agents"
            )
        # C7 reverse consistency
        if eto is not None and eto_resolved:
            target_fm = agents[eto][1]
            target_efrom = target_fm.get("escalates_from")
            if target_efrom != aid:
                fails.append(
                    f"{rel(path)}: [C7] reverse consistency broken: this agent escalates_to "
                    f"'{eto}', but {eto}.escalates_from = '{target_efrom}' (expected '{aid}')"
                )

        ra = fm.get("response_authority")
        if not isinstance(ra, dict):
            continue  # C2b already flagged if it was meant to be a dict

        # C8 authority mapping
        approval_keys = [k for k in ra.keys() if REQUIRES_APPROVAL_RE.match(k)]
        for key in approval_keys:
            need = ra.get(key)
            if not isinstance(need, list):
                continue  # already flagged in C2b
            need_set = set(need)
            if eto is None:
                fails.append(
                    f"{rel(path)}: [C8] has {key}={sorted(need_set)} but escalates_to is null "
                    f"(no upstream agent to approve)"
                )
                continue
            if not eto_resolved:
                # C5 already flagged; skip to avoid duplicate noise and KeyError
                continue
            target_ra = agents[eto][1].get("response_authority")
            if not isinstance(target_ra, dict):
                fails.append(
                    f"{rel(path)}: [C8] has {key}={sorted(need_set)} but '{eto}' has no "
                    f"response_authority (missing all items)"
                )
                continue
            target_can = target_ra.get("can_approve")
            if not isinstance(target_can, list):
                fails.append(
                    f"{rel(path)}: [C8] has {key}={sorted(need_set)} but "
                    f"'{eto}'.response_authority has no can_approve list (missing all items)"
                )
                continue
            target_can_set = set(target_can)
            diff = need_set - target_can_set
            if diff:
                fails.append(
                    f"{rel(path)}: [C8] {key}={sorted(need_set)} NOT ⊆ "
                    f"{eto}.can_approve={sorted(target_can_set)}, missing: {sorted(diff)}"
                )

        # C9 delegates_to forward refs (WARN only)
        delegates = ra.get("delegates_to")
        if isinstance(delegates, dict):
            for role_key, target_id in delegates.items():
                if not isinstance(target_id, str):
                    fails.append(
                        f"{rel(path)}: [C2b] delegates_to.{role_key} must be a string "
                        f"agent_id, got {type(target_id).__name__}"
                    )
                    continue
                if target_id not in agents:
                    warns.append(
                        f"{rel(path)}: [C9] delegates_to.{role_key} → '{target_id}' "
                        f"(forward ref, not yet implemented)"
                    )

    # Output
    print(f"Found {len(agents)} agents in {len(files)} files")
    print()
    for w in sorted(warns):
        print(f"WARN: {w}")
    if warns:
        print()
    for fl in sorted(fails):
        print(f"FAIL: {fl}")
    if fails:
        print()
        print(f"✗ {len(fails)} failure(s), {len(warns)} warning(s)")
        return 1
    print(f"✓ All checks passed ({len(warns)} warning(s))")
    return 0


if __name__ == "__main__":
    sys.exit(main())
