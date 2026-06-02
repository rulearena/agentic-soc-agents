# Triage Agents — Tuning Backlog

本檔案記錄 triage 角色定義（`triage-l1-soc-analyst`, `triage-l2-soc-analyst`）在實測中發現、尚未併入主檔的改善建議。

每一條代表「**目前定義在實際 triage 任務上會被新人或自動化測試挑出來的弱點**」，不是 bug。處理優先序與是否採納依 repo 維護節奏決定。

格式：每條含**問題**、**測試來源**、**建議方向**、**優先序**。Resolved 後移到底部 Changelog。

---

## triage-l1-soc-analyst

### TUN-L1-004 — 缺 IOC 取得操作層細節 中

**問題**：定義說 L1 用 VirusTotal「**看結果**」，但沒寫「**如何從 EDR 撈到 hash 才能查**」這段銜接動作。對新人不夠 actionable。

**測試來源**：Test A

**建議方向**：在「工具掌握度」表的 CrowdStrike Falcon 列補充：「能從 Process Explorer / Host Search 取得 file hash 餵給 VT」；或在「核心任務 → Context Enrichment」加一條 micro-workflow。

### TUN-L1-006 — 常見 triage heuristic quick reference 擴充 低

**問題**：目前 MITRE ATT&CK 對應表只列 6 條 technique，實務常見的 rundll32 / regsvr32 / mshta / wmic / certutil 等 LOLBin 濫用 pattern、Temp 路徑落地、export name pattern 等 heuristic 沒有快速 reference。

**測試來源**：Test A（分析師需自行套用 LOLBin + Temp path heuristic）

**建議方向**：在 MITRE 表後加 `Common Triage Heuristics` 小節（不是教學文，是 cheatsheet），列：
- 高頻 LOLBin + 對應 abuse pattern
- 可疑落地路徑（user Temp、Windows Temp、ProgramData）
- 可疑 export name / function name pattern

### TUN-L1-007 — Handover note 加 tuning ticket 追蹤欄 低

**問題**：Shift Handover 範本的 `Systemic Issues Observed` 區塊只記「觀察到什麼」，沒有追蹤「是否已開 tuning request ticket」。L1 可能只「記下來」但沒實際往上推。

**測試來源**：Test B

**建議方向**：Handover 範本 Systemic Issues 區塊改為 table 格式，欄位：`Issue` / `量化數據` / `Tuning Ticket #` / `Owner` / `Status`。

---

## triage-l2-soc-analyst

### TUN-L2-004 — Investigation Report 加 `Affected Data Assets` 子段 中

**問題**：Scope Expansion 範本目前偏 host 維度（host、user 表），但 data exfil 場景（例：repo zip 被拉走）需明確列 data asset 維度。L2 自行擴展容易遺漏。

**測試來源**：Test C（dev.alice 拉 3 個 private repo zip 與 dump 時序重疊）

**建議方向**：Investigation Report 範本的 Scope Expansion 區塊加子段 `Affected Data Assets`（含資料類型、敏感等級、外傳證據、合規影響預估）。

### TUN-L2-005 — L1 已 break-glass page IR 時 L2 的並行責任 低

**問題**：定義的 workflow 假設「L2 調查 → 升級 IR」線性流程，但 L1 已 break-glass 直接 page IR 的場景下，L2 與 IR 是**並行起步**。L2 應該先做哪些 containment 才不會卡 IR、handoff 時機與 evidence 完整度標準沒寫。

**測試來源**：Test C（L1 已 break-glass page IR，L2 邊調查邊收 IR 問題）

**建議方向**：Workflow 章節加分支 `Break-glass Parallel Path` —— L1 已 page IR 時 L2 的最小 containment 集合、與 IR 的同步節奏、handoff 完整度的閾值（不能等 100% 才交，要分段交）。

---

> IR Commander 等其他角色的 tuning backlog 應放在對應子目錄（例：`incident-response/TUNING-BACKLOG.md`），本檔聚焦 `triage/` 角色。

---

## Changelog (Resolved)

- 2026-05-20: `TUN-L1-001` resolved in this PR — added Tuning Request Redirect template (溝通範本 #4) to `triage-l1-soc-analyst.md`; 越界邀請 family（cross-ref `TUN-IRA-002`, `TUN-CA-002`）.
- 2026-05-21: `TUN-L2-001` resolved in this PR — clarified `disable-user-session` does NOT apply as an L2 stop-gap for service / privileged accounts (反應權限); escalate IR via `account-disable-for-privileged-user`.
- 2026-05-21: `TUN-L2-002` resolved in this PR — added hard escalation rule (single malware artifact across ≥2 business units → auto IR) to 升級條件.
- 2026-05-23: `TUN-L1-002` resolved in this PR — added `Process / Systemic Escalation Paths` sub-section (systemic issue → Detection Engineer / SOC Engineer / SOC Manager + ticket queue / Slack channel / weekly review + 留痕) to `triage-l1-soc-analyst.md` §升級條件.
- 2026-05-28: `TUN-L1-003` resolved in this PR — added `Time-Critical TP Fast-Track` sub-section (升級 + 並行 enrichment) to `triage-l1-soc-analyst.md` §工作流程; triggers on credential dumping / AD attack / ransomware staging patterns.
- 2026-06-02: `TUN-L1-005` resolved in this PR — added Evidence Pending 標註規範 sub-section to `triage-l1-soc-analyst.md`; PENDING evidence 須填 reason/ETA/owner + 補回留痕、不靜默替換、平台異常記入 Systemic Issues Observed；PENDING ≠ 跳過 enrichment. 非 ROADMAP rep. P2.
- 2026-06-02: `TUN-L2-003` resolved in this PR — added `跨單位同一 artifact：hunt 與 IR 並行起步` sub-section to `triage-l2-soc-analyst.md` §協作與回饋通道; 跨單位 artifact 硬規則命中時 hunt seed 與升 IR 並行起步（指向 §升級條件、不重述 trigger）、hunt 屬平行協作非升級鏈、L2 不自下 supply chain 結論. 非 ROADMAP rep. P2.
