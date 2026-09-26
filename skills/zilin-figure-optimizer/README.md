# Zilin Figure Optimizer

> *Smaller files. Details that matter.*

A Codex skill that reduces figure asset and compiled PDF sizes in LaTeX and other
document projects by measuring rendered placement, choosing suitable raster
resolution and compression, and visually checking the rebuilt document.

[![Codex Skill](https://img.shields.io/badge/Codex-Skill-111111)](https://developers.openai.com/)
[![LaTeX](https://img.shields.io/badge/LaTeX-008080?logo=latex&logoColor=white)](https://www.latex-project.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../LICENSE)

`$zilin-figure-optimizer` builds a baseline, measures how large each active figure
appears, tests compression candidates from preserved originals, and compares the
rebuilt PDF before accepting changes. It targets useful savings while preserving
scientific detail, vector graphics, and the document's layout.

| It can | It will not |
| --- | --- |
| Size raster assets for their largest rendered placement | Apply a universal pixel cap to every figure |
| Test lossless optimization and suitable high-quality JPEG encoding | Promise mathematical losslessness for resizing or JPEG |
| Inspect labels, masks, boundaries, textures, and colors after rebuilding | Rasterize vector plots or alter scientific content |
| Report actual PDF savings separately from asset savings | Count unused assets as compiled-PDF savings |
| Work toward a supplied file-size limit | Silently degrade figures to meet an unattainable limit |

## Installation

Follow the [collection installation instructions](../../README.md#installation) and
select this skill. See [SKILL.md](SKILL.md) for the complete workflow.

## Example Usage

**User**

```text
Use $zilin-figure-optimizer to reduce this LaTeX project's compiled PDF
below 20 MB if possible. Preserve segmentation boundaries and small labels,
keep recoverable originals, and compare the rebuilt PDF with the baseline.
```

A size limit is optional:

```text
Use $zilin-figure-optimizer to check which active figures make this paper
large and optimize them conservatively. Give me the rebuilt PDF, optimized
source, and a per-asset report of savings and visual checks.
```

## Inputs and Requirements

- The source project, its build command, and the intended output PDF.
- Optional submission size limit and details that need extra care, including
  insets, supplementary pages, or other outputs sharing the same assets.
- A working document build environment, such as the project's LaTeX toolchain.
- PDF inspection and rendering tools, such as Poppler and PyMuPDF, plus
  deterministic image processing tools appropriate to the assets.

This package contains workflow instructions and agent metadata; it does not bundle
a compiler, compression engine, or helper scripts. Available tools are checked
during use. If the current source cannot be built or visual checks cannot be
completed, the result must identify those verification limits.

## What You Receive

- A rebuilt PDF and usable optimized source or asset patch.
- A manifest of changed assets with dimensions, rendered sizes, effective PPI,
  encoding settings, before/after bytes, and visual QA outcomes.
- Measured final PDF size and percentage savings, reported separately from assets.
- A record of preserved originals and whether requested remote changes were applied.

Remote publication requires a separate request within the optimization workflow.

## License

MIT License. See [LICENSE](../../LICENSE) for details.

---

> "Built by Codex. ⭐"
