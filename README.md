# Wayne's Codex Skills

> A growing collection of focused skills for Codex.

[![Codex Skills](https://img.shields.io/badge/Codex-Skills-111111)](https://learn.chatgpt.com/docs/build-skills)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Each directory under [`skills/`](skills) is a self-contained skill with its own
`SKILL.md` and any resources it needs. New skills can be added without changing
the existing ones.

## Skills

| Skill | Purpose | Example invocation |
| --- | --- | --- |
| [`codex-cat-hatcher`](skills/codex-cat-hatcher) | Create realistic animated Codex pets from a cat photo. | `Use $codex-cat-hatcher to create a Codex pet for my cat.` |
| [`codex-paper-adapter`](skills/codex-paper-adapter) | Migrate an existing LaTeX paper to an official conference template without rewriting its content. | `Use $codex-paper-adapter to migrate this paper to the official target template.` |
| [`codex-paper-checker`](skills/codex-paper-checker) | Audit near-final computer vision and robotics papers for technical, formatting, venue, and reference problems. | `Use $codex-paper-checker to audit this submission.` |

## Install

Clone the collection once:

```bash
git clone https://github.com/Wayne2Wang/codex-cat-hatcher.git ~/codex-skills
mkdir -p ~/.agents/skills
```

Then symlink whichever skills you want Codex to discover:

```bash
ln -s ~/codex-skills/skills/codex-cat-hatcher ~/.agents/skills/codex-cat-hatcher
ln -s ~/codex-skills/skills/codex-paper-adapter ~/.agents/skills/codex-paper-adapter
ln -s ~/codex-skills/skills/codex-paper-checker ~/.agents/skills/codex-paper-checker
```

Codex follows symlinked skill directories. Restart Codex if a newly installed
skill does not appear immediately.

To update every installed skill, pull the collection once:

```bash
git -C ~/codex-skills pull
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
