# Threat Intelligence — 威脅情資

## 分類定位

把外部世界的威脅資訊轉成內部可作業的 context。職責是讓 SOC 在判定告警時有足夠的「敵情」資料，而不是只看內部 telemetry。

**典型工作**：
- TI feed 收集（OSINT、商業情資、ISAC、政府機關）
- IOC 生命週期管理（aging、source hygiene 指標、dedup / deconfliction）
- TTP 對應 MITRE ATT&CK、actor-profile context（只作脈絡，不下 attribution 結論）
- Threat landscape 報告（產業別、地理別、時間別）
- 把情資轉成 Detection Engineering 的 hunt hypothesis 或新 rule

**不在這分類**：
- 寫 detection rule → 屬 [`detection-engineering/`](../detection-engineering/)（合作但職責不同）
- 主動搜索 → 屬 `detection-engineering-threat-hunter`
- 跟客戶/監管溝通 → 屬 [`incident-response/`](../incident-response/) 或 [`governance/`](../governance/)

## 角色清單

✅ 已完成、⏳ 規劃中

- ✅ [`threat-intel-analyst`](threat-intel-analyst.md) — IOC / TTP contextualization、source reliability、confidence marking、actor-profile context（非 attribution）
- ✅ [`threat-intel-ioc-curator`](threat-intel-ioc-curator.md) — IOC lifecycle / aging / dedup / source hygiene execution（依既定 policy，提供 hygiene metrics 不下 source reliability judgment）
