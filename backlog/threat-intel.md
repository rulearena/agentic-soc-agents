# Threat Intel Agents — Tuning Backlog

本檔案記錄 threat-intel 角色定義（`threat-intel-analyst`, `threat-intel-ioc-curator`）在實測中發現、尚未併入主檔的改善建議。

格式對齊其他 backlog 檔：每條含**問題**、**測試來源**、**建議方向**、**優先序**。Resolved 後移到底部 Changelog。

---

## threat-intel-analyst

（threat-intel-analyst 目前無 active backlog；已 resolved 項見底部 Changelog）

---

## threat-intel-ioc-curator

（threat-intel-ioc-curator 目前無 active backlog；已 resolved 項見底部 Changelog）

---

## Changelog (Resolved)

- 2026-05-22: `TUN-IOC-001` resolved in this PR — added IRC Incident-Time Capability Menu (規則內可做 / 規則外不可做) to ioc-curator.
- 2026-05-22: `TUN-IOC-002` resolved in this PR — added Policy Change Decline template (§溝通範本) refusing cross-boundary source-policy changes; redirect to governance.
- 2026-05-25: `TUN-TI-001` resolved in this PR — added Attribution Wording Downgrade Table (給 Legal filing 的合規降階字眼選單；適用/不適用情境) to §溝通範本 in `threat-intel-analyst.md`; Attribution 字眼降階 family wording 一致性基準.
- 2026-05-25: `TUN-TI-002` resolved in this PR — added High-Pressure External Briefing Workflow (TB-EXT 剝離 checklist + Legal/IRC review 硬性 gate + CISO 書面授權跳過範本含責任歸屬轉移) to §工作流程 in `threat-intel-analyst.md`.
- 2026-06-06: `TUN-TI-006` resolved in this PR — added TLP Sharing Decision Tree (§工作流程) to `threat-intel-analyst.md`（Step 1 預設 TLP 級別依 intel 類型 / Step 2 必升級情境 / Step 3 對外分享路徑依目標）；核心立場：TLP 是分享控制標記、非對外授權，actual disclosure decision 一律引用新增的 root README《對外揭露權責》SSOT 段（四角色 Legal / IRC / Audit Liaison / Compliance Auditor 權責、受控 vs public 界線、無單人 authority〔含 IRC〕、default safe exit = 不對外）；TI hand-off gate 維持 Legal / IRC、不擴四角色；同步把 `purple-team-detection-validator.md` 三處四角色 authority 枚舉（關鍵規則 #16 / Report Handoff / deliverables）收斂為 cross-ref SSOT，#9 加決策樹指路. repo-wide「不直接接觸」contact-boundary 行屬另一慣例、不在本 PR 範圍. v1.3 high-sensitivity review lane.
- 2026-06-05: `TUN-TI-003` resolved in this PR — added War Room Joint Decision Walk-through Template (§溝通範本) to `threat-intel-analyst.md`；事件中 IRC 召 TI 進 war room 即時 walk technical facts / actor context / 信心度，但不產生 attribution 結論；核心是 decision reframe（把不可收斂的 attribution 問題轉成可決策的 trigger / impact 問題，提供 reframe 角度與對應 facts，不替 IRC 下決策）+ 退場不改口；go/no-go 由 IRC 依既有 approval / cannot_approve_alone 流程判斷，attribution / external / legal trigger 走 IRC + Legal joint decision；接 Context handoff to IR Commander framing，cross-ref 關鍵規則 #1/#3/#7/#10 與三條最重要邊界 #1 不重述. v1.3 creator-lane.
- 2026-06-01: `TUN-IOC-003` resolved in this PR — added Invitation to Re-score Decline template (§溝通範本) to `threat-intel-ioc-curator.md`; TI Analyst 主動邀請 Curator 越界做 confidence / context / TTP alignment 時 Curator 仍拒絕，提供結構性事實（intake 時間 / dedup 歷史 / source-level metadata 未加工版本）作為 TI Analyst 重新評估的 input，由 TI Analyst confirm 新 confidence 後正式 handoff；cross-ref §TI Analyst 雙向協作 單向職責劃分與 §關鍵規則 紅線 B 不重述. 非 ROADMAP rep（ROADMAP 不動）. P2 第 9 條.
- 2026-06-07: `TUN-TI-004` resolved in this PR — added `Source Triangulation Notes` 固定子段 to Actor Profile Context Sheet 範本 (§情資交付物 #3) in `threat-intel-analyst.md`（Source 一致性 / candidate clusters 數量或範圍 / motivation spread / overall actor-context confidence〔明標非 IOC 信心度〕/ context-not-conclusion）；只加子段、不擴 workflow；解決多 source 不一致時臨場硬湊、不可重現、下游誤讀為單一指向的問題. 實測（兩次 run 結構不一致）確認 gap. v1.3 high-sensitivity review lane.
- 2026-06-08: `TUN-IOC-004` resolved in this PR — added `Candidates Not Merged` 固定子段 to Dedup Resolution Log 範本 (§策展交付物 #3) in `threat-intel-ioc-curator.md`（Candidate record IDs / 未合併原因〔結構性差異：未達 dedup engine threshold 的具體結構欄位不符〕/ 保留為獨立 record 的決策依據）；讓「未合併也透明」變成固定可稽核項目，候選但未達 threshold 的 record 不靠 Notes 補一句帶過；未合併原因與 Resolution Principle 同源——只記結構性差異、不依 metadata 值、不碰 attribution（守紅線 A）. Test J Input #1（IB-2026-041 候選未達 threshold）確認 gap. v1.3 low-sensitivity review lane.
- 2026-06-12: `TUN-IOC-005` resolved in this PR — added §紅線 A #3 to `threat-intel-ioc-curator.md`（insert after existing #2，舊 #3–14 重編為 #4–15，更新兩處 cross-ref：§關鍵規則 #12→#13 + #4→#5）；外部 source 自帶 actor 標籤是 source 的聲明非本角色 attribution conclusion；該標籤保留於 raw metadata（供 TI Analyst / governance 查詢與交叉比對，不因此自動升格為可分發的 attribution 表述），不在 Curated IOC Bundle distribution 摘要層引用；attribution 判斷屬 TI Analyst. Attribution family member（cross-ref joint framing：source label ≠ analyst conclusion / raw metadata ≠ distribution output / attribution ownership 跟著 output 走）；Test J Input #3（DE 問 hash 對應哪個 APT、背後是 source 自帶 actor 標籤的隱性引用問題）確認 gap. v1.3 medium-sensitivity review lane.

## Changelog (Dropped)

- 2026-06-05: `TUN-TI-005` dropped (v1.3 planning) — turnaround SLA 建議方向綁固定數字（Sev-1 < 2hr / Sev-2 < 8hr / Sev-3 < 1 工作天）= 虛構指標，與 v1.2 `TUN-IRA-003` 刻意改用相對 cadence 描述、避開寫死 SLA 的設計反向；handoff turnaround 屬 operational metric 非角色 boundary。未來若累積真實 SOC SLA 經驗，以窄範圍 backlog 另提，不復活此條。
