#!/usr/bin/env python3
"""Mirror approved extracted running-right cells into running-left cells."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image, ImageOps


FRAME_COUNT = 8
CELL_SIZE = (192, 208)


def frame_paths(folder: Path) -> list[Path]:
    return [folder / f"{index:02d}.png" for index in range(FRAME_COUNT)]


def validate_source(paths: list[Path]) -> None:
    missing = [str(path) for path in paths if not path.is_file()]
    if missing:
        raise SystemExit("missing approved running-right frame(s): " + ", ".join(missing))
    for path in paths:
        with Image.open(path) as image:
            if image.size != CELL_SIZE:
                raise SystemExit(f"{path} is {image.size}; expected {CELL_SIZE}")
            if image.convert("RGBA").getbbox() is None:
                raise SystemExit(f"approved source frame is empty: {path}")


def update_manifest(run_dir: Path, note: str, completed_at: str) -> None:
    manifest_path = run_dir / "imagegen-jobs.json"
    if not manifest_path.is_file():
        return
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    for job in manifest.get("jobs", []):
        if job.get("id") == "running-left":
            job.update(
                {
                    "status": "complete",
                    "source_path": "derived:frames/running-right",
                    "derived_from": "running-right",
                    "completed_at": completed_at,
                    "mirror_decision": {
                        "approved": True,
                        "approved_at": completed_at,
                        "note": note,
                        "transform": "clean-cell-horizontal-mirror-preserving-order",
                    },
                }
            )
            break
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def require_approved_right_job(run_dir: Path) -> None:
    manifest_path = run_dir / "imagegen-jobs.json"
    if not manifest_path.is_file():
        raise SystemExit(f"job manifest not found: {manifest_path}")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    for job in manifest.get("jobs", []):
        if job.get("id") == "running-right":
            if job.get("status") != "complete":
                raise SystemExit("running-right must be complete and approved before mirroring")
            return
    raise SystemExit("running-right job not found in imagegen-jobs.json")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", required=True)
    parser.add_argument(
        "--confirm-appropriate-mirror",
        action="store_true",
        help="Required after checking that markings and accessories remain valid when flipped.",
    )
    parser.add_argument("--decision-note", required=True)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if not args.confirm_appropriate_mirror:
        raise SystemExit("refusing to mirror without --confirm-appropriate-mirror")
    note = args.decision_note.strip()
    if not note:
        raise SystemExit("--decision-note must explain why mirroring preserves identity")

    run_dir = Path(args.run_dir).expanduser().resolve()
    require_approved_right_job(run_dir)
    source_dir = run_dir / "frames" / "running-right"
    target_dir = run_dir / "frames" / "running-left"
    sources = frame_paths(source_dir)
    targets = frame_paths(target_dir)
    validate_source(sources)
    existing = [path for path in targets if path.exists()]
    if existing and not args.force and not args.dry_run:
        raise SystemExit(
            f"running-left frames already exist under {target_dir}; pass --force to replace all eight"
        )

    if not args.dry_run:
        target_dir.mkdir(parents=True, exist_ok=True)
        for source, target in zip(sources, targets):
            with Image.open(source) as image:
                ImageOps.mirror(image.convert("RGBA")).save(target, format="PNG")

    completed_at = datetime.now(timezone.utc).isoformat()
    if not args.dry_run:
        update_manifest(run_dir, note, completed_at)
    report = {
        "ok": True,
        "run_dir": str(run_dir),
        "source_state": "running-right",
        "target_state": "running-left",
        "frame_count": FRAME_COUNT,
        "transform": "clean-cell-horizontal-mirror-preserving-order",
        "decision_note": note,
        "outputs": [str(path) for path in targets],
        "dry_run": args.dry_run,
        "applied_at": completed_at,
    }
    if not args.dry_run:
        qa_dir = run_dir / "qa"
        qa_dir.mkdir(parents=True, exist_ok=True)
        (qa_dir / "cat-hatcher-running-left-derivation.json").write_text(
            json.dumps(report, indent=2) + "\n",
            encoding="utf-8",
        )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
