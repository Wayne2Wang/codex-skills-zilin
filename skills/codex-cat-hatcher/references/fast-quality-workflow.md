# Fast Quality Workflow

This workflow preserves the full `$hatch-pet` v2 contract while moving inexpensive checks ahead of dependent generation. It is optimized for realistic photo-derived cats and the default action template.

## Stage 1: Lock The Plan

1. Prepare the `$hatch-pet` run.
2. Apply the cat action template and any user overrides.
3. Confirm `qa/cat-hatcher-template-application.json` is valid before image generation.

The template preloads the failures most likely to cause retries: idle contact shadows, failed-state redraw scaling, incoherent gait phases, weak up/down cardinals, and row-10 screen-left drift.

## Stage 2: Probe Before Fan-Out

Generate the base, then `idle` and `running-right` first.

- Idle is the forbidden-effect probe. Reject any gray/black/brown/translucent patch beneath or around the body.
- Running-right is the extraction and cadence probe. Inspect its source strip and its GIF immediately. If the source has stable equal slots but component extraction creates size popping, re-extract with `stable-slots` before doing dependent work.
- Generate the remaining independent standard rows while those probes are checked.

Do not generate `running-left` independently when clean mirroring is identity-safe. Mirror approved 192x208 right-facing cells with `derive_clean_running_left.py`; never mirror a decoded strip that may contain cross-slot fragments.

Generate one canonical row for each active `sharedActionGroups` entry and derive its target rows with `derive_shared_action_rows.py`.

## Stage 3: Standard Motion Gate

Before any look-direction generation, review all standard-row contact sheets and GIFs for:

- correct confirmed action and realistic identity
- no contact shadows or detached effects
- stable apparent body/head scale and baseline
- coherent cadence with no standing/loaf reset inside directional gait
- smooth loop closure
- clean complete silhouettes and no cross-slot fragments

Fix failures now. Do not perform final despill yet.

## Stage 4: Look Preflight

Run `prepare_look_inputs.py` after the standard contact sheet exists.

It performs two deterministic tasks:

- selects a seated normal-scale registration frame, preferring review, waiting, then active working, and copies it to `references/look-neutral.png`
- compacts canonical identity plus the standard contact sheet when a look job would exceed the built-in image generator's five-reference limit, without dropping the layout guide, approved cardinals, or completed row 9

Review `qa/cat-hatcher-look-preflight.json`. Do not start look generation if any job exceeds five references or the selected neutral is a sleeping/curled pose.

## Stage 5: Cardinal Gate Before Rows

Generate and extract the four approved anchors. The cat-specific prompt lock requires:

- `000`: unmistakable up pitch at 192x208, nose above center, chin/lower muzzle exposed, original irises high, eyelids lifted
- `090`: nose and visible pupils on screen-right of head center
- `180`: unmistakable down bow at 192x208, nose below center, more crown visible, original irises low
- `270`: nose and visible pupils on screen-left of head center

Create `qa/cat-hatcher-cardinal-blind-sheet.png` with `make_cardinal_blind_sheet.py`. Give only that sheet to a fresh reviewer and require correct A-D classifications with no ambiguity. The parent compares the verdict with the hidden answer key. Repair a failed anchor before row 9.

## Stage 6: One Look Row At A Time

Generate row 9, register it with `references/look-neutral.png`, and run edge, semantic, scale, baseline, and continuity QA immediately.

Only then generate row 10. Enforce its monotonic screen-left landmark schedule: slight at 202.5, moderate at 225, strong at 247.5, maximum at 270, then strong/moderate/slight through 337.5. A row that flips to screen-right or loses the down axis at 180 is a failed family; do not select it.

## Stage 7: Finish Once

After both look rows pass:

1. Assemble the extended atlas using `references/look-neutral.png`.
2. Run direction semantics, continuity, and normal-size blind review.
3. Repair any semantic or visual failure before chroma cleanup.
4. Run final despill once.
5. Run v2 atlas validation, contact-sheet QA, and the mandatory three isolated blind direction reviews.
6. Package only when every gate passes.

Keep debug artifacts by default. Cleanup is optional and requires explicit user authorization because it removes generation evidence.
