# Anthropic Intelligence

Living knowledge base on Anthropic, Claude Code, and AI engineering best practices.

## Why this exists

Information from Anthropic ships fast: blog posts, model cards, Claude Code release
notes, engineering employees on X / personal blogs, Reddit threads, conference talks.
Most of it never reaches our internal systems. This repo (subtree) closes that gap:

- **Continuous monitoring** of curated sources via GitHub Actions cron
- **Weekly diff logs** of what changed in the Anthropic ecosystem
- **Monthly synthesis** of logs into topic-level KB articles
- **Engineer profiles** so we know whose ideas we're tracking

## Layout

| Path | Purpose |
|---|---|
| `topics/` | Synthesized, versioned KB articles per topic (HTML output, caching, tool use, agents, hooks, etc.) |
| `engineers/` | Profiles of key Anthropic engineers (Boris Cherny, Erik Schluntz, Sholto Douglas, Cat Wu, Thariq Shihipar) and external voices (Simon Willison) |
| `sources.yaml` | Registry of feeds, blogs, GitHub repos, X handles being watched |
| `monitoring/logs/` | Auto-generated weekly diff logs from scanner |
| `scripts/` | Python: source fetcher + monthly synthesizer |
| `../.github/workflows/anthropic-*.yml` | Cron workflows (weekly scan, monthly synthesis) |

## Cadence (recommended)

- **Weekly (Monday 06:00 UTC)** — scanner fetches all sources, writes diff log, opens PR
- **Monthly (1st of month, 06:00 UTC)** — synthesizer aggregates 4 weeks of logs, updates topic articles, opens PR
- **Ad-hoc** — major releases (Claude model launches, Claude Code major versions)

See `CADENCE.md` for rationale.

## Extracting to a standalone repo (future)

This lives as a subtree because the standalone `klangschalen/anthropic-intelligence`
repo could not be created from the current integration scope (403 from GitHub API).
To extract later:

```bash
git subtree split --prefix=anthropic-intelligence -b anthropic-intelligence-export
# create the standalone repo manually on github.com, then:
git push git@github.com:klangschalen/anthropic-intelligence.git anthropic-intelligence-export:main
```

## First artifact

`topics/output-formats-html-vs-markdown.md` — deep research into the May 2026
shift toward HTML as default Claude output format, with concrete recommendations
for our prompts and agents.
