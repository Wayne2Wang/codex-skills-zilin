# Zilin Paper Adapter

> *You write. It formats.*

A Codex skill that initializes an empty Overleaf or LaTeX project from a personal
Overleaf starter, then adapts it to a verified official conference template.
Existing papers are migrated directly without importing the starter over them.

[![Codex Skill](https://img.shields.io/badge/Codex-Skill-111111)](https://developers.openai.com/)
[![LaTeX](https://img.shields.io/badge/LaTeX-008080?logo=latex&logoColor=white)](https://www.latex-project.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../LICENSE)

`$zilin-paper-adapter` inspects the whole project, verifies the live official
source, and chooses initialization, content-preserving migration, or an audit.
New scaffolds preserve the starter’s reusable structure and macros, with explicit TODOs in place of sample metadata. Existing author content stays intact.

| It can | It will not |
| --- | --- |
| Initialize an empty project from the personal starter | Draft manuscript prose or add fake references |
| Reorganize files and update template wiring | Rewrite existing manuscript content |
| Download the verified official template | Use a remembered or unofficial template |
| Keep required author sections active with obvious TODOs | Invent authors, results, or disclosures |
| Show unused key template components as explained commented lines | Load unnecessary optional components silently |

A new scaffold follows the starter’s layout; this is its general shape. migrations preserve equivalent clean structures
and existing manuscript filenames:

```text
paper/
├── main.tex
├── main.bib
├── preamble.tex
├── sections/
│   ├── 0_abstract.tex
│   ├── 1_intro.tex
│   ├── ...
│   └── X1_appendix.tex
└── style_<venue><year>/      complete, unchanged official bundle
```

The resulting entry point accounts for the official template's key components. Optional components that are not needed remain visible as commented loading lines with an explanation, while mandatory author-supplied sections remain active with a conspicuous TODO until the authors complete them.

## Installation

Follow the [collection installation instructions](../../README.md#installation) and
select this skill. See [SKILL.md](SKILL.md) for the complete workflow.

## Example Usage

**User**

```text
Use $zilin-paper-adapter to initialize this empty LaTeX project with the
personal Overleaf starter, then adapt it to the official conference review
template for the venue and year I specify.
Use headings and TODOs only; do not draft manuscript text or add citations.
```

For an existing paper:

```text
Use $zilin-paper-adapter to migrate this existing Overleaf paper
from the NeurIPS 2025 template to the official ICLR 2027 review template.
```

You can also ask for an audit without requesting changes:

```text
Use $zilin-paper-adapter to audit whether this repository conforms
to the official ICML 2027 submission template. Do not modify any files.
```

## Inputs and Requirements

- The project directory and target conference, year, and submission stage.
- Access to the configured personal Overleaf starter for initialization (or an exported copy).
- An optional alternative starter or section outline.
- Access to the live official author guidelines and template download.
- A compatible LaTeX build environment and PDF inspection tools for validation.

This package contains workflow instructions and agent metadata, not a compiler
or bundled conference templates. An unavailable or conflicting official release
requires an explicit source or fallback choice; a prior-year fallback retains its
actual year and is reported as provisional.

## What You Receive

- An initialized scaffold or migrated project with the complete official template bundle.
- Preserved author content, or clearly marked placeholders and an empty author bibliography.
- A source and validation report identifying unresolved author TODOs, inactive
  optional components, and any old template files retained or removed.

Bibliography and appendix inputs remain active, including `sections/X1_appendix.tex`.
Empty bibliographies can produce no-citation diagnostics; the skill reports these
instead of disabling references or inserting fake citations.

An empty scaffold is not a completed or submission-ready paper. Bibliography
rendering may remain unvalidated until the first real citation is added. Audit-only
requests produce findings without file changes.

## License

MIT License. See [LICENSE](../../LICENSE) for details.

---

> "Built by Codex. ⭐"
