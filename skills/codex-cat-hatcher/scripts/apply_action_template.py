#!/usr/bin/env python3
"""Apply the Codex Cat Hatcher action template to a hatch-pet run."""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path


STATE_PROMPT_NAMES = {
    "idle": "idle",
    "running-right": "running-right",
    "running-left": "running-left",
    "waving": "waving",
    "jumping": "jumping",
    "failed": "failed",
    "waiting": "waiting",
    "running": "running",
    "review": "review",
    "look-directions-a": "look-row-9",
    "look-directions-b": "look-row-10",
}


STATE_LABELS = {
    "idle": "Idle",
    "running-right": "Moving right",
    "running-left": "Moving left",
    "waving": "Greeting",
    "jumping": "Jumping (on hover)",
    "failed": "Failed/error",
    "waiting": "Waiting for user input",
    "running": "Active working",
    "review": "Reviewing",
    "look-directions-a": "Looking around, first half",
    "look-directions-b": "Looking around, second half",
}


def validate_shared_action_groups(template: dict, rows: dict[str, dict]) -> list[dict]:
    groups = []
    for group in template.get("sharedActionGroups", []):
        states = group.get("states", [])
        canonical_state = group.get("canonicalState")
        missing_states = [state for state in states if state not in rows]
        if canonical_state not in rows:
            missing_states.append(canonical_state)
        if missing_states:
            raise SystemExit(
                f"shared action group {group.get('id', '<unknown>')} references unknown states: "
                + ", ".join(sorted(set(missing_states)))
            )
        groups.append(dict(group))
    return groups


def apply_row_override(row: dict, override: dict) -> None:
    for key, value in override.items():
        if key in {
            "row",
            "state",
            "addConstraints",
            "removeConstraints",
            "append_constraints",
            "remove_constraints",
        }:
            continue
        row[key] = value

    constraints = list(row.get("constraints", []))
    for item in override.get("addConstraints", []) + override.get("append_constraints", []):
        if item not in constraints:
            constraints.append(item)
    for item in override.get("removeConstraints", []) + override.get("remove_constraints", []):
        constraints = [constraint for constraint in constraints if constraint != item]
    row["constraints"] = constraints


def apply_global_constraints(rows: dict[str, dict], overrides: dict) -> list[str]:
    global_constraints = (
        overrides.get("globalConstraints")
        or overrides.get("global_constraints")
        or []
    )
    for row in rows.values():
        constraints = list(row.get("constraints", []))
        for item in global_constraints:
            if item not in constraints:
                constraints.append(item)
        row["constraints"] = constraints
    return list(global_constraints)


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def replace_section(text: str, title: str, body: str) -> str:
    pattern = re.compile(
        rf"(?ms)^{re.escape(title)}:.*?(?=^State requirements:|^Clean extraction:|^One centered complete pose|\Z)"
    )
    replacement = f"{title}: {body.rstrip()}\n\n"
    if not pattern.search(text):
        raise ValueError(f"missing section: {title}")
    return pattern.sub(replacement, text, count=1)


def replace_requirements(text: str, requirements: list[str]) -> str:
    lines = "\n".join(f"- {item}" for item in requirements)
    replacement = f"State requirements:\n{lines}\n\n"
    pattern = re.compile(r"(?ms)^State requirements:\n.*?(?=^Clean extraction:|^One centered complete pose|\Z)")
    if not pattern.search(text):
        raise ValueError("missing section: State requirements")
    return pattern.sub(replacement, text, count=1)


def row_requirements(row: dict) -> list[str]:
    requirements = [
        f"Template state: {row['state']} ({STATE_LABELS.get(row['state'], row['state'])}).",
        f"Required action: {row['action']}",
        f"Required motion: {row['motion']}",
    ]
    requirements.extend(row.get("constraints", []))
    return requirements


def upsert_lock(text: str, marker: str, requirements: list[str]) -> str:
    start = f"{marker} START"
    end = f"{marker} END"
    lines = "\n".join(f"- {item}" for item in requirements)
    block = f"{start}\n{lines}\n{end}\n\n"
    pattern = re.compile(
        rf"(?ms)^{re.escape(start)}\n.*?^{re.escape(end)}\n\n?"
    )
    if pattern.search(text):
        return pattern.sub(block, text, count=1)
    first_break = text.find("\n\n")
    if first_break < 0:
        return text.rstrip() + "\n\n" + block
    insert_at = first_break + 2
    return text[:insert_at] + block + text[insert_at:]


def patch_cardinal_prompts(
    run_dir: Path,
    look_policy: dict,
    dry_run: bool,
) -> tuple[list[str], list[str]]:
    cardinal_constraints = look_policy.get("cardinalConstraints", {})
    shared_constraints = look_policy.get("sharedConstraints", [])
    if not cardinal_constraints:
        return [], []

    targets: list[tuple[Path, list[str]]] = [
        (
            run_dir / "prompts" / "look-cardinals.md",
            [
                f"{degree}: {constraint}"
                for degree, constraint in cardinal_constraints.items()
            ]
            + list(shared_constraints),
        )
    ]
    for degree, constraint in cardinal_constraints.items():
        targets.append(
            (
                run_dir / "prompts" / "look-anchor-repairs" / f"{degree}.md",
                [f"{degree}: {constraint}"] + list(shared_constraints),
            )
        )

    checked: list[str] = []
    patched: list[str] = []
    for path, requirements in targets:
        if not path.exists():
            raise SystemExit(f"look-direction prompt not found: {path}")
        checked.append(str(path))
        original = path.read_text(encoding="utf-8")
        updated = upsert_lock(original, "CAT HATCHER CARDINAL LOCK", requirements)
        if updated != original:
            patched.append(str(path))
            if not dry_run:
                path.write_text(updated, encoding="utf-8")
    return checked, patched


def patch_prompt(prompt_path: Path, row: dict, dry_run: bool) -> bool:
    original = prompt_path.read_text(encoding="utf-8")
    marker = "CAT HATCHER TEMPLATE LOCK"
    if "State action:" in original or "Action:" in original:
        action_title = "State action" if "State action:" in original else "Action"
        patched = replace_section(original, action_title, row["action"])
        patched = replace_requirements(patched, row_requirements(row))
    elif prompt_path.stem in {"look-row-9", "look-row-10"}:
        template_lock = (
            f"{marker}: {row['action']} Motion: {row['motion']} "
            f"Constraints: {'; '.join(row.get('constraints', []))}.\n\n"
        )
        if marker in original:
            patched = re.sub(rf"(?ms)^{marker}:.*?\n\n", template_lock, original, count=1)
        else:
            patched = original.replace("\n\n", "\n\n" + template_lock, 1)
    else:
        raise ValueError("missing section: State action or Action")
    if patched == original:
        return False
    if not dry_run:
        prompt_path.write_text(patched, encoding="utf-8")
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", required=True, help="Prepared hatch-pet run directory.")
    parser.add_argument(
        "--template",
        required=True,
        help="Codex Cat Hatcher action template JSON, usually assets/templates/default-action-template.json.",
    )
    parser.add_argument(
        "--overrides",
        help="Optional JSON file with row overrides using rows[].state/action/motion/constraints.",
    )
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    run_dir = Path(args.run_dir).expanduser().resolve()
    template_path = Path(args.template).expanduser().resolve()
    template = load_json(template_path)
    rows = {row["state"]: dict(row) for row in template["rows"]}
    overridden_states: set[str] = set()
    global_constraints: list[str] = []

    if args.overrides:
        overrides = load_json(Path(args.overrides).expanduser().resolve())
        global_constraints = apply_global_constraints(rows, overrides)
        for override in overrides.get("rows", []):
            state = override["state"]
            if state not in rows:
                raise SystemExit(f"override references unknown state: {state}")
            apply_row_override(rows[state], override)
            overridden_states.add(state)

    shared_action_groups = validate_shared_action_groups(template, rows)
    active_shared_action_groups = []
    disabled_shared_action_groups = []
    for group in shared_action_groups:
        states = set(group.get("states", []))
        touched_states = sorted(states & overridden_states)
        if touched_states:
            disabled = dict(group)
            disabled["disabledReason"] = (
                "User override touched grouped state(s): " + ", ".join(touched_states)
            )
            disabled_shared_action_groups.append(disabled)
        else:
            active_shared_action_groups.append(group)

    patched_paths: list[str] = []
    checked_paths: list[str] = []
    for state, row in rows.items():
        prompt_name = STATE_PROMPT_NAMES.get(state)
        if not prompt_name:
            raise SystemExit(f"no prompt mapping for state: {state}")
        prompt_path = run_dir / "prompts" / "rows" / f"{prompt_name}.md"
        retry_path = run_dir / "prompts" / "row-retries" / f"{prompt_name}.md"
        for path in [prompt_path, retry_path]:
            if not path.exists():
                raise SystemExit(f"prompt not found: {path}")
            checked_paths.append(str(path))
            try:
                changed = patch_prompt(path, row, args.dry_run)
            except ValueError as error:
                raise SystemExit(f"{path}: {error}") from error
            if changed:
                patched_paths.append(str(path))

    cardinal_checked, cardinal_patched = patch_cardinal_prompts(
        run_dir,
        template.get("lookDirectionPolicy", {}),
        args.dry_run,
    )
    checked_paths.extend(cardinal_checked)
    patched_paths.extend(cardinal_patched)

    manifest = {
        "ok": True,
        "template": str(template_path),
        "run_dir": str(run_dir),
        "checked_prompts": checked_paths,
        "patched_prompts": patched_paths,
        "global_constraints": global_constraints,
        "shared_action_groups": active_shared_action_groups,
        "disabled_shared_action_groups": disabled_shared_action_groups,
        "look_direction_policy": template.get("lookDirectionPolicy", {}),
        "dry_run": args.dry_run,
        "applied_at": datetime.now(timezone.utc).isoformat(),
    }
    if not args.dry_run:
        qa_dir = run_dir / "qa"
        qa_dir.mkdir(parents=True, exist_ok=True)
        (qa_dir / "cat-hatcher-template-application.json").write_text(
            json.dumps(manifest, indent=2) + "\n",
            encoding="utf-8",
        )
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
