# v1.1 Tactical Backlog

> **Note**：本目錄是 v1.0 release 之後在實測中發現、尚未併入 14 個 agent 主檔的改善建議集合。v1.1 spec-update 的優先排序見 [`triage-v1.1.md`](triage-v1.1.md)（25 P1 / 33 P2 / 22 Later）；P1 已全數收口、selected P2 已 ship，其餘為 v1.2 candidate（候選池，非承諾交付範圍）。contribution 前請先在對應 category 檔案 search 既有 `TUN-*` ID 避免重複提案。

## 一句話定位

每一條 backlog item 代表「目前 agent 定義在實際 SOC 任務上會被新人或自動化測試挑出來的弱點」，**不是 bug**。處理優先序與是否採納依 repo 維護節奏決定。

## 索引

| Category | 檔案 | Active | Resolved | 對應 agent 檔名 stem |
|---|---|---|---|---|
| Triage | [triage.md](triage.md) | 5 | 7 | `triage-l1-soc-analyst`, `triage-l2-soc-analyst` |
| Incident Response | [incident-response.md](incident-response.md) | 8 | 8 | `incident-response-ir-commander`, `incident-response-forensics-analyst`, `incident-response-ir-analyst` |
| Detection Engineering | [detection-engineering.md](detection-engineering.md) | 5 | 6 | `detection-engineering-threat-detection-engineer`, `detection-engineering-threat-hunter` |
| Threat Intel | [threat-intel.md](threat-intel.md) | 6 | 5 | `threat-intel-analyst`, `threat-intel-ioc-curator` |
| Governance | [governance.md](governance.md) | 7 | 11 | `governance-soc-manager`, `governance-compliance-auditor`, `governance-audit-liaison` |
| Purple Team | [purple-team.md](purple-team.md) | 5 | 7 | `purple-team-adversary-emulator`, `purple-team-detection-validator` |
| **合計** | — | **36 active** | **44 resolved** | 14 個 agent（total corpus 80）|

## v1.1 排序狀態

v1.0 release 後對 80 條 backlog item 的 v1.1 tactical triage 結果見 [`triage-v1.1.md`](triage-v1.1.md)：

- **25 條 P1**（v1.1 候選，分 boundary/authority 17 條與 public-facing wording/consistency 8 條兩組）
- **33 條 P2**（v1.1 以後考慮；含 3 條原 ⭐ 高降 P2）
- **22 條 Later**（cheatsheet / format polish / nice-to-have template）

> **這份排序不是對外 ROADMAP，也不是時程承諾**。P1 = 「v1.1 候選」≠ 「v1.1 必出」；實際進入 v1.1 由 issue / PR 過程決定。對外方向見 [`ROADMAP.md`](../ROADMAP.md)（themes，**不含時程**）。

## 條目格式

每條含四欄：
- **問題**：定義裡缺什麼或哪個邊界鬆
- **測試來源**：實測中由哪個測試挑出（Test A–O 等）
- **建議方向**：可採取的修法草案
- **優先序**：⭐ 高 / 中 / 低（**僅內部設計優先序，不等於 release 順序**）

## 使用方式

1. **想提案新條目** → 先 search 對應 category 檔案的既有 TUN-id，確認沒有重複後再開 issue
2. **想領一條來修** → 開 PR 修對應 agent 主檔（例：`triage/triage-l1-soc-analyst.md`），在 PR description 引用 `TUN-L1-001`；修完後該條移到該檔底部 `Changelog`
3. **想做 batch tuning** → 看下方 Cross-file design patterns 段落，相關條目可一起設計避免 churn

## Cross-file design patterns

下表列「可共同設計或應注意措辭一致」的跨檔 pattern。只有 `TUN-DV-002` ↔ `TUN-AL-003` 是檔案內明確 cross-reference；其餘是依 backlog 條目問題描述歸納出的 shared design family，實作時仍需逐條確認。

| Pattern | 涉及條目 | 依據與設計注意 |
|---|---|---|
| **Fait accompli / 業務 framing 識別**（purple ↔ governance） | `TUN-DV-002` ↔ `TUN-AL-003` | **檔案內明確 cross-reference**：`purple-team.md` 寫「Cross-reference Audit Liaison TUN-AL-003（一致設計）」。前者列 fait accompli pattern 清單，後者列業務 framing 壓力辨識指引；兩者共用「業務語言包裝 process 違規」的識別與拒絕設計，應同步修。 |
| **Attribution 拒絕 / 字眼降階 family**（detection-engineering ↔ threat-intel ↔ incident-response） | `TUN-HUNT-005` ↔ `TUN-TI-001` ↔ `TUN-TI-003` ↔ `TUN-IOC-005` ↔ `TUN-FOR-003` | **歸納 pattern（非檔案 cross-reference）**：v1.0「無人下 final attribution」原則的具體 framing。`TUN-HUNT-005` Threat Hunter 對 TI 引誘 attribution 的回應範本、`TUN-TI-001` TI Analyst 字眼合規降階對照表、`TUN-TI-003` TI war room joint decision、`TUN-IOC-005` IOC Curator 對 source 自帶 actor 標籤的處理屬同 framing；`TUN-FOR-003`（Forensics partial preservation acceptable threshold）關聯較間接，主軸是 preservation threshold 判斷、attribution 是其應用場景之一，措辭一致化時納入考量但不直接共用 template。 |
| **越界邀請拒絕範本 family**（triage ↔ incident-response ↔ detection-engineering ↔ governance） | `TUN-L1-001` ↔ `TUN-IRA-002` ↔ `TUN-DE-006` ↔ `TUN-CA-002` | **歸納 pattern（非檔案 cross-reference）**：不同 stakeholder 的越界邀請拒絕範本 — L1 對同儕越權請求、IR Analyst 對 exec 越級直接 ping、DE 對 SOAR Engineer 反向要求寫 YAML、Compliance Auditor 對 cross-role consolidation。底層結構（澄清分工 + 解釋風險 + 給替代品 + audit trail）相似，可考慮統一抽出 template，但具體 stakeholder 措辭與升級對象仍需分別設計。 |
| **灌水抵抗 framing**（detection-engineering ↔ governance） | `TUN-DE-005` ↔ `TUN-AL-003` | **歸納 pattern（非檔案 cross-reference）**：DE 拒 Audit Liaison 灌水要求 / Audit Liaison 自己辨識業務 framing 壓力。共用同一 reverse-argumentation framing（「標已覆蓋拿不出 evidence → audit finding 升等」），底層設計可一致化。注意 `TUN-AL-003` 也出現在第 1 條 fait accompli 對照中，是兩個 dimension 都涵蓋的 hub item。 |

> 若有 pattern 不在此表但你認為應列入，歡迎開 issue 補（附 TUN-id + 依據段落）。

## 為什麼公開

backlog 公開不是承諾 roadmap，而是讓貢獻者：
- 看到專案維運者已知的 gap（不必重複提案）
- 評估「想領的條目」是否與其他條目 coupled
- 對 agent 定義局限性保有透明預期

對外方向見 [`ROADMAP.md`](../ROADMAP.md)（themes，**不含時程**）。
