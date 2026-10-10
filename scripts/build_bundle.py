"""把所有內容檔合成 ALL-IN-ONE.md（給不能讀網址的 AI 一次貼上用）。

用法：
    python scripts/build_bundle.py          # 重新產生
    python scripts/build_bundle.py --check  # 只檢查是否過期，過期回傳 1
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "ALL-IN-ONE.md"

ORDER = [
    "START.md",
    "interview.md",
    "templates/my-travel-kit.md",
    "templates/trip-file.md",
    "templates/trip-review.md",
    "phases/plan.md",
    "phases/before.md",
    "phases/during.md",
    "phases/after.md",
    "guide/timeline.md",
    "guide/baselines.md",
    "guide/first-trip-and-solo.md",
    "guide/collaborate.md",
    "guide/packing.md",
    "guide/weather-clothing.md",
    "guide/emergencies.md",
    "guide/tools.md",
    "guide/trip-website.md",
    "guide/conference.md",
    "examples/sample-my-travel-kit.md",
    "examples/sample-trip-review.md",
]

HEADER = """# AI 旅行工具箱 — 全部內容（ALL-IN-ONE）

> 這是 https://github.com/drpwchen/ai-travel-kit 所有檔案合成的單一檔案，給不能讀網址的 AI 使用。
> 給 AI：以下每一段以 `=== FILE: 路徑 ===` 開頭，內文提到的檔名（例：`guide/timeline.md`）就是指這裡對應的段落。
> 請從第一段 START.md 開始照著做。你已經有全部內容，START.md §6（讀不到網址時）可以略過；
> 但仍然只依當前階段使用對應段落，不要一次把所有清單丟給使用者。
> 提醒使用者：下次開新對話，要把這個檔案（或網址）＋他的總檔＋（有進行中的旅行時）這趟檔一起給 AI。
> 本檔由 `scripts/build_bundle.py` 自動產生，請勿直接修改。
"""


def build() -> str:
    parts = [HEADER]
    for rel in ORDER:
        text = (ROOT / rel).read_text(encoding="utf-8").strip()
        parts.append(f"\n\n=== FILE: {rel} ===\n\n{text}\n")
    return "".join(parts)


def main() -> int:
    tracked = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob("*.md")}
    skip = {"README.md", "AGENTS.md", "CLAUDE.md", "CHANGELOG.md", "ALL-IN-ONE.md"}
    missing = sorted(t for t in tracked - skip - set(ORDER) if not t.startswith("my/"))
    if missing:
        print("ORDER 漏了這些檔：", ", ".join(missing))
        return 1
    new = build()
    if "--check" in sys.argv:
        old = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        if old != new:
            print("ALL-IN-ONE.md 已過期，請執行 python scripts/build_bundle.py")
            return 1
        print("ALL-IN-ONE.md 是最新的")
        return 0
    OUT.write_text(new, encoding="utf-8", newline="\n")
    print(f"已寫入 {OUT.name}（{len(new):,} 字元）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
