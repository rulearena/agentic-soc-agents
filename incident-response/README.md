# Incident Response — 事件回應

## 分類定位

把告警升級成事件之後接手的角色群組。職責是把混亂變成結構化的回應、把事件變成可學習的後續行動。

**典型工作**：
- 嚴重度判定、IR 角色分工（Commander / Comms Lead / Tech Lead / Scribe）
- Containment、eradication、recovery 操作
- Forensics：memory dump、disk imaging、artifact 分析
- Stakeholder 溝通（內部、客戶、監管機關）
- Post-mortem facilitation、follow-up action items 追蹤

**不在這分類**：
- 告警初步分流 → 屬 [`triage/`](../triage/)
- 偵測規則調校 → 屬 [`detection-engineering/`](../detection-engineering/)
- IOC 後續追蹤 → 屬 [`threat-intel/`](../threat-intel/)

## 角色清單

✅ 已完成、⏳ 規劃中

- ✅ [`incident-response-ir-commander`](incident-response-ir-commander.md) — IR 指揮、跨團隊協調、severity escalation、stakeholder 溝通
- ⏳ `incident-response-ir-analyst` — IR 執行、evidence collection、containment 操作、recovery 驗證
- ⏳ `incident-response-forensics-analyst` — Digital forensics、memory analysis、disk imaging、artifact 鑑識
