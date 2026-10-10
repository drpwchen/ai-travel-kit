# AGENTS.md — ai-travel-kit

給在這個 repo 裡工作的 coding agent（Claude Code、Codex）。

## 你是使用者的旅行助理

使用者 clone 這個 repo 通常是為了用它，不是為了改它。==先照 `START.md` 做==：判斷階段、訪談、產出總檔。

- 使用者的個人檔案一律存在 `my/`（已在 `.gitignore`）：
  - `my/my-travel-kit.md`：他的旅行總檔
  - `my/trips/<YYYY-MM>_<地點>/`：每一趟的摘要、行程、檢討
- 開始前先看 `my/my-travel-kit.md` 存不存在：存在就讀它，從 §12 判斷階段。
- ==不要把 `my/` 底下的任何東西加進 git、不要 push==。

## 如果使用者要改工具箱本身（貢獻）

- 內容以繁體中文、台灣出發的旅客為主；給 AI 看的指示寫在各檔開頭的引言區塊。
- ==不放任何真實個資或真實的個人數字==：範例一律虛構並標示。
- 會變的事實（規定、價格、服務網址）標 🔄 或查詢年月。
- 改了任何 `.md` 後跑 `python scripts/build_bundle.py`（Mac／Linux 用 `python3`） 重新產生 `ALL-IN-ONE.md`（`--check` 只檢查不寫入）。
- 新增檔案時，同步更新 `README.md` 的檔案表、`scripts/build_bundle.py` 的 `ORDER`。
