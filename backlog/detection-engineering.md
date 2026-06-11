# Detection Engineering Agents — Tuning Backlog

本檔案記錄 detection-engineering 角色定義（`detection-engineering-threat-detection-engineer`, `detection-engineering-threat-hunter`）在實測中發現、尚未併入主檔的改善建議。

格式對齊 `triage.md` / `incident-response.md`：每條含**問題**、**測試來源**、**建議方向**、**優先序**。Resolved 後移到底部 Changelog。

---

## detection-engineering-threat-detection-engineer

（detection-engineering-threat-detection-engineer 目前無 active backlog；已 resolved 項見底部 Changelog）

---

## detection-engineering-threat-hunter

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
- 2026-06-05: `TUN-HUNT-003` resolved (v1.3) — added `Fact vs Conclusion Line Drawing` sub-section (§關鍵規則 #4 後、§工具掌握度 前) to `detection-engineering-threat-hunter.md`（observable 寫成事實 / 斷定關係 · 同源 · 歸屬屬結論——actor 交 Threat Intel、incident 關聯交 IRC；含 ✅ 事實 / ❌ 結論 / 灰色地帶 三組 examples）. right-size：單一 ### 子節 elaborate 既有 rule #4，cross-ref §Hunt 中發現 active threat 的升級路徑 第 6 點（技術重疊是事實、定性留 IRC+TI）+ §反模式 #6 + HFP `Observed Technical Facts` fact-only 措辭，不重述. examples 全用佔位字（〔某 group〕/ INC-2026-XXX-001 / T-code），無真實 actor / family 命名（attribution 紅線）. +1 ### heading，既有 rules / 反模式 / HFP zero-diff. 非 ROADMAP rep（ROADMAP 不動）. 首個 v1.3 ship.
- 2026-06-11: `TUN-DE-006` resolved in this PR — added `### SOAR / SOC Engineer 反向邀寫 playbook 的越界拒絕` 範本 to `detection-engineering-threat-detection-engineer.md` §溝通範本（緊接既有「對 SOAR / SOC Engineer 的 playbook requirement handoff」後、War Room 前）；補 SOAR / SOC Engineer 因忙碌反過來邀 DE 直接寫 playbook YAML 的越界拒絕：固定回應講分工（DE 提供 trigger requirement、playbook authoring + 平台部署屬 SOAR / SOC Engineer）+ 越界後果（DE 不擁有 SOAR 平台變更權限、責任歸屬混亂；SOAR 平台特性 / deployment constraints / rollback / change process 屬平台 owner 責任範圍——拒絕站在責任歸屬非個人熟悉度）+ 更有價值替代品（trigger requirement / isolate·auto-action gate 設計建議 / autoresponse risk note，全在 DE 既有職能內）. 對齊 §關鍵規則 #5 / §核心任務 #5「不擁有平台變更權限」、未擴權；屬越界邀請拒絕 family（cross-ref triage `TUN-L1-001` / governance `TUN-CA-002`），cross-ref 既有兩範本不重述. review 修 2 P2：角色稱謂全程對齊「SOAR / SOC Engineer」（不收窄）+ 越界後果改責任語言（非個人熟悉度）. v1.3 low-sensitivity review lane. P2.

## Changelog (Dropped)

- 2026-06-05: `TUN-DE-005` dropped (v1.3 planning) — 灌水抵抗 reverse-argumentation framing 的 hub `TUN-AL-003`（business framing anti-pattern #9）已 ship，DE-005 屬「已 ship hub 的 P2 衛星」，core framing 已存在於 audit-liaison 主檔，DE 重述只升 framing 風險（triage-v1.1.md 原已 deferred: framing/size risk）；cross-ref backlog/README.md 灌水抵抗 family。
