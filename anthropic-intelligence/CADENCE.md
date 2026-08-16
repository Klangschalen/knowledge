# Update Cadence

## Recommended rhythm

| Frequency | What | Trigger | Output |
|---|---|---|---|
| Daily | nothing automatic | — | manual only, on demand |
| **Weekly (Mon 06:00 UTC)** | Source scan | `.github/workflows/anthropic-weekly-scan.yml` cron | `monitoring/logs/YYYY-WW.md` + PR |
| **Monthly (1st 06:00 UTC)** | Topic synthesis | `.github/workflows/anthropic-monthly-synthesis.yml` cron | Updates to `topics/*.md` + PR |
| Ad-hoc | Major release (new Claude model, Claude Code major) | Manual | Hand-crafted topic update |

## Why this cadence

- **Daily**: too noisy. Anthropic does not publish that often. Would create alert fatigue and PR spam.
- **Weekly**: sweet spot for catching blog posts, Simon Willison's weeknotes, Boris Cherny / Thariq Shihipar tweets, Claude Code minor releases. One human review per week max.
- **Monthly**: enough buffer for 3–4 weekly logs to accumulate before re-synthesizing topic articles. Avoids constant article churn and merge conflicts.
- **Ad-hoc**: model launches and Claude Code major versions warrant immediate, deeper treatment than the standard pipeline can deliver.

## Source priority tiers

Sources in `sources.yaml` carry a `priority` field:

- **P0** — must-check every scan (Anthropic blog, Claude Code releases, docs changelog)
- **P1** — weekly check (employee blogs, Simon Willison, key X accounts, model cards)
- **P2** — monthly check (community Reddit, broader news aggregation)

## Tuning the cadence

If weekly PRs feel too noisy, drop P2 sources from the weekly scan and only include them in the monthly synthesis. If a topic is hot (e.g. a model release week), temporarily bump cadence to twice weekly via `workflow_dispatch`.
