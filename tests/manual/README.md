# 手動測試 Corpus (Manual Test Corpus)

這裡放的是**情境式 spec 行為測試 prompt**，不是自動化測試。

`scripts/validate_authority_chain.py` 驗的是 **schema / 結構一致性**（檔名 ↔ `agent_id`、升級鏈雙向、authority mapping 子集規則）。本資料夾驗的是另一件事：**agent 在特定情境下交付的內容是否符合角色 spec**——這沒有自動 harness，靠把 prompt 餵給依本 repo 角色定義設定的 LLM，再人工比對輸出。

每個檔是一個可直接複製貼上的情境 prompt，對應一條 backlog `TUN-*` 條目，用來在 spec ship / drop 前做 **dry-run**，確認某個變更是否真的改變了 agent 行為（或確認現行 spec 是否已足夠、不需動）。

## 慣例

- 檔名 = backlog ID 小寫、去 `TUN-` 前綴：`ti-004.md` ↔ `TUN-TI-004`
- 每個 prompt 開頭明確要求「**完全依本 repo 的 `<role file>` 角色行事**」，確保測的是 repo spec、而非模型自由發揮
- 預期輸出 = 該角色 spec 定義的交付物範本結構（例如 Actor Profile Context Sheet）

## 現有案例

| 檔案 | Backlog | 測什麼 | 該測導向的決策 |
|---|---|---|---|
| [`ti-004.md`](ti-004.md) | `TUN-TI-004` | TI Analyst 面對 4 個互相衝突的外部歸因來源，是否依 Actor Profile Context Sheet 範本穩定交付、不臨場硬湊成單一指向 | **shipped (v1.3)**：兩次 run 結構不一致 → 暴露真 gap → 範本補 `Source Triangulation Notes` 固定子段 |
| [`for-003.md`](for-003.md) | `TUN-FOR-003` | Forensics Analyst 面對部分證據（3 台主機只保住 2 台）時，向 IRC 回覆證據充分性是否 in-lane、適度 bounded、不過度承諾、不自行拍板 | **dropped (v1.3 planning)**：現行 spec 已逼出 bounded 回應；固化「n=1/2/3 信心度框架」反而有假精確風險 → 不動 |

> `for-003.md` 對應的條目最後是 **dropped**——保留它是因為這份 dry-run 正是 drop 決策的依據：測試顯示現行 spec 已足夠，補規則反而有害。corpus 記錄的是「為什麼這樣決定」，不只是「通過的案例」。

## 怎麼跑

1. 開一個乾淨對話（Claude Code / Cursor / 任何 LLM），把對應角色檔（如 `threat-intel/threat-intel-analyst.md`）載入為 system / role prompt
2. 把 `tests/manual/<id>.md` 的內容當 user prompt 貼入
3. 對照該角色 spec 的交付物範本，人工檢查輸出：結構對不對、有沒有越權、邊界守不守得住

無 pass / fail 自動判定——這是 spec 行為的人工 dry-run，不是 CI gate。新增案例時沿用上述慣例，並在「現有案例」表補一列。
