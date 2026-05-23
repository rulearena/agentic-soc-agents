# v1.1 Triage Result

> **Note**：本檔是 v1.0 release 後 80 條 backlog item 的 v1.1 spec update 排序結果。
> - 原 `backlog/*.md` 內每條的 ⭐ 高 / 中 / 低 是「設計優先序」（內部評估時用，**不改**）
> - 本檔 P1 / P2 / Later 是「v1.1 排序」（哪些進下一波 spec update）
> - 兩者不衝突也不必對齊：本檔 P1 不代表原本是 ⭐ 高；本檔 Later 不代表不重要

## 排序原則

**P1 候選（25 條，分兩組）：**
1. 角色邊界（boundary）
2. authority / approval / override
3. public-facing wording / disclaimer / 對外措辭
4. 跨角色一致性（cross-role consistency）/ cross-file family hub

**Later 候選：**
- cheatsheet / quick reference
- template format polish
- 純 nice-to-have template / example library

## P1 list（25 條）

### 第一組：boundary / authority / 拒絕範本（17 條，建議優先）

| # | ID | 標題 | Principle tag | Family / 備註 |
|---|---|---|---|---|
| 1 | [TUN-L1-001](triage.md) | 缺「越權請求拒絕範本」 | 拒絕 / boundary | **越界邀請 family hub** — ✅ shipped in this PR |
| 2 | [TUN-L1-002](triage.md) | 缺 process / tuning escalation 路徑 | boundary | — |
| 3 | [TUN-L2-001](triage.md) | Privileged service account 出現在 attack scope 的 SOP 不夠明確 | authority / approval | ✅ shipped in this PR |
| 4 | [TUN-L2-002](triage.md) | 跨業務單位同 dropper / IOC 的硬升級規則 | authority / escalation | ✅ shipped in this PR |
| 5 | [TUN-IRA-001](incident-response.md) | Verification query scope 邊界沒明示 | boundary | — |
| 6 | [TUN-IRA-002](incident-response.md) | 業務 owner / exec 越級直接 ping 執行端的拒絕範本缺 | 拒絕 / boundary | 越界邀請 family — ✅ shipped in this PR |
| 7 | [TUN-FOR-001](incident-response.md) | Side-channel pressure 處理範本缺 | 拒絕 | ✅ shipped in this PR |
| 8 | [TUN-DE-001](detection-engineering.md) | Mode B 範圍邊界需具體化（atomic IOC vs behavioral rule） | boundary | ✅ shipped in this PR |
| 9 | [TUN-DE-002](detection-engineering.md) | War room IRC immediate response 範本缺 | 拒絕 / authority | ✅ shipped in this PR |
| 10 | [TUN-HUNT-001](detection-engineering.md) | Break-glass page IRC 對象選擇規則缺 | authority / escalation | ✅ shipped in this PR |
| 11 | [TUN-IOC-001](threat-intel.md) | IRC 事件期間「在規則內可做事項」明確 menu 缺 | boundary / authority | ✅ shipped in this PR |
| 12 | [TUN-IOC-002](threat-intel.md) | Policy Change Decline Template（拒絕 SOC Manager 跨界改 source policy） | 拒絕 / boundary | ✅ shipped in this PR |
| 13 | [TUN-AE-001](purple-team.md) | CISO / executive 越權的明確處理章節 | authority / override | — |
| 14 | [TUN-MGR-001](governance.md) | CISO override pressure response playbook | authority / override | **+ TUN-MGR-006 (P2) 同步設計** |
| 15 | [TUN-CA-001](governance.md) | Time-pressure escalation playbook | authority | — |
| 16 | [TUN-CA-002](governance.md) | Cross-role consolidation 拒絕範本 | 拒絕 / boundary | 越界邀請 family — ✅ shipped in this PR |
| 17 | [TUN-AL-001](governance.md) | AL escalation protocol when receiving CISO/Exec override directive | authority / override | — |

### 第二組：public-facing wording / consistency（8 條，第一組穩定後）

| # | ID | 標題 | Principle tag | Family / 備註 |
|---|---|---|---|---|
| 18 | [TUN-DV-001](purple-team.md) | Sample size disclaimer 範本 | public-facing wording | ✅ shipped in this PR |
| 19 | [TUN-DV-002](purple-team.md) | Fait accompli 圈套 pattern 清單 | wording / consistency | **Fait accompli family hub** — ✅ shipped in this PR |
| 20 | [TUN-AL-003](governance.md) ⬆ | 業務 framing 壓力的辨識指引（原中升 P1） | wording / consistency | **Fait accompli + 灌水 hub** — ✅ shipped in this PR |
| 21 | [TUN-TI-001](threat-intel.md) | Attribution 字眼合規降階對照表缺 | public-facing wording | Attribution family |
| 22 | [TUN-TI-002](threat-intel.md) ⬆ | 24 小時高壓對外 briefing 緊急流程缺 | wording / authority / 對外風險 | — |
| 23 | [TUN-AE-003](purple-team.md) | Engagement 期間發現 scope 外真實漏洞的 disclosure handoff 範本 | wording / boundary | — |
| 24 | [TUN-MGR-002](governance.md) | 個人 vs 制度的 PIR 分流機制 | consistency / boundary | — |
| 25 | [TUN-AL-002](governance.md) | DRAFT evidence pack 的 access control 與 distribution log 規格 | control / wording | — |

**升 P1 說明（2 條）：**
- **TUN-AL-003**（原 中）：是 fait accompli + 灌水 **兩個 family 的 hub**，purple-team.md 已 cross-reference TUN-DV-002 → 不升會讓 TUN-DV-002 變單腳 design
- **TUN-TI-002**（原 ⭐ 高）：同時踩 public-facing wording + Legal/IRC review gate + SOC Manager pressure handling + 對外發布風險 4 個 risk vector

**從原 ⭐ 高降 P2（3 條）：**
- **TUN-MGR-003**（Recognition framework）— framework 性質、非緊急 boundary
- **TUN-FOR-002**（Anti-forensics SOP）— 技術 SOP 而非 wording/boundary
- **TUN-AE-002**（Scope drift 自我通報）— disclosure path 但比 AE-003 弱

---

## P2 list（33 條，含 3 條原⭐高降 P2）

| # | ID | 標題 | 原 priority | Family / 備註 |
|---|---|---|---|---|
| 1 | [TUN-L1-003](triage.md) | 缺 time-critical TP 快速升級決策框架 | 中 | — |
| 2 | [TUN-L1-005](triage.md) | Evidence pending 處理規範 | 中 | — |
| 3 | [TUN-L2-003](triage.md) | Supply chain hypothesis 的並行 hand-off 路徑 | 中 | — |
| 4 | [TUN-IRC-001](incident-response.md) | `cannot_approve_alone` 缺法規時限速查 hook | 中 | — |
| 5 | [TUN-IRC-002](incident-response.md) | 業務 owner 跨界引導技術決策的 Anti-Pattern 缺位 | 中 | — |
| 6 | [TUN-IRA-003](incident-response.md) | Pending action 在 BLOCK 狀態下的回報節奏沒明示 | 中 | — |
| 7 | [TUN-IRA-004](incident-response.md) | 跨 rotation IR-A 接班的 handoff template 缺 | 中 | — |
| 8 | [TUN-FOR-002](incident-response.md) | Anti-forensics 觸發場景的 SOP 缺 | ⭐ 高（降）| — |
| 9 | [TUN-FOR-003](incident-response.md) | Partial preservation acceptable threshold 判斷材料缺 | 中 | Attribution family 邊緣成員 |
| 10 | [TUN-FOR-004](incident-response.md) | Override 流程的「業務時程壓力」入口未明說 | 中 | — |
| 11 | [TUN-DE-003](detection-engineering.md) | Replacement readiness gate 機制未明寫 | 中 | — |
| 12 | [TUN-DE-004](detection-engineering.md) | Production FP rate ongoing measurement 路徑未定義 | 中 | — |
| 13 | [TUN-DE-005](detection-engineering.md) | Audit Liaison 拒灌水的 framing 範本缺 | 中 | 灌水 family（hub = AL-003 P1） |
| 14 | [TUN-HUNT-002](detection-engineering.md) | Hunt 補充 enrichment 給 IR Analyst 的邊界未明示 | 中 | — |
| 15 | [TUN-HUNT-003](detection-engineering.md) | 「事實 vs 結論」line drawing examples 缺 | 中 | Attribution family |
| 16 | [TUN-HUNT-004](detection-engineering.md) | SOC Manager 越界場景的明確邊界缺 | 中 | — |
| 17 | [TUN-TI-003](threat-intel.md) | IRC war room joint decision walk-through 範本缺 | 中 | Attribution family |
| 18 | [TUN-TI-004](threat-intel.md) | Actor context multi-cluster triangulation 範本欄位缺 | 中 | — |
| 19 | [TUN-TI-005](threat-intel.md) | Hunter handoff → TI 出 IB+TPS+APC turnaround SLA 缺 | 中 | — |
| 20 | [TUN-TI-006](threat-intel.md) | TLP 對外分享分級決策樹缺 | 中 | — |
| 21 | [TUN-IOC-003](threat-intel.md) | TI Analyst 邀請越界的明確邊界規則 | 中 | — |
| 22 | [TUN-MGR-003](governance.md) | Recognition framework 設計原則 | ⭐ 高（降）| — |
| 23 | [TUN-MGR-004](governance.md) | Staffing change 在 incident 後的冷卻期 | 中 | — |
| 24 | [TUN-MGR-005](governance.md) | Metrics-to-performance 防火牆語言 | 中 | — |
| 25 | [TUN-MGR-006](governance.md) | War room observer 條款 | 中 | **與 TUN-MGR-001 (P1) 同步設計**（避免 authority wording 之後重修） |
| 26 | [TUN-CA-004](governance.md) | CIN as policy input 流程 | 中 | — |
| 27 | [TUN-AL-004](governance.md) | Chain of custody 簽收的「合理優化 vs 違規捷徑」分界 | 中 | — |
| 28 | [TUN-AE-002](purple-team.md) | Scope drift 自我通報範本 | ⭐ 高（降）| 弱於 AE-003 (P1) |
| 29 | [TUN-AE-004](purple-team.md) | 疑似 real event 期間 Engagement Log 是否屬 forensic evidence | 中 | — |
| 30 | [TUN-AE-005](purple-team.md) | Executive override attempt 的 audit trail | 中 | 與 AE-001 (P1) 同層級 authority 議題 |
| 31 | [TUN-DV-003](purple-team.md) | Single-engagement vs cross-engagement 結論的時間維度限制 | 中 | — |
| 32 | [TUN-DV-004](purple-team.md) | 高 authority 拒絕語言範本 | 中 | — |
| 33 | [TUN-DV-005](purple-team.md) | 與 Audit Liaison 的具體 handoff workflow | 中 | — |

---

## Later list（22 條）

| # | ID | 標題 | 原 priority |
|---|---|---|---|
| 1 | [TUN-L1-004](triage.md) | 缺 IOC 取得操作層細節 | 中 |
| 2 | [TUN-L1-006](triage.md) | 常見 triage heuristic quick reference 擴充 | 低 |
| 3 | [TUN-L1-007](triage.md) | Handover note 加 tuning ticket 追蹤欄 | 低 |
| 4 | [TUN-L2-004](triage.md) | Investigation Report 加 `Affected Data Assets` 子段 | 中 |
| 5 | [TUN-L2-005](triage.md) | L1 已 break-glass page IR 時 L2 的並行責任 | 低 |
| 6 | [TUN-IRC-003](incident-response.md) | Sev-1 暫定 → confirm/downgrade 缺時間框架 | 低 |
| 7 | [TUN-IRC-004](incident-response.md) | Break-glass 合理使用 vs 濫用的 post-incident 判定範本 | 低 |
| 8 | [TUN-IRC-005](incident-response.md) | AAR 範本缺 `Parallel notification (non-blocking)` 欄位 | 低 |
| 9 | [TUN-IRA-005](incident-response.md) | 「自己不做但建議拉誰進來」的 phrasing 邊界沒明示 | 低 |
| 10 | [TUN-IRA-006](incident-response.md) | Operational evidence 的 attach / 保存格式範本缺 | 低 |
| 11 | [TUN-FOR-005](incident-response.md) | 「ETA 超出 IRC 要求」的回應姿態未範本化 | 低 |
| 12 | [TUN-DE-006](detection-engineering.md) | SOAR Engineer 反向要求寫 YAML 的拒絕範本缺 | 低（越界邀請 family member）|
| 13 | [TUN-HUNT-005](detection-engineering.md) | TI 引誘 attribution 的標準回應範本缺 | 低（Attribution family member）|
| 14 | [TUN-IOC-004](threat-intel.md) | Dedup Resolution Log 加 "Candidates Not Merged" 欄位 | 中 |
| 15 | [TUN-IOC-005](threat-intel.md) | Source 自帶 actor 標籤的處理規則缺 | 低（Attribution family member）|
| 16 | [TUN-MGR-007](governance.md) | Multi-input pressure session 的優先序協議 | 低 |
| 17 | [TUN-CA-003](governance.md) | Sister evidence vs disputed pressure 範例庫 | 中 |
| 18 | [TUN-CA-005](governance.md) | Audit Liaison rotation 間協作邊界 | 低 |
| 19 | [TUN-CA-006](governance.md) | Customer-facing letter 措辭支援範圍 | 低 |
| 20 | [TUN-AL-005](governance.md) | 與 Legal 的「分工但不背書」邊界範本 | 低 |
| 21 | [TUN-AE-006](purple-team.md) | Multi-source charter input 整合 protocol | 低 |
| 22 | [TUN-DV-006](purple-team.md) | Re-test backlog 在 Emulator 容量受限期的處理 | 低 |

---

## Cross-file family 整合建議

引用 [`README.md` 的 cross-file design patterns](README.md#cross-file-design-patterns) 段落，列出對應 P1 / P2 / Later 成員。

下表 membership 以 README 為基準；標 **adjacent** 的條目是 triage 階段新增的 wording-related 邊緣成員，README 原 family 表內沒列。

| Family | 成員（按 v1.1 排序）|
|---|---|
| **Fait accompli + 業務 framing**（直接 cross-reference）| `TUN-DV-002` **(P1)** ↔ `TUN-AL-003` **(P1，升)** |
| **Attribution 拒絕 / 字眼降階** | `TUN-TI-001` **(P1)** + `TUN-TI-003` (P2) + `TUN-HUNT-003` (P2，**adjacent**：「事實 vs 結論」line drawing 影響 attribution framing) + `TUN-FOR-003` (P2 邊緣) + `TUN-IOC-005` (Later) + `TUN-HUNT-005` (Later) |
| **越界邀請拒絕範本** | `TUN-L1-001` **(P1)** + `TUN-IRA-002` **(P1)** + `TUN-CA-002` **(P1)** + `TUN-DE-006` (Later) |
| **灌水抵抗** | `TUN-DE-005` (P2) + `TUN-AL-003` **(P1，灌水/fait accompli hub)** |

→ Family hub 進 P1 時 family 成員的措辭應預先納入 spec update design，避免 P1 修完後 P2/Later 還要 refactor。

### 額外設計連動（非 family 但有依賴）

- **`TUN-MGR-001` (P1) ↔ `TUN-MGR-006` (P2)**：前者處理 CISO override pressure response、後者處理 War room observer 條款。兩者皆 CISO/exec authority 議題；做 MGR-001 時同步考慮 MGR-006 的 wording 與 audit trail，避免 P1 修完後 P2 還要 refactor authority 語言
- **`TUN-AE-001` (P1) ↔ `TUN-AE-005` (P2)**：前者是 executive override 處理章節、後者是 override attempt 的 audit trail；同層級 authority 議題，做 AE-001 時可順便草擬 AE-005 的 audit trail 欄位骨架

---

## 對外承諾邊界

本檔**不是 ROADMAP** — **不承諾時程**。P1 = 「v1.1 候選」≠ 「v1.1 必出」。實際進 v1.1 由 issue/PR 過程決定。對外方向見 [`ROADMAP.md`](../ROADMAP.md)（themes，**不含時程**）。
