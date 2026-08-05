# Changelog

## 2026-08-05 - Zentrales Claude-Plugin aktiviert (Konsolidierung Phase 1)

### Added
- `.claude/settings.json`: Marketplace `sound-spirit` (Klangschalen/claude-config)
  registriert und Plugin `sound-spirit-core` aktiviert. Textpruefung laeuft ab jetzt
  ueber den zentralen Skill `/text-check` (HWG aus Supabase-SSoT + Cialdini) statt
  ueber repo-lokale Kopien. Details: claude-config docs/KONSOLIDIERUNG-2026-08.md

Alle nennenswerten Änderungen an diesem Projekt werden in dieser Datei dokumentiert.

Das Format basiert auf [Keep a Changelog](https://keepachangelog.com/de/1.1.0/),
und dieses Projekt folgt [Semantic Versioning](https://semver.org/lang/de/).

## [Unreleased]

### Geändert

- geo/2026-06-19-ai-overviews-control-sota.md: Primaerquelle Milan 2026 (@SearchStefano,
  Google First-Party) nachgetragen, 403-/Offen-Status aufgeloest; Kernaussagen um Google-
  First-Party ergaenzt (Commodity-Test, Original-Source, Schema-Kontext-Layer, Loyalty-Schema,
  Page-vs-Site); Verweis auf GEO-001..022. Effektzahlen als Sekundaer-Recherche markiert.

### Hinzugefügt

- supabase/SUPABASE-INVENTUR.md: Erste vollstaendige Live-Inventur der Supabase
  (85 Tabellen, 5 Anwendungs-Bloecke, 4 kritische Luecken, Konsolidierungs-Empfehlung).
  Beantwortet "wir wissen nicht wie die Supabase aufgebaut ist" mit belegten Zahlen
  vom 2026-07-18.
- geo/2026-06-19-ai-overviews-control-sota.md: Cross-Projekt-SOTA zu AI-Overviews-
  Kontrolle (RAG-Passagen, Zitations-Hebel, Bot-Matrix). Verweist auf website-audit
  GEO-001..014 und llms-txt-geo Primaerquelle.
- security/ssh: SOTA-Analyse SSH-Schlüssel & Rotation (für Frank, Michael, Christina) (#7)

[Unreleased]: https://github.com/Klangschalen/knowledge/commits/main
