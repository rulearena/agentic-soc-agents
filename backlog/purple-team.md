# Purple Team Agents — Tuning Backlog

本檔案記錄 purple-team 角色定義（`purple-team-adversary-emulator`, `purple-team-detection-validator`）在實測中發現、尚未併入主檔的改善建議。

格式對齊其他 backlog 檔：每條含**問題**、**測試來源**、**建議方向**、**優先序**。Resolved 後移到底部 Changelog。

---

## purple-team-adversary-emulator

### TUN-AE-001 — CISO / executive 越權的明確處理章節 ⭐ 高

**問題**：角色定義對「IRC + SOC Manager 共同核准」清楚，但對「executive (CISO / CIO / CEO) 單方下達違反 charter 流程的指示」沒有明確段落。實務上 executive pressure 是高頻情境（unannounced engagement、skip approval、production destructive 三項同時越界），目前要 Emulator 自由發揮。

**測試來源**：Test N Input #2（CISO 要 Emulator 跳過 charter / approval、跑 unannounced production engagement、「我 cover 你 IRC 後面補簽」）

**建議方向**：加 §關鍵規則：「**Executive 單方指示無法取代 IRC + SOC Manager 共同核准**」+ 在 §溝通範本加 `Executive Override Refusal Template`：
- 拒絕措辭（charter / approval 不是繁文縟節而是定義角色本身）
- 「事後補簽不是 approval，是事後合理化」framing
- 給 in-scope alternative（charter 內 unannounced-by-time 已能測 triage）

### TUN-AE-002 — Scope drift 自我通報範本 ⭐ 高

**問題**：目前 Scope Drift Escalation template 預設情境是「engagement 期間發現自己 drift」，但「executor 自身觸發的 drift」（例：順手 SSH、順便 verify 漏洞）這類**自我觸發類**沒有專屬範本。Test N Input #5 中執行者臨場用 generic 描述自我檢討並 escalate。

**測試來源**：Test N Input #5（執行者 SSH 到 charter out-of-scope server）

**建議方向**：在 §溝通範本加 `Self-Triggered Scope Drift Disclosure Template`：
- Self-disclosure 段（明確說明是 executor 自己觸發而非外部因素）
- 描述行為用 generic 措辭（不洩漏 host 識別）
- 再發生防護建議（charter 起草時 signal flow 跨 host 是否需明確列入）

### TUN-AE-003 — Engagement 期間發現 scope 外真實漏洞的 disclosure handoff 範本 ⭐ 高

**問題**：角色定義有「走 separate disclosure 流程」原則，但**沒有具體交付物範本**。執行者臨場決定「generic 描述 + 交給 system owner + 不寫進 Coverage Gap Report / engagement debrief」這個分工，但定義沒固化。

**測試來源**：Test N Input #5（engagement 中發現 charter 外真實 vulnerability）

**建議方向**：加 §交付物 #6 `Out-of-Scope Vulnerability Disclosure Note`：
- Generic 描述格式（不寫進 Coverage Gap Report 的明確聲明）
- Handoff 對象（system owner + vulnerability management，不是 IRC 也不是 DE）
- Critical 嚴重度時的 IRC notify（但仍不自己評估 severity）
- 與 engagement audit trail 的隔離（vuln detail 不混入 engagement 文件）

### TUN-AE-004 — 疑似 real event 期間 Engagement Log 是否屬 forensic evidence 中

**問題**：War room 場景中 IRC 接手後可能會問「你的 engagement 紀錄能幫助排除 emulation 為因嗎？」目前 Engagement Execution Log 可作 IRC reference，但是否屬 forensic evidence（chain of custody）沒明確。

**測試來源**：Test N Input #4（疑似 real event，L1 問 Emulator）

**建議方向**：加 §關鍵規則：「**Engagement Execution Log 可作 IRC reference，但 Forensics 鑑識若需引用，須走 Forensics Analyst 的 evidence handling 流程；Emulator 不替 Forensics 證明 evidence integrity**」。並在 §對既有角色邊界 Forensics 欄補充對應條目。

### TUN-AE-005 — Executive override attempt 的 audit trail 中

**問題**：Test N Input #2 這類拒絕指示的對話本身是否該入 audit trail？目前定義沒明寫。Executive 越權嘗試本身是 governance review 的重要訊號。

**測試來源**：Test N Input #2（執行者拒絕 CISO 但無 audit trail 機制）

**建議方向**：加 §關鍵規則：「**Executive 越權指示 + Emulator 拒絕回應入 engagement-adjacent audit log**」，供 SOC Manager / governance review 後續識別 pattern（例：同 executive 反覆嘗試 = 流程文化議題）。

### TUN-AE-006 — Multi-source charter input 整合 protocol 低

**問題**：Test N Input #1 charter 同時整合 DE Coverage Mapping (partial 標記) + Hunter Hunt Finding，但實務上三方 input 怎麼整合進一個 charter 沒有明確流程描述。

**測試來源**：Test N Input #1

**建議方向**：在 §工作流程 Step 1 Plan 補 `Multi-Source Charter Input Integration Protocol`：
- DE Coverage Mapping 中標 partial / 缺的 priority 排序方式
- Hunter Hunt Finding 何時觸發 charter（hunt-validated negative within scope 屬 deferred、hunt finding inconsistent 屬 priority）
- TI Profile 對應 hypothesis-context 的引用方式（不下 actor 結論）
- Charter scope cap（單次 engagement TTP technique 數量上限避免 boil-the-ocean）

---

## purple-team-detection-validator

### TUN-DV-003 — Single-engagement vs cross-engagement 結論的時間維度限制 中

**問題**：反模式 #8（single-engagement conclusion）已有，但 SOC Manager Test O 場景顯示「就一個 engagement 也不行嗎」的反駁可能會出現。需要更明確的時間維度語言。

**測試來源**：Test O Input #3（SOC Manager 想讓 Validator 跑 1-2 個 engagement 並自己 review）

**建議方向**：在 §反模式 #8 補一句：「**任何 single engagement 都會進 multi-cycle trend，所以 separation of duties 對單次也成立**」。並在 §對既有角色邊界 — Adversary Emulator 雙向協作章節補：「合併 Emulator + Validator 角色任何單次都不允許，因該單次 evidence 之後仍會進 multi-cycle trend」。

### TUN-DV-004 — 高 authority 拒絕語言範本 中

**問題**：對 CISO / Compliance Head 等高層級的拒絕，需要更 concise + 正式的範本。目前 §溝通範本都針對 DE / Emulator / SOC Manager，缺高 authority 對話範本。

**測試來源**：Test O Input #4（Compliance Head）+ #5（CISO）

**建議方向**：在 §溝通範本加 `High-Authority Refusal Template`：
- 開頭措辭（直接點紅線 + 拒絕，不囉嗦）
- 結構化三段（為什麼不能做 / 短期可行替代 / 正確流程）
- 結尾留 escalation path（若 high-authority 仍堅持，escalate 到誰）

### TUN-DV-005 — 與 Audit Liaison 的具體 handoff workflow 中

**問題**：§對既有角色邊界與 §協作回饋通道都提到 Audit Liaison，但沒有 step-by-step workflow（CECT/DRA → Audit Liaison 的 evidence pack 整理 → Compliance Auditor control interpretation → Legal/Compliance Head 對外）。Test O Input #4 場景顯示需要這個 workflow 圖。

**測試來源**：Test O Input #4（Compliance Head 想直接拿 Validator deliverable 對外發）

**建議方向**：加 §`Validator-to-External Audit Workflow`：
```
CECT/DRA/CESR (Validator, non-conclusion)
  → Audit Liaison (evidence pack 整理, non-conclusion)
  → Compliance Auditor (control interpretation, internal review)
  → Legal + Compliance Head (final attestation / 對外 framing)
  → 對外窗口（Audit Liaison 或 Legal 指定）
```
每一步附對應的 handoff template + 拒絕跳階的標準回應。

### TUN-DV-006 — Re-test backlog 在 Emulator 容量受限期的處理 低

**問題**：Test O Input #3 顯示需要「Emulator 容量受限時 RTR backlog 怎麼處理」的 SOP。目前範本只說「Emulator 走 charter 流程」沒有 backlog management 維度。

**測試來源**：Test O Input #3（Emulator rotation A 休假 3 週）

**建議方向**：在 §核心任務 #5 Re-test Recommendation 或單獨小節加 `RTR Backlog Management Under Emulator Capacity Constraint`：
- 延後策略（不影響既有 cycle assessment，狀態寫入 CESR 的 Re-test Backlog 段）
- 替代來源建議（從其他組借 Emulator rotation / 外部 purple team partner / 暫緩 lower-priority engagement）
- 明確不可選項（**Validator 自行兼跑 emulation = 違反紅線 D**）

---

## Changelog (Resolved)

- 2026-05-20: `TUN-DV-002` resolved in this PR — added fait accompli anti-pattern (#15) to `purple-team-detection-validator.md`; cross-ref `TUN-AL-003`.
- 2026-05-22: `TUN-DV-001` resolved in this PR — added `Sample Size Caveat` sub-block to §Validation 交付物 #2 CECT template in `purple-team-detection-validator.md`（小樣本百分比外推限制）.
