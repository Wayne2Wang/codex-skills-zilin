# Realistic Cat Row Recipe

Use this as the starting animation plan. User edits override these defaults.

| Row | State | Default cat action |
| --- | --- | --- |
| 0 | idle | Sleeping in a compact curled or loaf-like pose, one paw covering both eyes, subtle breathing or tiny paw/head movement. |
| 1 | running-right | Directional walk/run to screen-right with a clean alternating cadence and no detached effects. |
| 2 | running-left | Directional walk/run to screen-left, derived by mirroring clean extracted right-facing frames when safe. |
| 3 | waving | Small cute paw wave; no wave marks or effects. |
| 4 | jumping | Small cute paw wave. |
| 5 | failed | Sad or crying facial expression with a gradual slump and smooth return; tears stay attached and apparent body/head scale stays stable. |
| 6 | waiting | Cute attention-getting pose such as showing belly or staring at the user. |
| 7 | running | Active working state, usually sitting and licking fur or another contained focused action, not literal sprinting. |
| 8 | review | Focused/cute review state. |
| 9-10 | look directions | Maintain realistic cat identity and seated scale through 16 directions with strong up/down pitch and monotonic viewer-coordinate yaw. |

Loop rules:

- Keep motion visible but small.
- Keep the final frame compatible with the first frame.
- Keep each frame inside its 192x208 cell.
- Use whole-body readable silhouettes; avoid cropped ears, paws, tails, or face.
- Reject detached secondary blobs larger than tiny antialiasing specks.
- Keep duplicate-action relationships in template-level `sharedActionGroups`; row action text should stay concrete and standalone.
- Use a seated neutral standard frame for look registration; a sleeping idle frame makes the look family visibly underscaled.
- Treat `000` up and `180` down as hard normal-size semantics, and keep row 10's intermediate landmarks screen-left until the 000 boundary.
