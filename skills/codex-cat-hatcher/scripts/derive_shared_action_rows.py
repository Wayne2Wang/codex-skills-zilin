#!/usr/bin/env python3
"""Derive shared-action frame rows from a generated canonical row."""

from __future__ import annotations

import argparse
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def frame_files(state_dir: Path) -> list[Path]:
    return sorted(path for path in state_dir.glob("*.png") if path.stem.isdigit())


def resample_indices(source_count: int, target_count: int) -> list[int]:
    if source_count <= 0:
        raise ValueError("source row has no frames")
    if target_count <= 0:
        raise ValueError("target row needs no frames")
    if target_count == 1:
        return [0]
    if source_count == 1:
        return [0 for _index in range(target_count)]
    return [
        round(index * (source_count - 1) / (target_count - 1))
        for index in range(target_count)
    ]


def state_rows(template: dict) -> dict[str, dict]:
    return {row["state"]: row for row in template.get("rows", [])}


def selected_groups(template: dict, group_id: str | None) -> list[dict]:
    groups = template.get("sharedActionGroups", [])
    if group_id is None:
        return groups
    matches = [group for group in groups if group.get("id") == group_id]
    if not matches:
        raise SystemExit(f"shared action group not found: {group_id}")
    return matches


def derive_group(
    frames_root: Path,
    template_rows: dict[str, dict],
    group: dict,
    dry_run: bool,
) -> dict:
    canonical_state = group["canonicalState"]
    derive_targets = group.get("deriveTargets") or [
        state for state in group.get("states", []) if state != canonical_state
    ]
    source_files = frame_files(frames_root / canonical_state)
    if not source_files:
        raise SystemExit(f"canonical frames not found: {frames_root / canonical_state}")

    derived_targets = []
    for target_state in derive_targets:
        if target_state not in template_rows:
            raise SystemExit(f"target state not found in template: {target_state}")
        target_count = int(template_rows[target_state]["usedColumns"])
        indices = resample_indices(len(source_files), target_count)
        target_dir = frames_root / target_state
        outputs = [target_dir / f"{index:02d}.png" for index in range(target_count)]
        if not dry_run:
            target_dir.mkdir(parents=True, exist_ok=True)
            for existing_file in frame_files(target_dir):
                existing_file.unlink()
            for output, source_index in zip(outputs, indices):
                shutil.copy2(source_files[source_index], output)
        derived_targets.append(
            {
                "target_state": target_state,
                "target_count": target_count,
                "source_indices": indices,
                "outputs": [str(output) for output in outputs],
            }
        )

    return {
        "group_id": group.get("id"),
        "canonical_state": canonical_state,
        "canonical_count": len(source_files),
        "derived_targets": derived_targets,
    }


def update_manifest(run_dir: Path, results: list[dict], dry_run: bool) -> None:
    manifest_path = run_dir / "imagegen-jobs.json"
    if dry_run or not manifest_path.exists():
        return
    manifest = load_json(manifest_path)
    completed_at = datetime.now(timezone.utc).isoformat()
    for result in results:
        canonical_state = result["canonical_state"]
        for target in result["derived_targets"]:
            target_state = target["target_state"]
            for job in manifest.get("jobs", []):
                if job.get("id") == target_state:
                    job.update(
                        {
                            "status": "complete",
                            "source_path": f"derived:{canonical_state}",
                            "completed_at": completed_at,
                        }
                    )
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", required=True, help="Prepared hatch-pet run directory.")
    parser.add_argument(
        "--template",
        required=True,
        help="Codex Cat Hatcher action template JSON.",
    )
    parser.add_argument(
        "--frames-root",
        help="Extracted frames root. Defaults to <run-dir>/frames.",
    )
    parser.add_argument("--group-id", help="Only derive one shared action group.")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    run_dir = Path(args.run_dir).expanduser().resolve()
    frames_root = (
        Path(args.frames_root).expanduser().resolve()
        if args.frames_root
        else run_dir / "frames"
    )
    template = load_json(Path(args.template).expanduser().resolve())
    template_rows = state_rows(template)

    results = [
        derive_group(frames_root, template_rows, group, args.dry_run)
        for group in selected_groups(template, args.group_id)
    ]
    update_manifest(run_dir, results, args.dry_run)

    report = {
        "ok": True,
        "run_dir": str(run_dir),
        "frames_root": str(frames_root),
        "dry_run": args.dry_run,
        "results": results,
        "applied_at": datetime.now(timezone.utc).isoformat(),
    }
    if not args.dry_run:
        qa_dir = run_dir / "qa"
        qa_dir.mkdir(parents=True, exist_ok=True)
        (qa_dir / "cat-hatcher-shared-actions.json").write_text(
            json.dumps(report, indent=2) + "\n",
            encoding="utf-8",
        )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
