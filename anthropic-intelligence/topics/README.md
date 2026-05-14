# Topics

Synthesized, versioned knowledge base articles.

Each topic file follows this front-matter template:

```yaml
---
topic: output-formats-html-vs-markdown
status: stable | draft | deprecated
last_synthesized: 2026-05-12
sources_consulted:
  - id: anthropic-engineering
    url: https://www.anthropic.com/engineering/...
    fetched: 2026-05-12
  - id: simon-willison
    url: https://simonwillison.net/2026/May/...
    fetched: 2026-05-12
related:
  - prompting
  - claude-code
---
```

## Current topics

| File | Status | Last synthesized |
|---|---|---|
| [output-formats-html-vs-markdown.md](./output-formats-html-vs-markdown.md) | draft | 2026-05-12 |

## Planned topics (stubs to be filled)

- `claude-code-best-practices.md` — hooks, skills, slash commands, MCP
- `prompt-caching.md` — cache breakpoints, hit-rate optimization, gotchas
- `tool-use.md` — schema design, parallel tool calls, error handling
- `agents-and-subagents.md` — when to use, isolation modes, prompt design
- `extended-thinking.md` — budget, output handling, when it actually helps
- `model-selection.md` — Opus vs Sonnet vs Haiku decision matrix per task
