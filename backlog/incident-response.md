# Incident Response Agents — Tuning Backlog

本檔案記錄 incident-response 角色定義（`incident-response-ir-commander`, `incident-response-ir-analyst`, `incident-response-forensics-analyst`）在實測中發現、尚未併入主檔的改善建議。

格式對齊 `triage.md`：每條含**問題**、**測試來源**、**建議方向**、**優先序**。Resolved 後移到底部 Changelog。

---

## incident-response-ir-commander

（incident-response-ir-commander 目前無 active backlog；已 resolved 項見底部 Changelog）

---

## incident-response-ir-analyst

（incident-response-ir-analyst 目前無 active backlog；已 resolved 項見底部 Changelog）

---

## incident-response-forensics-analyst

（incident-response-forensics-analyst 目前無 active backlog；已 resolved 項見底部 Changelog）

---

## Changelog (Resolved)

- 2026-05-20: `TUN-IRA-002` resolved in this PR — added Side-channel Pressure Refusal template (§溝通範本) to `incident-response-ir-analyst.md`; 越界邀請 family（cross-ref `TUN-L1-001`, `TUN-CA-002`）.
- 2026-05-22: `TUN-FOR-001` resolved in this PR — added Side-channel Pressure Refusal template (§溝通範本) to `incident-response-forensics-analyst.md`; forensics 版（preservation 充分性 / 放行屬 IRC joint decision、ad-hoc snapshot ≠ forensic-grade、evidence handling 不接受 DM 指令）；結構姊妹 `TUN-IRA-002`（不 cross-edit）.
- 2026-05-24: `TUN-IRA-001` resolved in this PR — annotated SIEM verification-query scope boundary (綁定 AAR target；超界 pivot 屬 hunting → Threat Hunter) + added Stop-and-Report trigger row (verification pivot 超界 → Scope Drift Report → IRC) to `incident-response-ir-analyst.md`.
- 2026-05-28: `TUN-IRA-004` resolved in this PR — added IR-A Shift Handoff Brief template (§溝通範本) to `incident-response-ir-analyst.md`; rotation A→B 同角色接班的執行狀態交接（executing/completed/pending AAR 狀態 + holding scope drift items 摘要 + verification monitor 移交 + 未結 Execution Report 與 finalize ETA），與 #4 IR-A→L2 handoff 明確區分、引用 SDR 機制不重寫. 非 ROADMAP rep（ROADMAP 不動）. 首條 P2.
- 2026-06-01: `TUN-FOR-002` resolved in this PR — extended §工作流程 `### 3. Acquire` in `incident-response-forensics-analyst.md` with the anti-forensics acquisition SOP（區分工具故障 vs anti-forensics 主動干擾的判斷訊號、對應選項清單 [重做 / kill 可疑 session 再採 / cold acquisition / IRC joint decision]、與 IR Analyst 的 kill session 責任界線）. kill session 框成 Forensics 提 preservation risk signal → IR Analyst 走 IRC approval 執行、不自己 contain（cross-ref §關鍵規則 7）. +0 heading, single-location prose append. 非 ROADMAP rep（ROADMAP 不動）.
- 2026-06-02: `TUN-IRC-001` resolved in this PR — added `cannot_approve_alone` 法規時限速查 hook (§反應權限) to `incident-response-ir-commander.md`; 對外通知/disclosure 類決策可能受法規/合約/監理時限約束時，IRC 啟動即向 Audit Liaison 發 time-sensitive regulatory check 取得最快 external deadline 作 Decision Log 時間錨點，不自行詮釋合規義務、由 Legal/Audit Liaison 認定. 非 ROADMAP rep. P2.
- 2026-06-02: `TUN-IRC-002` resolved in this PR — added 反模式 #9「業務 owner 跨界引導技術決策」to `incident-response-ir-commander.md`; 業務主管以「等不了/事後補/你拍板」引導 IRC 跳過 evidence preservation（#5）或 cannot_approve_alone 共同決策（#4）時回流程語言拒絕、Exec Sponsor 處理業務壓力取捨但 preservation/共同決策仍照既有流程. 非 ROADMAP rep. P2.
- 2026-06-02: `TUN-FOR-004` resolved in this PR — added 業務時程壓力 side-channel 責任分界 to §Override 流程 in `incident-response-forensics-analyst.md`; side-channel 業務時程壓力 → Forensics 報事實+量化 evidence loss+建議 IRC 啟動 joint decision，不繞過 IRC、不靜默改 evidence handling，IRC 未判斷就 override 則紀錄義務歸 IRC；cross-ref FOR-001 不重述. 非 ROADMAP rep. P2.
- 2026-06-04: `TUN-IRA-003` resolved (v1.2) — added §溝通範本 `Pending Action Status Ping` template to `incident-response-ir-analyst.md`; action 被 IRC BLOCK 或卡前置條件（等 Forensics preservation / 其他執行者 / 系統）進入 holding 時，IR Analyst 主動按節奏回報自身待命狀態並確認 hold 是否仍成立，避免「卡住但沒人知道」跨班次 / 跨人員漏接. 節奏依 IRC 指定 cadence / action urgency / blocker ETA / 狀態變更 / severity 調整、不寫死固定時數，範本含「下次回報」追蹤錨點；boundary：只回報狀態並把問題交回 IRC，不自行解除 BLOCK、不替 IRC 決定轉手執行者、不自行變更 / 重新指派他人 pending action（是否轉手或調整優先序由 IRC 協調；向 blocker owner 問 ETA 屬正常協作）；跨班次整體快照沿用 §IR-A 跨 rotation 接班簡報、不重述. 既有範本 zero-diff. 非 ROADMAP rep. P2.
- 2026-06-10: `TUN-IRC-005` resolved in this PR — added fixed `Parallel notification (non-blocking)` 欄 to Action Approval Record 範本 in `incident-response-ir-commander.md`（與 `Execution Delegation`〔blocking〕區分；Action #003 filled〔Platform/IT fallback、持有者主管知會〕、#007 N/A）+ 填寫原則含 carve-out：`cannot_approve_alone` 類（legal / customer / regulator / law-enforcement / public disclosure）一律 blocking 聯合決策、不得填本欄，判準=通知對象有無否決/共同拍板權；明確區分「決策層 blocking gate」vs「執行層 non-blocking ping」，防止把聯合決策 gate 降級成順手通知. 在既有 authority 模型內補固定欄位、未擴權. 因碰 incident authority（通知 blocking/non-blocking 決策權）改判中敏感、走 user-driven review（複審指出的失效 section 引用已修，對齊 §升級條件 (Escalation Criteria)）. v1.3 medium-sensitivity review lane. P2.
- 2026-06-10: `TUN-IRA-005` resolved in this PR — clarified IR Analyst 在 Scope Drift Report `Recommended Next Step` 的人員調度建議邊界 in `incident-response-ir-analyst.md`（範例補一條人員調度建議 + fenced block 後加 guardrail 範本說明）：IR-A **可**建議 IRC 拉 Threat Hunter / Detection Engineer 等角色進來（屬「給 IRC 決策參考」範圍）、但**不自行 ping / 召集**——實際人員調度屬 IRC / SOC Manager 職權，建議 ≠ 執行. 收束既有邊界、未授予新召集權、未引入新 escalation / approval / handoff path. v1.3 low-sensitivity review lane. P2.
- 2026-06-10: `TUN-IRA-006` resolved in this PR — added §執行交付物 `### 6. Operational Evidence Storage Convention` to `incident-response-ir-analyst.md`；為 operational evidence（command 輸出 / log snapshot / screen capture）定義最小一致格式：命名 `<ref>-evidence-<type>-<timestamp>`（ref=AAR 編號如 `AAR-003`、type=cmdout/logsnap/screencap、無對應 approval 用 case ref 如 `INC-2026-0042-preexec`）、一律 attach 到 IR ticket 並在報告中以檔名 reference 引用（不貼整段內容）、描述須可定位（把「auth log 7d snapshot」寫成具體檔名 + 來源 / 範圍 / 時間窗 / host）、保留期限對齊事件 retention policy. 邊界：只規範 operational evidence 的存放格式，memory / disk image 與 chain of custody 仍屬 forensic-grade、走 Forensics 保全流程不套用本格式（掛回 §關鍵規則 3）；IR Analyst 不自定保留期、不提前刪除，retention 由事件 / 合規政策認定、有疑義回報 IRC——純格式收束、未擴權、未引入新 path. 非 ROADMAP rep. v1.3 low-sensitivity review lane. P2.
- 2026-06-10: `TUN-FOR-005` resolved in this PR — added §溝通範本 `IRC 要求時程短於可行 ETA 時的回應（ETA 揭露與壓縮選項）` template to `incident-response-forensics-analyst.md`; 誠實 ETA 超出 IRC 期望時主動同步差距、姿態 = 報事實 + 量化 + 給選項；不退讓 = 已納入 scope 的每個 item 之 hash verification 與 chain of custody 完整性（§關鍵規則 1、8，integrity 不能半做）；可協商項明分兩類且對證據可用性影響不同——Scope 縮減（要不要採某 item、剩餘台品質不變）vs Depth 降級（full image → live triage、改變該 item 證據性質、forensic/法律可用性下降、掛回 §關鍵規則 4 operational-vs-forensic-grade），不可混為一談；壓縮與否與接受哪種影響最終由 IRC 拍板、Forensics 不自行壓縮/降級/跳步驟、不掩飾 depth 降級的可採性代價. 範例各選項以結果 ETA 呈現（含未達標殘差、兩項合併才達標）、per-endpoint 採集時間框為 incident-specific（不宣稱通用速率，避免與 §關鍵規則 8 估時 / MAR-014 互撞）、ETA 算術自洽. 與 `TUN-FOR-001` / `TUN-FOR-004` side-channel 骨幹同姿態（報事實 + 量化 + 決策交回 IRC），不轉移 authority、未擴權. 非 ROADMAP rep. v1.3 low-sensitivity review lane. P2.
- 2026-06-10: `TUN-IRC-003` resolved in this PR — added §workflow §2 Classify 一條「暫定分級的 confirmation 節奏」+ Severity Classification 範本後「暫定 vs 定案」慣例註記 in `incident-response-ir-commander.md`；commander 可先給暫定 (provisional) severity 以啟動流程，但暫定不應無限延續：重新評估由觸發門檻驅動（證據到位 / 三軸輸入變動 / containment 或 scope 狀態改變 / 接近 mandatory notification 門檻），**不綁固定時數**（避免虛構 SLA，對齊 `TUN-IRA-003` 相對 cadence 設計、與被 drop 的 `TUN-TI-005` 固定 SLA 反向）；每次 confirm / downgrade 更新 Severity Classification（標暫定 → 定案版本變更）+ 記 Decision Log，暫定須在 Severity Classification 標為暫定並掛「下次 severity review」錨點（對齊 Command Brief Next Decision Points）. 邊界：只規範**何時**重新評估 severity 的節奏，不改變既有分級職權、不新增升降 severity 的權限——authority 收束未擴權. 非 ROADMAP rep. v1.3 low-sensitivity review lane. P2.
- 2026-06-11: `TUN-IRC-004` resolved in this PR — added §指揮交付物 `### 7. Break-glass Post-incident Review Checklist（事後審查）` to `incident-response-ir-commander.md`；補〈關鍵規則〉#7 + 反模式 #6 缺的「如何判定 break-glass 合理 vs 濫用」結構化模板：審查表六維度（trigger context / alternatives considered / evidence of urgency / investigation chain continuity / approval trail / rollback·follow-up needs）+ 三檔判讀結論（合理 / 合理但有 follow-up / 需檢討）。三層防滑釘死定位：(1) 只**事後**審查**已發生**的 break-glass、(2) 是給 post-incident review board 的結構化輸入服務問責·校正·流程改進、非事件當場拍板、(3) **不是授權工具**——不定義「符合哪些條件即可 break-glass」、不新增任何可即時援引略過 L2 的權限，緊急通道成立與否仍依既有 #7；額外加「即使判讀合理也不構成未來預先授權」+「濫用訊號是回顧性警訊、非事前禁令清單」。backlog 原建議的 cross-dept / critical asset / 時序壓力 拆進 retrospective 維度（trigger context / evidence of urgency），不列成事前綠燈清單. 收束既有 break-glass 邊界、未擴權、未引入新 path. 因碰 break-glass authority 邊界由 user 上修為「低到中、按中敏感心態處理」、走 user-driven review（user 釘三條護欄 + 提 2 P2 措辭精修：範例首行改「未經標準逐級升級；L2 已同步通知」避免說成「跳過 L2」、表格列名 `Scope containment` → `Investigation chain continuity` 避免誤聯想技術 containment）. v1.3 medium-sensitivity review lane. P2.

## Changelog (Dropped)

- 2026-06-07: `TUN-FOR-003` dropped (v1.3 planning) — 實測（Forensics，3 host 2/3 保全情境）顯示現行 spec 已逼出 in-lane、適度 bounded 的回應（forensic-grade vs operational evidence 區分、不可外推 partial→full、Legal evidentiary impact、不自行拍板）；固化「n=1/2/3 信心度量化框架」會讓 forensic sufficiency 看起來比實際可量化、有假精確風險。未來若再測出失敗，以更窄的 partial-preservation quick-reference 另提，不照原 TUN-FOR-003 全量補.
