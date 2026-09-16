# Zilin Skill Integrator

> *Your skills. One consistent home.*

A Codex skill that prepares new and updated skills for Zilin's GitHub collection,
matching its documentation, packaging, and review conventions.

[![Codex Skill](https://img.shields.io/badge/Codex-Skill-111111)](https://developers.openai.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../LICENSE)

`$zilin-skill-integrator` inspects the source package and repository, writes a
matching README, updates the catalog, validates the integration, and presents it
for review within your requested commit and publication scope.

For a **new skill**, it checks for name collisions, creates the package and README,
and adds a catalog entry. For an **update**, it reconciles added, changed, and
obsolete files, preserves repository-only content where appropriate, and refreshes
the existing catalog entry without changing its category unless requested.

| It can | It will not |
| --- | --- |
| Match existing README branding and structure | Replace the skill's purpose with generic boilerplate |
| Package required scripts, references, and templates | Include private runs or unrelated generated output |
| Check metadata, links, and relevant helper behavior | Run paid production workflows as a packaging test |
| Prepare a preview and publish when authorized | Treat a preview request as permission to push |

## Installation

Follow the [collection installation instructions](../../README.md#installation) and
select this skill. See [SKILL.md](SKILL.md) for the complete workflow.

## Example Usage

**User**

```text
Use $zilin-skill-integrator to add my new skill to codex-skills-zilin.
Match the existing READMEs and show me the changes before committing.
```

For an existing package:

```text
Use $zilin-skill-integrator to compare this updated skill with its repository
copy, integrate the changes, and check its documentation and dependencies.
```

## Inputs and Requirements

Provide the source skill name or folder and the destination checkout when they
are not already available in the task. Local integration uses filesystem and
Git access plus the repository's validation tools. Publication requires GitHub
access and authorization for the intended destination. Task-history access is
only needed when recovering past preferences from conversations.

The skill checks the supplied path or current workspace to identify the repository.
If the destination is missing or ambiguous, it asks for the checkout path before
editing it.

## What You Receive

- A self-contained skill package with consistent names and resource paths.
- A matching README and concise catalog entry.
- Validation results and a reviewable local diff.
- Precise installation, commit, and publication status for the actions requested.

The package includes a reusable [README template](assets/readme-template.md) and
[repository conventions](references/repository-conventions.md).

## License

MIT License. See [LICENSE](../../LICENSE) for details.

---

> "Built by Codex. ⭐"
