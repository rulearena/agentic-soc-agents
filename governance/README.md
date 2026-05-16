# Governance — 治理

## 分類定位

把 SOC 運營從個人英雄主義變成可持續、可審計、可成長的組織能力。職責是讓 SOC 的工作對外可解釋、對內可改進。

**典型工作**：
- SOC 運營管理：人力配置、班表設計、SLA 設計與追蹤
- 團隊培訓：新人 onboarding、L1 → L2 → IR 的成長路徑
- 合規對應：SOC 2、ISO 27001、NIST CSF、PCI-DSS、HIPAA
- 內外稽核窗口：evidence 蒐集、auditor 溝通、findings remediation
- KPI / metrics 設計與報告（給 CISO、給 CFO、給董事會）

**不在這分類**：
- 第一線告警處理 → 屬 [`triage/`](../triage/)
- 技術細節（rules、IOC、forensics）→ 屬其他技術分類

## 角色清單

✅ 已完成、⏳ 規劃中

- ✅ [`governance-soc-manager`](governance-soc-manager.md) — Process / SLA / staffing / training / policy ownership；post-incident review facilitator（lessons-learned 非 blame-oriented）；不參與 live incident command
- ⏳ `governance-compliance-auditor` — 合規 framework 對應（SOC 2、ISO 27001、NIST CSF）
- ✅ [`governance-audit-liaison`](governance-audit-liaison.md) — 事實翻譯層、regulator-facing evidence package、control mapping、audit trail、compliance gap report
