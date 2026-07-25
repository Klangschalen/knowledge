# Sound-Spirit Systemlandkarte

**Stand:** 25. Juli 2026  
**Status:** Erster organisationsweiter Wiki-Entwurf  
**Umfang:** 37 verbundene Repositories, zentrale Dokumente, erkennbare Abhängigkeiten und öffentlich verfügbare Open-Source-Bausteine

> Dieses Dokument ist die schnelle Einstiegskarte. Es ersetzt keine technische Detaildokumentation der einzelnen Projekte. Aussagen zu undokumentierten Repositories bleiben ausdrücklich offen.

---

## 1. Das Ziel in einem Satz

Sound-Spirit braucht keine weitere Sammlung einzelner Programme, sondern eine **modulare Verkaufs-, Wissens- und Medienplattform**, die vorhandene Fachlogik bewahrt, bewährte Open-Source-Systeme integriert und alle Abläufe messbar verbindet.

## 2. Die wichtigste Entscheidung

### Selbst entwickeln

Nur das, was Sound-Spirit einzigartig macht:

- Klangschalen-, Planetenton- und Anwendungswissen
- Produkt- und Setlogik für Einzelstücke
- AFS- und Gambio-spezifische Adapter
- Sound-Spirit-Tonlage, HWG-Regeln und Qualitätsmaßstäbe
- PL-SETS, Klangmessung und fachliche Auswahlmodelle
- Verkaufslogik für Beratung, Seminare und digitale Produkte

### Nicht selbst entwickeln

Bewährte Standard-Infrastruktur:

- Workflow-Automation und iPaaS
- CRM-Grundfunktionen
- Projektmanagement-Grundfunktionen
- LLM-Gateway, Kostenkontrolle und Modellrouting
- LLM-Tracing, Prompt-Versionen und Evaluation
- Produktanalyse, Session-Replay und A/B-Tests
- Medienbibliothek, Metadaten und Freigabeabläufe
- Secret-Management
- Standard-ELT, Datenmodellierung und Monitoring

---

## 3. Zielarchitektur

```text
KANÄLE
Gambio | WordPress | Landingpages | Apps | YouTube | Meta | Google Ads | E-Mail
                                  |
                                  v
INTEGRATIONS- UND EREIGNISSCHICHT
Activepieces oder n8n | Webhooks | Queues | API-Adapter | Retry | Audit-Log
                                  |
              +-------------------+-------------------+
              |                                       |
              v                                       v
OPERATIVE PLATTFORM                          ANALYSE-PLATTFORM
Supabase/Postgres                            BigQuery
- Produkte und Unikate                       - Ads, GA4, Shop und CRM
- Personen und Organisationen                - Kampagnenleistung
- Entitäten und Beziehungen                  - Deckungsbeiträge und Kohorten
- Wissensgraph                               - Content- und SEO-Wirkung
- Dokumente und pgvector                     - Experimente
- Freigaben und Zustände                     - dbt-Modelle
              |
              v
FACHDIENSTE
- AFS-Adapter
- Gambio-Adapter
- ActiveCampaign-Adapter
- Google/Meta-Ads-Adapter
- Content- und GEO-Engine
- Medien-Pipeline
- Seminar- und Digitalprodukt-Dienste
              |
              v
KI-SCHICHT
LiteLLM-Gateway | Google ADK | Langfuse | RAG | Regeln | Human Approval
              |
              v
QUALITÄT UND BETRIEB
GitHub Actions | Quality-System | Security Scanner | OpenTelemetry | Backups
```

### Leitregel

**Supabase ist das operative Gehirn. BigQuery ist das analytische Gedächtnis.**  
Operative Datensätze werden nicht in BigQuery gepflegt. Berichte und historische Analysen werden nicht in Supabase nachgebaut.

---

## 4. Das zentrale Datenmodell

Supabase soll nicht nur Dokumente und Vektoren speichern. Es soll die Geschäftswelt von Sound-Spirit abbilden.

### Kernentitäten

- `products`, `product_units`, `product_sets`, `product_measurements`
- `planetary_tones`, `effects`, `body_regions`, `applications`
- `people`, `organizations`, `contacts`, `consents`
- `courses`, `events`, `digital_products`, `enrollments`
- `content_items`, `content_blocks`, `claims`, `sources`
- `media_assets`, `media_variants`, `usage_rights`, `approvals`
- `campaigns`, `ads`, `creative_variants`, `offers`
- `orders`, `order_items`, `customer_events`
- `knowledge_documents`, `knowledge_chunks`, `embeddings`
- `entities`, `relations` oder fachlich klar benannte Relationstabellen

### Jede wichtige Entität braucht

- stabile UUID
- Quellsystem und Quell-ID
- Zeitstempel und Version
- fachlichen Status
- Verantwortliche Person
- Herkunft und Beleg
- Freigabestatus
- Datenschutzklasse
- Änderungs- und Ereignisprotokoll

### Ereignisse als verbindende Sprache

Beispiele:

- `product.created`
- `product.updated`
- `product.sold`
- `content.approved`
- `content.published`
- `lead.created`
- `lead.tagged`
- `course.booked`
- `ad.performance_updated`
- `media.asset_approved`

Die Ereignisse lösen Workflows aus. Dadurch müssen Systeme einander nicht direkt kennen.

---

## 5. Repository-Landkarte

### A. Steuerung, Standards und Wissen

| Repository | Zweck | Einordnung | Empfehlung |
|---|---|---|---|
| `claude-config` | Produktiver Master-Hub für Regeln, Commands, Hooks und Arbeitsabläufe | Kern | Behalten; keine Fachlogik hineinziehen |
| `engineering-principles` | Zitierfähige Engineering-Lehre und wiederverwendbare Muster | Kern | Behalten; als Referenzbibliothek führen |
| `quality-system` | Verbindliche Standards, ADRs, Specs und Freigabe-Gates | Kern | Zum organisationsweiten Quality Control Plane ausbauen |
| `.github` | Wiederverwendbare Workflows und Org-Audits | Kern | Behalten; zentrale CI-Regeln erweitern |
| `repo-template` | Vorlage für neue Repositories | Kern | Manifest und Mindestdokumentation ergänzen |
| `knowledge` | Allgemeine Knowledge Base | Neu zu schärfen | Dieses Wiki aufnehmen; nicht mit Fach-Wissensgraph vermischen |
| `wissensgraph` | Lebendes Klangschalen-Fachwissen in Supabase | Fachkern | Behalten; als fachliche Source of Truth ausbauen |
| `zentrale` | Org-weite Assets, Pläne, Ausgaben und Backups | Unklar überlappend | Rolle gegenüber `quality-system`, Wiki und Projektsteuerung festziehen |
| `frank-docs` | Nicht ausreichend dokumentiert | Offen | README, Owner, Zweck und Lebenszyklus nachtragen |

### B. Agenten und KI

| Repository | Zweck | Einordnung | Empfehlung |
|---|---|---|---|
| `agenten-systeme` | Content-Pipeline, PL-SETS, Regeln und große Agentensammlung | Fachkern | Fachlogik behalten; Laufzeit entkoppeln |
| `unified-agent-system` | Konsolidiertes Agentensystem, KB-MCP und Governance | Überlappung | In klare Pakete zerlegen oder in Kernsysteme zurückführen |
| `adk-agents` | Google-ADK-Agenten und FastAPI-Dienst | Ziel-Laufzeit | Zum zentralen Agent Service machen |
| `agent-templates` | Agentenkatalog, Vorlagen und weitere ADK-Struktur | Überlappung | Vorlagen nach `repo-template`, Agenten nach `adk-agents` verschieben |
| `Gstack-` | Lösungsseiten für Gambio mit Agenten-Workflow | Produkt/Experiment | Als kontrollierten Pilot führen; nicht zum neuen Master-Hub machen |
| `llms-txt-geo` | GEO-optimierte `llms.txt` und AI-Auffindbarkeit | Fachmodul | In Content-/GEO-Pipeline integrieren |

### C. Shop, Schnittstellen und Produktdaten

| Repository | Zweck | Einordnung | Empfehlung |
|---|---|---|---|
| `weboffice` | Historisch gewachsene Shop-, AFS- und Verwaltungstools | Legacy-Kern | Strangler-Migration; nicht großflächig refaktorieren |
| `schnittstellen-doku` | Historische und aktuelle Integrationsplanung | Referenz | Aktuelle API-Verträge in maschinenlesbare Specs überführen |
| `shop-tuner-dokumentation` | Sehr gute Betriebs- und Onboarding-Dokumentation | Vorbild | Wiki-Muster organisationsweit übernehmen |
| `shop-api-test` | Einzelseiten vor/nach Änderungen messen | Kernwerkzeug | Als MESSEN-Rolle behalten |
| `gambio-modul-content` | Schema.org-Modul mit Repo/Live-Kontrolle | Produktiv | Muster „Quelle → Deploy → Live-Check“ beibehalten |
| `pl-sets` | Set-Eingabe, Produkttext-Pipeline, AFS- und Gambio-Export | Fachkern | Als eigener fachlicher Dienst stabilisieren |
| `klangschalen-analyse` | Audioanalyse und Messdaten | Fachkern | API-/JSON-Vertrag härten; Secrets und Altlasten bereinigen |
| `profihost-server` | Serverbezogene Dateien und Verbindungen | Sensibel | Keine Zugangsdaten in README; Infra-Doku und Secrets trennen |

### D. Website, SEO, GEO und Conversion

| Repository | Zweck | Einordnung | Empfehlung |
|---|---|---|---|
| `seiten-bausteine` | Eine Quelle, Generatoren, Surfaces und Quality-Gates | Architekturvorbild | Muster auf Header, Seiten, E-Mails und Medien ausweiten |
| `sf-analyse` | Website-weite Crawl- und GSC-Analyse | Kernwerkzeug | ANALYSIEREN-Rolle behalten; Ausgaben in BigQuery/Supabase registrieren |
| `website-audit` | Acht Dimensionen für Website-Qualität | Kern im Aufbau | Mit `quality-system` verzahnen; doppelte Checks vermeiden |
| `design-sound-spirit` | Nur Titel vorhanden | Offen | Zweck, Design-Tokens und Source of Truth dokumentieren |

### E. Marketing, Ads und Verkauf

| Repository | Zweck | Einordnung | Empfehlung |
|---|---|---|---|
| `content-engine` | Datengetriebene Meta-Creatives mit Compliance und Upload-Specs | Starkes Fachmodul | Auf alle Kanäle erweitern; Resultate zurück in BigQuery schreiben |
| `ads-steuerung` | Google-Ads-Berichte, BigQuery-Auswertung und Gegencheck | Fachmodul | In ein Marketing Control Center integrieren |
| `biokleidung` | Affiliate-Site-Generator | Eigenes Geschäftsprojekt | Vom Sound-Spirit-Kern trennen, Plattformbausteine gemeinsam nutzen |
| `biokleidung-site` | Nicht ausreichend dokumentierter Site-Stand | Offen | Gegen `biokleidung` abgrenzen oder archivieren |

### F. Medien und digitale Produkte

| Repository | Zweck | Einordnung | Empfehlung |
|---|---|---|---|
| `sound-spirit-bildstudio` | Bildstil, Erzeugung, Prüfung und Medienverwaltung | Kern im Aufbau | Zu einer kanalübergreifenden Media Factory erweitern |
| `qigong-app` | Offline-PWA, Bildgenerierung, Versionierung und Verifier-Loops | Produkt/Innovationslabor | Wiederverwendbare Medien- und Verifier-Komponenten extrahieren |
| `life-design-app` | Nicht ausreichend dokumentiert | Offen | Zweck und Bezug zu digitalen Produkten klären |

### G. Sicherheit und Betrieb

| Repository | Zweck | Einordnung | Empfehlung |
|---|---|---|---|
| `security-scanner-laravel` | Cloudbasierte SCA/SAST/DAST- und Live-Prüfungen | Kern | Als zentrale Security Control Plane behalten |
| `security-monitoring` | Schlanke Übergangslösung für Live-Prüfungen | Doppelung | Funktionsvergleich, danach in Scanner integrieren und archivieren |

### H. Projektsteuerung

| Repository | Zweck | Einordnung | Empfehlung |
|---|---|---|---|
| `projekt-board` | Einfaches React-Kanban mit LocalStorage | Prototyp | Nicht zum Firmen-PM ausbauen; GitHub Projects oder fertiges PM-System nutzen |

---

## 6. Offizielle Plattformrollen

Die bereits erkennbare Vierertrennung wird verbindlich:

| Rolle | Repository | Verantwortet |
|---|---|---|
| **STANDARDS** | `quality-system` | Soll, ADRs, Specs, Freigaberegeln |
| **BAUEN** | `seiten-bausteine` und fachliche Generatoren | Versionierte Quellen und Generatoren |
| **MESSEN** | `shop-api-test` | Vorher/Nachher, Browser, Performance, Schema |
| **ANALYSIEREN** | `sf-analyse` und `website-audit` | Website-weite Befunde, Priorisierung, Trends |

Ergänzt werden zwei weitere Rollen:

| Rolle | Zielsystem | Verantwortet |
|---|---|---|
| **INTEGRIEREN** | Activepieces oder n8n + eigene Adapter | Workflows, Webhooks, Retries und Audit |
| **LERNEN** | BigQuery + dbt + Langfuse/PostHog | Wirkung, Kosten, Qualität und Experimente |

---

## 7. Open-Source-Radar

Sternzahlen sind nur ein Signal. Gewichtet werden zusätzlich Lizenz, Aktivität, Integrationsbreite, Datenhoheit und ersetzte Eigenentwicklung.

### Sofort prüfen

| Projekt | Einsatz bei Sound-Spirit | Warum relevant | Entscheidung |
|---|---|---|---|
| `activepieces/activepieces` | CRM-, Ads-, Shop- und Freigabe-Workflows | Self-hosted, Human-in-the-loop, eigene Integrationen leicht baubar | **Pilot neben n8n-Vergleich** |
| `n8n-io/n8n` | Breite Workflow-Automation | Sehr großes Ökosystem und viele Integrationen; Lizenz für internen Einsatz prüfen | **Referenz und Vergleichssieger prüfen** |
| `BerriAI/litellm` | Zentrales LLM-Gateway | Ein API-Format, Routing, Kosten, Limits, Logging und Fallbacks | **Übernehmen** |
| `langfuse/langfuse` | KI-Tracing, Prompt-Versionen und Evaluation | Verhindert blinde Agenten- und Textpipelines | **Übernehmen** |
| `PostHog/posthog` | Produktanalyse, Session-Replay, Feature Flags und Experimente | Verbindet digitale Produkte, Shop-UX und Conversion | **Pilot für neue Oberflächen** |
| `growthbook/growthbook` | Warehouse-native A/B-Tests mit BigQuery | Gut für Landingpages, Angebote und Content-Varianten | **Später, falls PostHog nicht genügt** |
| `Infisical/infisical` | Secrets und Schlüsselrotation | Ersetzt Schlüssel in Dateien und lokalen `.env`-Silos | **Dringend prüfen** |
| `directus/directus` | Daten- und Medienoberfläche auf SQL | Schnell nutzbare Admin-UI, Assets, Rollen und Workflows | **Pilot für Medien und redaktionelle Daten** |

### Beobachten und Muster übernehmen

| Projekt | Nutzen | Grenze |
|---|---|---|
| `NousResearch/hermes-agent` | Lernschleifen, Skills aus Erfahrung, persistentes Gedächtnis, Modellfreiheit | Nicht als Ersatz für eure fachliche Plattform übernehmen; Architektur und Lernmuster studieren |
| `garrytan/gstack` | Klarer Agenten-Workflow für Planung und Umsetzung | Nur als Entwicklungs-Harness, nicht als Geschäftssystem |
| `dbt-labs/dbt-core` | Versionierte BigQuery-Modelle und Tests | Erst sinnvoll, sobald gemeinsame Analytics-Modelle definiert sind |
| `airbytehq/airbyte` | Große ELT-Connector-Bibliothek | Für kleine Datenmengen möglicherweise zu schwer; gegen Activepieces prüfen |
| `meilisearch/meilisearch` | Schnelle Shop- und Wissenssuche | Erst nach sauberem Produkt- und Rechte-Modell einsetzen |
| `open-telemetry/opentelemetry-collector` | Einheitliche technische Telemetrie | Braucht ein klares Betriebsziel und Backend |
| `remotion-dev/remotion` | Programmgesteuerte Videoerzeugung | Ideal für wiederkehrende Formate, nicht für jedes kreative Video |
| `Comfy-Org/ComfyUI` | Reproduzierbare Bild- und Video-Workflows | Betrieb und Modelle erfordern klare Hardware- und Rechteplanung |

### Nicht durch Sterne täuschen lassen

- Große Repositories können für ein kleines Team zu schwer sein.
- Source-available ist nicht automatisch uneingeschränkt Open Source.
- Ein Tool ohne klaren Owner erzeugt neue Pflege statt Entlastung.
- Ein Connector ersetzt keinen stabilen Datenvertrag.
- Ein Agenten-Framework ersetzt keine Qualitätsmessung.

---

## 8. Medienplattform

`sound-spirit-bildstudio` wird zur **Sound-Spirit Media Factory**.

### Benötigte Pipeline

```text
Briefing
  -> Produkt-/Wissensdaten laden
  -> Format und Kanal wählen
  -> Bild, Video oder Skript erzeugen
  -> Marken-, Anatomie-, Rechts- und Qualitätsprüfung
  -> menschliche Freigabe
  -> Varianten und Formate rendern
  -> Medienbibliothek speichern
  -> Shop, Website, YouTube und Social ausspielen
  -> Leistung nach BigQuery zurückführen
```

### Medien-Metadaten

Jedes Asset erhält:

- eindeutige ID
- Produkt-, Thema- und Kampagnenbezug
- Urheber und Erzeugungsweg
- Modell, Prompt und Seed, soweit sinnvoll
- Nutzungsrechte und Ablaufdatum
- C2PA-/KI-Kennzeichnung
- Freigabestatus
- Alt-Text und Untertitel
- Kanalvarianten und Seitenverhältnis
- Leistungsdaten

### Video- und YouTube-Bausteine

- Skript aus echten Produkt- und Wissensdaten
- Shotlist und B-Roll-Liste
- Untertitel und Kapitel
- Titel-, Thumbnail- und Beschreibungstests
- Hochkant-, Quer- und Kurzfassungen
- Upload-Paket statt unkontrolliertem Auto-Publishing
- Performance-Rückfluss nach BigQuery

---

## 9. Verkaufs- und Marketingkreislauf

```text
BigQuery erkennt Chance
  -> Content Engine erzeugt Varianten
  -> Quality-System prüft Marke, Recht und Fakten
  -> Mensch gibt frei
  -> Activepieces/n8n verteilt an ActiveCampaign, Meta, Google und Website
  -> PostHog/GA4/Ads messen Verhalten und Umsatz
  -> BigQuery bewertet Zielgruppe, Angebot, Creative und Kanal
  -> Gewinner fließen als belegtes Wissen nach Supabase
```

### Überverkäufe richtig aufbauen

Nicht pauschal „ähnliche Produkte“ zeigen. Empfehlungen werden aus Beziehungen gebildet:

- Produkt ergänzt Produkt
- Schale passt zu Klöppel
- Produkt passt zu Anwendung
- Seminar vertieft Produktnutzung
- Digitalprodukt bereitet Seminar vor
- Wissen beantwortet Einwand
- Kundengruppe reagiert auf Nutzenwelt

Jede Empfehlung braucht einen Grund, eine Messung und eine Begrenzung gegen unpassende Angebote.

---

## 10. Sofortige Risiken

### Kritisch

1. **Historisch eingecheckte API-Schlüssel rotieren.** Löschen aus einer aktuellen Datei reicht nicht, weil Git-Historien erhalten bleiben.
2. Secrets künftig nur aus einem Secret-Manager oder GitHub Secrets laden.
3. `profihost-server` und andere Infrastruktur-Repositories auf Zugangsdaten, IPs, Nutzernamen und Verbindungsdetails prüfen.
4. Schutzregeln und Secret-Scanning auf alle privaten Repositories ausrollen.

### Architektur

1. Vier Agenten-Repositories beanspruchen ähnliche zentrale Rollen.
2. Zwei Security-Repositories prüfen teilweise dieselben Systeme.
3. Mehrere „Zentralen“ existieren: `claude-config`, `zentrale`, `knowledge`, `quality-system`, `wissensgraph`.
4. Undokumentierte Repositories verhindern sichere Wiederverwendung.
5. Lokale Pfade und direkte Dateikopplungen erschweren Cloud- und Teamarbeit.

---

## 11. 90-Tage-Plan

### Tage 1–14: Sicherheit und Inventar

- alle betroffenen API-Schlüssel rotieren
- Secret-Historie bewerten und gegebenenfalls bereinigen
- jedes Repo mit `system-manifest.yaml` versehen
- Owner, Zweck, Status, Daten, Schnittstellen und Lebenszyklus erfassen
- undokumentierte Repositories markieren
- doppelte Security- und Agentenfunktionen vergleichen

### Tage 15–30: Plattformgrenzen

- ADR für die sechs Plattformrollen verabschieden
- Supabase-Schemata und Verantwortungen festlegen
- Ereigniskatalog v1 definieren
- API-Verträge für AFS, Gambio, ActiveCampaign, Meta, Google und BigQuery dokumentieren
- Activepieces und n8n mit drei echten Abläufen vergleichen
- LiteLLM und Langfuse als kleinen Pilot aufsetzen

### Tage 31–60: Erster durchgängiger Verkaufsfluss

Pilot:

1. Produkt oder Set kommt aus AFS.
2. Adapter schreibt kanonische Daten nach Supabase.
3. PL-SETS und Content Engine erzeugen Shop-, SEO-, E-Mail- und Anzeigenbausteine.
4. Quality-System prüft Fakten, HWG, Stil und Pflichtfelder.
5. Mensch gibt frei.
6. Workflow verteilt Inhalte.
7. BigQuery sammelt Leistung.
8. Gewinnerwissen fließt zurück in den Wissensgraph.

### Tage 61–90: Medien und Experimente

- Media-Asset-Modell und Freigabefluss einführen
- Directus oder vergleichbare Oberfläche testen
- zwei wiederkehrende Videoformate mit Remotion/FFmpeg pilotieren
- PostHog auf einer neuen Oberfläche einsetzen
- ein kontrolliertes Landingpage-Experiment durchführen
- Kosten, Zeitgewinn und Qualitätsgewinn dokumentieren

---

## 12. Prioritäten

| Maßnahme | Wirkung | Sicherheit | Aufwand | Priorität |
|---|---:|---:|---:|---|
| Schlüssel rotieren und Secret-Management einführen | 10 | 10 | 8 | **MUST** |
| Automatisches Repo-Wiki und Manifest | 9 | 9 | 8 | **MUST** |
| Agenten-Repositories konsolidieren | 9 | 8 | 6 | **MUST** |
| Integrationsschicht pilotieren | 10 | 8 | 6 | **MUST** |
| LiteLLM und Langfuse einführen | 9 | 9 | 7 | **MUST** |
| Supabase-Ereignis- und Entitätenmodell härten | 10 | 8 | 5 | **MUST** |
| Media Factory als durchgängigen Ablauf bauen | 8 | 8 | 5 | **SHOULD** |
| PostHog-Pilot | 7 | 8 | 7 | **SHOULD** |
| Eigenes Projektboard ausbauen | 3 | 7 | 4 | **WONT** |
| Komplettmigration von Gambio auf einmal | 4 | 4 | 1 | **WONT** |

---

## 13. Automatisch erzeugtes Wiki

Das Wiki soll künftig täglich aus GitHub entstehen.

### Pflichtdatei pro Repository: `system-manifest.yaml`

```yaml
name: seiten-bausteine
purpose: Zentrale Generatoren für wiederkehrende Webseiten-Bausteine
owner: Michael
business_domain: website
lifecycle: production
criticality: high
source_of_truth_for:
  - footer-source
inputs:
  - quality-system standards
outputs:
  - HTML surfaces
integrations:
  - Gambio
  - WordPress
data_stores: []
contains_personal_data: false
runbook: README.md
status_file: STATUS.md
supersedes: []
superseded_by: null
```

### Der tägliche Generator prüft

- Zweck und Owner vorhanden
- letzte Aktivität
- Default-Branch und Release
- README, STATUS, CHANGELOG und SECURITY vorhanden
- offene Blocker und Pull Requests
- verwendete Sprachen und Frameworks
- Datenbanken und externe Dienste
- Source-of-Truth-Zuständigkeiten
- Überschneidungen mit anderen Repositories
- bekannte Secrets oder Sicherheitswarnungen
- Lifecycle: `production`, `pilot`, `legacy`, `archive`, `unknown`

### Wiki-Ansichten

1. **In einer Minute:** Was macht Sound-Spirit technisch?
2. **Nach Geschäftsbereich:** Shop, Wissen, Content, Ads, Medien, Seminare, Betrieb
3. **Nach Repository:** Zweck, Start, Owner, Inputs, Outputs, Risiken
4. **Nach Datenfluss:** Wo entstehen und landen Daten?
5. **Nach Source of Truth:** Welche Quelle entscheidet?
6. **Nach offenen Risiken:** Was blockiert oder doppelt sich?
7. **Open-Source-Radar:** übernehmen, pilotieren, beobachten, verwerfen

---

## 14. Definition of Done für neue Systeme

Ein neues System gilt erst als fertig, wenn:

- ein echter Geschäftsablauf vollständig läuft
- Owner und Vertretung feststehen
- Eingaben und Ausgaben versioniert sind
- API- oder Ereignisvertrag dokumentiert ist
- Tests und Qualitäts-Gates grün sind
- Monitoring und Fehlerweg existieren
- Secrets sicher verwaltet werden
- Datenschutz und Rechte geklärt sind
- Kosten und Nutzen messbar sind
- Wiki und Runbook aktualisiert sind
- Abschaltung oder Rückweg möglich bleibt

---

## 15. Endurteil

Sound-Spirit besitzt bereits viele wertvolle Bausteine. Das größte Potenzial liegt nicht in noch mehr Einzelprojekten. Es liegt in **klaren Plattformrollen, sicheren Schnittstellen, einer gemeinsamen Datenwelt und messbaren Lernkreisläufen**.

Die fachliche Eigenentwicklung bleibt euer Wettbewerbsvorteil. Standard-Infrastruktur wird konsequent übernommen. Jede neue Komponente muss entweder ein bestehendes System ersetzen, einen durchgängigen Geschäftsfluss schließen oder einen belegbaren Qualitätsgewinn liefern.
