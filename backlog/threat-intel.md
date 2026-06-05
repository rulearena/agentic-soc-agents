# Threat Intel Agents — Tuning Backlog

本檔案記錄 threat-intel 角色定義（`threat-intel-analyst`, `threat-intel-ioc-curator`）在實測中發現、尚未併入主檔的改善建議。

格式對齊其他 backlog 檔：每條含**問題**、**測試來源**、**建議方向**、**優先序**。Resolved 後移到底部 Changelog。

---

## threat-intel-analyst

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

- 2026-05-22: `TUN-IOC-001` resolved in this PR — added IRC Incident-Time Capability Menu (規則內可做 / 規則外不可做) to ioc-curator.
- 2026-05-22: `TUN-IOC-002` resolved in this PR — added Policy Change Decline template (§溝通範本) refusing cross-boundary source-policy changes; redirect to governance.
- 2026-05-25: `TUN-TI-001` resolved in this PR — added Attribution Wording Downgrade Table (給 Legal filing 的合規降階字眼選單；適用/不適用情境) to §溝通範本 in `threat-intel-analyst.md`; Attribution 字眼降階 family wording 一致性基準.
- 2026-05-25: `TUN-TI-002` resolved in this PR — added High-Pressure External Briefing Workflow (TB-EXT 剝離 checklist + Legal/IRC review 硬性 gate + CISO 書面授權跳過範本含責任歸屬轉移) to §工作流程 in `threat-intel-analyst.md`.
- 2026-06-01: `TUN-IOC-003` resolved in this PR — added Invitation to Re-score Decline template (§溝通範本) to `threat-intel-ioc-curator.md`; TI Analyst 主動邀請 Curator 越界做 confidence / context / TTP alignment 時 Curator 仍拒絕，提供結構性事實（intake 時間 / dedup 歷史 / source-level metadata 未加工版本）作為 TI Analyst 重新評估的 input，由 TI Analyst confirm 新 confidence 後正式 handoff；cross-ref §TI Analyst 雙向協作 單向職責劃分與 §關鍵規則 紅線 B 不重述. 非 ROADMAP rep（ROADMAP 不動）. P2 第 9 條.

## Changelog (Dropped)

- 2026-06-05: `TUN-TI-005` dropped (v1.3 planning) — turnaround SLA 建議方向綁固定數字（Sev-1 < 2hr / Sev-2 < 8hr / Sev-3 < 1 工作天）= 虛構指標，與 v1.2 `TUN-IRA-003` 刻意改用相對 cadence 描述、避開寫死 SLA 的設計反向；handoff turnaround 屬 operational metric 非角色 boundary。未來若累積真實 SOC SLA 經驗，以窄範圍 backlog 另提，不復活此條。
