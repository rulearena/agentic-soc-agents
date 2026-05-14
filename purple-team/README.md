# Purple Team — 紫隊

## 分類定位

紅藍融合的演練角色。職責是驗證 SOC 既有偵測與回應能力，把假想敵的 TTP 變成可量化的覆蓋率與時效。

**典型工作**：
- Adversary emulation（Atomic Red Team、CALDERA、MITRE Engenuity）
- Detection coverage 驗證：每個 rule 對應的 technique 真的會被觸發嗎？
- TTP-based exercises（基於 APT 集團的真實手法重現）
- 演練後 debrief：哪些偵測有用、哪些缺、哪些是噪音
- Detection roadmap 輸入：把演練結果回饋給 Detection Engineering

**不在這分類**：
- 真實事件回應 → 屬 [`incident-response/`](../incident-response/)
- 寫新 detection rule → 屬 [`detection-engineering/`](../detection-engineering/)（演練後合作改進）
- 純紅隊滲透測試（破壞為目的）→ 不屬本 repo 範圍

**為什麼不收純紅隊**：RuleArena 定位是藍隊（防守）視角；紅隊技術細節不在本 repo 範圍，避免內容方向衝突。

## 角色清單

⏳ 規劃中

- ⏳ `purple-team-adversary-emulator` — Atomic Red Team / CALDERA 對應、TTP-based exercise 設計
- ⏳ `purple-team-detection-validator` — 偵測規則驗證、coverage 測試、演練後 debrief
