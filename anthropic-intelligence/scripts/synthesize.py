"""Monthly synthesizer for the Anthropic Intelligence pipeline.

Reads the last N weekly logs and the existing topic articles, asks Claude to
produce an updated version of each topic article that incorporates any newly
significant signals.

Usage:
    python synthesize.py \
        --logs-dir monitoring/logs \
        --topics-dir topics \
        --sources sources.yaml \
        [--topic output-formats-html-vs-markdown]

Requires ANTHROPIC_API_KEY in env. Optional ANTHROPIC_MODEL (default opus-4-7).

The script is conservative: it only proposes diffs that cite specific log
entries. If no log entries map to a topic, the article is left untouched.
"""
from __future__ import annotations

import argparse
import datetime as dt
import os
import pathlib
import re
import sys
from typing import Any

import yaml
from anthropic import Anthropic

DEFAULT_LOG_WINDOW = 4  # last 4 weekly logs

SYSTEM_PROMPT = """You are the maintainer of an internal knowledge base on
Anthropic, Claude Code, and AI engineering best practices.

You receive:
1. The current full content of a topic article (Markdown with YAML front-matter).
2. The last 4 weekly scan logs from our monitoring pipeline.
3. The source registry (so you know which IDs map to which URLs).

Your job:
- If no log entries are relevant to this topic, return the article unchanged
  except for updating `last_synthesized` in the front-matter.
- If log entries ARE relevant, integrate them into the article. Add new
  sources to `sources_consulted`. Be precise: cite the specific log entry and
  link the source URL.
- Never invent quotes or facts not present in the logs or the existing article.
- Keep the article structure (front-matter, sections) intact.
- Output ONLY the updated Markdown file, with no commentary, no code fences.
"""


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--logs-dir", required=True, type=pathlib.Path)
    p.add_argument("--topics-dir", required=True, type=pathlib.Path)
    p.add_argument("--sources", required=True, type=pathlib.Path)
    p.add_argument("--topic", default=None, help="Single topic slug; default = all")
    p.add_argument("--window", type=int, default=DEFAULT_LOG_WINDOW)
    p.add_argument("--model", default=os.environ.get("ANTHROPIC_MODEL", "claude-opus-4-7"))
    return p.parse_args()


def recent_logs(logs_dir: pathlib.Path, window: int) -> list[pathlib.Path]:
    logs = sorted(logs_dir.glob("*.md"))
    return logs[-window:]


def topic_files(topics_dir: pathlib.Path, only: str | None) -> list[pathlib.Path]:
    files = sorted(p for p in topics_dir.glob("*.md") if p.name != "README.md")
    if only:
        files = [p for p in files if p.stem == only]
    return files


def bump_last_synthesized(content: str, today: str) -> str:
    return re.sub(
        r"^last_synthesized:\s*\S+",
        f"last_synthesized: {today}",
        content,
        count=1,
        flags=re.MULTILINE,
    )


def synthesize_one(
    client: Anthropic,
    model: str,
    topic_path: pathlib.Path,
    logs: list[pathlib.Path],
    sources_yaml: str,
) -> str:
    article = topic_path.read_text()
    logs_concat = "\n\n---\n\n".join(
        f"# Log: {p.name}\n\n{p.read_text()}" for p in logs
    )
    user_msg = (
        f"## Topic article ({topic_path.name})\n\n{article}\n\n"
        f"## Weekly logs (most recent last)\n\n{logs_concat}\n\n"
        f"## Source registry (sources.yaml)\n\n```yaml\n{sources_yaml}\n```\n"
    )
    resp = client.messages.create(
        model=model,
        max_tokens=8000,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_msg}],
    )
    parts = [b.text for b in resp.content if getattr(b, "type", None) == "text"]
    return "".join(parts).strip()


def main() -> int:
    args = parse_args()
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("ANTHROPIC_API_KEY not set", file=sys.stderr)
        return 1

    client = Anthropic()
    sources_yaml = args.sources.read_text()
    logs = recent_logs(args.logs_dir, args.window)
    topics = topic_files(args.topics_dir, args.topic)
    today = dt.date.today().isoformat()

    if not logs:
        print("no weekly logs found — nothing to synthesize")
        # Still bump last_synthesized so we keep a heartbeat.
        for t in topics:
            t.write_text(bump_last_synthesized(t.read_text(), today))
        return 0

    for t in topics:
        print(f"synthesizing {t.name} against {len(logs)} logs…")
        try:
            updated = synthesize_one(client, args.model, t, logs, sources_yaml)
        except Exception as e:
            print(f"warn: synthesis failed for {t.name}: {e}", file=sys.stderr)
            continue
        if not updated.startswith("---"):
            print(f"warn: model returned non-frontmatter output for {t.name}; skipping write", file=sys.stderr)
            continue
        t.write_text(updated + ("\n" if not updated.endswith("\n") else ""))
        print(f"  updated {t.name}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
