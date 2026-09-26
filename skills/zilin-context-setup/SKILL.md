---
name: zilin-context-setup
description: Set up and maintain a concise PROJECT_CONTEXT.md plus an AGENTS.md instruction to read and maintain it, preserving current project direction and a selective dated history of important developments. Use when starting a project with durable context, recording project decisions, or continuing work in a project that uses this context file. Do not create project documentation for unrelated one-off questions.
---

# Project Context

Maintain a useful project memory without turning it into a transcript. The project concept can change frequently; keep both an accurate current understanding and the history needed to explain important changes.

## Set up or resume

- Read applicable project instructions and any existing context file before editing. Prefer the existing filename and location, including `context.md` or `project_context.md`; do not create competing copies. Otherwise use `PROJECT_CONTEXT.md` at the project root.
- Create or update the project-root `AGENTS.md` with a short instruction to read the context file at the start of each chat before project work and follow its maintenance guidance. Use the actual context filename. Preserve existing instructions and avoid duplicate entries; do not replace an existing `AGENTS.md` wholesale. Check for an applicable `AGENTS.override.md`; if it would shadow this instruction, add the same concise pointer there without disturbing other guidance. Do not alter global configuration.
- Suggested instruction: "At the start of each chat in this project, read `PROJECT_CONTEXT.md` before doing project work. Follow its maintenance guidance: record only important developments, preserve meaningful changes in the dated log, and ask the user before logging anything whose significance is unclear."
- Build initial context from the user's statements and relevant project evidence. Do not invent goals, constraints, decisions, or results. If the project root is unclear, resolve it before writing.
- Capture enough to support future work: purpose and motivation, current direction and scope, important constraints or decisions, and consequential open questions. Adapt headings to the project and omit empty sections.
- Label the initial direction provisional unless it is settled. Distinguish user decisions, tentative proposals, hypotheses, and verified findings. Attribute consequential evidence with a compact source or artifact reference when available.
- Include a last-updated date, the maintenance convention below, and a dated evolution log when there are meaningful developments to record.

## Maintenance convention

Include this convention concisely in the project file so future work can follow it:

> Keep the current context accurate as the project evolves. Update it proactively for important decisions, findings, constraints, or changes in direction. Preserve meaningful changes in a dated evolution log, including their reasons when known. Omit routine exchanges and minor details. If uncertain whether something is important enough to record, ask the user before logging it. Distinguish tentative ideas from confirmed decisions and preserve superseded decisions in the history.

When continuing project work, consult the context before making assumptions and update it when the work produces a clearly important development. No separate confirmation is needed for clearly important updates within the user's authorized project work.

## Decide what belongs

Log a development when it materially changes future project choices or interpretation: a goal or scope change, an adopted or abandoned approach, a consequential constraint, a substantive finding, or a resolved question with lasting implications.

Do not log routine progress, individual tool calls, minor edits, repeated information, passing brainstorming, or every preference clarification. A useful filter is whether a future collaborator would make a materially different decision without this information.

If significance is genuinely uncertain, ask a short, specific question before recording the candidate item. Continue independent work while awaiting the answer; silence is not agreement. Do not ask about items that clearly meet or fail the importance threshold.

## Update without losing history

- Revise the current sections to reflect the latest supported understanding. An exploratory idea does not replace an agreed direction until adopted.
- Add a concise dated log entry for a meaningful change, stating what changed and why if known. Mark the status when relevant, such as tentative, decided, observed, or superseded.
- Preserve earlier important entries. Explicitly mark superseded decisions rather than silently rewriting history. Correct factual errors transparently.
- Combine overlapping entries from the same development and avoid repeating the full current-context narrative in the log. Do not append an entry merely to record that this file was edited or its maintenance wording changed.
- Refresh the last-updated date when content changes. Do not touch the file when there is nothing meaningful to update.
- Keep the document concise. If its history becomes unwieldy, propose an archive instead of silently deleting important history or proliferating files.

After setup, link both the context file and the project instructions file. After meaningful updates, briefly state what changed and link the affected file. Explain that `AGENTS.md` supplies the instruction for future project chats to read the context; the context file is not itself automatically injected, and the skill is not a background process. Do not modify global instructions, unrelated project files, or create automations merely to make it run everywhere.
