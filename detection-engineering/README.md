# Detection Engineering — 偵測工程

## 分類定位

把「該怎麼偵測」變成可長期維護的程式碼。職責是讓 Triage 看到的告警有意義、有覆蓋、有信號品質。

**典型工作**：
- Sigma rule 撰寫（vendor-agnostic）+ 編譯成 Splunk SPL / Sentinel KQL / Elastic EQL
- MITRE ATT&CK 覆蓋率分析、gap 補強
- Detection-as-code pipeline：rules in Git、CI 測試、自動部署
- 主動威脅搜索（threat hunting）將發現轉為自動化偵測
- False positive 調校、log source 健康監控

**不在這分類**：
- 接收告警執行 triage → 屬 [`triage/`](../triage/)
- 事件指揮 → 屬 [`incident-response/`](../incident-response/)
- TI feed 接入 → 屬 [`threat-intel/`](../threat-intel/)（與 Detection Engineer 合作但職責不同）

## 角色清單

✅ 已完成、⏳ 規劃中

- ✅ [`detection-engineering-threat-detection-engineer`](detection-engineering-threat-detection-engineer.md) — Detection rule 設計、coverage mapping、rule lifecycle 管理、6 個下游角色 detection feedback intake
- ⏳ `detection-engineering-threat-hunter` — Hypothesis-driven hunting、TTP-based search、hunt-to-detection 轉換
