# Agentic SOC Agents

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
- ⏳ `triage-l2-soc-analyst` — L2 進階分析師（pivot、enrichment、IR 銜接）

### 🔬 Detection Engineering（偵測工程）
- ⏳ `detection-engineering-threat-detection-engineer` — 偵測規則撰寫、Sigma rule、ATT&CK 覆蓋
- ⏳ `detection-engineering-threat-hunter` — 主動威脅搜索、hypothesis-driven hunting

### 🚨 Incident Response（事件回應）
- ⏳ `incident-response-ir-commander` — IR 指揮、跨團隊協調、stakeholder 溝通
- ⏳ `incident-response-ir-analyst` — IR 執行、evidence collection、containment
- ⏳ `incident-response-forensics-analyst` — Digital forensics、memory analysis、disk imaging

### 🧠 Threat Intelligence（威脅情資）
- ⏳ `threat-intel-analyst` — TI 收集、TTP 對應、actor profiling
- ⏳ `threat-intel-ioc-curator` — IOC 生命週期管理、ageing、源信譽評估

### 📋 Governance（治理）
- ⏳ `governance-soc-manager` — SOC 運營管理、SLA 追蹤、團隊培訓
- ⏳ `governance-compliance-auditor` — 合規對應（SOC 2、ISO 27001、NIST CSF）
- ⏳ `governance-audit-liaison` — 內外稽核窗口、evidence 蒐集

### 🟣 Purple Team（紫隊）
- ⏳ `purple-team-adversary-emulator` — Atomic Red Team、CALDERA 對應
- ⏳ `purple-team-detection-validator` — 偵測規則驗證、coverage 測試

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

---

## 設計原則

- **真實感優先**：所有範例（SPL、KQL、Sigma rule、Triage report）必須接近實務、可依環境調整後使用，不是 placeholder
- **角色邊界清楚**：L1 不寫 detection rule、Detection Engineer 不做 24/7 班輪值、IR Commander 不直接做 forensics
- **量化指標可調整**：成功指標標為 Example Metrics，附上「實際門檻依環境調整」說明，避免被讀者當絕對標準反駁
- **不貶低同業**：架構評論可，產品評論不可
- **繁中為主**：技術術語、產品名、code 保留英文；章節標題中英並列

---

## 對應 YouTube 系列

RuleArena 頻道 Agentic SIEM 系列影片發布後，會在對應的 agent 檔案末尾附上影片連結。

---

## License

[MIT](LICENSE)
