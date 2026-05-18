# Purple Team — 紫隊

## 分類定位

紅藍融合的演練角色。職責是驗證 SOC 既有偵測與回應能力，把假想敵的 TTP 變成可量化的覆蓋率與時效。

**典型工作**：
- Scope-controlled emulation engagement（scope + approval + comm plan + abort criteria）
- Lab / staging / signal-only validation；不在實際運行環境執行可能造成損害的操作
- TTP / ATT&CK technique ID 作為測試標記，不描述執行細節
- Coverage validation signal 與 Detection Engineering handoff
- Engagement charter / execution log / closure report 全程可稽核

**不在這分類**：
- 真實事件回應 → 屬 [`incident-response/`](../incident-response/)
- 寫新 detection rule → 屬 [`detection-engineering/`](../detection-engineering/)（演練後合作改進）
- 純紅隊滲透測試（破壞為目的）→ 不屬本 repo 範圍

**為什麼不收純紅隊**：RuleArena 定位是藍隊（防守）視角；紅隊技術細節不在本 repo 範圍，避免內容方向衝突。

## 角色清單

✅ 已完成、⏳ 規劃中

- ✅ [`purple-team-adversary-emulator`](purple-team-adversary-emulator.md) — Scope-controlled emulation engagement；collaborative purple（非 red team）；Coverage validation signal handoff to Detection Engineering
- ✅ [`purple-team-detection-validator`](purple-team-detection-validator.md) — Detection validation result interpretation、coverage 評估、result credibility review
