# Sound-Spirit Open-Source-Radar 2026

**Stand:** 25.07.2026  
**Zweck:** Große, reife und schnell wachsende Open-Source-Projekte finden, bewerten und gezielt in die Sound-Spirit-Systemlandschaft integrieren.

## 1. Ausgangspunkt

Die erste Recherche war zu eng. Sie betrachtete vor allem direkte Lücken in den bestehenden Repositories. Dieser Radar erweitert den Blick auf die gesamte Open-Source-Landschaft:

- Prozess- und Projektsteuerung
- interne Werkzeuge und Low-Code
- Schnittstellen und Datenflüsse
- Wissensbasis, Suche und RAG
- KI-Agenten, Modell-Gateways und Qualität
- CRM, Marketing, Support und Anzeigen
- Shop, ERP und digitale Produkte
- SEO, GEO, Crawling und Webqualität
- Bilder, Videos, YouTube und Medienverwaltung
- Betrieb, Sicherheit und Beobachtung

Das Ziel ist **nicht**, möglichst viele Programme zu installieren. Das Ziel ist, bewährte Bausteine zu finden, die eigene Entwicklung ersetzen und klare Systemgrenzen schaffen.

## 2. Quellen für den dauerhaften Radar

Diese Quellen sollen regelmäßig geprüft werden:

| Quelle | Nutzen |
|---|---|
| [GitHub Trending](https://github.com/trending) | neue und stark wachsende Projekte |
| [GitHub Topics](https://github.com/topics) | Repositories nach Fachgebiet und Sternen |
| [OSSInsight Collections](https://ossinsight.io/collections) | 100+ Fachsammlungen, Aktivität, Wachstum und historische Trends |
| [OSSInsight Trending](https://ossinsight.io/trending) | aktuelle Momentum-Signale |
| [Git Stars](https://git-stars.org/topics) | große Repositories nach Themen, Sprache und Sternen |
| [GStars](https://www.gstars.dev/) | Wachstum und Momentum statt nur Gesamtsterne |
| [GitHub Ranking](https://githubranking.com/repositories) | allgemeine Stern- und Fork-Ranglisten |
| [Awesome Selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | breit gepflegte Liste selbst hostbarer Software |
| GitHub Releases, Issues und Pull Requests | reale Pflege, Release-Takt und Community-Gesundheit |

## 3. Sterne sind nur ein Signal

Ein großes Projekt kann für Sound-Spirit unpassend, zu komplex oder lizenzrechtlich problematisch sein. Die Auswahl erfolgt deshalb nach einem 100-Punkte-Modell.

| Kriterium | Gewicht |
|---|---:|
| löst ein echtes Sound-Spirit-Problem | 20 |
| ersetzt eigene Entwicklung oder manuelle Arbeit | 15 |
| API, Webhooks, MCP oder gute Erweiterbarkeit | 15 |
| passt zu Supabase, BigQuery, PHP, Python und GitHub | 10 |
| Datenhoheit und Self-Hosting | 10 |
| Wartungsaktivität und Release-Takt | 10 |
| Lizenz und kommerzielle Nutzbarkeit | 10 |
| Sicherheits- und Betriebsreife | 5 |
| Community, Sterne und Wachstum | 5 |

**Entscheidungsklassen:**

- **A – Pilotieren:** hoher Nutzen, klare Schnittstelle, überschaubares Risiko
- **B – Evaluieren:** interessant, aber Architektur, Lizenz oder Aufwand prüfen
- **C – Beobachten:** starke Entwicklung, aber aktuell kein direkter Einsatz
- **D – Verwerfen:** überschneidet sich, ist zu schwer oder schafft neue Abhängigkeiten

## 4. Strukturprobleme: Welche Art System fehlt wirklich?

Ein Board verwaltet Aufgaben. Es stellt noch nicht sicher, dass ein Prozess korrekt abläuft.

Sound-Spirit braucht sechs getrennte Mechanismen:

| Ebene | Aufgabe | Geeignete Projekte |
|---|---|---|
| Arbeitssteuerung | Wer macht was bis wann? | Plane, OpenProject, Huly |
| strukturierte Fachverwaltung | Formulare, Entitäten, Rollen, Status | NocoBase, Appsmith, ToolJet, Budibase |
| Geschäftsprozess | feste Reihenfolge, Freigaben, Eskalationen | Flowable, Temporal, Kestra |
| Schnittstellen | Daten zwischen Systemen bewegen | Activepieces, n8n, Airbyte |
| Qualitäts-Gates | falsche Ergebnisse blockieren | GitHub Actions, Promptfoo, eigene quality-system-Gates |
| Beobachtung | Fehler, Kosten, Laufzeiten und Abweichungen sehen | Langfuse, OpenTelemetry, SigNoz, Uptime Kuma |

## 5. Empfohlener Sound-Spirit-Struktur-Stack

### 5.1 Menschliche Aufgaben: Plane

**Projekt:** [makeplane/plane](https://github.com/makeplane/plane)

Plane ist ein modernes Open-Source-System für Aufgaben, Zyklen, Dokumente, Triage und Produktarbeit. Es eignet sich besser als ein selbst gebautes LocalStorage-Kanban.

**Einsatz bei Sound-Spirit:**

- eine Aufgabe pro echter Lieferung
- klare Verantwortliche
- Abhängigkeiten und Blocker
- Freigabestatus
- Verbindung zu GitHub-Issues
- getrennte Ansichten für Frank, Michael, Christina, Julia und Marketing

**Klasse:** A – Pilotieren.

### 5.2 Fachliche Verwaltungsoberflächen: NocoBase

**Projekt:** [nocobase/nocobase](https://github.com/nocobase/nocobase)

NocoBase baut auf Datenmodellen, Rollen, Ansichten und Workflows auf. Es kann interne Oberflächen über Supabase-nahe PostgreSQL-Strukturen liefern, ohne jede Maske neu zu programmieren.

**Mögliche Module:**

- Produkt- und Unikateverwaltung
- Wissensgraph-Pflege
- Medienfreigabe
- Content-Kalender
- Anzeigen-Briefings
- Seminar- und Kursverwaltung
- Schnittstellenstatus

**Klasse:** A – Pilotieren.

### 5.3 Integrationen: Activepieces gegen n8n testen

**Projekte:**

- [activepieces/activepieces](https://github.com/activepieces/activepieces)
- [n8n-io/n8n](https://github.com/n8n-io/n8n)

**Activepieces** ist besonders interessant für Freigaben, Human-in-the-loop und agentische Abläufe. **n8n** besitzt das größere Integrations- und Vorlagen-Ökosystem.

**Pilotvergleich:**

1. Gambio-Produkt geändert
2. Daten nach Supabase spiegeln
3. Textpipeline starten
4. Qualitätsprüfung ausführen
5. Freigabe anfordern
6. ActiveCampaign aktualisieren
7. BigQuery-Ereignis schreiben
8. Fehler an Plane und E-Mail melden

**Klasse:** A – beide in einem identischen Pilotfall vergleichen.

### 5.4 Verbindliche Prozessausführung: Kestra oder Flowable

**Projekte:**

- [kestra-io/kestra](https://github.com/kestra-io/kestra)
- [flowable/flowable-engine](https://github.com/flowable/flowable-engine)
- [temporalio/temporal](https://github.com/temporalio/temporal)

**Kestra** passt gut für technische, sichtbare Daten- und Automationsabläufe. **Flowable** eignet sich für BPMN, Freigaben und nachvollziehbare Geschäftsprozesse. **Temporal** ist sehr robust, aber stärker entwicklerzentriert.

**Empfehlung:**

- Kestra für Daten-, Medien- und Contentpipelines pilotieren.
- Flowable nur testen, wenn visuelle Geschäftsprozesse mit Menschen zentral werden.
- Temporal beobachten, bis eigene Entwicklerkapazität und Betriebsreife ausreichen.

## 6. Große Longlist nach Fachgebiet

### 6.1 Projektarbeit, Wiki und Zusammenarbeit

| Projekt | Nutzen | Klasse |
|---|---|---|
| [Plane](https://github.com/makeplane/plane) | Aufgaben, Zyklen, Dokumente, Triage | A |
| [OpenProject](https://github.com/opf/openproject) | klassische Projekte, Gantt, Budgets, Workflows | B |
| [Huly](https://github.com/hcengineering/platform) | Projektarbeit, CRM, Wiki, Chat in einer Plattform | B |
| [AppFlowy](https://github.com/AppFlowy-IO/AppFlowy) | Wiki, Notion-Alternative, Aufgaben | B |
| [Vikunja](https://github.com/go-vikunja/vikunja) | schlanke Aufgabenverwaltung | C |
| [Leantime](https://github.com/Leantime/leantime) | Ziele und Projektarbeit für kleine Teams | C |
| [Focalboard](https://github.com/mattermost-community/focalboard) | Kanban und Boards | D – Plane ist stärker |
| [Backstage](https://github.com/backstage/backstage) | technischer Softwarekatalog und Entwicklerportal | B |
| [Doorstop](https://github.com/doorstop-dev/doorstop) | versionierte Anforderungen und Rückverfolgbarkeit | B |
| [Sphinx-Needs](https://github.com/useblocks/sphinx-needs) | Anforderungen, Tests und Nachweise in Doku | B |

### 6.2 Low-Code und interne Werkzeuge

| Projekt | Nutzen | Klasse |
|---|---|---|
| [NocoBase](https://github.com/nocobase/nocobase) | Datenmodelle, Rollen, Apps, Workflows | A |
| [Appsmith](https://github.com/appsmithorg/appsmith) | interne Dashboards und Admin-Oberflächen | B |
| [ToolJet](https://github.com/ToolJet/ToolJet) | interne Apps und Datenquellen | B |
| [Budibase](https://github.com/Budibase/budibase) | Apps, Automationen und Formulare | B |
| [NocoDB](https://github.com/nocodb/nocodb) | Airtable-artige Sicht auf Daten | B |
| [Teable](https://github.com/teableio/teable) | Postgres-basierte Tabellenoberfläche | B |
| [Refine](https://github.com/refinedev/refine) | Framework für eigene Admin-Oberflächen | C |

### 6.3 Workflow, Automatisierung und Ereignisse

| Projekt | Nutzen | Klasse |
|---|---|---|
| [n8n](https://github.com/n8n-io/n8n) | sehr großes Integrationsökosystem | A |
| [Activepieces](https://github.com/activepieces/activepieces) | Automationen, MCP, Human-in-the-loop | A |
| [Kestra](https://github.com/kestra-io/kestra) | deklarative Workflows und Datenpipelines | A |
| [Prefect](https://github.com/PrefectHQ/prefect) | robuste Python-Workflows | B |
| [Apache Airflow](https://github.com/apache/airflow) | etablierter Scheduler für Datenpipelines | C – für euch oft zu schwer |
| [Dagster](https://github.com/dagster-io/dagster) | Daten-Assets, Orchestrierung, Beobachtung | B |
| [Windmill](https://github.com/windmill-labs/windmill) | Skripte, Workflows und interne Apps | B |
| [Temporal](https://github.com/temporalio/temporal) | langlebige, fehlertolerante Prozesse | B |
| [Flowable](https://github.com/flowable/flowable-engine) | BPMN, CMMN und DMN | B |
| [Node-RED](https://github.com/node-red/node-red) | ereignisbasierte Low-Code-Flows | C |

### 6.4 Datenbewegung und Analyse

| Projekt | Nutzen | Klasse |
|---|---|---|
| [Airbyte](https://github.com/airbytehq/airbyte) | Daten aus APIs und Datenbanken nach BigQuery | A |
| [Meltano](https://github.com/meltano/meltano) | modulare ELT-Pipelines | B |
| [Mage](https://github.com/mage-ai/mage-ai) | ETL, Reverse ETL und Orchestrierung | B |
| [dbt-core](https://github.com/dbt-labs/dbt-core) | geprüfte Transformationen im Warehouse | A |
| [Multiwoven](https://github.com/Multiwoven/multiwoven) | Reverse ETL aus BigQuery zu Geschäftssystemen | B |
| [DuckDB](https://github.com/duckdb/duckdb) | schnelle lokale Analysen von CSV, Parquet und Daten | A |
| [ClickHouse](https://github.com/ClickHouse/ClickHouse) | große Ereignis- und Logdaten | C |
| [Metabase](https://github.com/metabase/metabase) | verständliche Business-Dashboards | A |
| [Apache Superset](https://github.com/apache/superset) | umfangreiche BI-Plattform | B |
| [PostHog](https://github.com/PostHog/posthog) | Produktanalyse, Replay, Funnels, Feature Flags | A |
| [Matomo](https://github.com/matomo-org/matomo) | selbst gehostete Webanalyse | B |
| [Plausible](https://github.com/plausible/analytics) | schlanke Webanalyse | C |
| [GrowthBook](https://github.com/growthbook/growthbook) | Experimente und Feature Flags | A |

### 6.5 Wissen, Suche und RAG

| Projekt | Nutzen | Klasse |
|---|---|---|
| [pgvector](https://github.com/pgvector/pgvector) | Vektorsuche direkt in PostgreSQL/Supabase | A – bereits passend |
| [Qdrant](https://github.com/qdrant/qdrant) | leistungsfähige Vektorsuche | B |
| [Milvus](https://github.com/milvus-io/milvus) | große Vektorbestände | C |
| [Weaviate](https://github.com/weaviate/weaviate) | Hybrid- und Vektorsuche | B |
| [Chroma](https://github.com/chroma-core/chroma) | einfache Vektorspeicherung | C |
| [Meilisearch](https://github.com/meilisearch/meilisearch) | schnelle Shop- und Wissenssuche | A |
| [Typesense](https://github.com/typesense/typesense) | fehlertolerante Produktsuche | B |
| [OpenSearch](https://github.com/opensearch-project/OpenSearch) | Suche und Analyse in großem Maßstab | C |
| [Neo4j](https://github.com/neo4j/neo4j) | klassischer Wissensgraph | B |
| [SurrealDB](https://github.com/surrealdb/surrealdb) | Multi-Model-Datenbank mit Graph-Funktionen | C |
| [FalkorDB](https://github.com/FalkorDB/FalkorDB) | Graphdatenbank für GraphRAG | C |
| [Dify](https://github.com/langgenius/dify) | KI-Anwendungen, Workflows und RAG | A |
| [RAGFlow](https://github.com/infiniflow/ragflow) | Dokumentverständnis und RAG | A |
| [AnythingLLM](https://github.com/Mintplex-Labs/anything-llm) | interne KI-Arbeitsoberfläche | B |
| [Open WebUI](https://github.com/open-webui/open-webui) | Oberfläche für lokale und externe Modelle | B |
| [LlamaIndex](https://github.com/run-llama/llama_index) | Dokumente, Agenten und Retrieval | B |
| [LangChain](https://github.com/langchain-ai/langchain) | breites Agenten- und RAG-Ökosystem | B |
| [Haystack](https://github.com/deepset-ai/haystack) | produktive Such- und RAG-Pipelines | B |
| [Cognee](https://github.com/topoteretes/cognee) | Wissensgraph und Agentengedächtnis | B |
| [mem0](https://github.com/mem0ai/mem0) | persistentes Agentengedächtnis | B |
| [memvid](https://github.com/memvid/memvid) | kompakte lokale Wissensspeicherung | C |

### 6.6 KI-Agenten, Modelle und Qualität

| Projekt | Nutzen | Klasse |
|---|---|---|
| [Google ADK](https://github.com/google/adk-python) | code-first Agenten, Evaluation und Deployment | A – passt zum Bestand |
| [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | schlanke Agentenlaufzeit | B |
| [AutoGen](https://github.com/microsoft/autogen) | Multi-Agenten-Systeme | B |
| [CrewAI](https://github.com/crewAIInc/crewAI) | rollenbasierte Agententeams | B |
| [LangGraph](https://github.com/langchain-ai/langgraph) | zustandsbasierte Agentenabläufe | B |
| [Mastra](https://github.com/mastra-ai/mastra) | TypeScript-Agenten und Workflows | C |
| [PydanticAI](https://github.com/pydantic/pydantic-ai) | stark typisierte Python-Agenten | B |
| [Agno](https://github.com/agno-agi/agno) | Multi-Agenten- und Wissenssysteme | C |
| [MetaGPT](https://github.com/FoundationAgents/MetaGPT) | Agententeams für Softwarearbeit | C |
| [CAMEL](https://github.com/camel-ai/camel) | Forschungs- und Agentenframework | C |
| [Hermes Agent](https://github.com/NousResearch/hermes-agent) | Gedächtnis, Skills, Terminal und autonome Arbeit | B – Pilot in Sandbox |
| [DeerFlow](https://github.com/bytedance/deer-flow) | lang laufende Recherche-, Code- und Medienaufgaben | C |
| [Flowise](https://github.com/FlowiseAI/Flowise) | visuelle Agenten und RAG | B |
| [LiteLLM](https://github.com/BerriAI/litellm) | ein Gateway für viele Modellanbieter | A |
| [Langfuse](https://github.com/langfuse/langfuse) | Tracing, Prompts, Kosten und Evaluation | A |
| [Phoenix](https://github.com/Arize-ai/phoenix) | KI-Beobachtung, Datensätze und Experimente | B |
| [Promptfoo](https://github.com/promptfoo/promptfoo) | Prompt-, Agenten- und RAG-Tests, Red Teaming | A |
| [DeepEval](https://github.com/confident-ai/deepeval) | automatisierte LLM-Evaluation | B |
| [Opik](https://github.com/comet-ml/opik) | Tracing und Evaluation | B |
| [Helicone](https://github.com/Helicone/helicone) | LLM-Observability und Kosten | C |
| [AgentOps](https://github.com/AgentOps-AI/agentops) | Agentenlaufzeiten und Kosten messen | C |

### 6.7 CRM, Marketing und Kundendienst

| Projekt | Nutzen | Klasse |
|---|---|---|
| [Twenty](https://github.com/twentyhq/twenty) | modernes Open-Source-CRM | A – gegen ActiveCampaign abgrenzen |
| [EspoCRM](https://github.com/espocrm/espocrm) | ausgereiftes CRM, E-Mail und Automationen | B |
| [ERPNext CRM](https://github.com/frappe/crm) | CRM auf dem Frappe-Stack | B |
| [Mautic](https://github.com/mautic/mautic) | Marketing-Automation und E-Mail-Strecken | B |
| [Listmonk](https://github.com/knadh/listmonk) | schnelle Newsletter- und Listenverwaltung | B |
| [Chatwoot](https://github.com/chatwoot/chatwoot) | Chat, E-Mail und Omnichannel-Support | A |
| [Zammad](https://github.com/zammad/zammad) | Helpdesk und Ticketprozesse | B |
| [FreeScout](https://github.com/freescout-help-desk/freescout) | gemeinsames Postfach und Support | A – einfacher Pilot |
| [Frappe Helpdesk](https://github.com/frappe/helpdesk) | moderner Support auf Frappe | B |
| [LibreDesk](https://github.com/abhinavxd/libredesk) | schlanker Omnichannel-Helpdesk | C |
| [Postiz](https://github.com/gitroomhq/postiz-app) | Social-Media-Planung und agentische Veröffentlichung | A |
| [Mixpost](https://github.com/inovector/mixpost) | Social-Media-Management auf Laravel | B |

### 6.8 ERP, Shop und digitale Produkte

| Projekt | Nutzen | Klasse |
|---|---|---|
| [ERPNext](https://github.com/frappe/erpnext) | ERP, CRM, Einkauf, Lager, Projekte | B – Referenz und Teilpilot |
| [Odoo](https://github.com/odoo/odoo) | sehr breites Business-System | C – zu schwer als kurzfristiger Ersatz |
| [Dolibarr](https://github.com/Dolibarr/dolibarr) | schlankeres ERP/CRM | C |
| [Medusa](https://github.com/medusajs/medusa) | flexibler Headless-Commerce-Stack | B |
| [Vendure](https://github.com/vendurehq/vendure) | TypeScript, GraphQL, Headless Commerce | B |
| [Saleor](https://github.com/saleor/saleor) | leistungsfähige Commerce-API | C |
| [Sylius](https://github.com/Sylius/Sylius) | PHP/Symfony-Commerce | B |
| [Spree](https://github.com/spree/spree) | Headless- und B2B-Commerce | C |
| [Frappe LMS](https://github.com/frappe/lms) | einfache Kursplattform | B |
| [Moodle](https://github.com/moodle/moodle) | sehr ausgereiftes LMS | C – hoher Betriebsaufwand |
| [Open edX](https://github.com/openedx/edx-platform) | große Lernplattform | C |
| [LearnHouse](https://github.com/learnhouse/learnhouse) | moderne Headless-Lernplattform | C |
| [Cal.com](https://github.com/calcom/cal.com) | Terminbuchung und Verfügbarkeit | B |

### 6.9 Webseiten, SEO, GEO und Content

| Projekt | Nutzen | Klasse |
|---|---|---|
| [Strapi](https://github.com/strapi/strapi) | großes Headless-CMS | B |
| [Directus](https://github.com/directus/directus) | Datenbank als Content-Plattform | A |
| [Payload](https://github.com/payloadcms/payload) | modernes TypeScript-CMS | B |
| [Ghost](https://github.com/TryGhost/Ghost) | Publishing, Membership und Newsletter | C |
| [Decap CMS](https://github.com/decaporg/decap-cms) | Git-basiertes CMS | C |
| [Firecrawl](https://github.com/firecrawl/firecrawl) | Websites für KI und RAG erfassen | A |
| [Crawl4AI](https://github.com/unclecode/crawl4ai) | KI-freundliches Crawling | A |
| [Crawlee](https://github.com/apify/crawlee) | robuste Browser- und Crawler-Pipelines | B |
| [Scrapy](https://github.com/scrapy/scrapy) | klassisches Python-Crawling | B |
| [Playwright](https://github.com/microsoft/playwright) | Browser-Tests, Screenshots und Messung | A – bereits passend |
| [Lighthouse](https://github.com/GoogleChrome/lighthouse) | Performance und Webqualität | A |
| [axe-core](https://github.com/dequelabs/axe-core) | Barrierefreiheit automatisiert prüfen | A |
| [Pa11y](https://github.com/pa11y/pa11y) | Accessibility-Tests per CLI | A |
| [sitespeed.io](https://github.com/sitespeedio/sitespeed.io) | wiederholbare Web-Performance-Messung | B |
| [Unlighthouse](https://github.com/harlan-zw/unlighthouse) | Lighthouse über ganze Websites | B |
| [changedetection.io](https://github.com/dgtlmoon/changedetection.io) | Wettbewerber-, Preis- und Seitendrift beobachten | A |
| [Linkinator](https://github.com/JustinBeckwith/linkinator) | tote Links in CI finden | A |

### 6.10 Bilder, Medien, Videos und YouTube

| Projekt | Nutzen | Klasse |
|---|---|---|
| [Immich](https://github.com/immich-app/immich) | sehr große Foto- und Videoverwaltung, Suche, Freigabe | A – Medienbibliothek pilotieren |
| [PhotoPrism](https://github.com/photoprism/photoprism) | KI-Suche und Fotoarchiv | B |
| [LibrePhotos](https://github.com/LibrePhotos/librephotos) | Gesicht, Objekt, Metadaten und semantische Suche | B |
| [TagStudio](https://github.com/TagStudioDev/TagStudio) | Dateien und Bilder über Tags organisieren | B |
| [MinIO](https://github.com/minio/minio) | S3-kompatibler Objektspeicher | A |
| [FFmpeg](https://github.com/FFmpeg/FFmpeg) | Basis für Video- und Audiokonvertierung | A |
| [yt-dlp](https://github.com/yt-dlp/yt-dlp) | Video, Audio, Metadaten und Untertitel beziehen | A |
| [Whisper](https://github.com/openai/whisper) | Transkription und Untertitel | A |
| [Remotion](https://github.com/remotion-dev/remotion) | Videos aus React und Daten erzeugen | A |
| [LosslessCut](https://github.com/mifi/lossless-cut) | schneller verlustfreier Schnitt | A |
| [Shotcut](https://github.com/mltframework/shotcut) | klassischer Videoeditor | B |
| [OpenShot](https://github.com/OpenShot/openshot-qt) | Videoeditor und Automationsbasis | B |
| [ComfyUI](https://github.com/comfyanonymous/ComfyUI) | visuelle Bild- und Video-KI-Pipelines | A |
| [AUTOMATIC1111 WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui) | großes Stable-Diffusion-Ökosystem | B |
| [InvokeAI](https://github.com/invoke-ai/InvokeAI) | Bildproduktion und Asset-Workflows | B |
| [Fooocus](https://github.com/lllyasviel/Fooocus) | einfache Bildgenerierung | C |
| [LivePortrait](https://github.com/KwaiVGI/LivePortrait) | Porträts animieren | C |
| [Wan](https://github.com/Wan-Video/Wan2.2) | offene Videogenerierung | C |
| [FunClip](https://github.com/modelscope/FunClip) | Sprache erkennen und Videos per Text schneiden | A |
| [OpenMontage](https://github.com/calesthio/OpenMontage) | agentische Videoproduktion | C – stark beobachten |
| [short-video-maker](https://github.com/gyoridavid/short-video-maker) | Shorts, Reels und TikTok über API/MCP | B |

### 6.11 Betrieb, Sicherheit und Zuverlässigkeit

| Projekt | Nutzen | Klasse |
|---|---|---|
| [Uptime Kuma](https://github.com/louislam/uptime-kuma) | Erreichbarkeit und einfache Alarme | A |
| [Gatus](https://github.com/TwiN/gatus) | Statusprüfungen als Konfiguration | A |
| [Grafana](https://github.com/grafana/grafana) | Dashboards über viele Datenquellen | A |
| [Prometheus](https://github.com/prometheus/prometheus) | Metriken und Alarmregeln | B |
| [Loki](https://github.com/grafana/loki) | zentrale Logs | B |
| [SigNoz](https://github.com/SigNoz/signoz) | Logs, Traces und Metriken in einer Oberfläche | A |
| [OpenTelemetry](https://github.com/open-telemetry/opentelemetry-collector) | einheitliche technische Telemetrie | A |
| [Sentry](https://github.com/getsentry/sentry) | Fehler und Performance in Anwendungen | A |
| [OpenObserve](https://github.com/openobserve/openobserve) | Logs, Traces und Metriken, kompakter Betrieb | B |
| [Netdata](https://github.com/netdata/netdata) | Server- und Datenbankmonitoring | B |
| [Trivy](https://github.com/aquasecurity/trivy) | Container, Abhängigkeiten, Secrets und SBOM | A |
| [Semgrep](https://github.com/semgrep/semgrep) | statische Codeanalyse | A – bereits genutzt |
| [Gitleaks](https://github.com/gitleaks/gitleaks) | Secrets in Repositories und Historie | A – organisationsweit Pflicht |
| [Renovate](https://github.com/renovatebot/renovate) | Abhängigkeiten automatisiert aktualisieren | A |
| [Infisical](https://github.com/Infisical/infisical) | Secrets und Konfiguration verwalten | A |
| [Vault](https://github.com/hashicorp/vault) | ausgereiftes Secret-Management | C – schwerer Betrieb |
| [Coolify](https://github.com/coollabsio/coolify) | Apps und Datenbanken selbst hosten | A |
| [Portainer](https://github.com/portainer/portainer) | Container verständlich verwalten | B |

## 7. Die 15 wichtigsten Piloten

Diese Projekte liefern den höchsten Nutzen, ohne sofort die gesamte Architektur umzubauen:

1. **Plane** – ersetzt das selbst gebaute Aufgabenboard.
2. **NocoBase** – baut interne Fachoberflächen über strukturierte Daten.
3. **Activepieces** – Freigaben und Integrationen mit Menschen im Ablauf.
4. **n8n** – Vergleichskandidat mit größtem Vorlagen- und Connector-Ökosystem.
5. **Kestra** – verbindliche technische Prozesse und Datenpipelines.
6. **Airbyte** – Daten nach BigQuery und Supabase bewegen.
7. **dbt-core** – BigQuery-Daten reproduzierbar und prüfbar aufbereiten.
8. **Metabase** – Geschäftszahlen verständlich darstellen.
9. **LiteLLM** – zentraler Modellzugang, Kosten und Fallbacks.
10. **Langfuse** – KI-Abläufe, Prompts, Qualität und Kosten sichtbar machen.
11. **Promptfoo** – Texte, Agenten und RAG vor Produktion testen.
12. **Chatwoot oder FreeScout** – Kundendienst und gemeinsames Postfach ordnen.
13. **Immich** – Medienbibliothek für Bilder und Videos testen.
14. **Postiz** – Social-Media-Veröffentlichung zentral steuern.
15. **Firecrawl plus changedetection.io** – Webwissen und Wettbewerberänderungen erfassen.

## 8. Empfohlener erster End-to-End-Prozess

Der erste Pilot soll einen echten Umsatz- und Strukturprozess vollständig abbilden:

### Prozess: Neues Klangschalen-Set veröffentlichen

1. Mitarbeiter legt Set in einer NocoBase-Maske an.
2. Supabase erzeugt eine feste Entitäts-ID.
3. Activepieces oder n8n startet den Prozess.
4. PL-SETS erzeugt Textbausteine.
5. Promptfoo und quality-system prüfen Regeln.
6. Plane erhält automatisch eine Freigabeaufgabe.
7. Freigegebener Text geht an AFS und Gambio.
8. Medien werden aus Immich/MinIO zugeordnet.
9. Content-Engine erzeugt Anzeigen und Social-Entwürfe.
10. Postiz plant Beiträge.
11. ActiveCampaign erhält Produkt- und Zielgruppendaten.
12. BigQuery erhält das Ereignis `product.published`.
13. PostHog und Ads-Daten messen Wirkung.
14. Metabase zeigt Ergebnis und Deckungsbeitrag.
15. Fehler landen in Plane, Sentry und einer eindeutigen Verantwortlichkeit.

Dieser Ablauf zeigt sofort, ob die Plattform wirklich Struktur schafft.

## 9. Automatischer Open-Source-Radar in Supabase

### Tabellen

- `oss_projects`
- `oss_categories`
- `oss_snapshots`
- `oss_releases`
- `oss_security_signals`
- `oss_scores`
- `oss_decisions`
- `oss_pilots`
- `oss_integrations`

### Wöchentlicher Lauf

1. GitHub-Topics und definierte Suchbegriffe abfragen.
2. Sterne, Forks, offene Issues, letzte Commits und Releases speichern.
3. 30- und 90-Tage-Wachstum aus Snapshots berechnen.
4. Lizenz, Archivstatus und Sicherheitsdateien prüfen.
5. Überschneidung mit bestehenden Sound-Spirit-Systemen bewerten.
6. Score neu berechnen.
7. Neue A-Kandidaten als Plane-Aufgabe anlegen.
8. Stark wachsende C-Kandidaten auf Beobachtung setzen.
9. Veraltete oder riskante Projekte automatisch abwerten.
10. Monatsbericht im Wiki und als Metabase-Dashboard erzeugen.

### Suchfelder

- `integration`, `workflow`, `automation`, `bpmn`
- `crm`, `marketing automation`, `customer support`
- `digital asset management`, `video generation`, `social media scheduler`
- `rag`, `knowledge graph`, `agent memory`, `llm observability`
- `seo audit`, `geo`, `crawler`, `structured data`
- `erp`, `headless commerce`, `lms`
- `security scanner`, `observability`, `secrets management`

## 10. Harte Architekturregeln

1. Kein neues internes Tool ohne Prüfung dieser Longlist.
2. Kein neues Repository ohne klaren Besitzer und Systemrolle.
3. Kein Prozess nur in Köpfen oder Chatverläufen.
4. Jeder wichtige Prozess besitzt Status, Ereignisse und Fehlerpfad.
5. Jede Automatisierung ist beobachtbar und erneut ausführbar.
6. Supabase speichert operative Entitäten und Beziehungen.
7. BigQuery speichert Analysen und langfristige Ereignisse.
8. GitHub speichert Code, Regeln, Spezifikationen und Entscheidungen.
9. Plane steuert menschliche Arbeit, nicht Fach- oder Analysedaten.
10. Ein Projekt wird nur eingeführt, wenn es ein bestehendes Werkzeug ersetzt oder einen klaren neuen Nutzen schafft.

## 11. Nächste Entscheidung

Nicht sofort zwanzig Systeme installieren. Zuerst den Strukturkern in einem echten Prozess beweisen:

**Plane + NocoBase + Activepieces/n8n + Kestra + Supabase + Langfuse + bestehendes quality-system.**

Danach folgen CRM, Medien, Social und weitere Bereiche schrittweise.