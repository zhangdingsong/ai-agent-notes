#!/usr/bin/env python3
"""Sync notes/*.md to iCloud Obsidian vault after each git commit."""

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
NOTES_DIR = REPO_ROOT / "notes"
OBSIDIAN_DIR = (
    Path.home()
    / "Library/Mobile Documents/iCloud~md~obsidian/Documents/VaultDS/AI基础知识"
)
BASE_URL = "https://zhangdingsong.github.io/ai-agent-notes"

DEMO_HEIGHTS = {
    "llm-inference.html": 720,
    "react-loop.html": 460,
    "agent-tools.html": 340,
}

DEMO_LINK_RE = re.compile(
    r"https://zhangdingsong\.github\.io/ai-agent-notes/demos/([a-zA-Z0-9._-]+\.html)"
)


def transform_for_obsidian(text: str) -> str:
    # 1. Convert relative ../assets/<file> paths to GitHub Pages URLs
    text = text.replace("](../assets/", f"]({BASE_URL}/assets/")

    # 2. Inject <iframe> below any line containing a demo link (if not already present)
    lines = text.splitlines()
    out_lines = []
    seen_demos = set()

    for idx, line in enumerate(lines):
        out_lines.append(line)
        matches = DEMO_LINK_RE.findall(line)
        if not matches:
            continue

        lookahead = "\n".join(lines[idx + 1 : idx + 4])
        for demo_file in matches:
            if demo_file in seen_demos:
                continue
            seen_demos.add(demo_file)
            if f"/demos/{demo_file}" in lookahead and "<iframe" in lookahead:
                continue
            height = DEMO_HEIGHTS.get(demo_file, 460)
            out_lines.append("")
            out_lines.append(
                f'<iframe src="{BASE_URL}/demos/{demo_file}" '
                f'width="100%" height="{height}" '
                f'style="border:none;border-radius:12px;"></iframe>'
            )

    result = "\n".join(out_lines)
    if text.endswith("\n"):
        result += "\n"
    return result


def main() -> None:
    if not NOTES_DIR.is_dir() or not OBSIDIAN_DIR.is_dir():
        return

    updated = 0
    for md_file in sorted(NOTES_DIR.glob("*.md")):
        raw = md_file.read_text(encoding="utf-8")
        converted = transform_for_obsidian(raw)
        target = OBSIDIAN_DIR / md_file.name

        if target.exists() and target.read_text(encoding="utf-8") == converted:
            continue

        target.write_text(converted, encoding="utf-8")
        updated += 1

    if updated > 0:
        print(f"[post-commit] Synced {updated} note(s) to Obsidian: {OBSIDIAN_DIR}")


if __name__ == "__main__":
    main()
