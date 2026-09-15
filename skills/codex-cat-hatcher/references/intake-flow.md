# Codex Cat Hatcher Intake Flow

Use this before generating a new pet. The goal is to collect the pet name first, confirm the user-facing action plan second, then collect the cat photo, then generate assets.

## Step 1: Ask For Pet Name

If the user has not already supplied a pet name, ask only:

```text
What would you like to name your pet?
```

After the user provides the name, continue to Step 2.

If the user already supplied a pet name, acknowledge it briefly and continue to Step 2.

## Step 2: Present Default Actions

Send one compact message with the default actions and ask whether to keep them or change specific actions. Do not mention row numbers to the user.

Use this wording:

```text
Pet name: <pet name>

Before I generate the pet, please confirm the action plan.

Defaults:
- Idle: sleeping compactly, one paw covering both eyes, subtle breathing.
- Greeting: small cute paw wave.
- Jumping (on hover): small cute paw wave.
- Failed/error: sad or crying face, no detached tears.
- Waiting for user input: showing belly or staring expectantly.
- Active working: sitting and licking fur.
- Reviewing: small focused cute pose.
- Moving right: small realistic run/trot to the right.
- Moving left: mirror the clean right-moving frames when safe.
- Looking around: realistic 16-direction look loop.

You can reply with either:
1. "Keep defaults"
2. Action changes, e.g. "Waiting should stare at me, reviewing should tilt head"
3. Constraints, e.g. "No toys", "more sleepy", "less movement"

After that, please send the cat photo.
```

If the user already provided a cat photo, replace the final line with:

```text
I already have the photo, so after you confirm the actions I’ll start generating the pet.
```

## Step 3: Apply User Changes

Parse the response as action overrides:

- Keep unchanged rows from `assets/templates/default-action-template.json`.
- Map user-facing action names to the corresponding internal template row.
- Apply explicit action changes to the corresponding row while preserving that row's default constraints unless they conflict with the new action.
- Apply global constraints such as "no toys" or "less movement" to every row unless the user limits them.
- Use row-level `addConstraints` for extra per-row constraints. Use row-level `removeConstraints` only for exact default constraints that conflict with the user's requested action. Use row-level `constraints` as a full replacement only when preserving defaults would be wrong.
- Build the generation plan from the confirmed text actions and the user's cat photo only.
- Use `sharedActionGroups` metadata for duplicate default actions. Do not encode duplicate-action relationships as prompt text.
- When a shared action group is active, generate only the canonical state and derive target rows deterministically after frame extraction.
- Do not use bundled example GIFs, previous pets, or other pet atlases as generation inputs.
- Preserve the realistic photo-derived style unless the user explicitly changes style.

If the user's response is ambiguous, ask one targeted follow-up. Do not ask about every action again.

## Step 4: Confirm Final Plan

Before asking for the photo or generating, summarize only changed actions plus global constraints.

If there are no changes, say:

```text
Using the default Codex Cat Hatcher action template. Please attach the cat photo.
```

If there are changes, say:

```text
I will keep defaults except:
- <state/action>: <new action/constraint>
- Global constraints: <constraints>

Please attach the cat photo when you’re ready.
```

If the photo is already available, end with:

```text
I have the photo and confirmed action plan, so I’ll start generation now.
```

## Step 5: Generate

After the pet name, action plan, and photo are available:

1. Read `$hatch-pet`.
2. Use the pet name for `displayName` and derive a clean lowercase hyphenated `petId`.
3. Use the photo as the identity source of truth.
4. Use the confirmed action plan as the internal row recipe.
5. Run `$hatch-pet`'s `prepare_pet_run.py`.
6. Immediately apply the confirmed action plan to the prepared row prompts with `scripts/apply_action_template.py`.
7. Verify `qa/cat-hatcher-template-application.json` reports `ok: true` before any visual generation.
8. Generate and validate the v2 pet package.

Do not regenerate actions merely because defaults were used. Defaults are valid explicit choices.
