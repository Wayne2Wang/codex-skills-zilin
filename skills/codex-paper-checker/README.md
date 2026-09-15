# Codex Paper Checker

> *Your paper. A sharper second look.*

A Codex skill that audits near-final computer vision and robotics papers before submission.

[![Codex Skill](https://img.shields.io/badge/Codex-Skill-111111)](https://developers.openai.com/)
[![LaTeX](https://img.shields.io/badge/LaTeX-008080?logo=latex&logoColor=white)](https://www.latex-project.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../LICENSE)

`$codex-paper-checker` checks mathematical and notation correctness, writing and
formatting errors, reviewer-facing risks, venue compliance, and bibliography integrity.

| It can | It will not |
| --- | --- |
| Check equations, notation, and technical consistency | Rewrite manuscript files unless asked |
| Verify every bibliography entry in a full audit | Treat sampled references as a complete audit |
| Check current official venue requirements | Claim compliance when checks remain unresolved |
| Separate proven errors from reviewer-facing risks | Guarantee acceptance or infallible verification |

## Install

Follow the [collection installation instructions](../../README.md#install) and
select this skill. See [SKILL.md](SKILL.md) for the complete workflow.

## Example Usage

**User**

```text
Use $codex-paper-checker to audit this submission PDF and LaTeX project.
Check every bibliography entry and report the highest-priority fixes.
```

For a focused check:

```text
Use $codex-paper-checker to check only the equations and notation in this paper.
```

## Inputs and Requirements

Provide the PDF and, when available, LaTeX source, bibliography, and supplementary
material. Include the venue and year for a venue-compliance check. Reference and
venue verification require access to authoritative online sources. Annotated PDF
creation uses an available PDF skill and rendering tools.

## What You Receive

- A reviewer-style assessment and prioritized findings.
- Equation and symbol coverage for a full audit.
- A reference-integrity table accounting for every bibliography entry.
- Venue-compliance findings when the venue is known.
- An annotated PDF when requested or useful.

The skill preserves manuscript files unless you explicitly request fixes. It
distinguishes proven errors from reviewer risks and reports unresolved checks.
See [SKILL.md](SKILL.md) for the full scope and completion criteria.

## License

MIT License. See [LICENSE](../../LICENSE) for details.

---

> "Built by Codex. ⭐"
