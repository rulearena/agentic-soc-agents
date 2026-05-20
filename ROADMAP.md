# Roadmap

> **這份 ROADMAP 是 public direction，不是 delivery commitment**：列出 agentic-soc-agents 接下來打算往哪走的方向（themes），但**不含時程**、**不承諾哪個 theme 何時完成**。Theme 狀態反映 maintainer 評估，會隨 issue / PR 進度移動。
>
> 想知道更細的 tactical 條目（具體 spec gap 與修法草案）見 [`backlog/triage-v1.1.md`](backlog/triage-v1.1.md)。

## 為什麼不寫日期

agentic-soc-agents 是 part-time 維運的 community-oriented repo。寫日期會逼維運者在「準時但品質打折」與「品質但跳票」之間二選一，兩種結果對 contributor 都不好。Themes 與 tactical backlog 提供方向；實際進度由 issue / PR 過程決定。

## 狀態圖例

- 🟡 **evaluating**：方向確認，spec 設計階段；歡迎 issue 與 design 提案
- 🔵 **in progress**：對應 PR 已開或合併進 main，但 family / cross-role 整合未完成
- ✅ **shipped**：v1.0 已併入 agent 主檔或新版本 release 已 publish

> **每個 theme 列的 `TUN-*` 條目是 representative（代表性），不是該 theme 的完整 scope**。Tactical source of truth 仍是 [`backlog/triage-v1.1.md`](backlog/triage-v1.1.md)（含 25 P1 / 33 P2 / 22 Later 完整表）。Theme 的最終實作範圍會在 issue / PR 過程中由 maintainer 與貢獻者共同決定。

## Themes

### 1. Authority Pressure Handling 🟡 evaluating

當 CISO / executive / Legal 對 SOC 角色施加越權壓力（override 既定 authority、跳過 approval gate、強迫 wording），各角色該怎麼識別、拒絕、留 audit trail。涵蓋 break-glass page 對象選擇、time-pressure escalation、override directive 升級 protocol、executive 越權處理章節等場景。

**Representative tactical source**（見 [`backlog/triage-v1.1.md`](backlog/triage-v1.1.md)，下列為代表性條目、非該 theme 完整列表）：
- `TUN-MGR-001` SOC Manager 對 CISO override response playbook
- `TUN-AE-001` Adversary Emulator 對 executive 越權處理章節
- `TUN-AL-001` Audit Liaison 對 CISO/Exec override directive 升級 protocol
- `TUN-CA-001` Compliance Auditor 對 Legal time-pressure escalation

### 2. Cross-Role Refusal Templates 🟡 evaluating

不同 stakeholder（同儕、業務 owner、exec、SOAR Engineer、跨角色合併）對 SOC 角色提出越界邀請時的拒絕範本 — 共用設計骨幹（澄清分工 + 解釋風險 + 給替代品 + audit trail），但具體 stakeholder 措辭與 redirect 對象分別設計。

**Representative tactical source**：
- `TUN-L1-001` L1 對同儕越權請求（越界邀請 family hub）
- `TUN-IRA-002` IR Analyst 對 exec 越級拒絕範本
- `TUN-CA-002` Compliance Auditor 對 cross-role consolidation 拒絕
- `TUN-IOC-002` IOC Curator 對 SOC Manager 跨界改 source policy 拒絕

### 3. Operational Boundary Specification 🟡 evaluating

把 v1.0 隱性的角色 / scope 邊界顯性化 — verification query scope、Detection Engineer Mode B 範圍（atomic IOC vs behavioral rule）、IRC 事件期間「在規則內可做事項」menu、DRAFT evidence pack access control 等實作層細節。讓新人讀 agent 主檔時不必猜邊界在哪。

**Representative tactical source**：
- `TUN-IRA-001` Verification query scope 邊界
- `TUN-DE-001` Detection Engineer Mode B 範圍（atomic IOC vs behavioral）
- `TUN-IOC-001` IRC 事件期間「在規則內可做事項」menu
- `TUN-AL-002` DRAFT evidence pack access control 與 distribution log

### 4. Public-Facing Wording & Disclaimers 🟡 evaluating

對外（regulator、auditor、CISO 報告、board）措辭的精確化 — attribution 字眼合規降階、sample-size disclaimer、fait accompli 識別、disclosure handoff 範本、PIR 個人 vs 制度分流。錯誤措辭一旦對外發出就很難收回，這個 theme 著重在「**寫出去之前就攔住**」的設計。

**Representative tactical source**：
- `TUN-DV-002` Fait accompli pattern 清單（fait accompli family hub）
- `TUN-AL-003` 業務 framing 壓力辨識指引（fait accompli + 灌水 hub）
- `TUN-TI-001` Attribution 字眼合規降階對照表
- `TUN-TI-002` 高壓對外 briefing 緊急流程

## 如何 influence Roadmap

- **想推動某個 theme** → 開 issue 引用對應 `TUN-*` ID，描述 use case 與設計建議；issue 引用 backlog 條目比抽象提案更容易被採納
- **想領一條來修** → 直接 PR，PR description 引用 `TUN-*` ID；修完後該條 backlog item 移到對應 `backlog/<category>.md` 底部 Changelog（v1.0 既有慣例）
- **想提案新 theme** → 開 issue 並引用 2 條以上 backlog 既有條目作支撐，避免發明新方向卻忽略已知 gap

## Out of scope（這份 ROADMAP **不**承諾）

- 沒有日期、沒有 quarter、沒有 ETA
- 沒有「某 theme 何時完成」的保證
- 沒有 release date 承諾
- 沒有對「哪條 P1 一定會修」的硬承諾

換言之：本檔列出**方向**，不列出**時間**。

## 連結

- [`backlog/`](backlog/) — 80 條 tactical backlog（內含 ⭐ 高 / 中 / 低 設計優先序）
- [`backlog/triage-v1.1.md`](backlog/triage-v1.1.md) — v1.1 tactical triage（25 P1 / 33 P2 / 22 Later）
- [`backlog/README.md`](backlog/README.md) — backlog 索引 + cross-file design patterns
