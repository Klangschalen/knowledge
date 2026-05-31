---
title: "PHP-Upgrade: Welche Version vertraegt unser Stack (WordPress + Gambio)?"
created: 2026-05-31
valid_from: 2026-05-31
invalid_from: null
superseded_by: null
status: active
audience: ["Frank", "Michael"]
tags: ["php", "upgrade", "wordpress", "gambio", "server", "eol", "managed-hosting"]
---

# PHP-Upgrade: Zielversion fuer unseren Stack

> **Anlass:** Die SSH-Erkennung des Security-Scanners hat gezeigt, dass auf dem
> Server **PHP 7.3.33** laeuft. Diese Version ist **seit 2021-12-06 End-of-Life**
> und bekommt keine Sicherheitsupdates mehr. Frage: Wohin koennen/sollen wir
> aktualisieren, ohne dass WordPress oder der Gambio-Shop kaputtgehen?

## Kurzantwort (fuer Frank)

**Ziel: PHP 8.2** (sicherer, gut getesteter gemeinsamer Nenner) — oder **PHP 8.3**,
wenn Michael etwas mehr Zukunftssicherheit will und vorher testet.

- **WordPress** ist flexibel: laeuft auf 8.1, 8.2, 8.3.
- **Gambio 5.0.2** (unsere Version, bestaetigt) ist fuer **PHP 8.2/8.3 freigegeben**
  und lief bei uns bereits darauf. Die fruehere Sorge "erst Gambio updaten" entfaellt.
- **Wir koennen PHP aber NICHT selbst umstellen** (Managed Server, siehe unten) —
  das Upgrade ist eine **Anfrage an den Hoster**, kein Selfservice.

## Wichtig: Managed Server — wir stellen PHP nicht selbst um

Unser Hosting ist ein **Managed Server**. Die PHP-Version wird vom **Hoster**
verwaltet, nicht von uns im Kunden-Menue. Konsequenz:

- Das PHP-Upgrade laeuft als **Support-Anfrage/Ticket an den Hoster** (wie zuletzt
  beim Spamhaus-/Mailthema), nicht als eigener Klick.
- Wir liefern dem Hoster die **Zielversion (8.2 oder 8.3)** und die Info, dass
  **Gambio 5.0.2 und unser WordPress** das vertragen.
- Den Test (Staging) und die Plugin-/Modulkontrolle machen wir; das **Schalten**
  der PHP-Version macht der Hoster.

## Warum Gambio den Ausschlag gibt

WordPress und Gambio teilen sich denselben PHP-Interpreter auf dem Server. Es kann
immer nur **eine** PHP-Version aktiv sein. Also muss die gewaehlte Version von
**beiden** vertragen werden. Gambio hat historisch die hoehere Anforderung — mit
**5.0.2** ist das aber kein Engpass mehr, weil 5.0.2 bis 8.3 unterstuetzt.

| Software | Vertraegt PHP ... | Quelle |
|---|---|---|
| WordPress 6.x | 7.4+, empfiehlt 8.3, voll 8.1/8.2/8.3 | wordpress.org/about/requirements |
| **Gambio 5.0.2** (unsere) | **8.2 / 8.3** (lief bereits) | Gambio Systemvoraussetzungen + eigene Erfahrung |
| **Gemeinsames Ziel** | **8.2 (sicher) bzw. 8.3** | — |

## Sicherer Ablauf (was wir tun, was der Hoster tut)

1. **Bestandsaufnahme (wir):** Gambio 5.0.2 bestaetigt; WordPress-Version + aktive
   Plugins notieren.
2. **Backup (wir/Hoster):** Dateien + Datenbank von Shop UND WordPress.
3. **Testkopie / Staging (wir):** falls verfuegbar PHP 8.2 testen und beide Systeme
   klicken (Shop: Bestellprozess; WordPress: Login, wichtige Seiten, Formulare).
4. **Plugins/Module pruefen (wir):** WordPress-Plugins auf 8.2-Kompatibilitaet
   aktualisieren; Gambio-Module checken.
5. **Hoster-Ticket (wir -> Hoster):** PHP-Zielversion 8.2 (oder 8.3) fuer unsere
   Domain(s) anfordern. Hinweis: Gambio 5.0.2 + WordPress vertragen das.
6. **Umschaltung (Hoster):** Hoster stellt PHP um, idealerweise zu vereinbartem
   Zeitfenster.
7. **Nachkontrolle (wir):** Security-Scanner-Lauf -> bestaetigt die neue PHP-Version
   im Inventar; Shop + WordPress kurz gegenklicken.

## Was das mit dem Security-Scanner zu tun hat

- Der Scanner hat das EOL-Problem **sichtbar gemacht** (vorher war PHP `unknown`).
- CVE-2012-1823, das die ROT-Mail ausloeste, betrifft 7.3.33 **nicht** (2012 gefixt) —
  das war ein Fehlalarm und ist im Scanner gefiltert (PR #67).
- Die **Gambio-Version 5.0.2** wird vom Scanner jetzt ebenfalls erfasst (PR #68:
  Auto-Erkennung aus `version_info/` + manuelle Angabe `CISA_KEV_GAMBIO_VERSION`).
- Nach dem PHP-Upgrade liest der naechste Scanner-Lauf automatisch die neue Version.

## Quellen

- WordPress Requirements (PHP 8.3): https://wordpress.org/about/requirements/
- WordPress PHP-Kompatibilitaet: https://make.wordpress.org/hosting/handbook/php-compatibility/
- Gambio Systemvoraussetzungen: https://docs.gambio.de/systemvoraussetzungen/
- PHP End-of-Life: https://endoflife.date/php (7.3 EOL 2021-12-06; 8.2 Security bis 12/2026, 8.3 bis 12/2027)

---

*Erstellt am 2026-05-31 · Sound-Spirit Wissensbasis · Kontext: KEV-Scanner
ROT-Mail CVE-2012-1823 + PHP-7.3-EOL-Befund. Korrigiert: Gambio 5.0.2 bestaetigt,
Managed-Server (PHP-Umstellung via Hoster).*
