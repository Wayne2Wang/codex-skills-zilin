---
name: codex-cat-hatcher
description: "Guide a user through a multi-step intake to create realistic Codex v2 animated pet assets from their cat photo: first ask for the pet name, then present default user-facing actions by trigger/state, ask whether to change actions or constraints, then request the cat photo, then use the hatch-pet workflow for generation, QA, and packaging. Use when a user asks to generate a Codex pet, realistic cat pet, cat-photo pet, pet spritesheet, pet.json package, or wants a template-driven pet skill with editable actions such as idle, waving, waiting, running-left, running-right, failed, active working, or review."
---

# Codex Cat Hatcher

## Overview

Create a realistic Codex-compatible v2 pet from a cat photo through a guided intake. First collect the pet name, then confirm the user-facing action plan, then collect the photo, then wrap `$hatch-pet` for image generation, atlas assembly, deterministic repair scripts, validation, and packaging.

## Workflow

1. Run the intake in `references/intake-flow.md` before generation unless the user already supplied an explicit action plan and photo.
2. Ask for the pet name first, unless already supplied.
3. Present the default actions from `assets/templates/default-action-template.json` using user-facing trigger/state names, not row numbers.
4. Ask whether the user wants to change any action or add constraints.
5. Ask for the cat photo only after the pet name and action plan are accepted or edited.
6. Read `$hatch-pet` before generating or repairing assets.
7. After `$hatch-pet` prepares the run folder, run `scripts/apply_action_template.py` against the run before any visual generation.
8. Use the user's cat photo as the identity source of truth.
9. Set style to realistic photo-derived cat, not cartoon, unless the user explicitly asks otherwise.
10. Follow the staged fast-quality path in `references/fast-quality-workflow.md`; it moves cheap failure checks before dependent generation.
11. Use `references/row-recipe.md` only when filling missing action details.
12. Use `references/qa-checklist.md` before accepting or installing the pet.
13. Package outputs as a v2 atlas with `spriteVersionNumber: 2`, an 8-column by 11-row spritesheet, and `pet.json`.

Do not start visual generation until all conditions are true:

- The action plan is confirmed.
- The pet name is known.
- A cat photo is available.

## Action Template

The default template is `assets/templates/default-action-template.json` in this skill. Each row's `action`, `motion`, and `constraints` must be concrete prompt text for that row. Cross-trigger reuse belongs only in top-level `sharedActionGroups` metadata, never in row prompt text that describes one trigger as a duplicate of another trigger.

Use `assets/templates/default-action-template.json` as the default internal row plan.

When using a template:

- Preserve row numbers and state names.
- Follow each row's `action`, `motion`, and `constraints`.
- "Keep defaults" means each generated row prompt must use the template row's exact `action`, `motion`, and `constraints`; do not place those defaults only in `pet_notes`.
- If the user asks to change an action, apply the change to the corresponding internal row plan before generating or repairing that row.
- A user action change only replaces `action` by default. Keep that row's safety/layout constraints unless the new action conflicts with them.
- Represent user constraints explicitly: `globalConstraints` appends constraints to every row; row-level `addConstraints` appends to one row; row-level `removeConstraints` removes exact default constraints; row-level `constraints` replaces the row's constraint list and should be used only when defaults are incompatible with the requested action.
- After `prepare_pet_run.py` creates prompts, resolve
  `CAT_HATCHER_SKILL_DIR` to the directory containing this `SKILL.md`, then run:

```bash
"$PYTHON" "$CAT_HATCHER_SKILL_DIR/scripts/apply_action_template.py" \
  --run-dir "$RUN_DIR" \
  --template "$CAT_HATCHER_SKILL_DIR/assets/templates/default-action-template.json"
```

- If the user changed actions, write the final internal row plan to a JSON overrides file and pass it with `--overrides`.
- If a top-level `sharedActionGroups` entry remains active, generate its `canonicalState` once, then derive each target row deterministically from approved extracted canonical frames with `scripts/derive_shared_action_rows.py`. Do not send duplicate visual generation jobs for target rows in the same active group.
- If the user overrides any state inside a shared action group, treat that group as disabled unless the override explicitly defines a new shared group.
- Do not start base or row visual generation until `qa/cat-hatcher-template-application.json` exists and reports `"ok": true`.
- The template application also installs the cat-specific cardinal prompt lock. Verify its report includes `look_direction_policy` and that the cardinal plus four repair prompts are listed under `checked_prompts`.
- Before accepting final output, compare `qa/cat-hatcher-template-application.json` and the row prompts to the confirmed action plan; a mismatch is a failed run even when the atlas validates.
- If copying one action to another row, copy approved extracted frames deterministically and adapt to the target state's required frame count. Record the copy in `qa/cat-hatcher-shared-actions.json`.
- For row 2 `running-left`, mirror clean extracted row 1 frames when safe. Do not mirror a dirty decoded strip with cross-slot overlap. Use `scripts/derive_clean_running_left.py` after the approved extraction method is final.

## Fast Quality Path

Use `$hatch-pet`'s normal v2 contract, but order the work to avoid multiplying a bad decision:

1. Generate the base first. Generate `idle` and `running-right` next as early identity, forbidden-effect, and gait probes.
2. Extract and preview each generated standard row immediately. For a visually stable equal-slot gait strip that pops only after component extraction, use `$hatch-pet`'s `stable-slots` correction before approving the frames.
3. After `running-right` frames pass, derive `running-left` from those clean 192x208 cells when mirroring preserves markings and accessories:

```bash
"$PYTHON" "$CAT_HATCHER_SKILL_DIR/scripts/derive_clean_running_left.py" \
  --run-dir "$RUN_DIR" \
  --confirm-appropriate-mirror \
  --decision-note "<why mirroring preserves this cat's identity>" \
  --force
```

4. Generate the active shared-action canonical row once and run `derive_shared_action_rows.py` for its targets.
5. Do not proceed to look directions until all standard-row GIFs pass action, identity, shadow/effect, scale, baseline, and loop checks.
6. Before the cardinal job, compact look references and select a seated neutral registration frame:

```bash
"$PYTHON" "$CAT_HATCHER_SKILL_DIR/scripts/prepare_look_inputs.py" \
  --run-dir "$RUN_DIR" \
  --max-inputs 5 \
  --neutral-state auto
```

The preflight must report `ok: true`, every look job at or below five inputs, and a non-idle `references/look-neutral.png`. Pass that neutral file to `$hatch-pet` assembly instead of a sleeping `idle/00` cell.

7. After extracting the four cardinal anchors, create the cheap blind preflight:

```bash
"$PYTHON" "$CAT_HATCHER_SKILL_DIR/scripts/make_cardinal_blind_sheet.py" \
  --run-dir "$RUN_DIR"
```

Give only `qa/cat-hatcher-cardinal-blind-sheet.png` to a fresh reviewer. Every A-D cell must be classified correctly and none may be ambiguous at displayed size. Repair a failing anchor before row 9.
8. Generate and fully approve row 9 before row 10. Apply the monotonic screen-coordinate schedules from the template; do not accept direction drift and hope final blind QA will resolve it.
9. Run semantic, continuity, and normal-size blind checks before final despill. Perform final despill once, then run the complete `$hatch-pet` validation and three-reviewer blind gate unchanged.

Never weaken a mandatory `$hatch-pet` acceptance criterion to save time. The speedup comes from derivation, reference compaction, early probes, and earlier rejection of bad dependencies.

## Intake Rules

Read `references/intake-flow.md` when the user asks to create a new pet from a cat photo. Keep the intake compact:

- Be polite and friendly when asking for user input.
- Ask for action changes in one message, not one question per animation state.
- Ask for the pet name before showing row actions.
- Offer "keep defaults" as the easiest path.
- If the user changes actions, summarize the final action plan before asking for the photo.
- If the user already attached the photo in the first message, do not ask for it again; confirm the action plan, then continue to generation.
- If the user provides only partial action changes, apply those changes and keep defaults for all other states.

## Generation Constraints

- Preserve the cat's face shape, coat color, markings, eye color, ear shape, and overall realism.
- Derive motion from the confirmed text action plan and the given cat photo only.
- Treat bundled example GIFs as human-facing demonstrations only; do not attach them to generation jobs.
- Prefer compact, cute, small actions. Avoid large pose changes unless the user explicitly asks.
- Make each loop end compatible with its start frame.
- Avoid props by default; introduce toys, UI objects, text, or symbols only when requested.
- Do not add detached effects such as motion lines, sparkles, dust, shadows, or floating tear drops.
- For directional movement, mirror clean extracted frames only after verifying no asymmetric identity issue.
- If a row has an artifact, prefer deterministic repair over regenerating a good-looking row.
- For sleeping idle, require the chroma background to touch the fur silhouette everywhere; a soft floor or contact patch is a failed source, not removable atmosphere.
- For `failed`, reject progressive redraw scaling during the slump even if each individual frame looks attractive.
- For look registration, prefer `review/00`, then `waiting/00`, then the contained active-working pose. Never register cat look rows against a sleeping or curled idle pose unless the user explicitly wants a low sleeping look family.
- Defer final chroma despill until semantic direction, motion, scale, baseline, and forbidden-effect gates pass, so repairs do not force repeated final assembly.

## Default Outputs

Place deliverables in a user-facing output folder:

- `pet.json`
- `spritesheet.webp`
- `contact-sheet-extended.png`
- optional focused debug strips such as `running-left-final-strip.png`
- optional `run-summary.json`

Use exactly these package filenames for generated pet assets:

```text
pet.json
spritesheet.webp
```

## Installing

When the user wants to use the pet in Codex, copy `pet.json` and `spritesheet.webp` to:

```text
~/.codex/pets/<pet-id>/
```

Validate the installed `spritesheet.webp` with the hatch-pet `validate_atlas.py --require-v2` script.
