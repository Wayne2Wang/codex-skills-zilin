---
name: zilin-paper-adapter
description: Initialize an empty Overleaf or LaTeX project with an official conference template, or migrate an existing paper while preserving all author-written content. Use for paper scaffolding, venue or template changes, project structure normalization, or template-conformance audits. Do not use to draft, rewrite, or complete manuscript content.
---

# Zilin Paper Adapter

Initialize a paper scaffold or convert an existing project structurally and losslessly: the result should use the verified official template for the requested venue, year, and submission stage, while the authors' title, prose, equations, figures, tables, labels, citations, bibliography records, comments, and supplementary material remain unchanged.

## Choose the mode

- **Initialize:** The project contains no author-written manuscript content, bibliography records, or assets; it may have an empty entry point or verified untouched template boilerplate. Set up a compiling skeleton with explicit author TODOs and no invented manuscript text.
- **Migrate:** Any author-written content exists, including partial drafts, comments, bibliography records, or assets. Preserve it and apply the existing migration workflow; a short or incomplete paper is not an empty project.
- **Audit or brainstorm:** If the user requests inspection or planning only, report findings or a proposed layout without modifying files.

Inspect the whole project before choosing a mode. An empty `main.tex` alone does not establish that the project is empty. If template boilerplate and author content cannot be distinguished confidently, preserve the ambiguous material and clarify only what blocks the work.

The boundaries, official-source checks, and verification below apply to both initialization and migration. Initialization does not require a compilable original or an old template to remove.

## Non-negotiable boundaries

- Do not write, paraphrase, shorten, expand, or "improve" manuscript content.
- Do not invent authors, affiliations, disclosures, checklist answers, acknowledgements, results, citations, or metadata. If the venue requires author-supplied information that is absent, keep the official section or hook active, add a prominent compiled TODO telling the authors exactly what they must supply, and report the unresolved requirement. The TODO must be unmistakably incomplete and must not resemble a valid disclosure or answer.
- Treat user-authored `.tex` and `.bib` material as content even when incomplete. Move it or update references to it, but do not silently delete or rewrite it.
- Distinguish old template assets and untouched sample boilerplate from author content. Remove old venue assets only after proving they are unused and contain no author additions. Preserve any ambiguous file and report it.
- Do not commit, push, change Overleaf settings, or enable camera-ready mode unless the user asks.

## Audit before changing anything

Inspect the repository, its instructions, Git status, and ignore rules. Do not assume `main.tex` is the entry point.

Build a dependency inventory covering:

- root entry-point `.tex` files and any configured Overleaf main document;
- `\input`, `\include`, `\usepackage`, `\documentclass`, bibliography, and graphics paths;
- section files, bibliography databases, figures, supplementary material, custom macros, and build configuration;
- existing venue-specific `.sty`, `.cls`, `.bst`, sample `.tex`, sample `.bib`, and documentation files;
- tracked and untracked user files, including local changes that must be preserved.

Classify each file as author content, project support, target-template material, old-template material, generated build output, or ambiguous. Record a content baseline using Git diff/status and file hashes or copies as appropriate. Compile the original project when practical so migration-only failures can be distinguished from existing failures.

## Normalize the project structure first

If the project already has an equivalent clean structure, preserve it rather than performing a cosmetic reorganization. Otherwise organize it before changing templates:

```text
project/
|-- main.tex                 primary entry point
|-- *.bib                    author bibliography database(s)
|-- sections/                author manuscript and supplement `.tex` files
`-- style_<venue><year>/     files distributed with the official template
```

Keep non-template assets such as figures and data in their existing sensible directories. Do not force a single bibliography file or merge section files. Move files with history-preserving operations where possible, then change only the path references needed to keep the same document connected.

The `style_<venue><year>/` directory should contain the complete official template bundle needed for provenance and reproducibility, including shipped style/class, bibliography-style, helper-package, example, sample-bibliography, and documentation files. Keep downloaded template files byte-for-byte intact. Adapt the project entry point to reference their subdirectory paths instead of editing the official files merely to accommodate the folder layout.

The resulting entry point must visibly account for every key component demonstrated or required by the official template. Key components normally include the venue class/style, shipped helper packages, bibliography style, submission/final-mode switch, optional macro files, required author-supplied sections, and appendix wiring. Do not silently omit a key component merely because the current manuscript does not use it.

## Identify the correct official template

Determine the exact conference, year, and submission stage from the request and repository. Ask the user only when one of these changes the template or anonymity mode and cannot be determined safely.

Templates and author rules are time-sensitive. Check the live official conference author/submission page and follow its link to the official archive or official Overleaf template. Prefer the conference-controlled source over third-party mirrors or remembered prior-year files. Verify that the downloaded archive and its internal version labels agree with the requested venue/year.

If the requested year's official template has not been released, or official sources conflict, stop before substituting another year. Present the evidence and ask the user which source or fallback to use. Keep a concise record of the source URL and retrieval date for the handoff, but do not add provenance prose to the manuscript.

## Initialize an empty project

Verify the official template before creating a scaffold that claims to target it. Use the project structure above and any known user conventions. In a new project, default to `main.tex`, `main.bib`, `preamble.tex` for custom packages/macros, and `sections/` for the abstract and manuscript sections. Add figures or tables directories only when useful. Keep the complete official bundle in `style_<venue><year>/`; do not mix sample bibliography records with the author's bibliography.

- Keep `main.tex` focused on the official class/style, submission-mode settings, title metadata, section order, bibliography, and appendix/supplement wiring. Load custom setup from `preamble.tex` without altering the vendor files.
- Use an explicitly requested section outline when available. Otherwise use conventional structural placeholders such as abstract, introduction, related work, method, experiments, and conclusion, making clear that they are editable scaffolding rather than an agreed research narrative. Section files may contain headings and TODOs, but no drafted claims or prose.
- Use obvious placeholders such as `TODO: Paper title` for unknown required metadata. Keep the official anonymous-author behavior in review mode; do not invent identities, affiliations, or a plausible submission ID. Retain an official placeholder ID when available and flag it for replacement.
- For a new scaffold, name the supplementary/appendix content file `sections/X1_appendix.tex`, not `supplementary.tex`, and use that path in its input hook. Preserve an existing manuscript's filenames unless the user requests renaming.
- Apply the active, inactive, and awaiting-author component states below. Required author-supplied sections must contain visible TODOs. Optional supplementary material can remain a commented hook until needed; do not force a separate supplement format before checking the venue's rules.
- Wire the bibliography to an empty author `.bib` file. Do not insert fake references, copy sample citations, or use `\nocite{*}` to conceal the absence of citations. If the bibliography tool fails on an uncited skeleton, keep the intended bibliography commands visibly commented with an instruction to enable them after adding the first real citation, and report that bibliography rendering is not yet validated.
- Include appropriate build-output ignore rules, preserving any existing ones. Do not add unnecessary packages, build infrastructure, or fabricated content merely to fill the template.
- If the requested year's template is unavailable, follow the source/fallback rule above. An explicitly authorized prior-year fallback must retain its actual year in its style directory and be reported as provisional; never relabel it as the requested official release.

Compile and visually inspect the resulting skeleton where supported. Report it as an initialized scaffold, with unresolved TODOs and untested content-dependent elements, not as a completed or submission-ready paper.

## Wire official-template components (both modes)

Use the official example only to learn required preamble, package, title/author, bibliography, appendix, and submission-mode wiring. Do not copy its example paper text into the manuscript.

For each key official-template component, choose one of these explicit states in the project entry point:

- **Active:** Load or invoke required components and optional components the manuscript actually uses.
- **Visible but inactive:** For an optional component that is unnecessary, retain its correct loading or invocation line as a commented line. Add an adjacent comment stating that it is an optional official-template component, why it is currently disabled, and that authors may enable it if they need its commands. For example, an unused official math macro file should appear as a commented `\input{style_<venue><year>/math_commands.tex}` line rather than disappearing from the entry point.
- **Active and awaiting authors:** For a mandatory author-supplied section or field, insert the official heading or structural hook in active, compiling form and place a conspicuous active TODO beneath it, such as `\textbf{TODO (authors -- required before submission): ...}`. Do not comment out the heading, hook, or TODO. Do not draft the missing substantive content, and do not let the placeholder read as compliance.

Keep explanatory comments next to inactive optional lines and author TODOs so the resulting Overleaf project is self-explanatory without consulting the migration report. Do not activate unused optional code solely to make every distributed file execute.

## Perform a content-preserving migration

Make the smallest structural edits needed to the entry point and project support files:

- replace the old venue's class/style invocation with the target invocation;
- preserve the existing title, author fields, abstract, section inputs, bibliography data, figures, tables, and supplement;
- switch citation or bibliography-style wiring without modifying bibliography records or citation intent;
- retain custom packages and macros unless they conflict with an explicit target rule; resolve conflicts structurally when possible and otherwise report them;
- use the correct review/anonymity mode by default for a submission-template request; enable final mode only when explicitly requested;
- place target-template assets in `style_<venue><year>/` and remove references to the old template;
- add mandatory author-supplied sections in active form with an obvious compiled TODO, while never filling in the substantive response on the authors' behalf;

Do not delete the old template bundle until the migrated project builds and a reference search confirms nothing uses it. Delete only files confidently classified as old template assets or generated outputs, never author content. If deletion was not clearly authorized or classification is uncertain, retain the files and tell the user what remains.

## Verify the result

Validate against both the official template and the current author guidelines, not merely successful compilation.

1. Compile from a clean build with the engine and bibliography workflow appropriate to the project.
2. Treat missing files, undefined control sequences, citation-system incompatibilities, accidental final mode, and wrong paper size as setup or migration defects.
3. Inspect the rendered PDF for required headers, line numbers, anonymity, margins, fonts, title layout, references, and appendix ordering. Do not repair content-originated overfull boxes by rewriting prose; report them.
4. Search for stale old-venue names, style paths, checklists, final-copy flags, and bibliography styles. Some occurrences may be legitimate citations or comments; inspect before changing them.
5. For initialization, verify that placeholders are clearly marked, sample prose and sample references have not entered the author files, and all active inputs resolve. For migration, compare the post-migration content inventory with the baseline. Every author content file and bibliography record must remain, with diffs limited to path/wiring changes explicitly required by the migration.
6. Review Git status and diff so generated build artifacts and accidental unrelated changes are absent.

Report the official source used, structural changes, validation performed, old template files removed or retained, and any requirements that still need author input. Explicitly list key optional template components left inactive, why each was unnecessary, and where its commented loading line appears. Also identify every active TODO that authors must replace. Describe the project as fully compliant only when every checkable requirement passes; otherwise distinguish template/format compliance from unresolved substantive author obligations.
