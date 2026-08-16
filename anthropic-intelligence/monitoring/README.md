# Monitoring

Auto-generated outputs from the weekly source scanner.

## Layout

- `logs/YYYY-WW.md` — one diff log per ISO week (e.g. `2026-19.md`)
- `logs/index.md` — auto-rebuilt index of all logs
- `state.json` — last-seen GUIDs per source, used by the scanner to compute deltas

Logs are designed for **append-only** writes. The monthly synthesizer reads
the last 4 logs, distills topic-level changes, and updates `../topics/*.md`.

## Manual scan

```bash
cd anthropic-intelligence
pip install -r scripts/requirements.txt
python scripts/fetch_sources.py --output monitoring/logs/$(date -u +%Y-%V).md
```
