# Zilin's Codex Skills

> A growing collection of focused skills for Codex.

[![Codex Skills](https://img.shields.io/badge/Codex-Skills-111111)](https://learn.chatgpt.com/docs/build-skills)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Each directory under [`skills/`](skills) is a self-contained skill with its own
`SKILL.md` and any resources it needs. New skills can be added without changing
the existing ones.

## Skills

### Paper Preparation

| Skill | Purpose |
| --- | --- |
| [zilin&#8209;paper&#8209;adapter](skills/zilin-paper-adapter) | Adapt LaTeX papers to official conference templates while preserving manuscript content. |
| [zilin&#8209;paper&#8209;checker](skills/zilin-paper-checker) | Audit papers for technical correctness, formatting, venue compliance, and reference integrity. |

### Miscellaneous

| Skill | Purpose |
| --- | --- |
| [zilin&#8209;cat&#8209;hatcher](skills/zilin-cat-hatcher) | Turn your cat photo into a realistic animated Codex pet. |

Open a skill's README for usage examples and requirements.

## Install

Clone the collection once:

```bash
git clone https://github.com/Wayne2Wang/codex-skills-zilin.git ~/codex-skills-zilin
mkdir -p ~/.agents/skills
```

Install skills by name through simlinks:

```bash
bash ~/codex-skills-zilin/scripts/install-skills.sh zilin-paper-adapter zilin-paper-checker
```

Or symlink all skills with one command:

```bash
bash ~/codex-skills-zilin/scripts/install-skills.sh
```

Existing installations are left untouched. Restart Codex if a newly installed
skill does not appear immediately.

To update every installed skill, pull the collection once:

```bash
git -C ~/codex-skills-zilin pull
```

## Adding another skill

Add a self-contained directory at `skills/<skill-name>/`, ensure its folder name
matches the `name` in `SKILL.md`, and add one row to the catalog above.
Maintain a `README.md` inside each skill folder with its purpose, examples,
requirements, and a link to the shared installation instructions.

Contributions welcome! Open an issue with an idea or submit a PR with a new skill or improvement.

## License

MIT License. See [LICENSE](LICENSE) for details.

---

> "Built by Codex. ⭐"
