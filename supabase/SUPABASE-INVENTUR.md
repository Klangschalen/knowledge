# Supabase-Inventur - sound-spirit Projekt

**Stand:** 2026-07-18 (Live-Auslesung via Supabase MCP, keine Vermutungen)
**Projekt:** `hdxmswteiesvcwqdgpwm` (eu-central-1, Postgres 17.6, Status ACTIVE_HEALTHY)
**Angelegt:** 2026-01-09

## Kernbefund in einem Satz

Die Supabase ist KEINE Knowledge Base, sondern eine geteilte Datenbank von
mindestens 5 verschiedenen Anwendungen - und der eigentlich dafuer gebaute
Wissens-Kern (`knowledge_atoms`) ist LEER (0 Zeilen).

## Die 5 Anwendungs-Bloecke (85 Tabellen in `public`)

### 1. Security-Scanner (Laravel) - GROESSTER Block, aktiv
| Tabelle | Zeilen |
|---------|--------|
| findings | 6.229 |
| vulnerability_feeds | 1.558 |
| cve_entries | 464 |
| patterns | 53 |
| software_versions | 48 |
| vulnerable_functions | 68 |
| taint_flows | 26 |
| scans / scanned_files / scan_history | 1 / 0 / 0 |

Dazu Laravel-Standard: jobs, cache, sessions, users (alle leer), migrations (68).

### 2. Content-Wissen (der eigentliche KB-Bestand) - GUT GEFUELLT
| Tabelle | Zeilen | Inhalt |
|---------|--------|--------|
| konzepte | 3.991 | Pain/Solution/Benefit-Bausteine je Ton (marketing_stufe 2.132, zugangsweise 1.053, charakter 377, innere_ebene 377, zielgruppe 52), alle aktiv |
| titel_pool | 2.332 | Generierte Titel mit HWG-Score, Qualitaets-Score, human_approved |
| seiten_inventar | 2.243 | ALLE Seiten von sound-spirit.de mit Typ/Keyword/GSC-Baseline (produkt 1.425, sonstig 663, info 142, trend 8, kategorie 5) - Status ALLE "offen" |
| learnings | 1.121 | Regel/Grund/Ton aus Gates |
| text_spinning + sections | 485 + 21 | Textbausteine Klang-/Planetenschale |
| learnings_v2 | 70 | Zentrale Fehler-DB (ersetzt feedback_*.md) |
| planetentoene | 26 | 50+ Felder je Ton (Hz, Chakra, Emotionen, Keymessages) - ABER: daten_verifiziert = false bei ALLEN 26 |
| seminars | 19 | Termine von der Live-Terminseite |
| settext_sets | 9 | Set-Erfassungen mit Gate-Report |

### 3. Agenten-Infrastruktur - ANGELEGT, FAST LEER
agent_sessions/messages/memories (je 1), agent_trace_spans (2),
agent_vector_memories (59, Modell nomic-embed-text, 768 Dim),
agent_prompt_* / agent_intents / claude_sessions (0).

### 4. Ideen / Quiz / Cashcow - TEILWEISE GEFUELLT
idea_evaluations (206), idea_scores (46), idea_tags (18), idea_categories (7),
service_designs (21), cashcow_categories (4), activity_log (118).
Alle quiz_*- und mapping-Tabellen: 0.

### 5. Affiliate (biokleidung) + Projekt-Management - ANGELEGT, LEER
affiliate_projects (1), articles/media/affiliate_links (0),
sprints/projects/team_members/assignments/milestones (0),
scores (40) + snapshots (18) = website-audit.

## Die 4 kritischen Luecken

1. **`knowledge_atoms` ist leer (0 Zeilen).** Die Tabelle ist fertig designt
   (knowledge_tier, review-Zyklus, confidence_score, embedding vector) - genau
   das Schema, das die neue Seiten-Strategie braucht. Es fehlt nur die Befuellung.
2. **Keine Embeddings auf dem Content.** pgvector 0.8.0 ist installiert, aber nur
   59 Vektoren existieren (Agent-Memories). konzepte, seiten_inventar,
   planetentoene: KEINE Vektorspalte, keine semantische Suche moeglich.
3. **planetentoene komplett unverifiziert.** Alle 26 Zeilen daten_verifiziert=false.
   Die SSoT-Regel (Fakten NUR aus planetentone.csv) ist damit in der DB nicht abgesichert.
4. **Doku-Luecke = dieses Problem.** knowledge_documents (7 Zeilen) ist nur
   Datei-Metadata des Security-Scanners, keine Wissensinhalte. Diese Inventur
   ist die erste Gesamt-Dokumentation der DB.

## Abweichungen von der bisherigen Doku (CLAUDE.md-Drift)

| Behauptung in CLAUDE.md | Realitaet in der DB |
|--------------------------|---------------------|
| "Embeddings: text-embedding-004, 768 Dim" (agenten-systeme) | nomic-embed-text, 768 Dim, nur 59 Vektoren |
| "PostgreSQL + pgvector 18.1 / 0.8.1" | Postgres 17.6, pgvector 0.8.0 |
| "Knowledge Base fuer 720+ Klangschalen-Artikel" | knowledge_atoms leer; Artikel-Wissen liegt verteilt in konzepte/titel_pool/seiten_inventar |

## HWG-Warnhinweis

Stichprobe konzepte enthaelt Formulierungen wie "Schlafstoerungen" (pain) und
"bessere Schlafqualitaet" (benefit). Vor OEFFENTLICHER Verwendung dieser
Bausteine ist der HWG-Gate Pflicht (Tier-Kennzeichnung fehlt in konzepte).

## Empfohlener Loesungsweg (Konsolidierung statt Neubau)

1. Diese Inventur = SSoT fuer den DB-Aufbau (dieses Dokument, bei Aenderungen fortschreiben).
2. `knowledge_atoms` aus Bestandsquellen befuellen (planetentoene, konzepte,
   learnings_v2) - mit knowledge_tier (HWG 1/2/3) und Quelle je Atom.
3. Einheitliches Embedding-Modell festlegen und alle Atoms vektorisieren
   (Entscheidung noetig: nomic-embed-text weiterfuehren oder wechseln).
4. Verknuepfung `seiten_inventar` zu `knowledge_atoms` bauen: welche Seite
   braucht welches Wissen. Damit wird "jede Seite bekommt umfangreiche
   Informationen" abfragbar statt haendisch.
5. planetentoene gegen planetentone.csv verifizieren und daten_verifiziert setzen.
