# Roadmap

> 方向主題，不含時程承諾。實際進度見 [`backlog/`](backlog/README.md)。

## 當前狀態

**初始 backlog 全清零（v1.3）**

v1.0 release 後累積的 80 條改善建議，已在 v1.1、v1.2、v1.3 三個迭代全數收口：75 條已併入 14 個 agent 主檔、5 條主動 drop。

| 版本 | 收口重點 |
|---|---|
| **v1.1** | Role boundary clarification（25 P1）+ selected P2 spec-update |
| **v1.2** | Boundary/scope/cadence 細化（P2 第二批）+ External Disclosure Authority 框架 |
| **v1.3** | Attribution framing（Threat Intel、Detection Engineering）+ Compliance Auditor worked examples |

## 開放貢獻方向

以下為目前 14 個 agent 定義仍有空間發展的主題，**非承諾交付範圍、無時程**。

### 跨角色協作情境

agent 主檔定義各角色邊界，但缺少「多 agent 協作的端對端情境範例」——例如 L1 escalation → L2 triage → IR Commander hand-off 完整案例、或 DE ↔ TI 聯合獵捕的協同流程。

### 平台差異化

agent 主檔以平台中立為原則（SPL / KQL / Sigma 皆有標注）。未來可補充「各平台版 quick reference」，讓使用者直接對應其 SIEM stack。

### Cheatsheet / 速查卡

v1.x 過程中有部分 format polish 與 cheatsheet 條目因優先序低而未進迭代。適合以 PR 形式補充。

### 新角色提案

14 個 agent 覆蓋主要 SOC 崗位，但部分常見角色尚未定義：SOAR 整合、雲端安全、Vulnerability Management 等。**新角色提案請先開 issue 討論邊界設計，再送 PR。**

### 情境驗證測試

`scripts/validate_authority_chain.py` 目前以結構規則為主。可考慮補充端對端情境腳本——輸入模擬 incident，驗證多個 agent hand-off 鏈是否符合定義。

## 貢獻方式

詳見 [backlog/README.md](backlog/README.md) § 使用方式。
