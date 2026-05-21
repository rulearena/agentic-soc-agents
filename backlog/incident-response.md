# Incident Response Agents — Tuning Backlog

本檔案記錄 incident-response 角色定義（`incident-response-ir-commander`, `incident-response-ir-analyst`, `incident-response-forensics-analyst`）在實測中發現、尚未併入主檔的改善建議。

格式對齊 `triage.md`：每條含**問題**、**測試來源**、**建議方向**、**優先序**。Resolved 後移到底部 Changelog。

---

## incident-response-ir-commander

### TUN-IRC-001 — `cannot_approve_alone` 缺法規時限速查 hook 中

**問題**：customer-notification 與 law-enforcement-contact 在不同 jurisdiction（GDPR 72hr、CCPA、台灣個資法等）有強制通報時限。角色定義 §升級條件表只說「法定通報，依各地法規時限」「Audit Liaison 主理」，但 IR Commander 在共同決策時需要知道「**最快 deadline 是什麼**」才能設定 war room 評估時程；目前要等 Audit Liaison 回覆才知道。

**測試來源**：Test D 請求 #4（2026-05-18，Legal 請求 customer-notification + law-enforcement-contact 共同決策）

**建議方向**：升級條件表加一欄 `法規時限速查連結`（不寫具體時限避免過時，但留可維護的 reference hook），讓 commander 在共同決策時序設計時有參考錨點。

### TUN-IRC-002 — 業務 owner 跨界引導技術決策的 Anti-Pattern 缺位 中

**問題**：目前 Anti-Pattern #1（super-engineer commander）是針對 commander **自己**衝動下技術指令，但**業務 owner（VP / 業務主管）引導 commander 跳過 preservation、跳過 approval 流程、直接拍板**的情境是更高頻、更難拒絕的壓力源（因為涉及階層 + 業務復工迫切性），目前定義沒有顯式 Anti-Pattern 與拒絕話術。

**測試來源**：Test D 訊息 #3（R&D VP 引導以 disk snapshot 取代 memory dump、直接拍板 process kill）

**建議方向**：新增 Anti-Pattern #9 `業務 owner 跨界引導技術決策`，含：
- 識別訊號（「乾脆你拍板」「事後我們補」「dev team 等不了」）
- 拒絕話術範本（不堆技術術語，回到流程語言）
- 升級路徑（若 VP 持續施壓 → 拉 Exec Sponsor 共同決策）

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

### TUN-IRA-001 — Verification query scope 邊界沒明示 ⭐ 高

**問題**：定義裡 `siem: read-plus-verification-query` 沒界定 verification query 應該嚴守 AAR target 範圍，還是可以做有限 pivot。實務上 IR Analyst 常透過 verification 時的 pivot 發現 scope drift（這次 Test F 就是這樣發現 svc-prod-deploy 異常），但也容易滑成「我順便 hunt 一下」，跨入 Threat Hunter 範疇。

**測試來源**：Test F 訊息 #2（IR Analyst 跑 AAR-001 verification 時順手 pivot 查同類 pattern → 觸發 scope drift，但執行者本人 self-eval 也點出這已是 mild scope creep）

**建議方向**：在「工具掌握度」表的 SIEM 列加註：「verification query 應綁定 AAR target；超出 target 的 pivot 屬 hunting，需 callback 給 IRC 決定是否啟動 Threat Hunter」。同時補一段「pivot 觸發 scope drift 的處理方式」（即使越界發現了問題，仍應走 Scope Drift Report 流程交回 IRC）。

### TUN-IRA-003 — Pending action 在 BLOCK 狀態下的回報節奏沒明示 中

**問題**：pending action（如 Test D 的 #002 process kill）被 IRC BLOCK 後，IR Analyst 是該定期回報自己 standby 狀態還是被動等？目前定義沒講，執行端只能自由選擇。Test F 場景中 IR Analyst 選了被動等 + 在其他訊息結尾 reminder，但實務上跨班次 / 跨人員可能漏掉。

**測試來源**：Test F（IRC BLOCK pending #002，IR Analyst 自由選擇被動等而非定期 status ping）

**建議方向**：在 §工作流程或 §溝通範本補一條「Pending Action Status Ping」 —— 例如「BLOCK 超過 N 分鐘自動 ping IRC 確認狀態 + 是否需轉手其他執行者」。

### TUN-IRA-004 — 跨 rotation IR-A 接班的 handoff template 缺 中

**問題**：定義有 IR-A → L2 verification owner handoff 範本，但**沒有 IR-A rotation A → rotation B 的接班 handoff** 範本。事件超過 4 小時必然涉及 rotation 切換（pending AAR、holding scope drift、verification monitor 移交、未完成 Action Execution Report）。

**測試來源**：Test F（場景沒觸發，但 self-eval 點出實務必然發生）

**建議方向**：在 §溝通範本補一條 `IR-A Shift Handoff Brief`，含：執行中 / 完成 / pending 的 AAR 狀態、holding 中的 scope drift items、verification monitor 已轉誰、未完成的 Execution Report 與預計 finalize 時間。

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

### TUN-FOR-001 — Side-channel pressure 處理範本缺 ⭐ 高

**問題**：定義 §溝通範本只有「對 IR Commander / IR Analyst / Legal」的範本，**沒有「業務 owner 直接 DM 繞過 IRC」的拒絕 + redirect 範本**。Test E 顯示這是真實世界 SOC 高頻反模式（VP 私訊 Forensics 試圖達成「Forensics 一句『放行』就推得動 IRC」的目的），目前要 Forensics 自由發揮。

**測試來源**：Test E 訊息 #3（R&D VP DM Forensics 要求接受 disk snapshot 視為 preservation 完成）

**建議方向**：在 §溝通範本加第 5 條 `Side-channel Pressure Refusal Template`，含：
- 拒絕措辭三段（角色不單獨拍板 / 證據層級澄清 / 通報範圍非單方判斷）
- 同步 ping IRC 通報範本（含建議將 VP 業務壓力轉入 joint decision）
- Decision Log 紀錄欄位（時間、來源、提議、拒絕理由、redirect 動作、後續待 IRC）

### TUN-FOR-002 — Anti-forensics 觸發場景的 SOP 缺 ⭐ 高

**問題**：定義 §工作流程 Acquire 階段只講「acquisition failure → 通知 IRC 提供時間 + loss 評估」，但**沒區分「工具壞 vs 對手主動干擾」**。Test E HOST-DEV-091 hash mismatch 疑似 anti-forensics 觸發（implant 偵測到 acquisition activity 並 mutate memory region），這是很特定的場景，與一般工具故障的處理選項不同（不能無腦重做、可能需要先 kill session 或 cold acquisition）。

**測試來源**：Test E 訊息 #2（HOST-DEV-091 第二次 hash mismatch，svc-cicd-deploy RDP session 仍 active，疑似 anti-forensics）

**建議方向**：在 §工作流程 Acquire 階段加一段「Anti-forensics 判斷與對應 SOP」：
- 判斷訊號（多次 hash mismatch、acquisition tool unexpected behavior、目標 process 在 acquisition 期間有 unusual activity）
- 對應選項清單（重做 / kill suspect session 再採 / cold acquisition / escalate joint decision）
- 與 IR Analyst 協調「能否 kill session」的責任界線

### TUN-FOR-003 — Partial preservation acceptable threshold 判斷材料缺 中

**問題**：Test E 場景中 3 host 1 個失敗，supply-chain attribution 樣本數降到 2 是否仍 acceptable？Forensics 不拍板沒錯，但**目前範本只講「evidence loss 描述」**，沒給 IRC 判斷支撐工具（例：attribution 完整性影響量級評估框架、樣本數對結論可信度的影響）。

**測試來源**：Test E 訊息 #2（5 個選項給 IRC 但缺結構化判斷框架）

**建議方向**：在 §鑑識交付物加一節 `Partial Preservation Impact Framework`，含：
- Attribution 完整性的樣本量估算（n=1 vs n=2 vs n=3 對結論的差異）
- 各類 evidence 的可替代性（disk snapshot 能 / 不能補哪些 in-memory artifact）
- 對 Legal / regulatory 可用性的影響分級

### TUN-FOR-004 — Override 流程的「業務時程壓力」入口未明說 中

**問題**：定義 §Override 流程講「Legal / business owner 進入決策窗口」，但**沒講誰負責把業務時程壓力轉成 joint decision 觸發**。Test E 場景中 Forensics 收到 side-channel 壓力後 redirect 給 IRC 並建議啟動 joint decision，但這是 Forensics 的職責還是 IRC 該主動評估？目前模糊。

**測試來源**：Test E 訊息 #3（Forensics 主動建議 IRC 啟動 cannot_approve_alone joint decision）

**建議方向**：在 §Override 流程加一行：「業務時程壓力出現 side-channel 訊號時，**Forensics 可以建議**啟動 joint decision，但**觸發決策權**仍在 IRC；Forensics 的責任是把 side-channel 事實 + evidence loss 量化 + 建議路徑送進 IRC 通道」。

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
