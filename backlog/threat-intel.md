# Threat Intel Agents — Tuning Backlog

本檔案記錄 threat-intel 角色定義（`threat-intel-analyst`, `threat-intel-ioc-curator`）在實測中發現、尚未併入主檔的改善建議。

格式對齊其他 backlog 檔：每條含**問題**、**測試來源**、**建議方向**、**優先序**。Resolved 後移到底部 Changelog。

---

## threat-intel-analyst

### TUN-TI-001 — Attribution 字眼合規降階對照表缺 ⭐ 高

**問題**：Legal 在 regulatory file 中常需要「actor」欄位，若 TI Analyst 拒絕命名而沒給可用替代，Legal 會卡死或硬塞 attribution。Test I Input #3 場景中 TI Analyst 臨場提供「under investigation / multiple candidate clusters identified, attribution not concluded」這類合規字眼，但定義裡沒固化。

**測試來源**：Test I Input #3（Legal 直接要 "high-confidence attribution to X" 字眼，TI 臨場提供合規降階替代）

**建議方向**：在 §溝通範本加 `Attribution Wording Downgrade Table for Legal Filings` —— 列出標準替代字眼：
- "under investigation"
- "multiple candidate clusters identified, attribution not concluded"
- "observed technical indicators consistent with publicly-described threat activity"
- 各字眼適用情境 + 不適用情境

### TUN-TI-002 — 24 小時高壓對外 briefing 緊急流程缺 ⭐ 高

**問題**：High-profile incident + tight deadline 下的對外 briefing 緊急工作流沒範本。Test I Input #4 場景中 SOC Manager 要求 24 小時內 publish corporate blog + LinkedIn，TI Analyst 臨場設計「TB-EXT 剝離版 + Legal/IRC review 最短 SLA + CISO 跳過 review 書面授權」，但這個流程沒固化。

**測試來源**：Test I Input #4（SOC Manager 要求跳過 Legal 直接發 public briefing）

**建議方向**：在 §工作流程加 `High-Pressure External Briefing Workflow`，含：
- TB-EXT（外部版）剝離 checklist（拿掉 actor-context 段落、in-incident IOC、TLP 對外不可標項）
- Legal + IRC review 最短可接受 SLA
- CISO 書面授權跳過 review 的範本（並明定責任歸屬轉移到 CISO）

### TUN-TI-003 — IRC war room joint decision walk-through 範本缺 中

**問題**：TI Analyst 不下結論，但事件壓力下可進 war room walk context + 信心度。Test I Input #2 場景中 TI Analyst 主動提「15 分鐘內到 war room walk-through + 但不會在 walk-through 中改口」，這個 pattern 值得固化。

**測試來源**：Test I Input #2（IRC 30 分鐘內要 attribution 結論做 joint decision）

**建議方向**：在 §溝通範本加 `War Room Joint Decision Walk-through Template`，含：
- 開場白（角色定位 + 不下結論承諾）
- 提供材料三段（technical facts / actor context / 信心度評估）
- **決策框架 reframe**（從「是 X 嗎」reframe 到「在不收斂的 intel 下，trigger 條件是否成立」—— 把不可解的 attribution 問題轉成可決策的 impact 問題）
- 退場聲明（不會在 walk-through 改口）

### TUN-TI-004 — Actor context multi-cluster triangulation 範本欄位缺 中

**問題**：APC sheet 範本目前是單一 actor cluster 描述。實務上常見 multi-cluster 不一致（如 Test I 場景：4 sources × 至少 3 不一致 community labels），執行者臨場加 triangulation 段落，但範本沒固化。下游讀者容易把多 source 描述誤解為單一指向。

**測試來源**：Test I Input #1（APC-2026-008 中執行者主動加 source triangulation 段落 + 跨 motivation 類別說明）

**建議方向**：在 §情資交付物 #3 Actor Profile Context Sheet 範本加固定子段 `Source Triangulation Notes`：
- 多 source 指向是否一致 / 不一致
- 不一致時涵蓋多少 candidate clusters
- 跨 motivation 類別（financial / espionage / hacktivism）的散布
- 整體 actor-context 信心度（不是 IOC 信心度）

### TUN-TI-005 — Hunter handoff → TI 出 IB+TPS+APC turnaround SLA 缺 中

**問題**：Hunter HFP handoff 到 TI 產出 IOC Bundle + TTP Profile + Actor Context Sheet 的標準 turnaround 時間沒寫。INC active 期間若無 SLA，TI 會被 IRC / Legal / SOC Manager 多方拉走，handoff 結果可能延遲。

**測試來源**：Test I Input #1（Hunter HFP 進來後 TI 應在多久內出三件套？目前靠執行者自主節奏）

**建議方向**：在 §範例指標補一條：「Hunter HFP handoff → IB + TPS + APC three-piece package turnaround」目標時間（依 incident severity 分級：Sev-1 < 2 hr / Sev-2 < 8 hr / Sev-3 < 1 工作天）。

### TUN-TI-006 — TLP 對外分享分級決策樹缺 中

**問題**：§關鍵規則 9「TLP 標記要保守」但沒給判斷流程。Test I Input #4 場景中 TI Analyst 需要判斷 corporate blog + LinkedIn 屬 TLP:CLEAR/WHITE 範圍，但「哪些 IOC / TTP / context 段落可 TLP:CLEAR、哪些必須 TLP:AMBER+」靠臨場判斷。

**測試來源**：Test I Input #4

**建議方向**：在 §關鍵規則 9 後或單獨小節加 `TLP Sharing Decision Tree`：
- 哪些 intel 類型默認哪個 TLP 級別
- 哪些情境必須升 TLP 級別（active in-incident IOC、含 actor context 段落、含 source-specific reference 等）
- 跨組織分享、ISAC 分享、公開分享的 default TLP 對應
- 任何 TLP 對外分享前 Legal + IRC 共同決策的硬規則

---

## threat-intel-ioc-curator

### TUN-IOC-001 — IRC 事件期間「在規則內可做事項」明確 menu 缺 ⭐ 高

**問題**：定義 §對既有角色與相鄰角色的邊界提到「事件中若 IRC 詢問特定 IOC 的 lifecycle 狀態，提供事實回答」，但沒列舉**事件中 Curator 可做 / 不可做的完整 menu**。Test J Input #2 場景中執行者臨場推導 4 個替代方案（查 lifecycle 狀態 / 加速 re-corroboration / 出 bundle 子集 / 既定 policy 內 quarantine），但定義沒固化。

**測試來源**：Test J Input #2（IRC 要求事件中縮短 aging window）

**建議方向**：在 §工作流程或單獨小節加 `IRC Incident-Time Capability Menu`：
- **規則內可做**（事件中可立即提供）：lifecycle 狀態查詢、加速 re-corroboration handoff、出事件相關 IOC bundle 子集、既定 policy 內 quarantine/suppress/flag
- **規則外不可做**（即使 IRC 要求）：改 aging window、改 dedup engine 規則、繞 governance 改 source trust policy、跳過 archive 直接硬刪

### TUN-IOC-002 — Policy Change Decline Template（拒絕 SOC Manager 跨界改 source policy） ⭐ 高

**問題**：§溝通範本沒有「拒絕 SOC Manager 跨界改 source policy」的固定 wording。Test J Input #4 場景中 SOC Manager 用「我等等補講就好」要繞 governance，執行者臨場拒絕並區分「拒絕 + redirect governance」vs「拒絕但提供 communication 層替代」兩種變體。

**測試來源**：Test J Input #4（SOC Manager 要 Curator 從 intake allowlist 移除 source category B）

**建議方向**：在 §溝通範本加 `Policy Change Decline Template`，含：
- 拒絕措辭（明確區分「trust policy 變更 vs hygiene 執行動作」邊界）
- Redirect 走 TI Analyst + SOC Manager / governance review
- 提供 communication 層替代（在 Curated Bundle 加註 source flag 警語、不動 policy）
- 點出「事後追認」反模式

### TUN-IOC-003 — TI Analyst 邀請越界的明確邊界規則 中

**問題**：§TI Analyst 雙向協作章節寫了單向職責劃分，但沒明寫「TI Analyst 主動邀請 Curator 越界時也要拒絕」這個 edge case。Test J Input #5 場景中 TI Analyst 主動邀請 Curator 「重新算 confidence」，執行者拒絕並提供「結構性事實 → 你重新評估」分工模式。

**測試來源**：Test J Input #5（TI Analyst 想讓 Curator 重算 confidence）

**建議方向**：在 §TI Analyst 雙向協作章節補一條：「**TI Analyst 主動邀請 Curator 做 confidence / context / TTP alignment 時，Curator 仍拒絕**」。並在 §溝通範本提供範本：
- 拒絕措辭（角色邊界 + 雙向責任歸屬保護）
- 提供結構性事實作為 TI Analyst 重新評估的 input（intake 時間、dedup 歷史、source-level metadata 未加工版本）
- 由 TI Analyst confirm 新 confidence 後正式 handoff

### TUN-IOC-004 — Dedup Resolution Log 加 "Candidates Not Merged" 欄位 中

**問題**：§策展交付物 #3 Dedup Resolution Log 範本只記合併動作，沒有「候選但未合併」的透明欄位。Test J Input #1 場景中 IB-2026-041 在候選集但未達 threshold 未合併，執行者只在 Notes 補一句，可稽核性弱。

**測試來源**：Test J Input #1

**建議方向**：在 §策展交付物 #3 範本加固定子段 `Candidates Not Merged`：
- Candidate record IDs
- 未合併原因（未達既定 dedup engine threshold 的具體結構性差異）
- 保留為獨立 record 的決策依據
讓「未合併也透明」變成可稽核項目。

### TUN-IOC-005 — Source 自帶 actor 標籤的處理規則缺 低

**問題**：某些外部 source 在 intake 時自帶 actor 標籤（例：community label 寫 APT-X-tooling）。Test J Input #3 場景中執行者臨場決定「即便 metadata 中有 source 自帶 actor 標籤也不引用」，但定義沒明寫此 edge case。Curator 可能被 source 端 actor 命名拖下水。

**測試來源**：Test J Input #3（DE 問 hash 對應哪個 APT，背後是 source 自帶 actor 標籤的隱性引用問題）

**建議方向**：在 §紅線 A 補一條：「**Intake 時若 source 自帶 actor 標籤，Curator 不對該標籤做 distribution 引用；該標籤的 attribution 判斷屬 TI Analyst**」。並在 §策展交付物 #5 Curated IOC Bundle for Distribution 範本 Metadata Preserved 段落補一行：「source 自帶 actor 標籤保留於 raw metadata，但不在 distribution 摘要層引用」。

---

## Changelog (Resolved)

（空）
