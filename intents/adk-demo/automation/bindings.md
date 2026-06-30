---
# Automation bindings for the `adk-demo` intent domain (tree-v1).
#
# Created by `intent-cli intent init-tree` so first-run `next-slice`,
# `host-check`, and `automation summary` recognize this domain without
# hand-authoring. Ask intent-cli before editing:
#   intent-cli guide intent-work setup --kind tree-layout --domain adk-demo --format markdown

# Implementation (child) repository this domain's issues target.
child_repo: quangtuyen88/intent-development-demo

# Execution-unit namespace filter used by `next-slice` and
# `automation summary` to select which execution units belong to this
# domain. The default `.*` accepts every execution unit (correct for a
# single-domain host). Narrow it (for example `^adk-demo-`) once you
# share a `.intent-cli/issues` root across multiple domains.
execution_unit_regex: .*
---

# adk-demo automation bindings

This file maps the `adk-demo` intent domain to its implementation
repository and durable automation state. intent-cli reads the
frontmatter fields above; the prose below is for humans and agents.

Ask intent-cli for the next action instead of inspecting source code to
recover first-run setup:

- `intent-cli intent host-check --domain adk-demo --format json`
- `intent-cli intent next-slice --dry-run --domain adk-demo --format json`
- `intent-cli automation summary --domain adk-demo --format json`
