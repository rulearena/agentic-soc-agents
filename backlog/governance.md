# Governance Agents — Tuning Backlog

本檔案記錄 governance 角色定義（`governance-soc-manager`, `governance-compliance-auditor`, `governance-audit-liaison`）在實測中發現、尚未併入主檔的改善建議。

格式對齊其他 backlog 檔：每條含**問題**、**測試來源**、**建議方向**、**優先序**。Resolved 後移到底部 Changelog。

---

## governance-soc-manager

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
- 2026-06-11: `TUN-CA-005` resolved in this PR — added rotation-protocol carve-out sub-bullet under §紅線 C #7 of `governance-compliance-auditor.md`; Audit Liaison rotation 間的工作協議 / 排班 / 交接不改變 CA 不接 evidence packaging(及 #8 evidence collection、#9 chain of custody)的邊界、任何此類 rotation-level 變更請求 escalate SOC Manager 走 cross-role norms governance. 強化紅線 C 未改寫 #7-9 本體、未給 CA 新權限,與 §對既有角色與相鄰角色的邊界 rotation 列同義並 cross-ref(把同一概念前移到紅線本體旁直接可見). sub-bullet 不動 §流程紀律 #10-14 編號. v1.3 low-sensitivity review lane. P2.

## Changelog (Dropped)

- 2026-06-05: `TUN-MGR-003` dropped (v1.3 planning) — Systemic Recognition Framework 建議方向（可表揚 contribution 類別 + 30hr=systemic failure reframe + 表揚詞範本）易寫成抽象管理價值宣言／反 hero-culture 道德論述，framing 風險高、邊界價值低；既有 §13「不表揚 firefighting」負面禁令已足夠，正面 recognition framework 屬管理文化設計非角色規格。
- 2026-06-05: `TUN-MGR-005` dropped (v1.3 planning) — §關鍵規則 #12「Metrics 不作為個人 performance 工具」既有禁令已足夠；四層 second-order effect 分析 + Goodhart's Law 案例易把角色規格寫成散文式管理教材，framing 敏感。未來若實測出具體操作缺口，應另建窄範圍 backlog，不復活此條。
