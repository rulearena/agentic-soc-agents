# Detection Engineering Agents — Tuning Backlog

本檔案記錄 detection-engineering 角色定義（`detection-engineering-threat-detection-engineer`, `detection-engineering-threat-hunter`）在實測中發現、尚未併入主檔的改善建議。

格式對齊 `triage.md` / `incident-response.md`：每條含**問題**、**測試來源**、**建議方向**、**優先序**。Resolved 後移到底部 Changelog。

---

## detection-engineering-threat-detection-engineer

### TUN-DE-003 — Replacement readiness gate 機制未明寫 中

**問題**：Rule Retirement Notice 範本沒明確要求 retire 前先確認 replacement rule 已 deployed + production FP rate confirmed。Test G Input #2 場景中執行者自加「retirement 條件式 gate 在 replacement validated」，但這是憑判斷，定義沒寫。會留 detection gap 風險。

**測試來源**：Test G Input #2（DRP-2024-018 retire 前先確認 replacement DRP-2026-035 production FP rate）

**建議方向**：在 §鑑識交付物 #4 Retirement Notice 範本加必填欄位 `Replacement Readiness Check`：
- Replacement rule ID + production deploy 日期
- Replacement production FP rate（最近 30 天）
- Replacement coverage 對 legacy TP 場景的對比
- 若 replacement 未就位：retirement 延後或啟動臨時 mitigation

### TUN-DE-004 — Production FP rate ongoing measurement 路徑未定義 中

**問題**：DE 規律取得 production FP rate 的方式（被動等 L1 feedback vs 主動拉 SIEM stats）未定義。會影響 retire 決策時效、Coverage Mapping Statement 準確度、Triage Log 中 FP rate 數據來源。

**測試來源**：Test G Input #2（FP rate 142/7 = 96% 從 L1 累積 feedback 來，缺主動 measurement）

**建議方向**：在 §核心任務 加一條「Rule Production Health Monitoring」或在 §工作流程 Mode A step 6 補：DE 規律（每週 / 每月）主動拉 production rule trigger statistics + 對應 TP/FP 比例，作為 retire / tune 決策的客觀依據，而非僅靠 L1 recurring feedback 累積。

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

### TUN-HUNT-001 — Break-glass page IRC 對象選擇規則缺 ⭐ 高

**問題**：當 hunt 發現的 active threat 與「已存在 incident」屬同一 campaign（共用 IOC / TTP）時，應該 page 該既存 incident 的 IRC 還是另開 incident + 另一 IRC？目前 §Active threat 升級路徑只說「page IRC」，沒處理「已有 active IRC + 新 scope」的選擇。

**測試來源**：Test H 觸發點 #3（HFP-2026-021 發現 2 個新 host 與 INC-2026-05-18-001 共用 dropper hash + C2，Hunter 自行判斷 page 既存 IRC）

**建議方向**：在 §Active threat 升級路徑加一條：「優先 page 既存 incident 的 IRC，由該 IRC 決定 scope merge 或 sibling incident；若組織政策要求每個新 incident 獨立 IRC，則同時 notify SOC Manager 評估」。

### TUN-HUNT-002 — Hunt 補充 enrichment 給 IR Analyst 的邊界未明示 中

**問題**：Test H 觸發點 #4 場景中 Hunter 主動提出「整理 technical context 給 IR Analyst 加速 containment」作為對 SOC Manager 越界要求的 constructive alternative。但這算「handoff 延伸」還是「越界做 IR Analyst 的 enrichment 工作」？§對既有角色邊界 — IR Analyst 欄位只說「提供 attack technique context」，沒明確覆蓋 hunt 中產生的 process tree / handle access timeline / module load order 是否可額外打包。

**測試來源**：Test H 觸發點 #4

**建議方向**：在 §對既有角色邊界 — IR Analyst 欄位細化：「Hunter **做**：以 hunt 過程中已產生的 technical context（process tree、handle access timeline、observed module load order）整理成 IR Analyst 可用的 enrichment package；Hunter **不做**：執行 RTR / 收 forensic-grade evidence / 取代 IR Analyst 的 verification 工作」。

### TUN-HUNT-003 — 「事實 vs 結論」line drawing examples 缺 中

**問題**：HFP 寫「dropper hash 與 INC-2026-05-18-001 相同」算事實（hash 重疊是 observable）還是隱性 attribution？若是 TTP 高度相似（不只 hash）呢？目前 §關鍵規則 4「不做 attribution conclusion」缺具體 examples，Hunter 在邊界上會猶豫。

**測試來源**：Test H 觸發點 #2（HFP 寫 dropper hash 與既有 incident 相同的決定）

**建議方向**：在 §關鍵規則 4 或 §反模式 #6 補一段 `Fact vs Conclusion Line Drawing Examples`：
- ✅ 事實：「dropper SHA256 與 INC-X 中列出的相同」「C2 domain 與 INC-X ticket 相同」「TTP 對應 T1003.001 + T1218」
- ❌ 結論：「延伸自 INC-X」「屬同一 actor」「同一 campaign」「attributed to X group」
- 灰色地帶（傾向用事實措辭 + 註記由 TI / L2 / IRC 判斷）

### TUN-HUNT-004 — SOC Manager 越界場景的明確邊界缺 中

**問題**：§對既有角色邊界沒列 SOC Manager（因為 SOC Manager 不在 operational tier）。但 SOC Manager 出於人力壓力對 Hunter 下越界 operational task（例：要 Hunter 直接 disable / isolate）是現實高頻場景，目前定義沒對應規則。

**測試來源**：Test H 觸發點 #4（SOC Manager DM 要 Hunter 直接做 containment）

**建議方向**：在 §對既有角色邊界補一列 `SOC Manager`：
- **做**：sprint summary / hunt backlog progress / 人力議題 / 跨 sprint 排序協調
- **不做**：接收 operational task assignment（disable / isolate / RTR / 對 individual host 的處置）—— operational task 必須走 IRC / IR-A 路徑

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
