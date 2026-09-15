#!/usr/bin/env python3
"""Create a shuffled, unlabeled normal-size cardinal preflight sheet."""

from __future__ import annotations

import argparse
import hashlib
import json
import random
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


DIRECTIONS = ("000", "090", "180", "270")
EXPECTED = {"000": "up", "090": "screen-right", "180": "down", "270": "screen-left"}
CELL_SIZE = (192, 208)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", required=True)
    args = parser.parse_args()

    run_dir = Path(args.run_dir).expanduser().resolve()
    anchors_dir = run_dir / "decoded" / "look-anchors"
    paths = {degree: anchors_dir / f"{degree}.png" for degree in DIRECTIONS}
    missing = [str(path) for path in paths.values() if not path.is_file()]
    if missing:
        raise SystemExit("missing cardinal anchor(s): " + ", ".join(missing))

    digest = hashlib.sha256()
    for degree in DIRECTIONS:
        digest.update(paths[degree].read_bytes())
    seed = int.from_bytes(digest.digest()[:8], "big")
    shuffled = list(DIRECTIONS)
    random.Random(seed).shuffle(shuffled)

    margin = 20
    label_height = 30
    gap = 20
    panel_width = CELL_SIZE[0] + margin * 2
    panel_height = CELL_SIZE[1] + label_height + margin * 2
    sheet = Image.new(
        "RGB",
        (panel_width * 2 + gap, panel_height * 2 + gap),
        (232, 232, 232),
    )
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.load_default(size=18)
    answer_key = []
    for index, degree in enumerate(shuffled):
        label = chr(ord("A") + index)
        column = index % 2
        row = index // 2
        x = column * (panel_width + gap)
        y = row * (panel_height + gap)
        draw.rectangle(
            (x, y, x + panel_width - 1, y + panel_height - 1),
            fill=(250, 250, 250),
            outline=(120, 120, 120),
            width=1,
        )
        draw.text((x + margin, y + 7), label, fill=(20, 20, 20), font=font)
        with Image.open(paths[degree]) as image:
            rgba = image.convert("RGBA")
            if rgba.size != CELL_SIZE:
                raise SystemExit(f"{paths[degree]} is {rgba.size}; expected {CELL_SIZE}")
            sheet.paste(rgba, (x + margin, y + margin + label_height), rgba)
        answer_key.append(
            {
                "label": label,
                "degree": degree,
                "expected": EXPECTED[degree],
            }
        )

    qa_dir = run_dir / "qa"
    qa_dir.mkdir(parents=True, exist_ok=True)
    sheet_path = qa_dir / "cat-hatcher-cardinal-blind-sheet.png"
    key_path = qa_dir / "cat-hatcher-cardinal-blind-answer-key.json"
    sheet.save(sheet_path, format="PNG", optimize=True)
    key = {
        "ok": True,
        "sheet": str(sheet_path),
        "answer_key": answer_key,
        "instructions": "Show only the sheet to a fresh reviewer. Classify A-D as up, down, screen-left, screen-right, or ambiguous at displayed size.",
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    key_path.write_text(json.dumps(key, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(key, indent=2))


if __name__ == "__main__":
    main()
