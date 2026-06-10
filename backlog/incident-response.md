# Incident Response Agents — Tuning Backlog

本檔案記錄 incident-response 角色定義（`incident-response-ir-commander`, `incident-response-ir-analyst`, `incident-response-forensics-analyst`）在實測中發現、尚未併入主檔的改善建議。

格式對齊 `triage.md`：每條含**問題**、**測試來源**、**建議方向**、**優先序**。Resolved 後移到底部 Changelog。

---

## incident-response-ir-commander

### TUN-IRC-003 — Sev-1 暫定 → confirm/downgrade 缺時間框架 低

**問題**：定義 §workflow §2 Classify 講「為何不是更高/更低」三軸評估，但沒有「Sev-1 **暫定** → N 分鐘內基於更多證據 confirm 或 downgrade」的明確時間框架。事件初期 commander 常需先暫定才能啟動流程，但暫定狀態能維持多久沒寫，可能導致 stakeholder 對嚴重度認知混亂。

**測試來源**：Test D（事件 09:55 暫定 Sev-1，但定義沒寫多久內必須 confirm）

**建議方向**：§workflow §2 Classify 補一條「Sev-1 暫定的 confirmation window」—— 例如「Sev-1 暫定後 30 分鐘內基於更多 evidence confirm 或 downgrade，confirmation 結果寫入 Severity Classification 第二版」。

### TUN-IRC-004 — Break-glass 合理使用 vs 濫用的 post-incident 判定範本 低

**問題**：定義 §關鍵規則 7 + Anti-Pattern #6 明確說「濫用才是流程議題」，但沒給「**如何判定濫用**」的範本。Commander 在 Decision Log 標「不入濫用 review」是憑直覺，缺結構化判定 checklist。

**測試來源**：Test D Decision Log 第 1 列（標「不入濫用 review」憑直覺判斷）

**建議方向**：在 §關鍵規則 7 後或單獨小節加 `Break-glass Review Checklist` —— 列出合理使用的判定條件（cross-dept + critical asset + 時序壓力等）vs 濫用訊號（L1 嫌 L2 慢、頻繁觸發、單一規則告警觸發等），作為 post-incident review 的結構化輸入。

---

## incident-response-ir-analyst

### TUN-IRA-005 — 「自己不做但建議拉誰進來」的 phrasing 邊界沒明示 低

**問題**：IR Analyst 在 Scope Drift Report 或 Execution Report 中可以「建議 IRC 拉 Threat Hunter / Detection Engineer 進來」嗎？這算建議 IRC 做人員調度（邊界 OK，自己沒 ping）還是越界（人員調度屬 IRC / SOC Manager）？目前定義沒明示。

**測試來源**：Test F 訊息 #2 Scope Drift Report 的 Recommended Next Step（建議 IRC 拉 Threat Hunter / Detection Engineer 進來）

**建議方向**：在 §核心任務 #4 scope drift 回報或 §溝通範本補一行：「Recommended Next Step 可包含人員調度建議，但**不自己 ping** 對應角色；ping 屬 IRC / SOC Manager 職權」。

### TUN-IRA-006 — Operational evidence 的 attach / 保存格式範本缺 低

**問題**：定義講 operational evidence（command 輸出、log snapshot、screen capture）由 IR Analyst 收，但沒給保存位置、命名、保留期限的範本。Test F 場景中 IR Analyst 寫了「auth log 7d snapshot」但 attach 路徑 / case ID 沒寫具體 reference，實務上 IR ticket 會要求一致格式。

**測試來源**：Test F 訊息 #1 self-eval 自我點出

**建議方向**：在 §執行交付物加一節 `Operational Evidence Storage Convention`，定義最小命名 + attach 規格（例：`AAR-<id>-evidence-<type>-<timestamp>` + 一律 attach 到 IR ticket、保留期限對齊事件 retention policy）。

---

## incident-response-forensics-analyst

### TUN-FOR-005 — 「ETA 超出 IRC 要求」的回應姿態未範本化 低

**問題**：Test E 場景中 IRC 要求 10:30 完成，Forensics 評估後給 10:34 + 不退讓 hash verification —— 這是基於 §關鍵規則 8 自己詮釋的，但 §溝通範本沒示範。實務上 Forensics 給「超出 IRC 期望」的 ETA 時容易被解讀為「鑑識在拖延」，需要範本化清楚的姿態。

**測試來源**：Test E 訊息 #1（Forensics 主動揭露 ETA 超 4 分鐘 + 解釋為什麼不退讓 hash）

**建議方向**：在 §溝通範本補一段「ETA Negotiation Template」，示範：
- 主動揭露差距（不要等 IRC 發現）
- 講清楚不退讓的具體項（hash / completeness / chain of custody 哪一條）
- 給「壓縮版」的選項（若 IRC 真要更快，可以省略哪些 → 對應 evidence 損失量級）
- 最終決策仍在 IRC

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

## Changelog (Dropped)

- 2026-06-07: `TUN-FOR-003` dropped (v1.3 planning) — 實測（Forensics，3 host 2/3 保全情境）顯示現行 spec 已逼出 in-lane、適度 bounded 的回應（forensic-grade vs operational evidence 區分、不可外推 partial→full、Legal evidentiary impact、不自行拍板）；固化「n=1/2/3 信心度量化框架」會讓 forensic sufficiency 看起來比實際可量化、有假精確風險。未來若再測出失敗，以更窄的 partial-preservation quick-reference 另提，不照原 TUN-FOR-003 全量補.
