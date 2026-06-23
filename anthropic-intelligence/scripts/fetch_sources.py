"""Weekly scanner for the Anthropic Intelligence pipeline.

Reads sources.yaml, fetches RSS/Atom feeds, compares against state.json,
emits a Markdown log of new entries. Sources without a feed are listed
with a manual-check note (we do not scrape arbitrary HTML).

Usage:
    python fetch_sources.py \
        --sources sources.yaml \
        --state monitoring/state.json \
        --output monitoring/logs/2026-19.md \
        --min-priority P2

Exit codes:
    0 — success (log written, even if empty)
    1 — unrecoverable error (bad config, IO failure)
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import sys
from typing import Any

import feedparser
import yaml

PRIORITY_ORDER = {"P0": 0, "P1": 1, "P2": 2}


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--sources", required=True, type=pathlib.Path)
    p.add_argument("--state", required=True, type=pathlib.Path)
    p.add_argument("--output", required=True, type=pathlib.Path)
    p.add_argument("--min-priority", default="P2", choices=PRIORITY_ORDER.keys())
    return p.parse_args()


def load_yaml(path: pathlib.Path) -> dict[str, Any]:
    with path.open() as f:
        return yaml.safe_load(f)


def load_state(path: pathlib.Path) -> dict[str, Any]:
    if not path.exists():
        return {"version": 1, "last_run": None, "sources": {}}
    with path.open() as f:
        return json.load(f)


def save_state(path: pathlib.Path, state: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w") as f:
        json.dump(state, f, indent=2, sort_keys=True)
        f.write("\n")


def scan_feed(source: dict[str, Any], seen: set[str]) -> list[dict[str, Any]]:
    feed = feedparser.parse(source["feed"])
    new_entries = []
    for entry in feed.entries:
        guid = entry.get("id") or entry.get("link")
        if not guid or guid in seen:
            continue
        new_entries.append({
            "guid": guid,
            "title": entry.get("title", "(no title)"),
            "link": entry.get("link", ""),
            "published": entry.get("published", entry.get("updated", "")),
            "summary": entry.get("summary", "")[:500],
        })
    return new_entries


def render_log(
    run_started: dt.datetime,
    by_source: dict[str, list[dict[str, Any]]],
    sources_by_id: dict[str, dict[str, Any]],
    manual_check: list[str],
) -> str:
    lines = [
        f"# Weekly scan {run_started.strftime('%Y-W%V')}",
        "",
        f"_Run started: {run_started.isoformat()}_",
        "",
    ]
    total = sum(len(v) for v in by_source.values())
    lines.append(f"**{total} new entries** across {len(by_source)} sources with deltas.")
    lines.append("")

    for source_id, entries in sorted(by_source.items()):
        if not entries:
            continue
        meta = sources_by_id[source_id]
        lines.append(f"## {meta['name']}  ({meta['priority']} · {meta['kind']})")
        lines.append(f"Source: {meta['url']}")
        lines.append("")
        for e in entries:
            lines.append(f"- **{e['title']}**")
            if e["published"]:
                lines.append(f"  _{e['published']}_")
            if e["link"]:
                lines.append(f"  <{e['link']}>")
            if e["summary"]:
                summary = e["summary"].replace("\n", " ").strip()
                lines.append(f"  > {summary}")
            lines.append("")

    if manual_check:
        lines.append("## Manual-check sources (no feed)")
        lines.append("")
        for sid in manual_check:
            meta = sources_by_id[sid]
            lines.append(f"- [{meta['name']}]({meta['url']}) — {meta['priority']} · {meta['kind']}")
        lines.append("")

    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    config = load_yaml(args.sources)
    state = load_state(args.state)

    min_priority = PRIORITY_ORDER[args.min_priority]
    sources = config["sources"]
    sources_by_id = {s["id"]: s for s in sources}

    run_started = dt.datetime.now(dt.timezone.utc)
    by_source: dict[str, list[dict[str, Any]]] = {}
    manual_check: list[str] = []

    for source in sources:
        if PRIORITY_ORDER[source["priority"]] > min_priority:
            continue
        if not source.get("feed"):
            manual_check.append(source["id"])
            continue

        seen_guids = set(state["sources"].get(source["id"], {}).get("seen", []))
        try:
            new_entries = scan_feed(source, seen_guids)
        except Exception as e:
            print(f"warn: failed to scan {source['id']}: {e}", file=sys.stderr)
            continue

        by_source[source["id"]] = new_entries
        # Update state — keep last 200 guids per source to bound growth.
        merged = list(seen_guids) + [e["guid"] for e in new_entries]
        state["sources"][source["id"]] = {
            "seen": merged[-200:],
            "last_scanned": run_started.isoformat(),
        }

    state["last_run"] = run_started.isoformat()

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(render_log(run_started, by_source, sources_by_id, manual_check))
    save_state(args.state, state)

    total = sum(len(v) for v in by_source.values())
    print(f"wrote {args.output} — {total} new entries across {len(by_source)} sources")
    return 0


if __name__ == "__main__":
    sys.exit(main())
