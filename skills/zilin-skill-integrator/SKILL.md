---
name: zilin-skill-integrator
description: Integrate a newly created or updated skill into Zilin's codex-skills-zilin GitHub collection, matching its README branding, catalog, packaging, installer, and validation conventions. Use for preparing a skill for this repository or reviewing an integration; not for executing the imported skill's workflow or building an unrelated plugin.
---

# Zilin Skill Integrator

Prepare an existing skill for the collection while preserving its functional behavior. Use the repository's current files and the user's current instructions as the authority. Read [repository conventions](references/repository-conventions.md) for established presentation and packaging choices; it records the prior workflow without requiring access to private conversation history.

## Inspect source and destination

Locate the source skill from the provided path or installed-skill catalog. Identify the destination checkout from the user's supplied path or current workspace, and verify its remote and collection layout. If neither identifies the intended repository, or multiple candidates remain ambiguous, ask for the checkout path before editing the destination; source inspection can continue. Check applicable `AGENTS.md` files, Git status, branch/upstream, and remote before editing. Do not assume the local branch name is the remote default branch. Preserve unrelated working changes.

Read the source `SKILL.md`, metadata, resource inventory, and relevant helpers to understand what must ship. Treat these as the package being integrated: a slide narration skill does not authorize generating narration, and a pet skill does not authorize generating a pet. Compare the current root README, two representative skill READMEs, installer, and CI workflow. Inspect source/repository differences before overwriting an existing package; do not silently choose between divergent versions.

Resolve symlinks before comparing or copying. If the installed source and repository destination resolve to the same directory, review the existing package in place; do not copy it onto itself or claim that matching paths independently verify synchronization.

When the user asks to recover past preferences, use task-list and task-read tools to inspect relevant project conversations. Extract explicit user choices, distinguish them from suggestions, and prefer later accepted choices and current repository evidence. Do not copy private transcripts, task IDs, local paths, or unrelated personal details into the public skill.

## Integrate the package

Choose the path from the requested work and the repository's existing packages. An existing matching name does not by itself authorize replacing that skill.

### New skill

Check for collisions in folder names, frontmatter names, and catalog entries before creating `skills/<zilin-name>/`. If a name belongs to another skill, resolve whether this is an intended update or needs a distinct name; do not overwrite it or silently rename the source. Create the package and its README, then add one catalog row in an existing fitting category. Use the user's requested category when supplied.

### Existing skill update

Compare the source and repository inventories to identify added, changed, and potentially removed files. Reconcile the differences rather than blindly copying over the folder or deleting every destination-only file. Inspect references and purpose before removing obsolete resources. Preserve repository-only documentation, intentional public examples, and unrelated local changes unless the requested update requires changing them. If divergent edits leave the intended version unclear, ask which version to retain while continuing unaffected work.

Refresh the README where behavior or requirements changed. Update the existing catalog row in place instead of appending a duplicate, preserving its category unless the user requests a move. Repair a missing row when needed. For an authorized rename, update the folder, metadata, references, and existing catalog link together so the old entry is not left behind.

### Shared packaging steps

1. Ensure `skills/<zilin-name>/` matches the frontmatter `name`. Preserve resource paths, executable permissions, dependency declarations, invocation policy, and functional instructions. Keep display names and `$skill-name` examples consistent when a rename is requested.
2. Include required scripts, references, templates, and intentional public examples. Exclude nested Git metadata, credentials, generated runs, caches, virtual environments, drafts, and unrelated outputs. Inspect dependencies before dropping any file. Keep scratch work outside the public tree or in an already ignored location.
3. Write or refine the per-skill README using [the README template](assets/readme-template.md). Match the shared title/slogan/description/badges/installation/examples/license/footer conventions. Preserve the factual description beneath a separate italic slogan. Add a capabilities table, inputs, or deliverables when useful; do not fabricate demo assets or dependency availability. Treat a newly proposed slogan as editable preview copy, not an already accepted user preference.
4. Ensure the root catalog has exactly one concise entry for the integrated skill, using its nonbreaking skill-name labels and the category selected above. Keep examples and detailed requirements in the skill README and shared installation instructions in the root.
5. Check that the existing name-based installer discovers the package without changes. Avoid introducing redundant per-skill installers or validation frameworks.

## Verify and preview

Run the checks actually defined by the current CI workflow, plus `git diff --check`. Check metadata, YAML/JSON, Python syntax where present, local Markdown links including image paths and section anchors, resource references, and stale fixed installation paths. Run the skill-creator validator when available; if a dependency prevents it from running, report that accurately and use the repository validator rather than claiming the skipped validator passed.

For Markdown templates, validate relative links from the intended generated file location. The bundled README template is copied to the skill root; its placeholders are intentional and must be replaced in the resulting README. Exclude literal code examples from documentation-link checks.

For imported helpers, use small meaningful smoke checks for the documented behavior without paid services or production mutations. Do not execute the whole imported workflow merely to validate packaging. Measure added media; optimize oversized README previews only when appropriate and visually compare the result. Do not rewrite Git history to shrink old media.

Review the complete change set, including untracked files, and compare functional files against the source so incidental workflow edits are visible. Preview the actual README file and the full integration diff in the app when available; otherwise provide file links. State what changed, which checks passed, and anything unverified. Honor preview-only or no-commit requests: leave the reviewed changes uncommitted until the user requests the next step.

## Install and publish within scope

Repository integration, local installation, a commit, and a remote push are distinct outcomes. Honor the current session's authorization for each without repeatedly asking about an already authorized action. Historical pushes in another task are evidence of workflow, not standing authorization for the present destination.

When local installation is requested, use the collection installer. It skips existing files and symlinks; inspect and report an existing standalone installation rather than claiming it was updated. Do not replace an existing installation or create duplicate discovery entries without resolving that migration within the user's scope.

When publication is authorized, verify the intended remote and branch, synchronize safely, stage only the intended files, commit, and push through the authorized route. Do not force-push or bypass an approval rejection. If blocked, finish the local preview and state the exact remaining action and reason. After a successful push, verify the remote commit and relevant CI status; distinguish pending CI from passed CI. Report local edits, commit, push, and installation status precisely.
