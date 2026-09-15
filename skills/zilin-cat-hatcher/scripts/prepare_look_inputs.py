#!/usr/bin/env python3
"""Prepare compact, scale-safe look-direction inputs for a cat-hatcher run."""

from __future__ import annotations

import argparse
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image, ImageOps


LOOK_JOB_IDS = ("look-cardinals", "look-row-9", "look-row-10")
NEUTRAL_PRIORITY = ("review", "waiting", "running", "jumping", "waving", "failed")
CANONICAL_PATH = "references/canonical-base.png"
CONTACT_PATH = "qa/contact-sheet.png"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def find_job(manifest: dict, job_id: str) -> dict:
    for job in manifest.get("jobs", []):
        if job.get("id") == job_id:
            return job
    raise SystemExit(f"job not found in imagegen-jobs.json: {job_id}")


def require_run_file(run_dir: Path, relative_path: str) -> Path:
    path = run_dir / relative_path
    if not path.is_file():
        raise SystemExit(f"required look input not found: {path}")
    return path


def choose_neutral(run_dir: Path, requested_state: str) -> tuple[str, Path]:
    states = NEUTRAL_PRIORITY if requested_state == "auto" else (requested_state,)
    for state in states:
        candidate = run_dir / "frames" / state / "00.png"
        if candidate.is_file():
            with Image.open(candidate) as image:
                if image.convert("RGBA").getbbox() is not None:
                    return state, candidate
    searched = ", ".join(states)
    raise SystemExit(
        f"no non-empty seated neutral frame found under frames/ for: {searched}. "
        "Pass --neutral-state with an approved seated state."
    )


def make_reference_board(sources: list[Path], output: Path) -> dict:
    if len(sources) < 2:
        raise ValueError("a reference board needs at least two images")

    opened: list[Image.Image] = []
    try:
        for source in sources:
            image = Image.open(source).convert("RGB")
            opened.append(ImageOps.contain(image, (1400, 1400), Image.Resampling.LANCZOS))

        columns = 2 if len(opened) > 2 else len(opened)
        rows = (len(opened) + columns - 1) // columns
        gap = 24
        column_widths = [0] * columns
        row_heights = [0] * rows
        for index, image in enumerate(opened):
            column = index % columns
            row = index // columns
            column_widths[column] = max(column_widths[column], image.width)
            row_heights[row] = max(row_heights[row], image.height)

        width = sum(column_widths) + gap * (columns + 1)
        height = sum(row_heights) + gap * (rows + 1)
        board = Image.new("RGB", (width, height), (245, 245, 245))
        y = gap
        for row in range(rows):
            x = gap
            for column in range(columns):
                index = row * columns + column
                if index >= len(opened):
                    break
                image = opened[index]
                left = x + (column_widths[column] - image.width) // 2
                top = y + (row_heights[row] - image.height) // 2
                board.paste(image, (left, top))
                x += column_widths[column] + gap
            y += row_heights[row] + gap

        if board.width > 4096 or board.height > 4096:
            board = ImageOps.contain(board, (4096, 4096), Image.Resampling.LANCZOS)
        output.parent.mkdir(parents=True, exist_ok=True)
        board.save(output, format="PNG", optimize=True)
        return {
            "output": str(output),
            "sources": [str(path) for path in sources],
            "width": board.width,
            "height": board.height,
        }
    finally:
        for image in opened:
            image.close()


def replace_inputs_with_board(
    inputs: list[dict],
    paths_to_replace: set[str],
    board_path: str,
    role: str,
) -> list[dict]:
    selected = [index for index, item in enumerate(inputs) if item.get("path") in paths_to_replace]
    if len(selected) < 2:
        return inputs
    insert_at = min(selected)
    kept = [item for index, item in enumerate(inputs) if index not in selected]
    kept.insert(insert_at, {"path": board_path, "role": role})
    return kept


def compact_job_inputs(
    run_dir: Path,
    job: dict,
    max_inputs: int,
    dry_run: bool,
) -> tuple[dict, list[dict]]:
    original = list(job.get("input_images", []))
    compacted = list(original)
    boards: list[dict] = []
    job_id = str(job.get("id"))

    if len(compacted) > max_inputs:
        pair = {CANONICAL_PATH, CONTACT_PATH}
        if pair.issubset({str(item.get("path")) for item in compacted}):
            board_rel = "references/identity-standard-combined.png"
            if not dry_run:
                board = make_reference_board(
                    [require_run_file(run_dir, CANONICAL_PATH), require_run_file(run_dir, CONTACT_PATH)],
                    run_dir / board_rel,
                )
                boards.append(board)
            compacted = replace_inputs_with_board(
                compacted,
                pair,
                board_rel,
                "lossless combined canonical-base and approved standard-row contact-sheet reference for identity, scale, and baseline",
            )

    if len(compacted) > max_inputs:
        identity_items = [
            item
            for item in compacted
            if item.get("role") == "pet reference"
            or "identity-standard-combined" in str(item.get("path"))
        ]
        if len(identity_items) >= 2:
            identity_paths = list(dict.fromkeys(str(item["path"]) for item in identity_items))
            board_rel = f"references/{job_id}-identity-sources-combined.png"
            if not dry_run:
                board = make_reference_board(
                    [require_run_file(run_dir, path) for path in identity_paths],
                    run_dir / board_rel,
                )
                boards.append(board)
            compacted = replace_inputs_with_board(
                compacted,
                set(identity_paths),
                board_rel,
                "combined user-photo and approved identity references; use for identity, markings, scale, and baseline",
            )

    if len(compacted) > max_inputs:
        raise SystemExit(
            f"{job_id} still has {len(compacted)} input images after safe compaction; "
            f"maximum is {max_inputs}. Review the manifest instead of dropping a semantic anchor."
        )

    if not dry_run:
        job["input_images"] = compacted
    result = {
        "job_id": job_id,
        "before_count": len(original),
        "after_count": len(compacted),
        "changed": original != compacted,
        "input_images": compacted,
    }
    return result, boards


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", required=True)
    parser.add_argument("--max-inputs", type=int, default=5)
    parser.add_argument(
        "--neutral-state",
        default="auto",
        help="Approved seated state for look registration; auto prefers review, waiting, then running.",
    )
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if args.max_inputs < 4:
        raise SystemExit("--max-inputs must be at least 4 to preserve layout, identity, cardinal, and continuity inputs")

    run_dir = Path(args.run_dir).expanduser().resolve()
    manifest_path = run_dir / "imagegen-jobs.json"
    manifest = load_json(manifest_path)
    neutral_state, neutral_source = choose_neutral(run_dir, args.neutral_state)
    neutral_output = run_dir / "references" / "look-neutral.png"
    if not args.dry_run:
        neutral_output.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(neutral_source, neutral_output)

    jobs: list[dict] = []
    boards: list[dict] = []
    for job_id in LOOK_JOB_IDS:
        result, created_boards = compact_job_inputs(
            run_dir,
            find_job(manifest, job_id),
            args.max_inputs,
            args.dry_run,
        )
        jobs.append(result)
        boards.extend(created_boards)

    report = {
        "ok": True,
        "run_dir": str(run_dir),
        "max_inputs": args.max_inputs,
        "neutral_state": neutral_state,
        "neutral_source": str(neutral_source),
        "neutral_output": str(neutral_output),
        "jobs": jobs,
        "reference_boards": boards,
        "dry_run": args.dry_run,
        "prepared_at": datetime.now(timezone.utc).isoformat(),
    }
    if not args.dry_run:
        temporary_manifest = manifest_path.with_suffix(".json.tmp")
        temporary_manifest.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
        temporary_manifest.replace(manifest_path)
        qa_dir = run_dir / "qa"
        qa_dir.mkdir(parents=True, exist_ok=True)
        (qa_dir / "cat-hatcher-look-preflight.json").write_text(
            json.dumps(report, indent=2) + "\n",
            encoding="utf-8",
        )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
