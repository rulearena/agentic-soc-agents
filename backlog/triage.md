# Triage Agents — Tuning Backlog

本檔案記錄 triage 角色定義（`triage-l1-soc-analyst`, `triage-l2-soc-analyst`）在實測中發現、尚未併入主檔的改善建議。

每一條代表「**目前定義在實際 triage 任務上會被新人或自動化測試挑出來的弱點**」，不是 bug。處理優先序與是否採納依 repo 維護節奏決定。

格式：每條含**問題**、**測試來源**、**建議方向**、**優先序**。Resolved 後移到底部 Changelog。

---

## triage-l1-soc-analyst

### TUN-L1-001 — 缺「越權請求拒絕範本」 ⭐ 高

**問題**：定義裡的 Anti-Pattern #10 只涵蓋「老闆說急著用」型的 IAM 社交工程情境，但實務上 L1 更高頻會碰到的是**同事善意請求型越權**（例：「你幫我寫一條 Sigma rule 把這個 noise suppress 掉」「幫我把 production threshold 改大一點」）。目前定義沒有對應的拒絕範本與 redirect 慣例。

**測試來源**：Test B（boundary test，2026-05-18）

**建議方向**：在「溝通範本 (Communication Templates)」章節新增第 4 條 `Tuning Request Redirect Template`，包含：
- 直接拒絕 + 引用 Anti-Pattern #8 / 「不在 L1 範圍」清單
- 解釋為什麼這是 risk decision，不是「調參數」
- 把使用者請求轉成正規 tuning ticket 的草稿模板（含應附量化數據）

### TUN-L1-002 — 缺 process / tuning escalation 路徑 ⭐ 高

**問題**：「升級條件 (Escalation Criteria)」表格只涵蓋 **incident escalation**（升給 L2 / IR），缺**制度回饋升級路徑**（噪音問題 → Detection Engineer、tool 異常 → SOC Engineer、SLA 不合理 → SOC Manager）。L1 拒絕越權後雖然知道「該記到 handover note」，但「該開 ticket 給誰、用什麼模板」沒有清楚指引。

**測試來源**：Test B

**建議方向**：在升級條件表加一列 `Systemic Issue → Process Escalation`，或獨立小節 `Process Escalation Paths`，明列各類 systemic issue 的對應角色 + 升級管道（ticket queue / Slack channel / weekly review）。

### TUN-L1-003 — 缺 time-critical TP 快速升級決策框架 中

**問題**：定義裡的 enrichment checklist 是**線性執行**（asset → temporal → external → behavioral），但對 credential dumping、ransomware 前置、Active Directory 攻擊等高時效告警，等 enrichment 全跑完才升級可能錯過 containment window。

**測試來源**：Test A（LSASS dump triage，分析師被迫在「先補 external context」vs「立刻升級保 containment window」之間做取捨）

**建議方向**：在 Workflow 章節加一個分支 `Time-Critical TP Fast-Track`：
- 列出哪些 alert pattern 觸發 fast-track（credential dumping、AD attack、known ransomware staging）
- 規範「升級 + 並行 enrichment」的工作方式
- ticket 註記模板：明確標註「fast-track escalation，enrichment 並行進行中」

### TUN-L1-004 — 缺 IOC 取得操作層細節 中

**問題**：定義說 L1 用 VirusTotal「**看結果**」，但沒寫「**如何從 EDR 撈到 hash 才能查**」這段銜接動作。對新人不夠 actionable。

**測試來源**：Test A

**建議方向**：在「工具掌握度」表的 CrowdStrike Falcon 列補充：「能從 Process Explorer / Host Search 取得 file hash 餵給 VT」；或在「核心任務 → Context Enrichment」加一條 micro-workflow。

### TUN-L1-005 — Evidence pending 處理規範 中

**問題**：當必要 evidence 暫時取不到（API 斷線、hash 還沒撈、enrichment source 故障），ticket 應有明確標註慣例，避免被 L2 / auditor 誤讀為「L1 偷懶」。

**測試來源**：Test A（VT lookup 因 raw alert 未含 hash 必須標 pending）

**建議方向**：在 Alert Triage Report 範本的 Evidence 區塊加標準格式：
```
- [Evidence Type]: <link or attachment> | **PENDING** — reason: <為何取不到>; ETA: <何時可補>; owner: <誰負責補>
```
另在 Anti-Pattern 章節澄清：**「誠實標 pending 並說明理由」≠「跳過 enrichment」**。

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

### TUN-L2-001 — Privileged service account 出現在 attack scope 的 SOP 不夠明確 ⭐ 高

**問題**：定義規定 `account-disable-for-privileged-user` 屬 `requires_ir_approval`，但**當 privileged service account 已出現明確 compromise indicator（例：interactive RDP 偏離 baseline）時，L2 是否可先用 `disable-user-session`（不停帳號、只切活躍 session）作為 stop-gap**沒寫清楚。L2 在邊界上會猶豫。

**測試來源**：Test C（svc-cicd-deploy 在 HOST-DEV-091 出現異常 interactive RDP，2026-05-18）

**建議方向**：在「反應權限 → Approved Playbooks」表的 `disable-user-session` 列補一行條件：「service account / privileged account 適用嗎？」並給明確規則。傾向：service account session 一斷可能 break CI/CD pipeline，因此**仍升 IR**，但要寫清楚理由，不是讓 L2 自己推。

### TUN-L2-002 — 跨業務單位同 dropper / IOC 的硬升級規則 ⭐ 高

**問題**：升級條件表寫「Confirmed TP 但影響範圍超出 L2 處理能力（多 host、critical asset、跨業務單位）」籠統，缺**硬規則**（單一 malware artifact 跨 ≥2 業務單位 = 自動 IR），L2 仍可能在邊界猶豫。

**測試來源**：Test C（同 dropper hash 跨 R&D + Finance 兩部門）

**建議方向**：升級條件表加一列 `Single artifact hits ≥2 business units → 自動升 IR`，列為硬規則（不需 L2 判斷）。

### TUN-L2-003 — Supply chain hypothesis 的並行 hand-off 路徑 中

**問題**：跨部門同 dropper 出現是強烈 supply chain 信號，但定義沒寫 L2 該不該**同時**開 Threat Hunter hypothesis（不是只升 IR）。目前文字隱含「升給 IR 之後 IR 再決定」，但 hunt 是平行協作，不是升級。

**測試來源**：Test C

**建議方向**：在「協作與回饋通道」章節的 Threat Hunter 列補：「跨業務單位同一 artifact 出現時，**同時**開 hunt hypothesis 並升 IR — 兩條路徑並行，不是先升 IR 等通知」。

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

（空）
