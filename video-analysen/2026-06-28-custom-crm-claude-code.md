# Lern-Extrakt: Custom CRM mit Claude Code

**Quelle:** YouTube "I Let Claude Code Build a Business — It Made €24,249 From Scratch",
Kanal *Income Stream Surfers*, 20:03, 28.06.2026.
**Basis:** Volltranskript (3.764 Woerter) + 125 visuell analysierte Storyboard-Frames.
**Typ:** Strategie-/Architektur-Walkthrough (kein Live-Build).

## Kernaussage
Marketing-Website mit Formular/Konfigurator sammelt Leads -> CRM als einzige "single source of
truth" hinter Login -> Claude Code baut/betreibt/bearbeitet ueber CLI, MCP oder Browser-Steuerung.
Der Gewinn liegt nicht im Bauen, sondern darin, **keinen Lead zu verschwenden**.

## 1. Geschaeftsmodell
- Beispiel: Ballynahown Park (Galway) — Event-Location fuer Stag/Hen-Partys.
- Claims: "permission to unwind", "a place without the noise".
- Verkauf **pro Person** (Erlebnisse/Upsells, z.B. Murder Mystery +50 EUR/Person) -> hoeherer AOV.
- Umsatzangabe im Video: ~10.000/Monat (Google Ads + Site, Umsatzbeteiligung). Titelzahl 24.249 = Clickbait.

## 2. Tech-Stack (Rolle | EU-/eigene Einordnung)
| Baustein | Rolle | Fuer uns |
|---|---|---|
| Claude Code | Baut/betreibt/bearbeitet Leads | Kern, vorhanden |
| GitHub (CLI) | Versionierung/Deploy | vorhanden |
| Astro | Marketing-Frontend | gut fuer Money-Pages/biokleidung |
| Clerk | Auth + Admin-Rollen | Alternative: Laravel-Auth |
| Convex | DB + BaaS + Cron | bei uns Supabase/Postgres |
| Stripe | Zahlungen (MCP) | DSGVO mit AVV |
| Resend | Transaktions-/Nurture-Mails | EU-Versand pruefen |
| Vercel | Hosting/Deploy | bei uns Profihost/Hetzner |
| PostHog | Analytics + Session-Replays | EU-Hosting, Empfehlung |
| Cloudflare Turnstile | Bot-/Spam-Schutz | haben wir |
| Google Ads (Search) | bezahlter Traffic | Inga steuert |

## 3. Drei Wege wie Claude Code "Dinge tut"
1. **CLI/Terminal** (bevorzugt): Claude liest CLI-Doku, fuehrt Befehle aus. Website-Launch = ~5 Woerter Prompt.
2. **Connectors/MCP** (Spezialfaelle): z.B. Stripe; Anbindung eigener DB, damit Claude Leads/Feedback zieht.
3. **Claude steuert Chrome** (wenn keine API): bedient Browser wie ein Mensch (z.B. Google Analytics einrichten).

Live-Demo "Claude hat Zugriff": zieht Feedback aus angebundener DB, ohne private Daten zu drucken.

## 4. Lead-Lebenszyklus
`New -> Contacted -> Quoted -> Bought -> Won/Lost`
Leads verschwinden in **48 h bis 7 Tagen**. Liegengelassene Leads = verbranntes Ad-Budget.

## 5. Die 6 Conversion-Hebel ("NOT WASTING LEADS IS THE WHOLE POINT")
1. **Speed to Lead** — sofortige Benachrichtigung + Angebot.
2. **Automated Nurture** — Mails nach 7/14/31 Tagen (Cron + Resend).
3. **Bot-/Spam-Schutz** — Cloudflare Turnstile (~10 Min Setup).
4. **Attack the Leaks** — PostHog Session-Replays; reales Bsp.: mobiler "Weiter"-Button unauffindbar -> Inquiry-Einbruch.
5. **Offline-Conversions an Google** — echte Kaeufe zuruekspielen, damit Google auf Zahler optimiert.
6. **Rollen & Reporting** — Clerk-Rollen, Provision, ein Dashboard (Leads/Quelle/Conversion/Umsatz).

Rule of thumb: allein nicht machbar -> Personal **oder** Claude Code mit Mensch-im-Loop.

## 6. Folien-/Story-Struktur (Bauplan, aus Frames rekonstruiert)
1. Talking-Head Intro -> 2. Titelfolie -> 3. Marketing-Site-Demo -> 4. Konfigurator/Formular (34/60/104 EUR)
-> 5. Sponsor Harbor (2.197 Seiten, ~800k Impressions, 14.987 Clicks) -> 6. "Pick how Claude Code does each step"
-> 7. "The stack" -> 8. "The build flow" -> 9. PostHog-Dashboards -> 10. "NOT WASTING LEADS" (Get->Nurture->Sell)
-> 11. "Conversion grid" -> 12. "Rule of thumb" + Cliffhanger.

## 7. Substanz vs. Clickbait
**Signal:** klare kopierbare Architektur; konkrete Tool-Liste; echtes Failure-Beispiel; On-Screen-Zahlen
decken sich mit Transkript (~2.200 Seiten, ~800k Impressions, ~15k Clicks).
**Rauschen:** Titelzahl 24.249 nicht hergeleitet; kein Live-Build; starker Sponsor-Push; "du musst nie
selbst etwas tun" ueberzogen; US-Stack ohne DSGVO-Betrachtung.

## 8. Uebertragung auf unsere Projekte
- **Gstack-CRM:** Status-Modell + 6 Hebel als Spec; Laravel+Supabase statt Convex/Clerk; Turnstile + PostHog.
- **Sound-Spirit:** Konfigurator = Set-Builder fuer Planetenschalen; HWG beachten (keine Heilversprechen in Nurture).
- **biokleidung:** Astro-Money-Pages + Newsletter-Nurture; "Anzeige"-Pflicht; Consent vor PostHog-Tracking.
- **Content-Engine:** Funnel-Story als wiederverwendbares Skript-Template.

## 9. Wiederverwendbare Bausteine
**Prompt-Muster:**
- `Du bist auf [CLI-DIENST] eingeloggt. Launch diese Website.`
- `Finde das neueste [Lead/Feedback] im [System]. Drucke keine privaten Daten. Gib mir die Eintraege nummeriert.`
- `Neuer Lead: [Daten]. Erstelle Angebot aus Konfigurator (z.B. 3 Naechte x 200 EUR = 600 EUR), sende via Resend.`

**Bessere Tutorial-Outline:** ehrlicher Titel -> Ergebnis zuerst -> Architektur (EU-Stack) -> 3 Mechaniken
mit echten Befehlen -> Daten-Beweis -> **DSGVO/HWG-Kapitel (Differenzierung)** -> Failure+Fix -> Checkliste.

**Sofort-Massnahmen:** Turnstile auf alle Formulare; PostHog (EU); Lead-Status-Spec; 7/14/31-Nurture;
Speed-to-Lead-Benachrichtigung; Offline-Conversions; Set-Builder pruefen; Funnel-Template ablegen.

## Methodik
Transkript via yt-dlp (json3 Auto-Captions) komplett gelesen; visuelle Analyse ueber 125 Storyboard-Frames
(Szenentyp/Folien-Titel/UI-Layout). Full-res-Video ueber Egress-Proxy (IP-gebundene googlevideo-URLs,
Org-Policy) nicht ladbar; pixelgenaue Terminal-Code-Zeilen daher nicht erfasst. Zahlen zweifach belegt.
