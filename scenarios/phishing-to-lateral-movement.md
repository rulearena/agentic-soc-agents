# Phishing → Token Theft → Lateral Movement：跨角色端到端協作情境 (Cross-Role Collaboration Scenario)

> **文件定位**：展示 agentic-soc-agents 中 6 個角色如何在單一事件中協作。所有角色動作嚴格落在其 spec 定義的邊界內。本情境為範例用，實際環境的參數（hostname、IP、threshold）請依環境調整。

---

## 1. 情境摘要 (Incident Summary)

一條偽裝成發票通知的釣魚信件，使受害者點擊後觸發惡意 macro，下載並執行身分竊取工具。攻擊者利用 MFA fatigue 手法取得雲端應用程式 session token，透過該 token 橫向移動至內部 finance 系統。

**事件鏈**：Initial Access（T1566.001）→ Execution（T1059.001）→ Credential Access（MFA fatigue T1621 → session cookie theft T1539 → use stolen token T1078）→ Lateral Movement（T1021.001）

**涉及角色**（依登場順序）：
1. **L1 SOC Analyst**（triage-l1-soc-analyst）— 24/7 alert triage，初步 enrichment
2. **L2 SOC Analyst**（triage-l2-soc-analyst）— 跨資料源 pivot、exec approved playbook、IR 升級判斷
3. **Threat Intel Analyst**（threat-intel-analyst）— 提供 IOC context 與 confidence marking
4. **IR Commander**（incident-response-ir-commander）— incident declaration、approval、跨團隊協調
5. **IR Analyst**（incident-response-ir-analyst）— 執行 IRC 核准的 containment、verification、scope drift 回報
6. **Detection Engineer**（detection-engineering-threat-detection-engineer）— post-incident detection gap 回饋接收

> 本情境不涉及：Governance 角色（SOC Manager、Compliance Auditor、Audit Liaison）、Purple Team 角色，將於未來情境補足。

---

## 2. 時間軸 (Timeline)

### Phase 1：L1 Triage（Day 1, 09:15–09:50）

#### Step 1.1 — L1 接收告警

| 欄位 | 內容 |
|---|---|
| Agent | L1 SOC Analyst |
| 動作 | 接收 SIEM alert 「Suspicious PowerShell Encoded Command Execution」（severity: High），affected host HOST-FIN-042，user finance.user01 |
| 邊界依據 | L1 spec §核心任務 #1 Alert Triage、§工作流程 Step 1 |
| 工具 | Splunk（主力 SIEM）+ CrowdStrike Falcon（EDR） |
| Hand-off | 無（初始接收） |

L1 在 SIEM queue 中認領 alert，確認時間戳 09:12，host 屬 finance 部門（medium criticality asset）。

#### Step 1.2 — L1 執行 Enrichment

| 欄位 | 內容 |
|---|---|
| Agent | L1 SOC Analyst |
| 動作 | 執行 enrichment checklist：查 EDR process chain、VT lookup file hash、SIEM 同 host 近期告警 |
| 邊界依據 | L1 spec §工作流程 Step 2（Asset / Temporal / External / Behavioral context） |
| 交付物 | 初步 Triage Report（見下方） |

**L1 Triage Report 片段**：

```
Ticket ID: SOC-2026-06-22-0018
Alert Rule: Suspicious PowerShell Encoded Command Execution
Severity: High

Process Chain (Falcon):
  OUTLOOK.EXE (PID 3201) →
  WINWORD.EXE (PID 3892) →
  CMD.EXE /c powershell.exe -enc <base64> (PID 4012) →
  POWERSHELL.EXE (PID 4050) connecting to hXXps://update-service[.]example/api

Temporal Context:
  09:05 — Unusual logon from 198.51.100.45 (not in user's baseline)
  09:07 — Outbound TLS to update-service[.]example (first seen this host)

External Intel (VT):
  Downloaded payload hash a8b9c0d1e2f3... → 14/70 vendors → Trojan
  C2 domain update-service[.]example → 8/70 vendors → malware C2

Preliminary: Phishing-driven malware, likely credential access targeting.
```

#### Step 1.3 — L1 Fast-track Escalation

| 欄位 | 內容 |
|---|---|
| Agent | L1 SOC Analyst |
| 動作 | 判斷 pattern 命中 fast-track 條件（credential access 訊號）→ 立即升級 L2，並行續跑 enrichment |
| 邊界依據 | L1 spec §Time-Critical TP Fast-Track：credential dumping 訊號（此處延伸至 token theft 亦有相似時效壓力），不等待 enrichment 全完成 |
| Hand-off | 升級給 **L2 SOC Analyst**（escalates_to: triage-l2-soc-analyst） |
| 交付物 | Fast-track ticket 註記（見下方） |

```
[Fast-Track] SOC-2026-06-22-0018
Status: fast-track escalation, enrichment 並行進行中
Trigger pattern: credential access signaling (phishing macro + C2 + encoded payload)
Enrichment status:
  - Asset context: done — HOST-FIN-042 (finance dept, medium criticality)
  - Temporal context: in progress — 同 host 近 24h 還有 2 條相關 alert
  - External context: done — VT 14/70 + 8/70
Handoff to: L2 SOC Analyst
```

**邊界檢查**：L1 不執行 containment、不寫 detection rule、不做 IR 判斷。fast-track 為 pattern-based，enrichment 仍並行續跑。

---

### Phase 2：L2 Investigation（09:50–11:30）

#### Step 2.1 — L2 接收升級、驗證 L1 Report

| 欄位 | 內容 |
|---|---|
| Agent | L2 SOC Analyst |
| 動作 | 接收 L1 升級 ticket，驗證 L1 Triage Report 完整性 |
| 邊界依據 | L2 spec §工作流程 Step 1：「先看 Triage Report 完整性，沒附完整 evidence 就 push back」 |
| Hand-off | 確認 L1 report 完整 → 進下一步 pivot |

L2 確認 L1 已附：process chain snapshot、VT lookup、初步時間軸。L2 不重做 L1 已完成的 enrichment。

#### Step 2.2 — L2 跨資料源 Pivot：發現 Token Theft

| 欄位 | 內容 |
|---|---|
| Agent | L2 SOC Analyst |
| 動作 | 從 L1 提供的 IOC 出發，跨 SIEM、IdP log、EDR 做 multi-source pivot |
| 邊界依據 | L2 spec §核心任務 #2：「串聯 SIEM、EDR、IAM、proxy、firewall、cloud logs 查多源 evidence」 |
| 交付物 | 攻擊鏈重建結果（見下方） |

**L2 發現**：
1. 查 IdP（Okta）log：user finance.user01 在 09:08–09:12 連續收到 14 次 MFA push notification（MFA fatigue pattern），第 15 次被接受
2. 同時段該 user 的 session 從 IP 198.51.100.45 發起，User-Agent 顯示 Linux curl（非 baseline Windows + Chrome）
3. 該 session token 隨後被用來存取內部 finance API（finance-api.internal.example/api/v1/invoices）
4. EDR 上 observable 的 payload tool 行為模式與公開描述的 token theft / cookie stealing 工具一致

**L2 攻擊鏈重建**：
```
T1566.001 — Phishing email → T1059.001 — PowerShell macro execution
  → T1621 — MFA fatigue (14 push notifications) + T1539 — session cookie theft
    → T1078 — Valid accounts (use stolen token as authenticated user)
      → T1071.001 — C2 exfiltration of session token
        → T1021.001 — Internal API access using stolen token
```

#### Step 2.3 — Threat Intel Analyst 平行協作（L2 Pivot 階段）

| 欄位 | 內容 |
|---|---|
| Agent | Threat Intel Analyst |
| 動作 | L2 在 pivot 中發現可疑 C2 domain，透過 MISP 查詢後向 TI Analyst 請求 context |
| 邊界依據 | TI spec §核心任務 #1-#2：提供 IOC context 與 confidence marking；不下 attribution |
| 交付物 | IOC context bundle（見下方） |

**TI Analyst 回覆**：

```
[Intel Context] IB-2026-042 — for L2 investigation SOC-2026-06-22-0018

IOC: update-service[.]example
Type: domain
Source(s): commercial feed A + ISAC feed
Source reliability: high + high
Confidence: high (multi-source corroborated)

Known behavior: C2 infrastructure pattern associated with token theft campaigns
TTP alignment: T1071.001 — Application Layer Protocol (HTTPS)

NOT for attribution: This context describes technical behavior patterns, not actor identity.
Any external reference requires Legal + IRC joint decision.

Confidence notes:
- Multi-source corroboration (2 independent feeds) — confidence high
- Domain age: 7 days (young domain increases suspicion, does not affect confidence level)
- No direct attribution link established or implied
```

**邊界檢查**：TI Analyst 提供 IOC context + confidence 兩軸，不下 actor 結論。不命名具體 group。對外引用前需過 Legal / IRC。

#### Step 2.4 — L2 執行 Approved Playbook

| 欄位 | 內容 |
|---|---|
| Agent | L2 SOC Analyst |
| 動作 | 觸發 SOAR playbook：isolate-workstation（HOST-FIN-042）、block-observed-ioc（C2 domain）、force-password-reset（finance.user01） |
| 邊界依據 | L2 spec §反應權限 approved_playbooks：isolate-workstation（單台 endpoint）、block-observed-ioc、force-password-reset。RDP 連線來自 HOST-FIN-042 → HOST-FIN-029 屬 lateral movement，但 server-isolation 需 IR 核准 |
| 交付物 | SOAR execution audit trail（見下方） |

```
Playbook: isolate-workstation
Target: HOST-FIN-042
Method: network-only
Audit ID: pl_2026062200423
Status: success — sensor offline confirmed

Playbook: block-observed-ioc
Target: update-service[.]example (full block — FW + DNS)
Audit ID: pl_2026062200431
Status: success — block rule deployed

Playbook: force-password-reset
Target: finance.user01
Audit ID: pl_2026062200435
Status: success — sent via self-service portal
```

執行後監控 15 分鐘：HOST-FIN-042 offline 確認。C2 domain 後續無新連線嘗試。

#### Step 2.5 — L2 判斷需升級 IR Commander

| 欄位 | 內容 |
|---|---|
| Agent | L2 SOC Analyst |
| 動作 | 發現 HOST-FIN-029（RDP target）亦受影響；DB host HOST-DBA-003 出現 SMB 連線異常。server-isolation + privileged account 操作超出 L2 範圍 |
| 邊界依據 | L2 spec §升級條件：server-isolation、account-disable-for-privileged-user 需 IR 簽核。§核心任務 #3 Decision：「scope 大或不可逆動作 → 升級 IR Commander」 |
| Hand-off | 升級給 **IR Commander**（escalates_to: incident-response-ir-commander） |
| 交付物 | L2 Investigation Report + Escalation（見下方） |

```
[L2 Escalation] SOC-2026-06-22-0018 → INC-2026-0022

Confirmed: Phishing → token theft → lateral movement to finance API + 2 additional hosts
Scope:
  - HOST-FIN-042 (origin) — isolated
  - HOST-FIN-029 (RDP target) — 出現相同 PowerShell IOC
  - HOST-DBA-003 (SMB connection, 10:45) — service-svc-dbops 帳號異常活動

L2 已執行:
  - isolate-workstation HOST-FIN-042 [done]
  - block-observed-ioc C2 domain [done]
  - force-password-reset finance.user01 [done]

需 IR Commander 核准:
  - server-isolation for HOST-FIN-029 (non-critical but confirmed infected)
  - server-isolation for HOST-DBA-003 (DB asset, business impact risk)
  - account-disable-for-privileged-user: service-svc-dbops (privileged account)
```

**邊界檢查**：L2 不自行執行 server-isolation（屬 requires_ir_approval）。不處理 privileged account disable。

---

### Phase 3：IR Commander + IR Analyst Execution（11:30–12:45）

#### Step 3.1 — IR Commander Declare Incident

| 欄位 | 內容 |
|---|---|
| Agent | IR Commander |
| 動作 | 建立 incident ticket INC-2026-0022，開 war room，暫定 severity Sev-2 |
| 邊界依據 | IRC spec §工作流程 #1 Declare：「建立 incident ticket、開 war room、依分級 SLA 通知 stakeholder」 |
| 交付物 | Incident Command Brief（見下方） |

```
# Incident Command Brief — INC-2026-0022
Declared at: 2026-06-22 11:30
Severity (provisional): Sev-2
Source: L2 escalation (SOC-2026-06-22-0018)

Scope (已知):
  - 3 host 受影響（FIN-042 isolated, FIN-029 pending, DBA-003 pending）
  - 2 user 涉入（finance.user01, service-svc-dbops）
  - 1 C2 domain 已 block

Initial Containment Status:
  - L2 已完成 3 項 approved playbook
  - 待 IRC 核准：server-isolation × 2 + account-disable × 1

Severity Assessment (暫定):
  - Business impact: Medium — 非生產系統，但 DB asset 有 business impact
  - Data exposure: Medium — token theft 可讀取 finance API
  - Spread risk: High — 跨 VLAN SMB 連線，scope 可能擴大

Next Decision Points:
  - 11:45 — server-isolation for FIN-029 & DBA-003 核准
  - 12:00 — service-svc-dbops account disable 核准
  - 12:15 — 評估是否升 Sev-1（視 spread risk 發展）
```

#### Step 3.2 — IR Commander 核准高風險 Action

| 欄位 | 內容 |
|---|---|
| Agent | IR Commander |
| 動作 | 檢視 L2 提交的 Action Approval Request，確認 evidence chain 與 risk assessment 後簽核 |
| 邊界依據 | IRC spec §反應權限 can_approve：server-isolation、account-disable-for-privileged-user |
| Hand-off | 委派 **IR Analyst** 執行（delegates_to.technical_containment: incident-response-ir-analyst） |
| 交付物 | Action Approval Record（見下方） |

```
# Action Approval Record — INC-2026-0022 / AAR-001

Action: server-isolation
Target: HOST-FIN-029 (RDP target, confirmed IOC)
Approved by: IR Commander (rotation A)
Approved at: 11:42

Risk Assessment:
  - 技術風險：低 — endpoint 非生產系統
  - 業務風險：低 — finance user workstation
  - Evidence 影響：低 — network isolation 不破壞 disk/memory evidence

Execution Delegation:
  - Delegate to: IR Analyst (rotation A)
  - Verification owner: L2 (rotation B)

Evidence Preservation Plan: N/A — server-isolation 不屬 evidence-wiping-risk-action

---

# Action Approval Record — INC-2026-0022 / AAR-002

Action: server-isolation
Target: HOST-DBA-003 (DB asset, SMB IOC)
Approved by: IR Commander (rotation A)
Approved at: 11:44

Risk Assessment:
  - 技術風險：中 — DB host isolation 可能影響下游應用
  - 業務風險：中 — DBA team 需預備 fallback
  - Evidence 影響：低

Execution Delegation:
  - Delegate to: IR Analyst (rotation A)
  - Verification owner: L2 (rotation B)
  - Parallel notification: DBA team (non-blocking, 同步通知)

---

# Action Approval Record — INC-2026-0022 / AAR-003

Action: account-disable-for-privileged-user
Target: service-svc-dbops (privileged service account)
Approved by: IR Commander (rotation A)
Approved at: 11:46

Risk Assessment:
  - 技術風險：中 — disable 後相關 DB 自動化作業可能中斷
  - 業務風險：中 — 需 IT 預備 fallback
  - Evidence 影響：低 — account state 可還原

Execution Delegation:
  - Delegate to: IR Analyst (rotation A)
  - Parallel notification: DBA team, account holder's manager (non-blocking)
```

#### Step 3.3 — IR Analyst 執行 Containment + Scope Drift

| 欄位 | 內容 |
|---|---|
| Agent | IR Analyst |
| 動作 | 依 AAR-001 ~ AAR-003 順序執行 containment：pre-execution check → execute → verify。執行 AAR-002 時發現第 N+1 台 host |
| 邊界依據 | IR Analyst spec §核心任務 #1-#4：只執行 IRC-approved action、執行後驗證、scope drift 時停下回報 |
| Hand-off | scope drift → 提交 Scope Drift Report 給 IR Commander（await decision） |
| 交付物 | Action Execution Report + Scope Drift Report（見下方） |

**AAR-001（HOST-FIN-029 isolation）— 執行成功**：

```
# Action Execution Report — INC-2026-0022 / AAR-001
Action: server-isolation
Target: HOST-FIN-029
Started: 11:48 | Completed: 11:52

Pre-execution Check:
  - target endpoint 在線、EDR sensor active ✓
  - approval 條件仍成立（IOC 仍活動）✓

Execution:
  - 11:48 EDR isolation command sent
  - 11:49 EDR 回應 success
  - 11:50 sensor 顯示 offline

Verification:
  - SIEM query: HOST-FIN-029 在 11:49 後無新 logon/process event ✓
  - EDR status: isolated ✓

Unexpected: 無
Handoff: Verification owner L2 (rotation B) 已通知
```

**AAR-002（HOST-DBA-003 isolation）— Scope Drift**：

```
# Action Execution Report — INC-2026-0022 / AAR-002
Action: server-isolation
Target: HOST-DBA-003
Started: 11:53

Pre-execution Check:
  - target endpoint 在線 ✓
  - DBA team 已通知 (non-blocking) ✓
  - 執行前 EDR cross-check: HOST-DBA-003 的 IOC 活動 ✓

Execution:
  - 11:53 EDR isolation command sent
  - 11:54 EDR 回應 success
  - 11:55 sensor 顯示部分離線

Verification:
  - SIEM query: HOST-DBA-003 在 11:54 後無新 event ✓
  - EDR 跨 host 查詢: HOST-DBA-005（finance db replica, 不在 AAR target list）在 11:50 出現相同 SMB IOC pattern

→ SCOPE DRIFT DETECTED: HOST-DBA-005 不在核准範圍
→ EXECUTION STOPPED per IR Analyst spec §回報 Commander 的觸發條件
```

**Scope Drift Report**：

```
# Scope Drift Report — INC-2026-0022 / SDR-001
Reporter: IR Analyst (rotation A)
Reported at: 11:56
Status: EXECUTION STOPPED, awaiting IRC decision

Approval in Effect:
  AAR-002: server-isolation HOST-DBA-003 (IRC approved 11:44)

Drift Observed:
  - 執行 HOST-DBA-003 isolation 後，EDR cross-host query 發現
    HOST-DBA-005（finance db replica）在 11:50 出現相同 SMB IOC pattern
  - HOST-DBA-005 不在 AAR-002 核准範圍

Why Stopped:
  - HOST-DBA-005 不在 approval target list → 不擴 scope
  - DB replica 的 IOC 提示橫向移動可能已擴散至 DB tier
  - 需 IRC 重新評估 severity + 決定是否擴大 isolation 範圍

已執行:
  - AAR-001 (HOST-FIN-029): completed
  - AAR-002 (HOST-DBA-003): completed (isolation 已生效)
  - AAR-003 (service-svc-dbops): 尚未執行（pending IRC decision on new scope）

Pending:
  - AAR-003: 待 IRC 確認新 scope 後執行
  - HOST-DBA-005: 需新 approval
```

**邊界檢查**：IR Analyst 不自行擴大 isolation 範圍、不自行核准新 action、不自行召集 Threat Hunter 或其他人員（見 IR Analyst spec §回報 Commander 的觸發條件最後一項：「超界 pivot 屬 hunting 範疇…不自行續查」）。

#### Step 3.4 — IR Commander 重新評估 + 核准新 Scope

| 欄位 | 內容 |
|---|---|
| Agent | IR Commander |
| 動作 | 收到 SDR-001 後重新評估 severity：決定升 Sev-1（spread risk 擴大至 DB tier）、核准新 action |
| 邊界依據 | IRC spec §工作流程 #2 Classify、#3 Approve |
| Hand-off | 重新 delegate 給 IR Analyst：新 AAR-004（HOST-DBA-005 isolation）+ AAR-003（原 service account disable） |

```
# Decision Log — INC-2026-0022 (11:56–12:20)
| 時間 | 決策 | 依據 | 決策人 |
|---|---|---|---|
| 11:56 | 升 Severity 至 Sev-1（暫定→定案）| DB tier replication 確認 scope 超出原評估 | IR Commander |
| 12:00 | 核准 AAR-004: HOST-DBA-005 server-isolation | scope drift 確認、業務影響評估 vs 擴散風險 | IR Commander |
| 12:05 | 核准 AAR-003: service-svc-dbops account-disable | privileged account 確有異常活動 | IR Commander |
| 12:10 | 不啟動 customer notification | data exposure 無外洩證據；Legal stand by 待事證升級 | IR Commander + Legal |
```

IR Analyst 在 12:20 完成 AAR-003 + AAR-004 執行與 verification。

---

### Phase 4：Detection Engineer 回饋（Post-incident）

#### Step 4.1 — Detection Gap 回饋

| 欄位 | 內容 |
|---|---|
| Agent | L2 SOC Analyst → Detection Engineer |
| 動作 | 事件中觀察到 lateral movement RDP detection 未及時觸發（HOST-FIN-042 → FIN-029 RDP 在 10:15 發生但 alert 在 10:40 才出），post-incident 提交 feedback 給 Detection Engineer |
| 邊界依據 | L2 spec §協作與回饋通道：「發現 noisy rule、false positive pattern → Detection feedback log」。Detection Engineer spec §核心任務 #4：「Feedback intake & triage」 |
| 交付物 | Detection feedback entry（見下方） |

```
[Detection Feedback] FB-2026-122
Source: L2 recurring feedback (INC-2026-0022)
Content: Rule "Lateral Movement RDP" 在本次事件中延遲 25 分鐘觸發（10:15 → 10:40）
Data: rule_id=lateral-movement-rdp, trigger count 1, latency 25min
Hypothesis: threshold 太鬆或 data source log lag
Suggested: review threshold + add network-level RDP correlation
```

**邊界檢查**：L2 只提交 feedback，不改 rule。Detection Engineer 後續做 triage（accepted / rejected / merged），不在事件當下處理。

---

## 3. Hand-off 觸發條件與交付物 (Hand-off Triggers & Deliverables)

| 步 | 從 | 到 | 觸發條件 | 核心交付物 | frontmatter 關係 |
|---|---|---|---|---|---|
| 1.3 | L1 | L2 | fast-track pattern 命中（credential access）+ enrichment 完成 | Triage Report + Fast-track 註記 | `escalates_to: triage-l2-soc-analyst` |
| 2.5 | L2 | IRC | scope 超出 L2 處理能力（server isolation + privileged account） | Investigation Report + Escalation | `escalates_to: incident-response-ir-commander` |
| 3.2 | IRC | IR Analyst | Action Approval Record 簽核完成 | Action Approval Record (AAR) | `delegates_to.technical_containment: incident-response-ir-analyst` |
| 3.3 | IR Analyst | IRC | scope drift（發現第 N+1 台 host 受影響） | Scope Drift Report (SDR) | workflow callback（非 escalates_to，IR-A 不在 tier 鏈） |
| 2.3 | L2 | TI Analyst | pivot 中發現不明 IOC 需 context | IOC context bundle (IB-2026-042) | 平行協作（非升級鏈） |
| 4.1 | L2 | DE | incident 中 detection gap 觀察 | Detection feedback (FB-2026-122) | 平行協作（非升級鏈） |

---

## 4. Authority / Disclosure 壓力點 (Authority & Disclosure Pressure Point)

### 情境

事件進行至 12:30，已升 Sev-1。Finance VP 直接聯繫 IR Commander（via war room），要求「通知我們最大的合作夥伴，對方有 NDA 且 data 可能涉及 invoice 系統，不能等正式報告再講」。

### IR Commander 的回應

IR Commander 依 README「對外揭露權責」框架處理：

```
VP：我理解業務關係的重要性。
但對外揭露（包含 NDA 合作夥伴）涉及 disclosure 授權，
不在我 IR Commander 的單人 authority 範圍內。
依 SOC 對外揭露框架：
  - 合作夥伴通知（customer-notification）
    屬 `cannot_approve_alone` 範疇，需要 Legal + IRC joint decision

我建議：15 分鐘內拉 Legal Counsel 進 war room，
共同決定通知內容、範圍、與 timing。
在此之前我不發布任何對外訊息。

Decision Log 會記錄此請求與處理過程。
```

### 結果

Legal Counsel 加入 war room，共同決策後決定：暫不對合作夥伴發布通知（因事證仍在收集中、scope 未定、不精確的通知可能引發合約糾紛），改由 IRC + Legal 聯合對 VP 提供一句話 briefing（「事件處理中，確認 scope 後 24h 內提供客戶-facing 摘要；在此之前不對外發言」）。

**邊界檢查**：IR Commander 不單方面決定 disclosure（`cannot_approve_alone`）。Legal 不替 IRC 做技術判斷。兩者 joint decision 後才發布對外訊息。

---

## 5. ATT&CK 對應 (MITRE ATT&CK Mapping)

| Tactic | Technique ID | 對應事件步 | 偵測/調查角色 | 說明 |
|---|---|---|---|---|
| TA0001 Initial Access | T1566.001 Spearphishing Attachment | Step 1.1 — L1 收 phishing alert | L1 triage | L1 查附件 hash + process chain |
| TA0002 Execution | T1059.001 PowerShell | Step 1.2 — L1 發現 encoded command | L1 enrichment / L2 pivot | L1 做 process chain；L2 做 fleet-wide spread check |
| TA0006 Credential Access | T1621 Multi-Factor Authentication Request Generation + T1539 Steal Web Session Cookie | Step 2.2 — L2 發現 IdP MFA pattern + cookie theft | L2 cross-source pivot | L2 查 IdP log 發現 MFA fatigue；session cookie 竊取 combined |
| TA0003 Persistence / TA0001 | T1078 Valid Accounts | Step 2.2 — token 被當合法身分存取 API | L2 cross-source pivot | 竊取的 session token 被重放冒充合法用戶 |
| TA0011 C2 | T1071.001 Application Layer Protocol | Step 1.2 / 2.3 — C2 domain outbound | L1 + TI Analyst | L1 查 external context；TI 提供 IOC enrichment |
| TA0008 Lateral Movement | T1021.001 Remote Desktop Protocol | Step 2.5 — FIN-042 → FIN-029 RDP | L2 cross-source pivot | L2 查 logon graph + SMB 連線 |
| TA0008 Lateral Movement | T1021.002 SMB/Windows Admin Shares | Step 2.5 — DBA-003 SMB 異常 | L2 發現 / IRC severity 評估 | L2 跨 host correlaton |


---

## 參考 (References)

- **MITRE ATT&CK Framework**（https://attack.mitre.org）
- **NIST SP 800-61** — Computer Security Incident Handling Guide
- **agentic-soc-agents role specs**（本 repo `triage/`、`incident-response/`、`detection-engineering/`、`threat-intel/`）— 所有角色邊界與 authority 定義來源
