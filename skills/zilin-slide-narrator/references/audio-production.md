# Audio production and resumability

## Native Mac draft

Use macOS `say`, default Samantha, rate 150. Discover installed voices and tools first; do not assume paths. Render each included slide separately to AIFF, then use FFmpeg to produce playable AAC/M4A. A typical command is `say -v Samantha -r 150 -f slide.txt -o slide.aiff`. Validate nonempty audio and decoded duration; speech service failures can create unusable files. Follow environment permission handling when Mac speech needs access. On a non-Mac host, explain the limitation and ask about a local substitute rather than silently using paid TTS.

Assemble native draft player and MP4 with transcripts and CC. Interim caption estimates are acceptable only if explicitly identified as draft during review, and must be replaced by actual-audio alignment in final output. Preserve native clips for fallback/debug review. Script edits invalidate only corresponding clips.

## ElevenLabs two-slide gate

Use available ElevenLabs tools/skill if genuinely callable; otherwise use the supported browser interface. Inspect current documentation/interface, voice identity, model, all parameters, output format, and credit balance. Do not infer availability from a plugin name or pretend a connector exists. If Evan is unavailable, ask for a replacement before generation.

Default: Evan — Calm, Grounded & Reflective; Multilingual v2; speed 0.92; stability 0.80; similarity 0.80; style 0; speaker boost enabled; panning 0.5; language override off; audio effects off; MP3 44.1 kHz / 128 kbps. Do not let an account upgrade change these implicitly.

Calculate characters and expected credit cost using the current product's model/voice pricing; do not assume every model always costs one credit per character. Explain total vs balance. Generate only the first two included slides (or all slides if fewer than two). Save audio, verify it corresponds to the right script, assemble a dedicated sample with automatic slide changes, and show it. Ask approval for the voice/pacing/settings before generating the remaining slides. Store the approved script and settings fingerprint.

If user adjusts settings, read them back, regenerate only the sample, and review again. A text-only revision can require only affected sample clips. Reuse approved samples in the full output, not a second paid copy.

## Bulk generation

Before each request, confirm text and settings match the approved run. History selection, account changes, or UI navigation can reset settings: inspect them again, and restore confirmed values before generating. The button may read Generate or Regenerate; ground the action in the current UI and verify what it did.

Save per-slide original audio, source script hash, actual settings, generation identifier if exposed, byte count, checksum, decoded duration, and status. Use existing generated history when a download fails. Never repeat a paid generation just because a click times out or the response is ambiguous; first inspect current/history state. Stop on a provider error or unresolved mismatch and preserve work.

Balance displays can lag. Recheck fresh state before claiming how much remains. With insufficient balance, generate whole slides that fit the approved budget, prioritizing contiguous progress. A later short slide may use the remainder if consistent with the user's approved partial-completion preference; report its exact page and skip it on resume. Never truncate a script to fit credits without permission. Never purchase a subscription or create/switch accounts on your own. Authorized account switches retain settings and scripts but require fresh checks.

## Download verification and browser fallbacks

Prefer supported downloads or connector-returned files. Verify a saved clip is complete, decodable, and corresponds to the selected narration; compare displayed player text and duration. Browser playback source can still point to the previous clip immediately after selection: wait for the selected text/source/duration to settle before saving.

In the original browser workflow, finished streams used blob URLs while reloading an existing history item exposed an audio data URL. If this is still true and supported, read only the DOM-backed media source through permitted tools. Large evaluation results can truncate: transfer bounded chunks, assert full length/no truncation marker, then decode and validate. Do not scrape private application state, call undocumented internal APIs, or bypass download restrictions. Re-observe current UI; do not hardcode old tab IDs, element indices, or history labels. Keep credentials out of files and logs.

## Revisions

Changes to captions alone never require new narration. Changes to script or settings invalidate matching audio/alignment signatures. Preserve previous good clips until replacements pass checks. “Stop generating” stops credit spending immediately; saved clips may still be assembled when authorized.
