# Zilin Paper Adapter

> *You write. It formats.*

A Codex skill that migrates an existing paper to a new official conference template.

[![Codex Skill](https://img.shields.io/badge/Codex-Skill-111111)](https://developers.openai.com/)
[![LaTeX](https://img.shields.io/badge/LaTeX-008080?logo=latex&logoColor=white)](https://www.latex-project.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../LICENSE)

`$zilin-paper-adapter` verifies the live official source, rewires the project, and leaves the manuscript unchanged.

| It can | It will not |
| --- | --- |
| Reorganize files and update template wiring | Rewrite manuscript prose |
| Download the verified official template | Use a remembered or unofficial template |
| Keep required author sections active with obvious TODOs | Invent authors, results, or disclosures |
| Show unused key template components as explained commented lines | Load unnecessary optional components silently |

The project is normalized toward:

```text
paper/
├── main.tex
├── references.bib
├── sections/
│   ├── introduction.tex
│   └── ...
├── figures/
└── style_iclr2027/
    ├── iclr2027_conference.sty
    └── ...
```

The resulting entry point accounts for the official template's key components. Optional components that are not needed remain visible as commented loading lines with an explanation, while mandatory author-supplied sections remain active with a conspicuous TODO until the authors complete them.

## Installation

Follow the [collection installation instructions](../../README.md#installation) and
select this skill. See [SKILL.md](SKILL.md) for the complete workflow.

## Example Usage

**User**
```text
Use $zilin-paper-adapter to migrate this existing Overleaf paper
from the NeurIPS 2025 template to the official ICLR 2027 review template.
```

You can also ask for an audit without requesting changes:

```text
Use $zilin-paper-adapter to audit whether this repository conforms
to the official ICML 2027 submission template. Do not modify any files.
```

## License

MIT License. See [LICENSE](../../LICENSE) for details.

---

> "Built by Codex. ⭐"
