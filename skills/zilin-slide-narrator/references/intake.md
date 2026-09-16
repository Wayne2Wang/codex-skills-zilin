# Guided intake

Ask in stages, using already supplied information. Keep each stage compact; offer “keep defaults” and allow specific overrides. Do not subject a returning user to the full intake again. Use asynchronous questions for text preferences when available, but ask for attachments in ordinary chat. Required answers must actually arrive before dependent work.

## 1. Identify the walkthrough and collect inputs

Ask for the presentation title, audience, authoritative deck, and any initial narration. Encourage the user with:

> Do you have a starting script, rough notes, or just a few key points? Incomplete is fine—I can turn them into a coherent teaching script and fill gaps from the slides. If you have no notes, I can start from the deck.

Also ask for target length if the user has one. Do not invent deadlines, assignment requirements, or course facts absent from the source. If multiple decks differ, show the difference and resolve which is authoritative. If reusing an existing recording could save work, ask whether they want to check course recordings first; do not derail production by doing so unasked.

## 2. Present the default plan

Use a readable table or short grouped list, not raw JSON:

- Coverage: all slides. Offer optional exclusions; for the teaching preset, include announcements/hackathon and exclude office hours and questions/Q&A. Confirm the actual page numbers once inspected. No silent skips.
- Teaching: natural instructor voice, concise but complete coverage of each slide; transitions and explanations; no added running examples.
- Development: Mac Samantha at 150 words/minute, player and video for script review first.
- Final voice: Evan — Calm, Grounded & Reflective, Eleven Multilingual v2; speed 0.92, stability 80%, similarity 80%, style 0, speaker boost on, centered panning. First two included slides are a review sample before bulk generation.
- Outputs: player + 1080p MP4 + audio-aligned CC + SRT/VTT + per-slide transcript; original slide proportions preserved, about one second between slides.
- Appearance: existing navy/gold player theme, clean student interface. Ask if they prefer matching a course website and request its URL if so.
- Budget: use available credits only; never purchase automatically. Confirm whether partial completion is acceptable if credits are insufficient.

Ask: “Keep these defaults, or which parts would you like to customize?” Accept selective changes and preserve everything else. An explicit “use defaults” counts as confirmation of this displayed plan.

## 3. Ask the deployment question explicitly

> Do you want (1) local files only, (2) a ready-to-upload website package, or (3) online deployment?

Default is local/package delivery, not automatic publication. If online, collect provider, account/repository destination, presentation/site name, public vs restricted access, and whether a root presentation collection homepage should list multiple labs. Default suggested structure is one repository per course/term, `lab01/`, `lab02/`, etc., not one repository per lab. The prior name `eecs498a2se-fall2026` is a contextual example, not a new course's assumed name. Prefer GitHub Pages for the exact public static player if the user wants that approach; for course-restricted video delivery discuss MiVideo/Canvas. Do not silently substitute a platform.

## 4. Confirm and proceed

Summarize the resolved plan once, including source identity, exclusions, review gates, budget behavior, and deployment choice. Ask only about unresolved essentials. Do not repeatedly ask permission for already approved choices.

After intake, the remaining review gates are meaningful artifacts: native-voice/script approval, then two-slide final-voice approval. Show the actual playable samples before asking approval. User may explicitly waive or change these gates; record the override rather than treating the template as stronger than the user's request.
