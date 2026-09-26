# Zilin Context Setup

> *Keep the direction. Remember what changed.*

A Codex skill that sets up and maintains concise project context, preserving
the current direction and a selective dated history of important developments.

[![Codex Skill](https://img.shields.io/badge/Codex-Skill-111111)](https://developers.openai.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../LICENSE)

`$zilin-context-setup` reads existing project guidance, creates or updates a context
file, and adds an instruction in `AGENTS.md` for future project chats to read and
maintain it. It reuses an existing context filename where present and otherwise
uses `PROJECT_CONTEXT.md`.

| It can | It will not |
| --- | --- |
| Record purpose, current direction, constraints, and consequential open questions | Invent project goals or treat tentative proposals as decisions |
| Preserve meaningful changes and their reasons in a dated history | Turn project memory into a transcript of routine exchanges |
| Maintain existing project instructions and account for overrides | Change global configuration or create background automations |
| Update clearly important developments during authorized work | Log developments of uncertain significance without asking |

## Installation

Follow the [collection installation instructions](../../README.md#installation) and
select this skill. See [SKILL.md](SKILL.md) for the complete workflow.

## Example Usage

**User**

```text
Use $zilin-context-setup to establish concise context for this project.
Capture its current direction and important decisions from the existing files,
and make sure future project chats are instructed to read and maintain it.
```

For an existing project:

```text
Use $zilin-context-setup to record our agreed scope change in the existing
project context. Update the current direction and preserve the previous
decision and the reason for changing it in the dated history.
```

## Inputs and Requirements

- An identifiable project root with access to its files and instructions.
- The user's statements and relevant project evidence for the initial context.
- Any existing context file and applicable `AGENTS.md` or `AGENTS.override.md`.

This package contains instructions and agent metadata; no external service or
helper scripts are required. `AGENTS.md` supplies the instruction to read the
context in future project chats. The context file is not automatically injected,
and the skill does not run as a background process.

## What You Receive

- A concise context file covering the project's supported current understanding.
- A maintenance convention and a dated evolution log for meaningful developments.
- A project instruction pointing future chats to the context file.
- Links to the affected files and a brief explanation of important updates.

## License

MIT License. See [LICENSE](../../LICENSE) for details.

---

> "Built by Codex. ⭐"
