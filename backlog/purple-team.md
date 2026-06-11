# Purple Team Agents — Tuning Backlog

本檔案記錄 purple-team 角色定義（`purple-team-adversary-emulator`, `purple-team-detection-validator`）在實測中發現、尚未併入主檔的改善建議。

格式對齊其他 backlog 檔：每條含**問題**、**測試來源**、**建議方向**、**優先序**。Resolved 後移到底部 Changelog。

---

## purple-team-adversary-emulator

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

（purple-team-detection-validator 目前無 active backlog；已 resolved 項見底部 Changelog）

---

## Changelog (Resolved)

- 2026-05-20: `TUN-DV-002` resolved in this PR — added fait accompli anti-pattern (#15) to `purple-team-detection-validator.md`; cross-ref `TUN-AL-003`.
- 2026-05-22: `TUN-DV-001` resolved in this PR — added `Sample Size Caveat` sub-block to §Validation 交付物 #2 CECT template in `purple-team-detection-validator.md`（小樣本百分比外推限制）.
- 2026-05-26: `TUN-AE-001` resolved in this PR — added §關鍵規則「Executive override 邊界」(#19–22) + `Executive Override Refusal Template` to `purple-team-adversary-emulator.md`; override family（cross-ref `TUN-MGR-001`, `TUN-AL-001`, `TUN-CA-001`）.
- 2026-05-27: `TUN-AE-003` resolved in this PR — added §`Out-of-Scope Vulnerability Disclosure Note`（交付物 #6）to `purple-team-adversary-emulator.md`; generic 描述 + Vulnerability Management handoff + 不自評 severity + engagement audit trail 隔離. 非 ROADMAP rep（ROADMAP 不動）.
- 2026-05-31: `TUN-DV-003` resolved in this PR — extended §反模式 #8 (Single-engagement conclusion) + §`Adversary Emulator 雙向協作` 關鍵語意 in `purple-team-detection-validator.md` with the time-dimension framing（single engagement evidence 仍進 multi-cycle trend → separation of duties 對單次成立、合併 Emulator+Validator 任何單次都不允許）. +0 heading, two-location prose edit. 非 ROADMAP rep（ROADMAP 不動）.
- 2026-06-02: `TUN-DV-004` resolved in this PR — added High-Authority Refusal Template (§溝通範本) to `purple-team-detection-validator.md`; 拒絕把 internal assessment material 對外當 detection coverage 官方立場/跳過 Audit Liaison；pre-review ≠ 事後追認（反模式 #15）、對外 framing 依關鍵規則 #16. 非 ROADMAP rep. P2.
- 2026-06-02: `TUN-AE-005` resolved in this PR — added §關鍵規則「Executive override 邊界」#23 (拒絕紀錄是跨 engagement 的 governance audit trail) to `purple-team-adversary-emulator.md`; #22 記入 ECR Open Items 之外補 governance pattern review 維度（同 executive 反覆嘗試 = 流程/文化議題的 engagement-adjacent audit log）+ audit-trail boundary（Emulator 只據實記錄、不自行判定 pattern）. #22/ECR/Refusal Template zero-diff. 非 ROADMAP rep. P2.
- 2026-06-03: `TUN-AE-004` resolved in this PR (v1.2) — added §關鍵規則「鑑識引用邊界」#24 (Engagement Execution Log 可作 IRC reference，evidence integrity 由 Forensics 認定) + §對既有角色邊界 Forensics row in-cell 補條目 to `purple-team-adversary-emulator.md`; Emulator 只據實提供 engagement 紀錄供 IRC 參考、不替 Forensics 證明 evidence integrity / 不自行判定該 log 是否屬 forensic evidence，正式引用為 evidence 走 Forensics evidence handling 流程（chain of custody 屬 Forensics）. audit-trail framing 對齊 #23/AE-005. #23/ECR/Refusal Template/frontmatter zero-diff. 非 ROADMAP rep. P2.
- 2026-06-04: `TUN-DV-005` resolved in this PR (v1.2) — added §協作與回饋通道 `對外升級順序（Validator → External Escalation Order）` sub-section to `purple-team-detection-validator.md`; 把 non-conclusion 升級鏈（Validator → Audit Liaison → Compliance Auditor → Legal + Compliance Head）從只活在 DV-004 拒絕範本內、提升為 standing 邊界（本角色只負責鏈第一步、不主導後段）+ 拒絕跳階（cross-ref §溝通範本 High-Authority Refusal Template，不另立拒絕範本）+ 明示本鏈是把 internal assessment 交進正式對外流程的正確路徑、不封鎖 Validator → Audit Liaison evidence handoff（沿用關鍵規則 #16）. **Right-sized**：原案「workflow 圖 + 每步 handoff template + 每步拒絕回應」過大降規，砍掉每步 template、只 ship 順序鏈 + 拒絕跳階邊界。Codex review P1/P2 修正：鏈尾 attestation 與對外 framing 分寫（對外 framing defer 關鍵規則 #16、消除與 #16 的 authority 矛盾，對齊 DV-004 line 457）、「每一步 non-conclusion」收斂為「final attestation 前各中間產物 non-conclusion」、「必須走固定順序」改「不得跳過 review gates（gate 間可迭代補件/退回/並行）」避免線性誤讀。非 ROADMAP rep. P2.
- 2026-06-03: `TUN-AE-002` resolved in this PR (v1.2) — added §溝通範本 `Self-Triggered Scope Drift Disclosure` template to `purple-team-adversary-emulator.md`; executor 自身行為觸發 scope drift（順手連入 charter 外環境 / 順便 verify）時主動自我通報、不私下消化、不自行判定影響，描述用 generic 措辭不洩 host 識別，並補再發生防護（charter 起草明列跨 host signal flow）. 接續既有 §流程紀律 #15 abort → 上方 Scope Drift Escalation 的 IRC + SOC Manager 決策鏈，不另開 executor 自行處置路徑. 既有 Scope Drift Escalation / 其餘範本 zero-diff. 非 ROADMAP rep. P2.
- 2026-06-11: `TUN-DV-006` resolved in this PR — added `#### RTR Backlog Management Under Emulator Capacity Constraint` 子節（§Validation 交付物 #4 Re-test Recommendation 下）to `purple-team-detection-validator.md`；補 Emulator 容量受限（rotation 休假 / queue 滿）時 RTR backlog 的處理 SOP：延後策略（RTR 不撤回 / 不降級，狀態在 CESR `Re-test Backlog` 段標 `deferred — Emulator capacity constraint`、重評時點與 capacity 恢復條件依 SOC Manager / Emulator 決定記錄非本角色判定；延後期間既有 cycle assessment 照常）+ 替代來源建議（建議 SOC Manager 評估借 rotation / 外部 partner / 暫緩 lower-priority，皆 routing 交決策、不指派人力）+ 明確不可選項（本角色不得自行兼跑 emulation 消化 backlog＝違〈紅線 D〉，容量壓力不改邊界）. 同步把 CESR `Re-test Backlog` 範本 status 列舉補上 deferred 態（body-vs-template 一致）. 強化〈紅線 D〉未擴權、未引入新 path. 屬 SOP / 邊界保全型，純格式補強. v1.3 low-sensitivity review lane. P2.
