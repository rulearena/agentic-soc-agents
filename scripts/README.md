# scripts/

本目錄存放 repo 維護腳本。

## validate_authority_chain.py

驗證 agent frontmatter 與跨角色 authority mapping 一致性，守住 repo 容易壞的四件事：**檔名、agent_id、升級鏈、authority mapping**。

### 依賴

需要 Python 3 + PyYAML（不在 stdlib）：

```bash
python3 -m pip install pyyaml
```

若未安裝，腳本會印出明確訊息並以 exit code 1 結束，不會丟 `ModuleNotFoundError` traceback。

### 執行

從 repo root：

```bash
python3 scripts/validate_authority_chain.py
```

### 退出碼

- `0` —— 所有 FAIL 檢查通過（WARN 不影響退出碼）
- `1` —— 至少一條 FAIL，或缺 PyYAML 等環境問題

### 檢查項

| 代碼 | 檢查 | 等級 |
|---|---|---|
| C1  | Frontmatter 可解析（含 `---` 邊界與合法 YAML） | FAIL |
| C2  | 必填欄位齊全：`name` / `agent_id` / `seniority` / `escalates_to` / `escalates_from`（值可 null，key 必須存在） | FAIL |
| C2b | Frontmatter 結構型別正確：`response_authority` 是 dict、`requires_*_approval` / `can_approve` 是 list、`delegates_to` 是 dict（且 value 必須是 string agent_id） | FAIL |
| C3  | `agent_id` == 檔名 stem | FAIL |
| C4  | `agent_id` 全 repo 唯一 | FAIL |
| C5  | `escalates_to` 非 null 時對應 agent 存在 | FAIL |
| C6  | `escalates_from` 非 null 時對應 agent 存在 | FAIL |
| C7  | 反向一致性：`A.escalates_to=B` ⇒ `B.escalates_from==A` | FAIL |
| C8  | Authority mapping：`requires_*_approval` ⊆ `escalates_to` 對應 agent 的 `can_approve` | FAIL |
| C9  | `delegates_to` 指向尚未存在的 agent（forward ref） | **WARN** |

### Authority mapping 規則細節

`requires_*_approval` 是 regex pattern（不只 `requires_ir_approval`），未來新增 `requires_manager_approval` 等命名自動納入檢查。

C8 的邊界情況：
- 某 agent 有 `requires_*_approval` 但 `escalates_to: null` → FAIL（無升級對象）
- 某 agent 有 `requires_*_approval` 但 `escalates_to` 不存在 → C5 已 FAIL，C8 skip 不重複
- 升級對象沒有 `response_authority.can_approve` → FAIL（missing 全部 required items）

### 未來擴充（不在 v1）

- CI / GitHub Actions / pre-commit hook 整合
- pytest 單元測試
- 完整 schema validator（如 `tool_stack` key 列舉、`primary_tactics` 是 ATT&CK tactic ID）
- 若 `escalates_from` 改成 list（多入口升級鏈），C7 需擴為多值檢查
