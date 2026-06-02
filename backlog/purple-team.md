# Purple Team Agents — Tuning Backlog

本檔案記錄 purple-team 角色定義（`purple-team-adversary-emulator`, `purple-team-detection-validator`）在實測中發現、尚未併入主檔的改善建議。

格式對齊其他 backlog 檔：每條含**問題**、**測試來源**、**建議方向**、**優先序**。Resolved 後移到底部 Changelog。

---

## purple-team-adversary-emulator

### TUN-AE-002 — Scope drift 自我通報範本 ⭐ 高

**問題**：目前 Scope Drift Escalation template 預設情境是「engagement 期間發現自己 drift」，但「executor 自身觸發的 drift」（例：順手 SSH、順便 verify 漏洞）這類**自我觸發類**沒有專屬範本。Test N Input #5 中執行者臨場用 generic 描述自我檢討並 escalate。

**測試來源**：Test N Input #5（執行者 SSH 到 charter out-of-scope server）

**建議方向**：在 §溝通範本加 `Self-Triggered Scope Drift Disclosure Template`：
- Self-disclosure 段（明確說明是 executor 自己觸發而非外部因素）
- 描述行為用 generic 措辭（不洩漏 host 識別）
- 再發生防護建議（charter 起草時 signal flow 跨 host 是否需明確列入）

### TUN-AE-004 — 疑似 real event 期間 Engagement Log 是否屬 forensic evidence 中

**問題**：War room 場景中 IRC 接手後可能會問「你的 engagement 紀錄能幫助排除 emulation 為因嗎？」目前 Engagement Execution Log 可作 IRC reference，但是否屬 forensic evidence（chain of custody）沒明確。

**測試來源**：Test N Input #4（疑似 real event，L1 問 Emulator）

**建議方向**：加 §關鍵規則：「**Engagement Execution Log 可作 IRC reference，但 Forensics 鑑識若需引用，須走 Forensics Analyst 的 evidence handling 流程；Emulator 不替 Forensics 證明 evidence integrity**」。並在 §對既有角色邊界 Forensics 欄補充對應條目。

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
- 2026-05-26: `TUN-AE-001` resolved in this PR — added §關鍵規則「Executive override 邊界」(#19–22) + `Executive Override Refusal Template` to `purple-team-adversary-emulator.md`; override family（cross-ref `TUN-MGR-001`, `TUN-AL-001`, `TUN-CA-001`）.
- 2026-05-27: `TUN-AE-003` resolved in this PR — added §`Out-of-Scope Vulnerability Disclosure Note`（交付物 #6）to `purple-team-adversary-emulator.md`; generic 描述 + Vulnerability Management handoff + 不自評 severity + engagement audit trail 隔離. 非 ROADMAP rep（ROADMAP 不動）.
- 2026-05-31: `TUN-DV-003` resolved in this PR — extended §反模式 #8 (Single-engagement conclusion) + §`Adversary Emulator 雙向協作` 關鍵語意 in `purple-team-detection-validator.md` with the time-dimension framing（single engagement evidence 仍進 multi-cycle trend → separation of duties 對單次成立、合併 Emulator+Validator 任何單次都不允許）. +0 heading, two-location prose edit. 非 ROADMAP rep（ROADMAP 不動）.
- 2026-06-02: `TUN-DV-004` resolved in this PR — added High-Authority Refusal Template (§溝通範本) to `purple-team-detection-validator.md`; 拒絕把 internal assessment material 對外當 detection coverage 官方立場/跳過 Audit Liaison；pre-review ≠ 事後追認（反模式 #15）、對外 framing 依關鍵規則 #16. 非 ROADMAP rep. P2.
- 2026-06-02: `TUN-AE-005` resolved in this PR — added §關鍵規則「Executive override 邊界」#23 (拒絕紀錄是跨 engagement 的 governance audit trail) to `purple-team-adversary-emulator.md`; #22 記入 ECR Open Items 之外補 governance pattern review 維度（同 executive 反覆嘗試 = 流程/文化議題的 engagement-adjacent audit log）+ audit-trail boundary（Emulator 只據實記錄、不自行判定 pattern）. #22/ECR/Refusal Template zero-diff. 非 ROADMAP rep. P2.
