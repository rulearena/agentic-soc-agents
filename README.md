# Agentic SOC Agents

[![Validate Authority Chain](https://github.com/rulearena/agentic-soc-agents/actions/workflows/validate-agents.yml/badge.svg)](https://github.com/rulearena/agentic-soc-agents/actions/workflows/validate-agents.yml)

仿 [`msitarzewski/agency-agents`](https://github.com/msitarzewski/agency-agents) 格式打造的 SOC 專業角色庫。
30+ 個經驗導向的 AI agent 定義檔，**可作為 Claude Code / Cursor / Copilot 等 agentic coding 工具的角色提示與工作流參考**。

不同工具對 agent markdown 的支援程度不一，定義檔以**人類可讀為優先**；工具整合方式請參見各工具自己的 agent 文件。

---

## 為什麼做這個

現有的 SOC 教材多半在講「**該偵測什麼**」（rules、IOC、TTP），較少有人系統性整理「**SOC 各角色怎麼想、怎麼做**」。

這個 repo 把 SOC 從 L1 一線分流到 SOC Manager 治理層各角色的思維、工作流程、技術交付物、升級鏈條，整理成方便轉成 AI agent prompt / workflow reference 的角色定義檔。

**適用場景**：
- 訓練新人 SOC 分析師：用 agent 模擬資深角色給回饋
- Agentic SIEM / SOAR 開發：把人類角色定義翻譯成 AI agent 行為
- SOC 流程設計：以角色職責邊界為起點重新設計告警分流與升級

---

## 角色清單

✅ 已完成、⏳ 規劃中

### 🎯 Triage（一線分流）
- ✅ [`triage-l1-soc-analyst`](triage/triage-l1-soc-analyst.md) — L1 一線分析師（24/7 alert triage、初步調查、明確規則內處置）
- ✅ [`triage-l2-soc-analyst`](triage/triage-l2-soc-analyst.md) — L2 進階分析師（8x5 + on-call、跨資料源 pivot、執行 pre-approved containment playbook、IR 升級判斷）

### 🔬 Detection Engineering（偵測工程）
- ✅ [`detection-engineering-threat-detection-engineer`](detection-engineering/detection-engineering-threat-detection-engineer.md) — Detection rule 設計、coverage mapping、rule lifecycle、feedback intake
- ✅ [`detection-engineering-threat-hunter`](detection-engineering/detection-engineering-threat-hunter.md) — Hypothesis-driven hunting、hunt finding package handoff、coverage validation

### 🚨 Incident Response（事件回應）
- ✅ [`incident-response-ir-commander`](incident-response/incident-response-ir-commander.md) — IR 指揮、跨團隊協調、stakeholder 溝通
- ✅ [`incident-response-ir-analyst`](incident-response/incident-response-ir-analyst.md) — IR 執行、operational evidence collection、containment / eradication / recovery 驗證
- ✅ [`incident-response-forensics-analyst`](incident-response/incident-response-forensics-analyst.md) — Forensic-grade evidence acquisition、chain of custody、artifact analysis、preservation gating

### 🧠 Threat Intelligence（威脅情資）
- ✅ [`threat-intel-analyst`](threat-intel/threat-intel-analyst.md) — IOC / TTP contextualization、source reliability、confidence marking、actor-profile context（非 attribution）
- ✅ [`threat-intel-ioc-curator`](threat-intel/threat-intel-ioc-curator.md) — IOC lifecycle / aging / dedup / source hygiene execution（依既定 policy，提供 hygiene metrics 不下 source reliability judgment）

### 📋 Governance（治理）
- ✅ [`governance-soc-manager`](governance/governance-soc-manager.md) — Process / SLA / staffing / training / policy ownership；PIR facilitator（lessons-learned）；不參與 live incident command
- ✅ [`governance-compliance-auditor`](governance/governance-compliance-auditor.md) — Control framework internal interpretation（for review）、evidence sufficiency review、audit finding validation；不做 evidence packaging、不下 final compliance conclusion
- ✅ [`governance-audit-liaison`](governance/governance-audit-liaison.md) — 事實翻譯層、regulator-facing evidence package、control mapping、audit trail、compliance gap report

### 🟣 Purple Team（紫隊）
- ✅ [`purple-team-adversary-emulator`](purple-team/purple-team-adversary-emulator.md) — Scope-controlled emulation engagement；collaborative purple（非 red team）；Coverage validation signal handoff to Detection Engineering
- ✅ [`purple-team-detection-validator`](purple-team/purple-team-detection-validator.md) — Detection validation result interpretation、coverage 評估、result credibility review

---

## 使用方式

每個角色檔案是一份結構化 Markdown，含 frontmatter 元資料 + 多個章節。

- **Claude Code**：複製檔案內容到 `.claude/agents/<role>.md`，作為 subagent 定義
- **Cursor**：複製到 `.cursor/rules` 或作為 `@<role>` 引用的角色 prompt
- **Copilot / 其他**：直接複製或片段引用，作為對話 prompt 的角色設定

### Frontmatter 結構

每個 agent 檔案的 YAML frontmatter 採**雙層結構**：

```yaml
---
# === agency-agents 相容欄位 ===
name: L1 SOC Analyst                # Title Case，fork 工具直接相容
description: 一句話描述
color: blue
emoji: 🎯
vibe: 一句話的角色定位

# === RuleArena 擴充欄位（SOC 角色關係程式化解析用）===
agent_id: triage-l1-soc-analyst     # kebab-case，escalates_to 指向 agent_id
seniority: L1
shift_pattern: 24/7
primary_tactics: [TA0001, TA0002, TA0005]
escalates_to: triage-l2-soc-analyst
escalates_from: null
tool_stack:
  siem_primary: splunk
  siem_secondary: microsoft-sentinel
  edr: crowdstrike-falcon
  threat_intel: virustotal
---
```

上半相容 `agency-agents` 原格式，下半是 RuleArena 為 SOC 場景擴充的關係元資料（讓你能程式化分析角色升級鏈、工具盤點、ATT&CK 覆蓋）。

部分角色會有 optional extension fields，例如 `response_authority`：記載角色的 containment 與簽核邊界。Analyst tier（如 L2）含 `approved_playbooks`（可自主執行的 pre-approved playbook）與 `requires_ir_approval`（需升級簽核的高風險 action）；Incident Commander tier 含 `can_approve`（指揮鏈內可核准的 action，與下層 `requires_ir_approval` 對齊）、`cannot_approve_alone`（需與 Legal/Exec/PR 共同決策的 action 類別）、`delegates_to`（執行委派的 agent_id forward refs）。這類 extension 不是所有角色都有，依角色職責決定。

### 欄位語意設計原則

repo 內 frontmatter 關係欄位各自代表不同語意，**不混用**：

- `escalates_to` / `escalates_from`：**tier 升級鏈**（目前限 L1 → L2 → IR Commander 三角色）
- `delegates_to`：**指揮角色向下委派**（目前只有 IR Commander 用，指向具體執行 agent）
- `response_authority`：**角色本身的執行或簽核邊界**（`approved_playbooks` / `requires_*_approval` / `can_approve` / `cannot_approve_alone`）

純執行角色（如 IR Analyst）使用 `escalates_to/from: null` 並省略 `response_authority` 區塊；其 execution boundary 在 agent 正文描述。未來若有機器可讀的執行授權需求，再設計新 extension，不在現有欄位上堆疊不同語意。

---

## 驗證 (Validation)

repo 內附 `scripts/validate_authority_chain.py` 驗證跨 agent schema 一致性（檔名 ↔ agent_id、升級鏈雙向、authority mapping 子集規則等）。新增或修改 agent 後本地跑：

```bash
python3 -m pip install pyyaml          # 一次性依賴
python3 scripts/validate_authority_chain.py
```

WARN 不影響退出碼；FAIL 退出 1。詳細檢查項見 [`scripts/README.md`](scripts/README.md)。

上述 validator 只驗 **schema / 結構一致性**。spec 在特定情境下的**行為**（交付物結構是否符合角色定義、邊界守不守得住）沒有自動 harness，靠 [`tests/manual/`](tests/manual/README.md) 的情境 prompt 人工 dry-run——用來在 ship / drop 某條 backlog 條目前，確認 spec 變更是否真的改變了 agent 行為。

---

## 版本狀態 + Backlog

**v1.1 spec-update 已收口**：v1.0 release 後對 80 條 backlog item 做的 v1.1 spec-update，P1 全部 25 條已併入 agent 主檔、selected P2 closure set 已併入；其餘 P2 與 attribution / framing 相關條目移為 v1.2 candidate（候選池，非承諾交付範圍）。這不代表 backlog 清空——v1.1 是一個 spec-update 里程碑，不是 backlog 終點。

**v1.2 spec-update 已收口**：v1.1 之後再併入一組 agent 邊界與範圍細化（7 條 P2 boundary / scope / cadence 條目）；其餘 candidate 條目維持候選池（非承諾交付範圍）。

**v1.3 spec-update 已收口**：attribution framing 完整化（Threat Intel、Detection Engineering）、Compliance Auditor worked examples、L2 triage template consistency；初始 80 條 backlog 全數收口（75 resolved / 5 dropped）。

backlog 已全清零。歡迎 issue / PR 引用對應 `TUN-*` ID 提案新改善（先 search 避免重複）。對外方向（themes，不含時程）見 [`ROADMAP.md`](ROADMAP.md)。

---

## 設計原則

- **真實感優先**：所有範例（SPL、KQL、Sigma rule、Triage report）必須接近實務、可依環境調整後使用，不是 placeholder
- **角色邊界清楚**：L1 不寫 detection rule、Detection Engineer 不做 24/7 班輪值、IR Commander 不直接做 forensics
- **量化指標可調整**：成功指標標為 Example Metrics，附上「實際門檻依環境調整」說明，避免被讀者當絕對標準反駁
- **不貶低同業**：架構評論可，產品評論不可
- **繁中為主**：技術術語、產品名、code 保留英文；章節標題中英並列

---

## 對外揭露權責 (External Disclosure Authority)

跨角色治理規則：定義「誰能授權對外分享、各自邊界」。本段為**單一權威來源**；各 agent 檔（如 [`threat-intel-analyst`](threat-intel/threat-intel-analyst.md)、[`purple-team-detection-validator`](purple-team/purple-team-detection-validator.md)）只 cross-ref 本段，不各自定義對外授權模型。

### 預設安全出口（硬規則）

- **預設 = 不對外發言。** 任何 intel / detection coverage / incident 技術細節，未明確命中下方授權路徑時，一律回落「不對外」。
- 任何 external / public sharing 都需要 **(a) 明確授權角色 + (b) 明確條件**；缺一即回落預設。
- **無單一角色可獨自授權對外發言（含 IRC）。** go-public 路徑一律為 joint / conditional decision，不存在單人 authority。

### 四角色權責邊界

| 角色 | 做（authority scope） | 不做（boundary） |
| --- | --- | --- |
| **Legal** | 法律風險、合約、法遵義務、對外揭露限制 | 不對 incident facts 做技術判斷 |
| **IRC（IR Commander）** | incident response coordination、對外溝通節奏；協調訊息發布 | 不單獨決定可公開哪些技術細節 |
| **Audit Liaison** | 稽核 / 第三方審查資料窗口；受控揭露（controlled disclosure）初判 | 受控揭露 ≠ public disclosure；不開放公開分享 |
| **Compliance Auditor** | 合規證據、控制項符合性確認 | 不代表公司對外發言 |

### 揭露類型分層

1. **內部分享**（SOC team / DE / Hunter / SOC Manager / IRC）— 不觸發本框架。
2. **受控揭露**（regulator / 第三方稽核資料窗口）— 由 **Audit Liaison 初判**是否屬受控窗口；**Compliance Auditor** 確認合規證據與控制項符合性，但不對外發言。一旦超出受控審查 / 稽核窗口，**必須升級 Legal + IRC joint review**。
3. **公開 / 跨組織分享**（corporate blog、社群、ISAC、對 external auditor 發表立場）— 需 **Legal + IRC joint decision** + 明確授權條件，回落「無單人 authority」原則。

### 與各 agent hand-off gate 的關係

- 各 supporting agent（如 TI Analyst）的「對外引用前過 Legal / IRC」是**上游 hand-off gate**：確保對外候選內容先經 Legal / IRC，再進入本框架的 disclosure decision。
- hand-off gate **不等於** disclosure authority；agent 不自行跑完四角色決策，只負責識別「涉及外部揭露、需授權」並交付 sanitized draft + 標記需授權確認段落。actual disclosure decision 才引用本段。

---

## 對應 YouTube 系列

RuleArena 頻道 Agentic SIEM 系列影片發布後，會在對應的 agent 檔案末尾附上影片連結。

---

## License

[MIT](LICENSE)
