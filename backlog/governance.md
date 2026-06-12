# Governance Agents — Tuning Backlog

本檔案記錄 governance 角色定義（`governance-soc-manager`, `governance-compliance-auditor`, `governance-audit-liaison`）在實測中發現、尚未併入主檔的改善建議。

格式對齊其他 backlog 檔：每條含**問題**、**測試來源**、**建議方向**、**優先序**。Resolved 後移到底部 Changelog。

---

## governance-soc-manager

（governance-soc-manager 目前無 active backlog；已 resolved 項見底部 Changelog）

---

## governance-compliance-auditor

（governance-compliance-auditor 目前無 active backlog；已 resolved 項見底部 Changelog）

---

## governance-audit-liaison

（governance-audit-liaison 目前無 active backlog；已 resolved 項見底部 Changelog）

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
- 2026-06-12: `TUN-MGR-007` resolved in this PR — added `Consistency Across Pressure Events Checklist`（§溝通範本，接 `Upward Pressure Resistance Template` 後）to `governance-soc-manager.md`; 多 pressure input session 的 facilitator 跨事件一致性自檢——逐 input 對應紅線(A/B/C)、同類紅線同樣對待(防選擇性執法／看施壓強度下菜)、session 結束自審(補償心理軟化、疲勞略過留痕)、差異留痕入 §5 CRN. 錨回紅線 A/B/C + §Upward Pressure Resistance Template(單事件) + §5 Cross-Role Norms Decision Log，引用不重定義、不新增紅線、不改寫判準. v1.3 low-sensitivity review lane.
- 2026-06-12: `TUN-AL-005` resolved in this PR — added `Legal Cooperation Without Conclusion Template`（§溝通範本，接「對 Legal Counsel 的 evidence pack 提交」後）to `governance-audit-liaison.md`; 當 Legal 主動要 AL 在 evidence pack 內代寫法律結論(如 GDPR Article 33 是否觸發)時的拒絕措辭 + 替代協作路徑(結論寫獨立 Legal Opinion 文件 reference REP-001、事實層與判斷層分離 = process maturity) + evidentiary integrity 論證(結論一旦入 pack 提交、後續更新無法悄悄撤回). 操作化關鍵規則 #1(不做 legal judgment) / #8(紀錄當下完成事後不抹)，引用不重定義、不對法條表態、不寫對外承諾. v1.3 low-sensitivity review lane.
- 2026-06-12: `TUN-CA-003` resolved in this PR — added `#### Worked Examples（AFV 分類決策錨點）` after AFV template in `governance-compliance-auditor.md`; corroborated / disputed / supplemented 三分類各一個 worked example + 一個「同情境硬標 disputed」反例（DE partial + 事件未 fire = corroborated 非 disputed）；決策錨：分類依內部 evidence 實際情況，不依組織希望結論調整；強化既有 §關鍵規則 #12 非 audit defense 主軸，不重定義三分類語意、不給 CA 新權限. v1.3 user-driven review lane.

## Changelog (Dropped)

- 2026-06-05: `TUN-MGR-003` dropped (v1.3 planning) — Systemic Recognition Framework 建議方向（可表揚 contribution 類別 + 30hr=systemic failure reframe + 表揚詞範本）易寫成抽象管理價值宣言／反 hero-culture 道德論述，framing 風險高、邊界價值低；既有 §13「不表揚 firefighting」負面禁令已足夠，正面 recognition framework 屬管理文化設計非角色規格。
- 2026-06-05: `TUN-MGR-005` dropped (v1.3 planning) — §關鍵規則 #12「Metrics 不作為個人 performance 工具」既有禁令已足夠；四層 second-order effect 分析 + Goodhart's Law 案例易把角色規格寫成散文式管理教材，framing 敏感。未來若實測出具體操作缺口，應另建窄範圍 backlog，不復活此條。
- 2026-06-12: `TUN-CA-006` resolved in this PR — added customer-facing letter boundary to §對既有角色與相鄰角色的邊界 Legal Counsel / Compliance Head row of `governance-compliance-auditor.md`；「做」欄補：若詢問可提供 framework intent 解讀作為起草 input，CA 的 input 限 framework 條文意圖描述不評估措辭是否符合 framework；「不做」欄補：不起草 customer-facing letter 措辭、不提供 attestation 字眼或 customer-facing 直譯文字（客戶溝通措辭的起草權不屬 CA，不因詢問方是誰而改變）. v1.3 low-sensitivity review lane. P2.
