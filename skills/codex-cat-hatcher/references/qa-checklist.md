# Cat Pet QA Checklist

Run this before delivering or installing a pet.

## Visual QA

- The pet still reads as the user's cat, not a generic cat.
- The style remains realistic, not cartoon or sticker-like, unless requested.
- Every row's visible action matches the confirmed Codex Cat Hatcher action template, not generic `$hatch-pet` row defaults.
- The motion was generated from the confirmed text action plan and cat photo, not copied from bundled example GIFs or another pet.
- Idle defaults to the confirmed sleeping/paw-over-eyes action when the user chose "keep defaults".
- Jumping/on-hover defaults to a small paw-wave action when the user chose "keep defaults".
- Actions are cute and compact, with no overly large pose changes.
- Each animation loops smoothly enough that the end does not visibly jump back to the start.
- No row contains floating artifacts, old-frame remnants, chroma fragments, detached limbs, detached tears, or motion effects.
- Idle has no cast/contact shadow, gray floor patch, grounding ellipse, halo, reflection, or soft pixels outside the fur silhouette; chroma touches the silhouette everywhere.
- Directional gait remains one coherent alternating cycle with no standing, sitting, or loaf reset and no extraction-induced size pop.
- Failed/error keeps stable apparent body size, head size, torso width, and baseline while the expression/slump changes.
- Look rows are registered against an approved seated neutral frame, not the smaller sleeping/curled idle pose.
- `000` and `180` read unmistakably as up and down at normal 192x208 size; `090` and `270` visibly oppose in viewer/screen coordinates.
- Row 10 stays on the screen-left side from 202.5 through 337.5 and follows a monotonic left-yaw trajectory around 270.

## Deterministic QA

- Atlas is 1536x2288, 8 columns by 11 rows.
- Cell size is 192x208.
- `pet.json` uses `spriteVersionNumber: 2`.
- `qa/cat-hatcher-template-application.json` exists and reports `ok: true`.
- Prepared row prompts' `State action` and `State requirements` reflect `assets/templates/default-action-template.json` plus any user overrides.
- User action overrides preserve default constraints unless the override explicitly records added, removed, or replacement constraints.
- Duplicate default actions are represented by `sharedActionGroups` metadata, not row prompt text.
- Active shared action groups either have `qa/cat-hatcher-shared-actions.json` or a documented reason they were generated separately.
- Safe mirrored left gait has `qa/cat-hatcher-running-left-derivation.json` and was derived from approved extracted 192x208 right-gait frames.
- `qa/cat-hatcher-look-preflight.json` exists, reports every look job at five or fewer input images, and identifies the approved seated `references/look-neutral.png`.
- `qa/cat-hatcher-cardinal-blind-answer-key.json` exists and a fresh reviewer correctly classified every displayed anchor without ambiguity before row 9 generation.
- Unused cells are transparent.
- Look rows contain all 16 directions.
- `validate_atlas.py --require-v2` passes with no errors.

## Known Repair Patterns

If `running-left` shows fragments:

1. Inspect row 2 frames, especially frames 5 and 6.
2. Check whether fragments exist in the decoded strip, extracted frames, or only final atlas.
3. If right-running is clean, mirror the clean extracted `running-right` 192x208 frames into `running-left`.
4. When replacing row 2 in the extended atlas, paste/overwrite the whole RGBA row, including transparent pixels. Do not alpha-composite over the old row.
5. Re-run atlas validation and make a focused `running-left` strip for review.

If standard motion pops after extraction:

1. Confirm the generated source strip itself keeps stable equal-slot scale and placement.
2. Re-extract only that row with `$hatch-pet`'s `stable-slots` method.
3. Re-run frame inspection and its GIF preview before deriving or assembling dependent rows.
4. Regenerate only when the source strip itself changes scale, clips, or overlaps; do not regenerate an otherwise good row for an extraction artifact.

If a look family fails a cardinal or flips horizontal direction:

1. Reject the complete dependent row; do not package a single repaired cell beside a different family.
2. Repair ambiguous cardinal anchors before either look row.
3. For `000`, strengthen whole-head up pitch, nose-above-center, exposed chin, high original irises, and lifted eyelids.
4. For row 10, use the template's explicit slight/moderate/strong/maximum screen-left landmark schedule.
5. Repeat normal-size blind review after regeneration; labeled review alone is insufficient.
