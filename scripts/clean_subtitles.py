"""Clean yt-dlp auto-generated SRT files that often repeat lines.

Usage:
    python3 clean_subtitles.py /path/to/file.srt
    python3 clean_subtitles.py /path/to/file.srt --output clean_transcript.txt
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


def clean_srt_text(srt_text: str) -> str:
    lines = srt_text.splitlines()
    text_lines = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if re.fullmatch(r"\d+", stripped):
            continue
        if "-->" in stripped:
            continue
        if stripped in {"♪", ">>", ">>>"}:
            continue
        text_lines.append(stripped)

    deduped = []
    i = 0
    while i < len(text_lines):
        if i + 2 < len(text_lines) and text_lines[i] == text_lines[i + 1] == text_lines[i + 2]:
            deduped.append(text_lines[i])
            i += 3
            continue
        deduped.append(text_lines[i])
        i += 1

    clean_text = " ".join(deduped)
    clean_text = re.sub(r"\s+", " ", clean_text).strip()
    return clean_text


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_path")
    parser.add_argument("--output")
    args = parser.parse_args()

    srt_text = Path(args.input_path).read_text(encoding="utf-8")
    clean_text = clean_srt_text(srt_text)

    if args.output:
        Path(args.output).write_text(clean_text, encoding="utf-8")
        print(f"Saved {len(clean_text)} chars to {args.output}")
    else:
        print(clean_text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
