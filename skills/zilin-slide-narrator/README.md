# Zilin Slide Narrator

A Codex skill that turns a PDF slide deck and optional rough notes into a naturally taught narrated walkthrough, a synchronized slide player, and an MP4 with audio-aligned captions.

## Installation

Follow the [collection installation instructions](../../README.md#installation), selecting `zilin-slide-narrator`:

```bash
bash ~/codex-skills-zilin/scripts/install-skills.sh zilin-slide-narrator
```

See [SKILL.md](SKILL.md) for the complete workflow.

## Example usage

```text
Use $zilin-slide-narrator to turn this PDF and my rough notes into a narrated
walkthrough for beginners. Keep all slides and deliver the player and video locally.
```

```text
Use $zilin-slide-narrator for this training deck. Match our website's style,
review the script with me, and prepare a package for deployment.
```

The skill first confirms the source, audience, coverage, voice, visual style, and
delivery choices. It develops the script with a native Mac voice draft, then
previews two slides with ElevenLabs before generating the remaining approved
audio. Final captions follow the actual recordings. Saved progress supports
resuming work without unnecessarily regenerating paid audio.

## Requirements

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

## License

MIT License. See [LICENSE](../../LICENSE) for details.
