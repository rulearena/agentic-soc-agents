# Governance Agents — Tuning Backlog

本檔案記錄 governance 角色定義（`governance-soc-manager`, `governance-compliance-auditor`, `governance-audit-liaison`）在實測中發現、尚未併入主檔的改善建議。

格式對齊其他 backlog 檔：每條含**問題**、**測試來源**、**建議方向**、**優先序**。Resolved 後移到底部 Changelog。

---

## governance-soc-manager

### TUN-MGR-003 — Recognition framework 設計原則 ⭐ 高

**問題**：§13「不表揚 firefighting」是負面禁令，缺**正面 systemic recognition framework**：什麼樣的貢獻該被表揚、表揚機制如何避免變回 hero culture、spot bonus 與 systemic contribution award 的分工。Test K Input #5 中執行者臨場改寫表揚詞並設計分層處理（spot bonus 不阻擋 + 對外敘事抗 hero narrative + 暫緩 Hero of Quarter 獎項）。

**測試來源**：Test K Input #5（CISO 要表揚 IR Commander「30 小時連續處理」）

**建議方向**：加 §`Systemic Recognition Framework Design Principles`，含：
- 可表揚的 systemic contribution 類別（補 detection coverage gap / 修 process bottleneck / 主持成功 cross-role training / 提出被採納的 process improvement）
- 30 小時連續工作 = systemic failure signal 而非英雄事蹟的 reframe 邏輯
- 表揚詞範本（聚焦 systemic ability + 把 staffing 不足歸 governance 責任）

### TUN-MGR-005 — Metrics-to-performance 防火牆語言 中

**問題**：§關鍵規則 #12 是禁令「Metrics 不作為個人 performance 工具」，缺**具體話術 + 替代設計**。Test K Input #4 中執行者用四層 second-order effect 分析（action item 被做小 / TP rate 反向激勵 / hero culture 強化 / PIR 不誠實）說服 CISO，這個 framing 值得固化。

**測試來源**：Test K Input #4（CISO 要把 PIR action item closure rate + 個人 case TP rate 綁 bonus）

**建議方向**：在 §溝通範本加 `Metrics-Bonus Decoupling Template`，含：
- 結構化拒絕（四層 second-order effect 分析）
- Team-level systemic contribution metrics 範本（替代 individual KPI）
- Goodhart's Law 應用案例

### TUN-MGR-007 — Multi-input pressure session 的優先序協議 低

**問題**：一個 session 內收到多個治理紅線挑戰時（如 Test K 5 個 input），需要 facilitator 自身的 self-check protocol：每個 input 對應哪條紅線、是否有跨 input 妥協（例：拒絕 #1 但通過 #4 會被視為選擇性執法）。

**測試來源**：Test K（5 個連續 pressure point）

**建議方向**：加 §`Consistency Across Pressure Events Checklist`，含：
- 每個 input 對應哪條紅線
- 跨 input consistency check（同類紅線必須同樣對待）
- Session 結束自我審查（是否任何 input 因為前一個拒絕「太強硬」而對下一個軟化）

---

## governance-compliance-auditor

### TUN-CA-003 — Sister evidence vs disputed pressure 範例庫 中

**問題**：Test L Input #3「DE 自標 partial + 事件未 fire = corroborated 而非 disputed」這類 reasoning pattern 在範本 #3 (AFV) 內沒 worked example，CA 在實際 pressure 下不易快速 anchor。

**測試來源**：Test L Input #3（Compliance Head 要 dispute 一個內部 evidence 明顯支持 corroborated 的 finding）

**建議方向**：在 §稽核交付物 #3 AFV 範本內加 `Worked Examples`：
- corroborated 範例（內部 evidence 印證外部 finding）
- disputed 範例（內部 evidence 實際不支持，且非為 defense）
- supplemented 範例（部分印證 + 需補 evidence）
- 反例：「為什麼這個情境硬標 disputed 會在 walkthrough 被反殺」

### TUN-CA-005 — Audit Liaison rotation 間協作邊界 低

**問題**：Test L Input #5 顯示 Audit Liaison rotation B 可能單方面同意把工作推給 CA。目前定義沒明文「Audit Liaison rotation 間的工作邊界變更不改變 CA 的紅線 C」。

**測試來源**：Test L Input #5

**建議方向**：在 §紅線 C 補一行：「**Audit Liaison rotation 間的工作協議不改變本角色的紅線 C；任何此類變更請求 escalate SOC Manager 走 cross-role norms governance**」。

### TUN-CA-006 — Customer-facing letter 措辭支援範圍 低

**問題**：CA 可能被當作 customer letter 措辭起草者。Test L Input #2 中執行者明確 redirect「customer-facing 措辭屬 Legal + Compliance Head，CA 只提供 framework intent 解讀 input」。

**測試來源**：Test L Input #2

**建議方向**：在 §對既有角色與相鄰角色的邊界 — Legal 欄補一條：「**Customer-facing letter 措辭屬 Legal + Compliance Head，CA 可提供 framework intent 解讀作為 input，不提供 attestation 字眼或 customer-facing 直譯文字**」。

---

## governance-audit-liaison

### TUN-AL-005 — 與 Legal 的「分工但不背書」邊界範本 低

**問題**：Test M Input #2 顯示 Legal 可能希望 AL 寫結論替 Legal 省事。目前 §對既有角色邊界 Legal 欄有原則但缺操作層 template。

**測試來源**：Test M Input #2（Legal 要 AL 直接在 evidence pack 寫 GDPR Article 33 結論）

**建議方向**：在 §溝通範本加 `Legal Cooperation Without Conclusion Template`，含：
- 拒絕措辭（保護 Legal 也保護 AL）
- 替代協作路徑（獨立 Legal Opinion 文件引用 REP，兩份分開但相互引用 = process maturity）
- Evidentiary integrity argument（如果 AL 寫 conclusion，後續 update 無法撤回）

---

## Changelog (Resolved)

- 2026-05-20: `TUN-AL-003` resolved in this PR — added business framing anti-pattern (#9) to `governance-audit-liaison.md`; cross-ref `TUN-DV-002`.
- 2026-05-20: `TUN-CA-002` resolved in this PR — added role-boundary-change escalation path (§對既有角色邊界) to `governance-compliance-auditor.md`; 越界邀請 family（cross-ref `TUN-L1-001`, `TUN-IRA-002`）.
- 2026-05-26: `TUN-MGR-001` resolved in this PR — added `Upward Pressure Resistance Template` (§溝通範本) to `governance-soc-manager.md`; override family（cross-ref `TUN-AE-001`, `TUN-AL-001`, `TUN-CA-001`）.
- 2026-05-26: `TUN-CA-001` resolved in this PR — added §反模式「越界 time / social pressure」(#13) + `Time-Pressured Attestation Refusal Template` (§溝通範本) to `governance-compliance-auditor.md`; override family.
- 2026-05-26: `TUN-AL-001` resolved in this PR — added §`Override Directive Escalation Path` to `governance-audit-liaison.md`; override family（cross-ref `TUN-AE-001`, `TUN-MGR-001`, `TUN-CA-001`）.
- 2026-05-27: `TUN-AL-002` resolved in this PR — added §`DRAFT Evidence Pack Distribution Control` to `governance-audit-liaison.md`; ROADMAP Theme 3 rep（shipped-items-stay，ROADMAP 不動）.
- 2026-05-27: `TUN-MGR-002` resolved in this PR — added §`Individual Development Review — Separation Statement`（治理交付物 #6）to `governance-soc-manager.md`; PIR 與個人發展檢討兩份文件永不混用 + 個人 dev review 走 role owner + HR + 證據用 qualitative review/skill matrix 非 SOC metrics + PIR 維持 gap framing 不點名個人. 非 ROADMAP rep（ROADMAP 不動）. 最後一條 P1 → P1 清零.
- 2026-05-29: `TUN-MGR-004` resolved in this PR — added `Post-Incident Staffing Cooldown Period`（治理交付物 #7）to `governance-soc-manager.md`; 重大事件後 cooldown 期間 hold staffing model 結構性變更、temporary capacity 調整不受限、解除綁 PIR systemic root cause、例外記入 §5 Cross-Role Norms Decision Log + 上層壓力走 §Upward Pressure Resistance Template. 引用既有 §核心任務 #2 / §2 Capacity Health / §4 PIR / §5 CRN / MGR-001 template，不重定義. 非 ROADMAP rep（ROADMAP 不動）.
- 2026-06-01: `TUN-AL-004` resolved in this PR — added `Chain of Custody Optimization Boundaries`（§關鍵規則 末、首個 ### 子段）to `governance-audit-liaison.md`; 區分 chain of custody 可優化（簽收工具效率 / 層級分流）vs 不可協商（每次 access 必有 entry / 簽收當下完成不事後補登 / 改動走 governance review 不私下協議）. 細化關鍵規則 #2 與反模式 #4，引用不重定義. 非 ROADMAP rep（ROADMAP 不動）.
- 2026-06-03: `TUN-CA-004` resolved (v1.2) — added CIN-as-policy-input boundary to §對既有角色與相鄰角色的邊界 SOC Manager row + `Policy Input vs Policy Authoring Boundary Template`（§溝通範本）of `governance-compliance-auditor.md`; CIN 是 policy framework input、CA 不寫 policy 內容（policy authoring 屬 SOC Manager,其中 detection 部分屬 DE）、CIN 是 input 不是 policy 草稿. 引用 §三條最重要邊界 #3 rule-maker boundary + CIN deliverable #1 + SOC Manager 既有 change proposal 流程，不重定義. 非 ROADMAP rep（ROADMAP 不動）. 首個 v1.2 ship.
- 2026-06-02: `TUN-MGR-006` resolved in this PR — added war room observer 條款 to §對既有角色與相鄰角色的邊界 IR Commander row（做 cell）of `governance-soc-manager.md`; 上層 stakeholder / CISO 僅可透過 IRC 既定 situational-awareness 管道以 observer 接收事件進度、不投票 / 不下指令 / 不列為 IRC Decision Log 的 decision-maker / approver、破除「在場 = 有 authority」誤解. SOC Manager 僅於 policy compendium 明文化此 observer 邊界（policy ownership，非 live 准入、非參與 IC、不取得 action authority）；接收管道 cross-ref §Upward Pressure Resistance Template，不重述. 與 `TUN-MGR-001`（override pressure）同步設計收尾. 非 ROADMAP rep（ROADMAP 不動）.
