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
| [codex&#8209;paper&#8209;adapter](skills/codex-paper-adapter) | Adapt LaTeX papers to official conference templates while preserving manuscript content. |
| [codex&#8209;paper&#8209;checker](skills/codex-paper-checker) | Audit papers for technical correctness, formatting, venue compliance, and reference integrity. |

### Miscellaneous

| Skill | Purpose |
| --- | --- |
| [codex&#8209;cat&#8209;hatcher](skills/codex-cat-hatcher) | Turn your cat photo into a realistic animated Codex pet. |

Open a skill's README for usage examples and requirements.

## Install

Clone the collection once:

```bash
git clone https://github.com/Wayne2Wang/codex-skills.git ~/codex-skills-zilin
mkdir -p ~/.agents/skills
```

Install one skill by name:

```bash
bash ~/codex-skills-zilin/scripts/install-skills.sh codex-cat-hatcher
```

Or specify several skills:

```bash
bash ~/codex-skills-zilin/scripts/install-skills.sh codex-cat-hatcher codex-paper-checker
```

Or symlink all skills with one command:

```bash
bash ~/codex-skills-zilin/scripts/install-skills.sh
```

Existing installations are left untouched. Run this command again after pulling
to install newly added skills.
If any requested name is unknown, the script lists available skills and exits
before installing anything.

Codex follows symlinked skill directories. Restart Codex if a newly installed
skill does not appear immediately.

To update every installed skill, pull the collection once:

```bash
git -C ~/codex-skills-zilin pull
```

### Existing standalone installations

The repository root is no longer a skill directory. If you previously cloned
`codex-cat-hatcher` directly into a Codex skills folder, reinstall it using the
nested `skills/codex-cat-hatcher` directory above. Keep only one installed copy
of each skill name so Codex does not show duplicates.

## Adding another skill

Add a self-contained directory at `skills/<skill-name>/`, ensure its folder name
matches the `name` in `SKILL.md`, and add one row to the catalog above.
Maintain a `README.md` inside each skill folder with its purpose, examples,
requirements, and a link to the shared installation instructions.

## License

MIT License. See [LICENSE](LICENSE) for details.

---

> "Built by Codex. ⭐"
