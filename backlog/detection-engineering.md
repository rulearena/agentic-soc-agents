# Detection Engineering Agents — Tuning Backlog

本檔案記錄 detection-engineering 角色定義（`detection-engineering-threat-detection-engineer`, `detection-engineering-threat-hunter`）在實測中發現、尚未併入主檔的改善建議。

格式對齊 `triage.md` / `incident-response.md`：每條含**問題**、**測試來源**、**建議方向**、**優先序**。Resolved 後移到底部 Changelog。

---

## detection-engineering-threat-detection-engineer

### TUN-DE-005 — Audit Liaison 拒灌水的 framing 範本缺 中

**問題**：Test G Input #5 場景中執行者用「audit 風險反向論證」（標『已覆蓋』但拿不出 validated rule → audit finding 等級會更嚴重）說服 Audit Liaison 不灌水，這個 framing 比道德論述有效得多。目前 §溝通範本沒固化此 pattern。

**測試來源**：Test G Input #5（Audit Liaison 要求全 14 tactic 標已覆蓋）

**建議方向**：在 §溝通範本加 `Audit Liaison Coverage Honesty Response Template`，包含：
- 用 audit 機制反向論證（標已覆蓋拿不出 evidence → finding 等級升）
- 提供誠實的 Covered / Partial / 缺 對應 + Detection Rule Backlog 連結（顯示有 plan）
- 「scope-out」項目附理由（risk-based 取捨）
- 把 regulator-facing 翻譯權威 redirect 給 Compliance Auditor / Audit Liaison

### TUN-DE-006 — SOAR Engineer 反向要求寫 YAML 的拒絕範本缺 低

**問題**：§溝通範本有「DE → SOAR Engineer 的 Playbook Requirement handoff」（DE 主動方向），但**沒有**「SOAR Engineer 反過來邀請 DE 寫 YAML」這種越界邀請的拒絕範本。Test G Input #4 顯示這是真實情境（SOAR Engineer 太忙、推給「懂 detection logic 的人」）。

**測試來源**：Test G Input #4（SOAR Engineer 要 DE 直接寫 playbook YAML）

**建議方向**：在 §溝通範本加 `SOAR Engineer Cross-boundary Refusal Template`：
- 明確說明分工（DE 提供 trigger requirement、SOAR Engineer 做 playbook authoring + platform deploy）
- 解釋越界後果（DE 不擁有 SOAR 平台變更權限、責任歸屬混亂、SOAR Engineer 對平台特性掌握更完整）
- 給更有價值的替代品（trigger requirement + isolate gate 設計建議 + autoresponse risk note）

---

## detection-engineering-threat-hunter

### TUN-HUNT-003 — 「事實 vs 結論」line drawing examples 缺 中

**問題**：HFP 寫「dropper hash 與 INC-2026-05-18-001 相同」算事實（hash 重疊是 observable）還是隱性 attribution？若是 TTP 高度相似（不只 hash）呢？目前 §關鍵規則 4「不做 attribution conclusion」缺具體 examples，Hunter 在邊界上會猶豫。

**測試來源**：Test H 觸發點 #2（HFP 寫 dropper hash 與既有 incident 相同的決定）

**建議方向**：在 §關鍵規則 4 或 §反模式 #6 補一段 `Fact vs Conclusion Line Drawing Examples`：
- ✅ 事實：「dropper SHA256 與 INC-X 中列出的相同」「C2 domain 與 INC-X ticket 相同」「TTP 對應 T1003.001 + T1218」
- ❌ 結論：「延伸自 INC-X」「屬同一 actor」「同一 campaign」「attributed to X group」
- 灰色地帶（傾向用事實措辭 + 註記由 TI / L2 / IRC 判斷）

### TUN-HUNT-005 — TI 引誘 attribution 的標準回應範本缺 低

**問題**：§溝通範本只有「Hunt finding handoff to TI」（Hunter 主動方向），沒有「TI 反問或引誘 attribution」的回應範本。Test H 觸發點 #5 是高頻場景（TI 拿外部報告對應 Hunter finding，邀 Hunter 在 finding package 加 attribution 句子）。

**測試來源**：Test H 觸發點 #5（TI Analyst 邀 Hunter 在 HFP-2026-021 加「attributed to CrimsonOrca」）

**建議方向**：在 §溝通範本加 `Response to TI Attribution Request Template`：
- 拒絕措辭（角色分工 + 方法學風險：commodity tooling / affiliate / false flag）
- 提供替代協作（HFP 保留 observed facts + TI 自產 actor profile 引用 HFP + 需要技術細節從 HMD 補）
- 強調「技術事實由 Hunter 給，attribution 結論由 TI 下」的分工原則

---

## Changelog (Resolved)

- 2026-05-22: `TUN-DE-001` resolved in this PR — added Mode B 可做/不可做 對照表 (atomic IOC / threshold tune vs behavioral / correlation rule → Mode A) to threat-detection-engineer §工作流程.
- 2026-05-22: `TUN-DE-002` resolved in this PR — added War Room IRC Immediate Response template (§溝通範本) with (A) 立即可做 / (B) 必走完整流程 / (C) 折衷 三段; preserves validate-before-deploy boundary.
- 2026-05-23: `TUN-HUNT-001` resolved in this PR — added IOC/TTP-overlap escalation rule (page existing incident's IRC; IRC decides scope merge vs sibling incident; notify SOC Manager if policy requires separate incident) to threat-hunter §Active threat 升級路徑.
- 2026-05-29: `TUN-DE-004` resolved in this PR — added `Rule Production Health Monitoring` sub-section (每週 high-volume + 每月全 rule snapshot; TP/FP measurement feeds into tune/retire decisions; does not redefine Replacement Readiness Check or replace §4 Rule Retirement / Tuning Notice) to `detection-engineering-threat-detection-engineer.md` §工作流程.
- 2026-06-03: `TUN-DE-003` resolved (v1.2) — added a required `Replacement Readiness Check` gate to the §鑑識交付物 #4 Rule Retirement / Tuning Notice template in `detection-engineering-threat-detection-engineer.md`（必填 gate；retire 前須確認 replacement 已 production deploy + 最近 30 天 production FP rate 在預期內〔觀察窗未滿視為未確認〕；任一項未確認 → retirement 延後至 replacement 就位，或先啟動經既有 change process 核准的臨時 detection mitigation，避免 legacy rule 先下線留 detection gap）. 把 Test G Input #2「執行者憑判斷自加 gate」定為明文必填；right-size：2 confirm + 1 fail-branch，不重列既有 `## Replacement` 已有的 coverage 對比；同時補實 §工作流程 Health Monitoring 段（line 155/163）已 forward-reference 但未定義的 `Replacement Readiness Check` 名詞. +0 heading（code-fence 內 `##`）. 非 ROADMAP rep（ROADMAP 不動）.
- 2026-06-03: `TUN-HUNT-002` resolved (v1.2) — refined the `IR Analyst` row in §對既有角色與相鄰角色的邊界 table in `detection-engineering-threat-hunter.md`（做：將 hunt 過程已產生的 operational technical context [process tree / handle access timeline / observed module load order] 整理成隨 L2 / IRC handoff 進入 IR flow、供 IR Analyst 使用的 enrichment package；不做：此 package 僅為 input、不取代 IR Analyst 的 verification、不為打包額外執行 RTR 或收 forensic-grade evidence → 需要時移交 Forensics）. +0 heading, single-row in-cell edit. 鄰列（IRC / Forensics / Detection Engineer 等）row_zerodiff 保護；framing 與 Forensics row「hunt 收 operational evidence、非 forensic-grade」一致. 非 ROADMAP rep（ROADMAP 不動）.
- 2026-06-01: `TUN-HUNT-004` resolved in this PR — appended a `SOC Manager` row to §對既有角色與相鄰角色的邊界 table in `detection-engineering-threat-hunter.md`（做：Hunt sprint summary / Hunt Backlog 進度 / 人力·資源議題 / 跨 sprint 排序協調；不做：接收 operational task assignment [disable / isolate / RTR / individual host 處置] → 走 IRC / IR-A 路徑、不因 SOC Manager 人力壓力接手 containment）. +0 heading, single-location table-row append. 既有 8 rows（含 IR Analyst HUNT-002 scope）row_zerodiff 保護、HUNT-001 step 6 staffing context zero-diff. 非 ROADMAP rep（ROADMAP 不動）.
