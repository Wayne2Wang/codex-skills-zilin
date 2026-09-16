# Zilin Slide Narrator

> *Your slides. A voice that guides.*

A Codex skill that turns a PDF slide deck and optional rough notes into a naturally taught narrated walkthrough, a synchronized slide player, and an MP4 with audio-aligned captions.

[![Codex Skill](https://img.shields.io/badge/Codex-Skill-111111)](https://developers.openai.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../LICENSE)

`$zilin-slide-narrator` guides you from rough notes through script review, voice
previews, and synchronized delivery.

| It can | It will not |
| --- | --- |
| Develop instructor narration from slides and rough notes | Require a complete script to begin |
| Rehearse with a Mac voice and preview two ElevenLabs slides | Generate the remaining paid audio before sample approval |
| Align final captions to the actual recordings | Present estimated caption timing as final alignment |
| Package a slide player and narrated video | Publish to a hosting destination without authorization |

## Installation

Follow the [collection installation instructions](../../README.md#installation) and
select this skill. See [SKILL.md](SKILL.md) for the complete workflow.

## Example Usage

**User**
```text
Use $zilin-slide-narrator to turn this PDF and my rough notes into a narrated
walkthrough for beginners. Keep all slides and deliver the player and video locally.
```

For a presentation with a specific visual style:

```text
Use $zilin-slide-narrator for this training deck. Match our website's style,
review the script with me, and prepare a package for deployment.
```

The skill first confirms the source, audience, coverage, voice, visual style, and
delivery choices. It develops the script with a native Mac voice draft, then
previews two slides with ElevenLabs before generating the remaining approved
audio. Final captions follow the actual recordings. Saved progress supports
resuming work without unnecessarily regenerating paid audio.

## Inputs and Requirements

- A PDF slide deck; rough notes or key points are optional.
- macOS speech synthesis for the default Samantha draft voice. On other hosts,
  agree on a substitute before production.
- Access to ElevenLabs through available tools or its browser interface, a
  confirmed available voice, and sufficient credits for approved generation.
- PDF rendering tools, FFmpeg, Python 3 for the run checker, and a supported
  forced-alignment tool for final captions.
- Browser access for player verification; a hosting destination only when
  deployment is requested.

The skill provides workflow instructions, configurable
[defaults](assets/defaults.json), and a [run checker](scripts/check_run.py).
Production tools and services are separate dependencies. Local delivery is the
default; paid generation proceeds through explicit review gates.

## What You Receive

- A complete per-slide instructor script and native-voice draft for review.
- A two-slide ElevenLabs preview before bulk generation.
- A synchronized player with slide navigation, captions, and transcripts.
- A narrated MP4 and SRT/VTT captions aligned to the final audio.
- A clean static package and homepage when deployment is requested.

## License

MIT License. See [LICENSE](../../LICENSE) for details.

---

> "Built by Codex. ⭐"
