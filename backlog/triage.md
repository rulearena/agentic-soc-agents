# Triage Agents — Tuning Backlog

本檔案記錄 triage 角色定義（`triage-l1-soc-analyst`, `triage-l2-soc-analyst`）在實測中發現、尚未併入主檔的改善建議。

每一條代表「**目前定義在實際 triage 任務上會被新人或自動化測試挑出來的弱點**」，不是 bug。處理優先序與是否採納依 repo 維護節奏決定。

格式：每條含**問題**、**測試來源**、**建議方向**、**優先序**。Resolved 後移到底部 Changelog。

---

## triage-l1-soc-analyst

（triage-l1-soc-analyst 目前無 active backlog；已 resolved 項見底部 Changelog）

---

## triage-l2-soc-analyst

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
- 2026-06-08: `TUN-L1-004` resolved in this PR — added `EDR → hash → VT micro-workflow`（Falcon Host Search / Process Explorer 定位 process → 取 file SHA256 → VT 查 ratio/first seen/community → 寫進 Triage Report External Intel 段並 attach evidence）to `triage-l1-soc-analyst.md` §工作流程 Step 2 External context，並在 §工具掌握度 CrowdStrike Falcon 列補 hash 取得能力. 補上「怎麼撈到 hash 才能查」的操作層銜接. v1.3 low-sensitivity review lane. P2.
- 2026-06-09: `TUN-L2-004` resolved in this PR — added `Affected Data Assets` 子段（資料資產維度）to `triage-l2-soc-analyst.md` Investigation Report 範本 §Scope Expansion 發現；補上 host/user 維度之外的「哪些**資料**被接觸 / 外傳」表格（資料資產 / 資料類型 / 敏感等級 / 外傳證據 / 合規影響預估）+ 填寫原則（外傳證據只寫已觀測 log 事實、合規影響為初判輸入非最終裁定、最終認定由 IR Commander + Legal/DPO 決定、敏感等級依組織 data classification）. data exfil 場景補強，L2 不下合規最終裁定. v1.3 low-sensitivity review lane. P2.
- 2026-06-10: `TUN-L1-007` resolved in this PR — converted Shift Handover Report 範本 §`Systemic Issues Observed` 從 bullet list 改為 table（欄位 `Issue` / `量化數據` / `Tuning Ticket #` / `Owner` / `Status`）to `triage-l1-soc-analyst.md`；補上「是否已開 tuning ticket 往上推」的追蹤維度，避免 L1 只記不推；加填寫原則 note 明示並非每個 systemic issue 都對應 tuning ticket（平台事件 / 供應商 outage 標 `N/A` 改走 incident / Reminders track，但仍須填 `Owner` + `Status`），防止讀者誤把 Ticket # 當硬性必填亂開單. v1.3 low-sensitivity review lane. P2.
- 2026-06-11: `TUN-L1-006` resolved in this PR — added `Common Triage Heuristics（速查，非教學）` 子節 to `triage-l1-soc-analyst.md` §MITRE ATT&CK 對應 末尾（MITRE 表後、§工作流程 前）；補實務常見但原 6-technique 表沒有的 quick reference：高頻 LOLBin abuse pattern 表（rundll32 / regsvr32 / mshta / wmic / certutil 各列正常用途 vs triage 角度可疑訊號）+ 可疑落地路徑（user Temp / Windows Temp / ProgramData）+ 可疑 export / function name pattern。定位 = cheatsheet 非教學、非偵測邏輯；intro 護欄明寫「命中 ≠ TP、是值得多查一步 / 提高升級權重的訊號、最終判定仍走 §工作流程 Step 3 搭配 §Process Chain」守 L1 scope（不跨偵測規則撰寫）。每列均為防守 triage 訊號、不寫攻擊武器化細節（守藍隊紅線）；review 修 2 P2：`DllRegisterServer` 可疑點綁回路徑 / 執行脈絡（非 entrypoint 本身、它是正常 COM 註冊進入點）+ 移除 rundll32 列「無參數執行」low-signal 訊號. v1.3 low-sensitivity review lane. P2.
