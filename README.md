# Codex Cat Hatcher

> A Codex skill that turns your cat into a realistic, animated Codex pet.

[![Codex Skill](https://img.shields.io/badge/Codex-Skill-111111)](https://developers.openai.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

`$codex-cat-hatcher` guides users through the animation plan and delegates generation, QA, and packaging to `$hatch-pet`.


For example, here is what I got for my tabby cat `pipi`.

<p align="center">
  <img src="assets/examples/default-cat/pipi.jpg" width="260" alt="Pipi, the tabby cat featured in the example animations">
</p>

| Idle | Greeting | Jumping (on hover) | Failed | Waiting |
| --- | --- | --- | --- | --- |
| <img src="assets/examples/default-cat/gifs/idle.gif" width="130" alt="Idle animation"> | <img src="assets/examples/default-cat/gifs/waving.gif" width="130" alt="Greeting animation"> | <img src="assets/examples/default-cat/gifs/jumping.gif" width="130" alt="Jumping animation"> | <img src="assets/examples/default-cat/gifs/failed.gif" width="130" alt="Failed animation"> | <img src="assets/examples/default-cat/gifs/waiting.gif" width="130" alt="Waiting animation"> |

| Active Working | Reviewing | Moving Right | Moving Left | Looking Around |
| --- | --- | --- | --- | --- |
| <img src="assets/examples/default-cat/gifs/active-working.gif" width="130" alt="Active working animation"> | <img src="assets/examples/default-cat/gifs/review.gif" width="130" alt="Reviewing animation"> | <img src="assets/examples/default-cat/gifs/running-right.gif" width="130" alt="Moving right animation"> | <img src="assets/examples/default-cat/gifs/running-left.gif" width="130" alt="Moving left animation"> | <img src="assets/examples/default-cat/gifs/look-directions.gif" width="130" alt="Looking around animation"> |

## Install

Clone this repo directly into your Codex skills folder:

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/Wayne2Wang/codex-cat-hatcher.git ~/.codex/skills/codex-cat-hatcher
```

Restart Codex if the skill does not appear immediately.

## Example Usage

**User**
```text
Use $codex-cat-hatcher to create a realistic Codex pet for my cat.
```

**Codex**
```text
Before I generate the pet, please confirm the action plan.
```

| Trigger | Default motion |
| --- | --- |
| Idle | Sleeping compactly, one paw covering both eyes. |
| Greeting | Small cute paw wave. |
| Jumping (on hover) | Small cute paw wave. |
| Failed/error | Sad or crying face. |
| Waiting for user input | Showing belly or staring expectantly. |
| Active working | Sitting and licking fur. |
| Reviewing | Focused cute pose. |
| Moving right | Small realistic run/trot to the right. |
| Moving left | Mirror clean right-moving frames when safe. |
| Looking around | Realistic 16-direction look loop. |

**User**

You can reply with either:


```text
Keep defaults.
```

```text
Action changes, e.g. "Waiting should stare at me, reviewing should tilt head"
```

Action changes keep the default safety/layout constraints for that trigger unless the new action conflicts with them. Extra constraints are appended; incompatible defaults must be explicitly removed or replaced in the override plan.

```text
Constraints, e.g. "No toys", "more sleepy", "less movement"
```

## License

MIT License. See [LICENSE](LICENSE) for details.

---

> "Built by Codex. ⭐"
