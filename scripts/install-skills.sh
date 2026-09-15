#!/usr/bin/env bash
set -euo pipefail

repo_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
skills_dir="$HOME/.agents/skills"
mkdir -p "$skills_dir"

for skill in "$repo_dir"/skills/*/; do
  [[ -f "$skill/SKILL.md" ]] || continue
  target="$skills_dir/$(basename "$skill")"
  if [[ -e "$target" || -L "$target" ]]; then
    printf 'Skipped existing: %s\n' "$target"
    continue
  fi
  ln -s "${skill%/}" "$target"
  printf 'Installed: %s\n' "$target"
done
