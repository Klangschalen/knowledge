---
topic: output-formats-html-vs-markdown
status: draft
last_synthesized: 2026-05-12
first_published: 2026-05-12
related:
  - claude-code
  - prompting
  - tool-use
  - content-engine
sources_consulted:
  - id: thariq-x-original
    name: "Thariq Shihipar — 'Using Claude Code: The Unreasonable Effectiveness of HTML' (X, May 8 2026)"
    url: https://twitter.com/trq212/status/2052809885763747935
    fetched: 2026-05-12
    status: unreachable-during-research
  - id: thariq-examples
    name: "Thariq — 20 HTML example artifacts"
    url: https://thariqs.github.io/html-effectiveness/
    fetched: 2026-05-12
  - id: simon-willison-commentary
    name: "Simon Willison — 'Using Claude Code: The Unreasonable Effectiveness of HTML' (link blog)"
    url: https://simonwillison.net/2026/May/8/unreasonable-effectiveness-of-html/
    fetched: 2026-05-12
  - id: pasquale-deep-dive
    name: "Pasquale Pillitteri — 'HTML vs Markdown in Claude Code: Why Anthropic's Thariq Changed the Default'"
    url: https://pasqualepillitteri.it/en/news/2243/html-vs-markdown-claude-code-thariq-anthropic
    fetched: 2026-05-12
  - id: kurtis-counter
    name: "Kurtis Redux — 'The Unreasonable Ineffectiveness of HTML' (counter-piece)"
    url: https://kurtis-redux.medium.com/the-unreasonable-ineffectiveness-of-html-5bd01ae1e879
    fetched: 2026-05-12
  - id: uxhack-substack
    name: "UX Hack — 'Markdown is Dead? Why Claude is Pivoting back to HTML'"
    url: https://uxhack.substack.com/p/markdown-is-dead-why-claude-is-pivoting
    fetched: 2026-05-12
  - id: seo-suedwest-de
    name: "SEO Südwest — Markdown-Files für KI-Optimierung (DE perspective on related question)"
    url: https://www.seo-suedwest.de/10654-wie-sinnvoll-sind-markdown-files-fuer-die-ki-optimierung.html
    fetched: 2026-05-12
  - id: dogum-html-artifacts-skill
    name: "dogum/html-artifacts — Claude skill for HTML artifacts (community)"
    url: https://github.com/dogum/html-artifacts
    fetched: 2026-05-12
---

# HTML vs Markdown as Claude output format (May 2026)

## TL;DR

- On **May 8, 2026** Thariq Shihipar (Anthropic, Claude Code team) published *"Using Claude Code: The Unreasonable Effectiveness of HTML"* on X. Within 16 hours: ~4.4M views.
- His claim: **HTML is the format Anthropic itself is increasingly defaulting to** for plans, code reviews, design systems, reports — wherever the output is meant to be *read* rather than further processed by tooling.
- Cost: HTML generation consumes **2–4× more output tokens** than Markdown for the same content. On Opus 4.7 (1M context) that's still <1% of context, ~€0.08 per detailed artifact.
- Markdown is **not dead**. There is a clean carve-out: READMEs, Slack/Discord snippets, LLM-to-LLM, RAG corpora, plain-text pipelines, anything humans need to edit by hand.
- For **our systems**: switch read-only, presentation-grade outputs (plans, reports, code reviews, dashboards, content-engine drafts) to HTML. Keep agent-to-agent, indexed, and edited-by-human outputs in Markdown.

## The thesis (Thariq, paraphrased)

> "I've started preferring HTML as an output format instead of Markdown and increasingly see this being used by others on the Claude Code team, this is why. … As agents have become more and more powerful, I have felt that Markdown has become a restricting format."
> — quoted via Threads / Glenn Gabe ([source](https://www.threads.com/@glenngabe/post/DYNbPjOkeA-/from-an-anthropic-engineer-html-beats-markdown-an-anthropic-engineer-argues))

Five arguments Thariq makes:

1. **Information density** — HTML embeds tables, SVG, CSS, JS, interactions in one file. Markdown needs external workarounds.
2. **Readability past ~100 lines** — Markdown files become "effectively unreadable"; HTML supports tabs, collapsibles, responsive layout.
3. **Sharing convenience** — HTML renders natively in any browser. Markdown needs an editor or converter.
4. **Two-way interaction** — HTML enables sliders, knobs, buttons. Documents become exploratory tools, not static dumps.
5. **Joy factor** — well-crafted HTML is more pleasant to read than "Markdown brackets."

Simon Willison ([link blog](https://simonwillison.net/2026/May/8/unreasonable-effectiveness-of-html/)) called the piece "thought-provoking" and said he'll "experiment more with rich HTML explanations in response to ad-hoc prompts" — a notable shift for someone whose three-year default was Markdown.

## Token economics (measured)

From Pasquale Pillitteri's [deep dive](https://pasqualepillitteri.it/en/news/2243/html-vs-markdown-claude-code-thariq-anthropic), measuring a real PR-review task (280 modified lines, 4 files, 3 findings):

| Format | Output tokens | % of Opus 4.7 (1M) context | Approx. cost |
|---|---:|---:|---:|
| Markdown | ~1,140 | 0.11% | ~€0.017 |
| Lean HTML | ~2,760 | 0.28% | ~€0.041 |
| Full HTML (with SVG, color coding) | ~5,480 | 0.55% | ~€0.082 |

Takeaways:

- The 2–4× token premium is **real but small in absolute terms** on Opus 4.7. The historical "Markdown saves tokens" argument was rooted in tight context windows that no longer exist.
- Latency premium is the more interesting cost: 2–4× more output tokens means 2–4× generation time. Matters for interactive UX; doesn't matter for async pipelines.

## Where HTML wins (9 categories × 20 examples)

From [thariqs.github.io/html-effectiveness](https://thariqs.github.io/html-effectiveness/):

| # | Example | Category | Notable technique |
|---:|---|---|---|
| 1 | Three code approaches | Exploration | Side-by-side trade-off layout |
| 2 | Visual design directions | Design | Live rendering of layout/palette |
| 3 | Implementation plan | Planning | Mixed timeline + data-flow + risk table |
| 4 | Annotated pull request | Code review | Diff with margin notes + severity tags |
| 5 | PR writeup for reviewers | Code review | Motivation → before/after → file tour |
| 6 | Module map | Architecture | Boxes-and-arrows graph, highlighted paths |
| 7 | Living design system | Design system | Copyable swatches/tokens |
| 8 | Component variants | Design | Contact-sheet of all states |
| 9 | Animation sandbox | Design | Sliders for duration/easing |
| 10 | Clickable flow | Prototyping | 4 linked screens, interaction testing |
| 11 | SVG figure sheet | Diagrams | Inline SVG, hand-tweakable |
| 12 | Annotated flowchart | Diagrams | Clickable deploy-pipeline steps + timings |
| 13 | Arrow-key slide deck | Presentation | No export, keyboard-driven |
| 14 | How a feature works | Explainer | Tabs + code + FAQ + TL;DR |
| 15 | Concept explainer | Explainer | Live ring sim + glossary |
| 16 | Weekly status | Reporting | Color-coded timeline + small charts |
| 17 | Incident timeline | Reporting | Minute-by-minute log + checklist |
| 18 | Ticket triage board | Tooling | Drag-and-drop + markdown export |
| 19 | Feature flag editor | Tooling | Toggle deps + diff export |
| 20 | Prompt tuner | Tooling | Live re-render on slot edits |

Note how many of these are **internal tooling artifacts**, not customer deliverables — i.e. exactly the kind of outputs *we* generate constantly across `klangschalen/projekt-board`, `quality-system`, `security-monitoring`, `weboffice`.

## Where Markdown still wins

From Pasquale's piece, cross-checked against the Kurtis Redux [counter-piece](https://kurtis-redux.medium.com/the-unreasonable-ineffectiveness-of-html-5bd01ae1e879):

- **Repository READMEs** — GitHub/GitLab render Markdown natively; HTML breaks collaborative editing and PR diffs.
- **Slack / Discord / Notion snippets** — code fences and basic Markdown are universal.
- **LLM-to-LLM and RAG corpora** — downstream parsers prefer Markdown; HTML adds noise to indexing.
- **Long git-history files / specs that get hand-edited** — "If it is a spec sheet of something complex, I want to be able to go in and edit what was produced. With an HTML document, that is much harder" (tmhrtly, HN, quoted in Pasquale).
- **Personal memos** — regeneration cost > value.
- **Email / RSS / newsletters** — mail-client HTML rendering is famously unpredictable.

## Counter-arguments worth taking seriously

1. **Security** (Kurtis Redux): "Running unvetted, AI-generated JS risks XSS or local data leaks." Real risk for HTML artifacts that include `<script>`. Mitigation: open in sandboxed contexts (Claude artifact iframe, isolated browser tab), strip `<script>` for any artifact destined for shared infra.
2. **Reviewability** (Kurtis Redux + HN): HTML diffs are noisier than Markdown diffs. Mitigation: store the *generating prompt* alongside the artifact and treat the prompt as the canonical reviewable unit.
3. **Token / ecosystem lock-in** (ryandsilva, HN): higher token consumption may quietly favor Anthropic's pricing. Worth tracking but doesn't change the per-task math for us at our volume.
4. **Format-agnostic point** (Planktonne, HN): "The real issue is bloated content, not format." Useful gut-check: if a Markdown report would have been short and clear, an HTML version that adds chrome adds nothing.

## Implications for our systems

### Agents & Claude Code (klangschalen/unified-agent-system, claude-config, agent-templates)

- **Add an `output_format` switch** to agent prompts: `markdown` (default for piped output) vs `html-artifact` (default for human review).
- Skill candidate: `/html-review` — wraps a code-review request to force the HTML-artifact format with Thariq's annotated-diff template. We can adapt [dogum/html-artifacts](https://github.com/dogum/html-artifacts).
- Update `klangschalen/engineering-principles` to codify when each agent should produce HTML vs Markdown.

### Content engine (klangschalen/content-engine, gambio-modul-content)

- Pipeline product texts: **stay Markdown** (RAG-indexed, edited downstream).
- One-off briefs, campaign concepts, audit reports: **switch to HTML artifacts** — better client deliverables, fewer round-trips.
- Sound-Spirit strategic texts (per existing skill): **HTML for client-facing outputs**, Markdown for internal drafts that flow into other systems.

### Knowledge & docs (klangschalen/knowledge, schnittstellen-doku, engineering-principles)

- KB articles (this repo): **stay Markdown**. They're indexed, diffed, edited by humans and other agents.
- One-off internal reports (audits, post-mortems): **HTML artifact** archived alongside the Markdown summary.

### Dashboards (klangschalen/security-scanner-laravel, life-design-app, security-monitoring — anything Filament)

- Filament widgets already produce HTML. The shift is upstream: when Claude *generates* widget content, prompt it for `html-artifact`-formatted output, then strip to inner body and inject. Cleaner than the current "Markdown → marked.js → inject" path.

### Quality / review (klangschalen/quality-system)

- Code-review outputs: **HTML artifact** with Thariq's annotated-diff template.
- Lint/check pipeline reports: **stay Markdown** (consumed by CI parsers).

## Concrete prompt templates

From Thariq, lightly adapted. Save these as agent templates under `klangschalen/agent-templates`:

### `agent-templates/html-artifact/code-review.md`

```
Help me review this PR by creating an HTML artifact that describes it.
I am not familiar with the {component} logic: focus the analysis there.
Render the actual diff with inline margin annotations, color-code findings
by severity (info/warn/error), and add whatever you need to convey the
concept clearly. Self-contained HTML, no external assets, no <script>.
```

### `agent-templates/html-artifact/option-comparison.md`

```
Generate {N} markedly different approaches to {problem}. Vary layout, tone,
and information density. Show them in a single HTML file in a grid so I can
compare them side by side. Label each one with the trade-off it is making.
```

### `agent-templates/html-artifact/concept-explainer.md`

```
I do not fully understand how {subsystem} works. Read the relevant code
and produce an HTML explainer page: a {core-concept} flow diagram, the 3–4
key code snippets annotated, and a "gotchas" section at the bottom.
Optimize it for a one-time read. No <script>, self-contained.
```

## Action items

- [ ] Add `output_format: markdown | html-artifact` to base agent prompt spec in `klangschalen/unified-agent-system`.
- [ ] Create the three prompt templates above under `klangschalen/agent-templates/html-artifact/`.
- [ ] Codify the carve-out rules (README/Slack/LLM-to-LLM = Markdown) in `klangschalen/engineering-principles`.
- [ ] Evaluate `dogum/html-artifacts` skill for adoption in `klangschalen/claude-config`.
- [ ] Switch Sound-Spirit client-facing outputs to HTML artifacts in `klangschalen/content-engine`.
- [ ] Re-fetch Thariq's original X post when rate limits clear; cross-check token economics against own measurements on Opus 4.7.
- [ ] Monthly synthesis: watch for an official Anthropic engineering blog post that supersedes Thariq's personal X post.

## Open questions

- Does the HTML preference extend to **input** (system prompts, RAG context) or only output? SEO Südwest's parallel piece suggests the same logic ("engines understand HTML already") may apply to inputs.
- Are there measured **task-quality** gains, not just presentation gains, from HTML outputs? Joe Njenga's Medium piece [claims yes](https://medium.com/@joe.njenga/anthropic-engineer-just-killed-markdown-as-ai-output-i-tested-his-html-in-claude-code-hes-right-71816cf8e414) but the public excerpt does not include his methodology. Track for next synthesis.
- How does Claude Code's web/desktop client handle HTML artifacts vs the CLI? Different UX surfaces may need different defaults.
