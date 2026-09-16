---
name: zilin-slide-narrator
description: "Turn any PDF slide deck and optional rough notes into a naturally taught narrated walkthrough through guided intake, Mac-voice script development, a two-slide ElevenLabs review, audio-aligned captions, and a synchronized player and video. Use for presentations, training, lectures, workshops, and other slide walkthroughs, with optional deployment."
---

# Zilin Slide Narrator

Produce an audience-facing slide player and narrated MP4. Start with a compact interactive intake modeled on the cat-hatcher workflow: show defaults, accept “keep defaults,” apply partial overrides, and carry accepted choices forward. This skill can run independently of that skill.

## Workflow and review gates

1. **Intake before production.** Read [intake](references/intake.md) and load [defaults](assets/defaults.json). Collect source, audience, rough script, coverage, voice, review, visual, output, and deployment choices. Encourage incomplete notes or key points; a complete initial script is not required. Read-only source inspection may proceed while waiting. Do not draft a full walkthrough or synthesize audio until the plan and source are settled.
2. **Inspect every slide.** Read [teaching](references/teaching.md). Establish the authoritative deck, render it, and map every original slide to included/excluded status. Do not reuse another deck's page count or narration. Attached slides take precedence over a different web version unless the user says otherwise.
3. **Write and rehearse.** Produce a complete per-slide instructor script. Generate a synchronized player and video using macOS Samantha at 150 words/minute. Revise cheaply until the user approves the script and native-voice draft. Native voice is a development aid, not a claim about final quality.
4. **Two-slide paid-voice gate.** Read [audio production](references/audio-production.md). Check voice availability and account balance; generate only the first two included slides with the confirmed ElevenLabs parameters. Download, assemble, and show their player/video preview. Wait for approval before bulk generation. Do not infer approval from silence. A request to change parameters and preview again resets this gate.
5. **Finish approved audio.** Generate the remaining approved scripts within the authorized credit budget. Save and verify each clip before moving on. Reuse completed matching clips. A credit shortage means assemble current work, disclose unfinished slides, and wait for a balance/account change; do not buy plans. User-authorized account changes require a fresh balance/settings check.
6. **Align captions to the audio.** Read [alignment and assembly](references/alignment-assembly.md). Use forced alignment on the final playable recordings, not text-length timing. Rebuild player CC, SRT/VTT, and MP4 subtitles from the same aligned word data. Verify every included slide and the complete output.
7. **Deliver or deploy.** Read [delivery](references/delivery.md). Always provide the player and video. Ask whether deployment is needed during intake; local/package-only is the default. When requested, build a course-level homepage and a clean static package, then publish only to the chosen destination/access under existing authorization.

## Defaults and customization

The JSON template is the source of defaults; user choices override it. For any PDF deck, include all slides by default and confirm exclusions explicitly. The optional teaching preset preserves the originating workflow: include announcements/hackathon if present and exclude office hours and questions/Q&A. Do not apply course-specific exclusions to an unrelated presentation.

Use all non-excluded slides, teach all substantive slide contents, avoid added running examples, and use concise but complete instructor speech. Explain relationships and transitions rather than reading bullets. Original code/examples already on a slide still need explanation.

No changes to voice, model, speed, narration, or deck should silently reuse stale approval or timestamps. Record approvals against the exact script/source/settings, and invalidate only the affected downstream work. Source audio remains untouched; import and align derived playback audio.

## Persistent run record

Keep `run.json` beside production files with source checksum/page count, resolved defaults/overrides, per-slide inclusion rationale, script and audio checksums, actual durations, voice/model/settings, generation state, observed credit balance/time, approvals, alignment signatures, and deployment status. Do not store account credentials. Distinguish `generated`, `downloaded`, `verified`, and `assembled`; a generation request alone is not completion.

For resumed tasks, inspect this record and existing artifacts before asking questions or generating. Honor “stop generating” immediately; assemble saved clips if asked. Do not regenerate approved audio merely to recover a download or fix CC.

## Audience-facing quality

Player defaults: dark navy/gold, automatic slide progression, seek, speed, slide selector, keyboard controls, fullscreen, CC, per-slide transcript, and video/caption/slide downloads. Keep voice parameters, debug labels, credit balances, editable-script links, cache tokens, internal paths, and raw errors out of the audience interface. Never claim the style matches a course website without inspecting it. Offer intentional style matching during intake.

## References and helpers

- [Intake](references/intake.md): staged prompts and confirmation boundaries.
- [Teaching](references/teaching.md): source mapping, script quality, review.
- [Audio production](references/audio-production.md): Mac drafts, ElevenLabs gates, credits, downloads.
- [Alignment and assembly](references/alignment-assembly.md): actual-audio timing, validation, synchronized outputs.
- [Delivery](references/delivery.md): package, homepage, deployment, handoff.
- `scripts/check_run.py RUN.json`: lightweight preflight for stage/approval consistency; does not authorize external actions or replace artifact verification. Read its error output and resolve mismatches before paid generation.
