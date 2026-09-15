#!/usr/bin/env bash
set -euo pipefail

repo_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
skills_dir="$HOME/.agents/skills"

if [[ "${1:-}" == "--help" || "${1:-}" == "-h" ]]; then
  printf 'Usage: bash %s [skill-name ...]\nWithout names, installs all skills. Existing installations are skipped.\n' "$0"
  exit 0
fi

selected_skills=()
if (( $# )); then
  for name in "$@"; do
    if [[ ! "$name" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ || ! -f "$repo_dir/skills/$name/SKILL.md" ]]; then
      printf 'Unknown skill: %s\nNo skills were installed. Available skills:\n' "$name" >&2
      for skill in "$repo_dir"/skills/*/; do
        [[ -f "$skill/SKILL.md" ]] || continue
        printf '  %s\n' "$(basename "$skill")" >&2
      done
      exit 1
    fi
    selected_skills+=("$repo_dir/skills/$name")
  done
else
  for skill in "$repo_dir"/skills/*/; do
    [[ -f "$skill/SKILL.md" ]] || continue
    selected_skills+=("${skill%/}")
  done
fi

mkdir -p "$skills_dir"
for skill in "${selected_skills[@]}"; do
  target="$skills_dir/$(basename "$skill")"
  if [[ -e "$target" || -L "$target" ]]; then
    printf 'Skipped existing: %s\n' "$target"
    continue
  fi
  ln -s "${skill%/}" "$target"
  printf 'Installed: %s\n' "$target"
done
