# Collection conventions

These conventions reflect the accepted cat-hatcher publication and subsequent
skills-monorepo migration workflow. Recheck the current repository before use;
later user choices supersede this snapshot.

## Identity and organization

- Public collection: `Wayne2Wang/codex-skills-zilin`; verify the actual remote.
- Collection title: **Zilin's Codex Skills**. Use Zilin for author branding;
  preserve the actual GitHub account name in URLs.
- Personal skill names use `zilin-` to avoid collisions. Folder name,
  frontmatter name, invocation examples, and UI prompt agree.
- Skills live in `skills/<name>/`, each with its own README. The root README
  contains the compact catalog and shared installation instructions.
- Existing catalog categories are **Research** and **Miscellaneous**. Use
  `Skill | Purpose` tables with `&#8209;` between words in display labels to
  discourage name wrapping. Keep normal hyphens in link targets. Do not try to
  force matching column widths across GitHub Markdown tables.

## Per-skill README

Use [the template](../assets/readme-template.md) and compare current siblings.

1. Human-readable title.
2. A short slogan as an italic blockquote directly below the title.
3. The factual description as a separate paragraph, retained when adding branding.
4. Codex Skill and MIT badges; domain badges only when relevant.
5. A short `$skill-name` overview. A capability/boundary table is useful for
   workflow skills; a real visual example can be more appropriate for visual skills.
6. **Installation**, linking to `../../README.md#installation` and `SKILL.md`.
7. **Example Usage**, with a **User** label and realistic invocation in a text fence.
8. **Inputs and Requirements** and **What You Receive** when they add useful detail.
9. **License**, using `MIT License. See [LICENSE](../../LICENSE) for details.`
10. A horizontal rule followed by `> "Built by Codex. ⭐"`.

Do not replace a real description with a slogan or copy a domain-specific badge
into an unrelated skill. Keep external service requirements honest. A polished
README is documentation, not evidence that the complete workflow has been tested.

## Installation and packaging

The root installation instructions use a shallow clone into
`~/codex-skills-zilin` and `scripts/install-skills.sh`. Named arguments install
one or several skills; no arguments discovers all skills. The script symlinks
into the user's agents skills directory and skips existing installations.
Pulling the clone updates skills already linked to it. Keep this shared logic
centralized; do not reintroduce the removed standalone-installation migration
section merely because it appeared in an older conversation.

Publish only intentional skill resources. Keep private work and generated runs
outside the public package. Maintain portable relative resource paths instead
of creator-specific absolute paths. Check for stale names after requested
rebranding, including template IDs and example paths.

Use small real example media when available. Measure before optimizing; preserve
already compact GIFs and visually check compressed photos at their display size.
The prior cat-hatcher photo was reduced substantially while its small GIFs were
retained. That is a method, not a universal dimension or compression target.

## Validation and review

Use the current shared CI, not removed historical standalone validation tooling.
At this snapshot it validates skill frontmatter/layout and agent YAML, compiles
Python helpers, and rejects fixed legacy installation paths in skill content.
Also check local documentation links and the final diff. Only add new validation
infrastructure when an actual unmet need justifies it.

The prior workflow included editing the actual Markdown and opening it for
preview before a requested commit or push. Respect the current user's review
boundary. Past successful pushes do not resolve a present approval rejection.
