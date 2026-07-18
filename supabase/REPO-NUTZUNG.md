# Supabase-Nutzung ueber alle Repositories - Landkarte

**Stand:** 2026-07-18 (Cross-Repo-Recherche ueber 26 lokal geklonte Repos + GitHub-Checks)
**Gehoert zu:** `SUPABASE-INVENTUR.md` (Live-DB-Inventur vom selben Tag)
**Projekt:** `hdxmswteiesvcwqdgpwm` - EINE geteilte Instanz fuer alles.

## Wer nutzt die Supabase AKTIV (echter Verbindungscode)

| Repo | Wie | Tabellen |
|------|-----|----------|
| security-scanner-laravel | Laravel pgsql direkt (ADR-0017) | findings, cve_entries, vulnerability_feeds, patterns, scans, 68 Migrations |
| claude-config | Python-REST-Tools + 2 GitHub-Workflows (Plan-Sync, Seiten-Inventar-Import) | scores, snapshots, idea_scores (+Embeddings), seiten_inventar, goals, Schema planning |
| agenten-systeme (pl_sets) | Python-REST-Client (supabase_client.py) | titel_pool, planetentoene, learnings, learnings_v2 |
| projekt-board | JS-fetch mit Anon-Key (hartcodiert) | idea_scores (Schema planning, lesen+schreiben) |
| quality-system | sync_seminars.py + Cron-Workflow | seminars |
| zentrale | Taeglicher Backup-Workflow | planetentoene, titel_pool, learnings, scores, snapshots, tasks, learnings_v2 |
| unified-agent-system | .env-Config + affiliate-Schema-SQL | affiliate_projects, articles, affiliate_links, media |
| sf-analyse (extern, GitHub) | scripts/import_seiten_inventar.py erzeugt das Inventar-JSON | seiten_inventar (Quelle: pages.csv 2,1 MB + keywords.csv 1,8 MB in data/processed/) |

## Wer hat Supabase GEPLANT (Doku/ADR, kein Code)

website-audit (wa_projects/wa_pages), Gstack-, biokleidung, engineering-principles
(ADR-0009 Three-Layer-Memory, knowledge_atoms), schnittstellen-doku (RFP mit
VECTOR-Spalten), shop-tuner-dokumentation (knowledge_atoms bi-temporal, E-15 offen),
agent-templates, knowledge (Inventur + Konsolidierungsplan).

## Nur beilaeufig erwaehnt / kein Treffer

Erwaehnt: weboffice, adk-agents, llms-txt-geo, security-monitoring.
Kein Treffer: content-engine (Repo komplett leer!), gambio-modul-content,
klangschalen-analyse, life-design-app, profihost-server, qigong-app.

## Kernmuster und Risiken

1. **Eine geteilte Instanz, 5 Anwendungs-Bloecke, kein Owner-Konzept.** Jedes Repo
   schreibt mit handgeschriebenen REST-Aufrufen (urllib/fetch), nirgends der
   offizielle Supabase-Client. Kein Repo kennt die Tabellen der anderen.
2. **knowledge_atoms wird von DREI Repos geplant** (engineering-principles,
   shop-tuner-dokumentation, unified-agent-system hat sogar 69 Atoms lokal in
   SQLite im KB MCP Server) - aber die Live-Tabelle ist leer. Das Wissen existiert,
   nur nicht am verabredeten Ort.
3. **projekt-board hat Anon-Key + URL hartcodiert im Frontend-Code** - pruefen ob
   RLS fuer planning.idea_scores schreibgeschuetzt genug ist.
4. **Doppel-Tracking offen** (OFFENE-AUFGABEN.md vs. planning.idea_scores,
   MUST seit 2026-06-10 ueberfaellig): Aufgaben leben an zwei Orten.
5. **Screaming-Frog-Kette funktioniert und ist versioniert:**
   sf-analyse (pages.csv/keywords.csv) -> seiten-inventar.json (claude-config,
   1,4 MB) -> GitHub-Workflow -> Supabase seiten_inventar (2.243 Zeilen, verifiziert).
   Frank kann sich darauf verlassen - nichts ist verloren.

## Stand der relevanten Plaene (2026-07-18)

| Plan | Status | Kern |
|------|--------|------|
| system-luecken-und-seiten-inventar (= floating-baking-conway, Baustufe 1) | ERLEDIGT (Count 2.243 verifiziert) | Seiten-Inventar in Supabase |
| klangschalenwissen-knowledge-base | IN_ARBEIT (Deadline 2026-07-15 UEBERSCHRITTEN) | 302 Atome extrahiert, 273 in idea_scores, offen: C.6 HWG-Check, C.7 Veroeffentlichung |
| webseiten-aufarbeitung-sound-spirit | AKTIV (Deadline 2026-08-31) | 5 Spuren, naechster Schritt Spur A.1 Domain-Liste |
| sound-spirit-redesign-master | AKTIV | G2 Top-10-Migration bis 2026-07-15 (pruefen), G4 alle 112 Seiten bis 2026-09-30 |
| Knowledge Base mit Graphiti | OFFEN (MUST seit 2026-05-22) | Entscheidung Graph-Substrat steht aus |

## Doku-Drift (gefunden 2026-07-18)

- STATUS.md-Staende vielfach aelter als letzte Commits (z.B. security-scanner:
  STATUS 2026-06-08, Commit 2026-07-16; claude-config: STATUS 2026-05-24).
- content-engine in PROJECT-REGISTRY.yaml als "active" gefuehrt, ist aber leer.
- CLAUDE.md agenten-systeme: Embedding-Modell und Postgres-Version stimmen nicht
  mit der Live-DB ueberein (siehe SUPABASE-INVENTUR.md).
