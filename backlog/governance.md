# Governance Agents — Tuning Backlog

本檔案記錄 governance 角色定義（`governance-soc-manager`, `governance-compliance-auditor`, `governance-audit-liaison`）在實測中發現、尚未併入主檔的改善建議。

格式對齊其他 backlog 檔：每條含**問題**、**測試來源**、**建議方向**、**優先序**。Resolved 後移到底部 Changelog。

---

## governance-soc-manager

### TUN-MGR-001 — CISO override pressure response playbook ⭐ 高

**問題**：定義有「不參與 live IC、不 approve action」禁令，但缺**當 reporting line 上層直接施壓時的拒絕 + redirect 模板**。Test K Input #1 中執行者臨場用「階級 ≠ authority」+ 「權限走角色職能而非職位高低」+ second-order effect（cannot_approve_alone 制度崩潰）抵抗 CISO override 要求。

**測試來源**：Test K Input #1（CISO 要 SOC Manager 進 war room override IRC BLOCK 決定）

**建議方向**：在 §溝通範本加 `Upward Pressure Resistance Template`，含：
- 階級 ≠ authority 論述（權限走角色職能不走職位高低）
- 拒絕 + cushion stakeholder 標準話術（CISO 可作 observer / IRC 可基於新資訊重評）
- Second-order effect framing（若上層能 override → cannot_approve_alone 制度崩潰）

### TUN-MGR-002 — 個人 vs 制度的 PIR 分流機制 ⭐ 高

**問題**：當 CISO / stakeholder 想看「誰錯了」時，需要明確的**第二通道**（individual development review，由 role owner + HR 走，與 PIR 分離），避免 PIR 被偷渡成 blame 文件。目前定義說「不點名個人」但沒給「個人 dev review 該怎麼分流」的機制。

**測試來源**：Test K Input #2（CISO 要 blame-oriented PIR 含人名）

**建議方向**：加治理交付物範本 #6 `Individual Development Review — Separation Statement`，明確分流：
- PIR 文件保持 gap framing
- 個人 development review 另開對話、走 role owner + HR、用 qualitative review + skill matrix 而非 SOC metrics
- 兩者文件絕不混在一起

### TUN-MGR-003 — Recognition framework 設計原則 ⭐ 高

**問題**：§13「不表揚 firefighting」是負面禁令，缺**正面 systemic recognition framework**：什麼樣的貢獻該被表揚、表揚機制如何避免變回 hero culture、spot bonus 與 systemic contribution award 的分工。Test K Input #5 中執行者臨場改寫表揚詞並設計分層處理（spot bonus 不阻擋 + 對外敘事抗 hero narrative + 暫緩 Hero of Quarter 獎項）。

**測試來源**：Test K Input #5（CISO 要表揚 IR Commander「30 小時連續處理」）

**建議方向**：加 §`Systemic Recognition Framework Design Principles`，含：
- 可表揚的 systemic contribution 類別（補 detection coverage gap / 修 process bottleneck / 主持成功 cross-role training / 提出被採納的 process improvement）
- 30 小時連續工作 = systemic failure signal 而非英雄事蹟的 reframe 邏輯
- 表揚詞範本（聚焦 systemic ability + 把 staffing 不足歸 governance 責任）

### TUN-MGR-004 — Staffing change 在 incident 後的冷卻期 中

**問題**：INC 結束後常有「立刻改 staffing」壓力（如 Test K Input #3）。目前 §關鍵規則 #14「不為了短期 SLA 把 staffing 拉緊到 burnout」是原則但沒給時程紀律。

**測試來源**：Test K Input #3（HR + CISO 跳過 L1 owner 諮詢改班輪 12-hour × 2）

**建議方向**：在 §核心任務 #2 Staffing 補一條紀律：「重大事件結束後 N 天內不做 staffing model 結構性變更，等 PIR 識別真正 root cause 再決定」。

### TUN-MGR-005 — Metrics-to-performance 防火牆語言 中

**問題**：§關鍵規則 #12 是禁令「Metrics 不作為個人 performance 工具」，缺**具體話術 + 替代設計**。Test K Input #4 中執行者用四層 second-order effect 分析（action item 被做小 / TP rate 反向激勵 / hero culture 強化 / PIR 不誠實）說服 CISO，這個 framing 值得固化。

**測試來源**：Test K Input #4（CISO 要把 PIR action item closure rate + 個人 case TP rate 綁 bonus）

**建議方向**：在 §溝通範本加 `Metrics-Bonus Decoupling Template`，含：
- 結構化拒絕（四層 second-order effect 分析）
- Team-level systemic contribution metrics 範本（替代 individual KPI）
- Goodhart's Law 應用案例

### TUN-MGR-006 — War room observer 條款 中

**問題**：Test K Input #1 場景需要明確：CISO 作為 stakeholder 可否進 war room observe？目前定義模糊，可能被解讀為「在場 = 有 authority」。

**測試來源**：Test K Input #1（執行者建議 CISO 可作 observer 但不投票）

**建議方向**：在 §對既有角色與相鄰角色的邊界 — IR Commander 欄補一條：「CISO / 上層 stakeholder 可作為 war room observer 接收 situational awareness，但**不投票、不下指令、不入 Decision Log decision row**；觀察者角色明文化避免『在場 = 有 authority』誤解」。

### TUN-MGR-007 — Multi-input pressure session 的優先序協議 低

**問題**：一個 session 內收到多個治理紅線挑戰時（如 Test K 5 個 input），需要 facilitator 自身的 self-check protocol：每個 input 對應哪條紅線、是否有跨 input 妥協（例：拒絕 #1 但通過 #4 會被視為選擇性執法）。

**測試來源**：Test K（5 個連續 pressure point）

**建議方向**：加 §`Consistency Across Pressure Events Checklist`，含：
- 每個 input 對應哪條紅線
- 跨 input consistency check（同類紅線必須同樣對待）
- Session 結束自我審查（是否任何 input 因為前一個拒絕「太強硬」而對下一個軟化）

---

## governance-compliance-auditor

### TUN-CA-001 — Time-pressure escalation playbook ⭐ 高

**問題**：Legal「時間趕」這類 social pressure 在 §反模式內未明文。Test L Input #2 中執行者臨場拒絕但需要更系統化的「time pressure 不改變 final attestation ownership」+ 替代材料範本。

**測試來源**：Test L Input #2（Legal 要 CA 直接寫 attestation 字眼說「時間趕」）

**建議方向**：在 §反模式補一條「**Time pressure 不改變 final attestation ownership**」+ 在 §溝通範本加 `Time-Pressured Attestation Refusal Template`，含：
- 拒絕理由（紅線 A 不可協商）
- 替代材料 menu（ESR + CIN + 非 attestation 措辭方向）
- 加速合作路徑（CIN 同日交付 + Legal 自己寫 attestation）

### TUN-CA-002 — Cross-role consolidation 拒絕範本 ⭐ 高

**問題**：IRC 想合併 CA + Audit Liaison 屬 cross-role boundary 變更，但角色定義內未明文「此類變更 escalate SOC Manager governance 而非 CA / IRC 單方面決定」。Test L Input #5 中執行者臨場用「separation of duties」+「handoff 是 control point 不是 overhead」說服。

**測試來源**：Test L Input #5（IRC 想把 evidence packaging 推給 CA + Audit Liaison rotation B 已同意）

**建議方向**：在 §對既有角色與相鄰角色的邊界補一條「**對 role boundary 變更請求的標準 escalation path**」：
- Cross-role consolidation 屬 SOC Manager governance ownership
- Audit Liaison rotation 間的工作邊界變更不改變 CA 紅線 C
- 「handoff 是 control point」的 framing（給拒絕者用）

### TUN-CA-003 — Sister evidence vs disputed pressure 範例庫 中

**問題**：Test L Input #3「DE 自標 partial + 事件未 fire = corroborated 而非 disputed」這類 reasoning pattern 在範本 #3 (AFV) 內沒 worked example，CA 在實際 pressure 下不易快速 anchor。

**測試來源**：Test L Input #3（Compliance Head 要 dispute 一個內部 evidence 明顯支持 corroborated 的 finding）

**建議方向**：在 §稽核交付物 #3 AFV 範本內加 `Worked Examples`：
- corroborated 範例（內部 evidence 印證外部 finding）
- disputed 範例（內部 evidence 實際不支持，且非為 defense）
- supplemented 範例（部分印證 + 需補 evidence）
- 反例：「為什麼這個情境硬標 disputed 會在 walkthrough 被反殺」

### TUN-CA-004 — CIN as policy input 流程 中

**問題**：SOC Manager 可能會把 CA 當 policy 共筆者。Test L Input #4 中執行者臨場 redirect「detection 部分屬 DE + policy framing 屬 SOC Manager，CA 提供 CIN 作 framework input 不寫 policy 內容」。

**測試來源**：Test L Input #4（SOC Manager 要 CA 直接寫 detection policy）

**建議方向**：在 §對既有角色與相鄰角色的邊界 — SOC Manager 欄補一條：「**CIN 是 policy framework input，CA 不寫 policy 內容；policy 內容由 SOC Manager + DE 主理**」。並加 §溝通範本 `Policy Input vs Policy Authoring Boundary Template`。

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

### TUN-AL-001 — AL escalation protocol when receiving CISO/Exec override directive ⭐ 高

**問題**：AL 拒絕 CISO/Exec 後若對方仍堅持 override，文件沒明確定義 AL 上報路徑（往 Compliance Head？往 IRC？往 Board Audit Committee？）。Test M Input #5 中執行者僅留「請走 IRC Decision Log + Legal sign-off」但未明定 AL 自己該往哪 escalate。

**測試來源**：Test M Input #5（CISO 要 AL 跳過 Legal 直接對 regulator 發 evidence pack）

**建議方向**：加 §`Override Directive Escalation Path`，含：
- 受到 conflict-with-rule directive 時的上報優先序（Compliance Head → Board Audit Committee → external escalation）
- 過程記錄要求（每次拒絕 + override 嘗試入 evidence pack audit trail）
- AL 自身保護（不接 directive 不是 insubordination 而是 role-defined refusal）

### TUN-AL-002 — DRAFT evidence pack 的 access control 與 distribution log 規格 ⭐ 高

**問題**：REP 標 DRAFT for Legal Review，但若 CISO 已透過內部 channel 拿到 DRAFT 並擅自轉發 regulator，AL 如何發現 / 追蹤 / 回應？定義缺 distribution control 規格。

**測試來源**：Test M Input #5（CISO 要直接寄 DRAFT REP-001 給 regulator）

**建議方向**：加 §`DRAFT Evidence Pack Distribution Control`：
- DRAFT 版本必須加 watermark + access log
- Distribution list 限定（Legal Counsel + Compliance Head + IRC，不含 CISO / Exec 直接 download）
- 若觀察到 DRAFT 外流：立即通知 Legal + Compliance Head 作為 process integrity issue

### TUN-AL-004 — Chain of custody 簽收的「合理優化 vs 違規捷徑」分界 中

**問題**：Test M Input #4 中 Forensics 訴求其實有正當性（流程繁瑣），AL 拒絕但 redirect 到 case 後 + governance review。目前定義沒明文「哪些 chain 流程優化可以做 / 哪些絕對不能談」。

**測試來源**：Test M Input #4（Forensics 想跳過 chain of custody 簽收）

**建議方向**：在 §關鍵規則 #2 後補 `Chain of Custody Optimization Boundaries`：
- **可優化**：簽收工具效率（GRC 平台 webhook 自動帶 entry、batch UI）、簽收層級分流（read-only vs modify 不同 workflow）
- **不可協商**：每次 access 必有 entry、簽收當下完成（不事後補）、改動走 governance review 而非雙方私下協議

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
