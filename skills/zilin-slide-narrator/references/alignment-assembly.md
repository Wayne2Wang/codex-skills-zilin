# Synchronization, captions, and final assembly

## Shared timeline

Keep a manifest containing included slides in order, original page, title, narration, image, audio, measured speech duration, playback duration, and cumulative start. Decode and measure the actual files the player uses. Do not derive final timing from word count or native-voice durations after replacing audio.

Preserve the slide aspect ratio inside a 1920×1080 frame, pad instead of cropping, normalize square pixels (SAR 1), use H.264 with AAC, and fast-start MP4. The original workflow used 2 fps for static slides; preserve it unless motion demands more. Add about one second of silence after each slide, rounding playback duration up to a half-second for the static-video pipeline. Use the same padded audio/duration for player and MP4. Watch for encoder delay and cumulative concat offsets; validate timeline boundaries, not just total duration.

## Required final caption alignment

Final CC must follow actual speech. Estimated allocation by characters, syllables, or sentence weights is not a final solution. Align the approved transcript to each final playable audio file using a supported forced-aligner (e.g. stable-ts/Whisper); use current documentation and isolated dependencies. Local alignment avoids additional TTS credits. If alignment is unavailable, disclose the blocker and do not present estimated captions as fixed.

The working approach used stable-ts with faster-whisper small.en on CPU/int8, `model.align(audio, text, language='en', regroup=False)`. Treat this as a starting configuration, not an immutable API. Cache word-level results keyed by playable audio checksum + exact normalized transcript + model/config. Transcript-only or audio changes invalidate the cache. Align the M4A the player uses, or account explicitly for differences from original MP3.

Map aligned word spans back to the approved narration, preserving punctuation and all words. Group into readable one/two-line cues, about 46 characters per line, at sentence/clause boundaries. Cue start is the first aligned word; cue end is the last aligned word with a small readable hold (about 80 ms), capped at the next cue start and slide boundary. Preserve true pauses; never stretch an entire sentence over silence. Use local timestamps for player captions, add manifest slide starts for global SRT/VTT/MP4 subtitles.

Validate: all narration words covered exactly once, no missing/duplicated text, nonnegative monotonic timestamps, positive cue durations, no overlap or slide overflow, no suspicious long/zero-word regions. Review flagged boundaries and spot-check beginning/middle/end, short and long slides, technical terms, and slide transitions against the audio. Automatic alignment is improved timing, not a promise of perfect manual verification.

Player caption lookup must use `audio.currentTime` so seek and playback-speed changes remain synchronized. Refresh captions during playback with animation frames (or equivalent accurate media events), not only a coarse `timeupdate` callback. Avoid spawning multiple concurrent animation loops. Clear captions during silence and at the end. Cache-bust changed caption data by asset fingerprint; keep the public page URL clean. Refresh the browser and verify it loaded the new asset, not a cached prior caption file.

## Outputs and checks

Generate player caption data, SRT, VTT, and an MP4 with a selectable English subtitle track from the same alignment. Retain a subtitle-free MP4 only if useful. Per-slide transcripts and full script remain available as deliverables; internal editable-script links stay out of the student UI.

Verify image/audio references, every included/excluded page, audio decoding, final-video decoding, duration, subtitle stream, caption text, and synchronized transitions. Smoke-test play/pause, seek, previous/next, speed, CC, transcript, and fullscreen where supported. Frame-level perfection is not established by a successful decode alone.

Keep the native debug version, original final-voice clips, and alignment caches in production storage. Publish only the clean deliverables. When the user reports drift, diagnose cue timing, browser caching, refresh cadence, encoding offsets, or stale audio; do not regenerate speech as a first response.
