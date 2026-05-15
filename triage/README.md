# Triage — 一線分流

## 分類定位

SOC 第一道分流關卡。職責是把告警佇列裡的訊號變成可調查的事件，或把雜訊變成可信任的「已查證 false positive」。

**典型工作**：
- 24/7 / 8x5 班輪值告警處理
- 初步真假快篩、enrichment、判定
- 明確規則內處置（mark FP、close ticket、發 advisory）
- 升級判斷（什麼狀況要交給 L2、什麼狀況要直接通知 IR）

**不在這分類**：
- 寫新 detection rule → 屬 [`detection-engineering/`](../detection-engineering/)
- 主動威脅搜索 → 屬 `detection-engineering-threat-hunter`
- 高風險 containment / eradication 屬 [`incident-response/`](../incident-response/)；L2 僅能執行 pre-approved、低到中風險 containment playbook（詳見 L2 agent 的「反應權限」章節）
- IOC 生命週期管理 → 屬 [`threat-intel/`](../threat-intel/)

## 角色清單

✅ 已完成、⏳ 規劃中

- ✅ [`triage-l1-soc-analyst`](triage-l1-soc-analyst.md) — L1 一線分析師：告警接收、真假快篩、明確規則內處置、升級到 L2 的判斷
- ✅ [`triage-l2-soc-analyst`](triage-l2-soc-analyst.md) — L2 進階分析師：多源 pivot、深度 enrichment、執行 pre-approved containment playbook、IR Commander 升級判斷
