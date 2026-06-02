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

### TUN-IRC-005 — AAR 範本缺 `Parallel notification (non-blocking)` 欄位 低

**問題**：實務上很多 approval 需要平行通知第三方（例：本次 Test D 的 Platform team 在 svc-cicd-deploy disable 前需預備 CI/CD fallback）。目前 Action Approval Record 範本沒有此欄位，commander 需自行塞入 Execution Delegation 或 Notes 區塊，容易遺漏。

**測試來源**：Test D 請求 #1（svc-cicd-deploy disable 需平行 ping Platform team）

**建議方向**：AAR 範本固定加一欄 `Parallel notification (non-blocking)`，與 `Execution Delegation`（blocking）區分。明確標示哪些通知是「同步進行不擋執行」vs 「必須完成才能執行」。

---

## incident-response-ir-analyst

### TUN-IRA-003 — Pending action 在 BLOCK 狀態下的回報節奏沒明示 中

**問題**：pending action（如 Test D 的 #002 process kill）被 IRC BLOCK 後，IR Analyst 是該定期回報自己 standby 狀態還是被動等？目前定義沒講，執行端只能自由選擇。Test F 場景中 IR Analyst 選了被動等 + 在其他訊息結尾 reminder，但實務上跨班次 / 跨人員可能漏掉。

**測試來源**：Test F（IRC BLOCK pending #002，IR Analyst 自由選擇被動等而非定期 status ping）

**建議方向**：在 §工作流程或 §溝通範本補一條「Pending Action Status Ping」 —— 例如「BLOCK 超過 N 分鐘自動 ping IRC 確認狀態 + 是否需轉手其他執行者」。

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

### TUN-FOR-003 — Partial preservation acceptable threshold 判斷材料缺 中

**問題**：Test E 場景中 3 host 1 個失敗，supply-chain attribution 樣本數降到 2 是否仍 acceptable？Forensics 不拍板沒錯，但**目前範本只講「evidence loss 描述」**，沒給 IRC 判斷支撐工具（例：attribution 完整性影響量級評估框架、樣本數對結論可信度的影響）。

**測試來源**：Test E 訊息 #2（5 個選項給 IRC 但缺結構化判斷框架）

**建議方向**：在 §鑑識交付物加一節 `Partial Preservation Impact Framework`，含：
- Attribution 完整性的樣本量估算（n=1 vs n=2 vs n=3 對結論的差異）
- 各類 evidence 的可替代性（disk snapshot 能 / 不能補哪些 in-memory artifact）
- 對 Legal / regulatory 可用性的影響分級

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
