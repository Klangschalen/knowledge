---
title: "PHP-Upgrade: Welche Version vertraegt unser Stack (WordPress + Gambio)?"
created: 2026-05-31
valid_from: 2026-05-31
invalid_from: null
superseded_by: null
status: active
audience: ["Frank", "Michael"]
tags: ["php", "upgrade", "wordpress", "gambio", "server", "eol"]
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
- **Gambio** ist der **bestimmende Faktor**: aktuelle Gambio-Versionen (4.x/4.9)
  verlangen **PHP 8.2 oder 8.3**. Das setzt die Untergrenze.
- **7.3 -> 8.2** ist ein grosser Sprung (mehrere Major-Schritte). Deshalb gilt:
  **niemals direkt auf Live**, sondern erst auf einer Kopie testen (siehe unten).

## Warum Gambio den Ausschlag gibt

WordPress und Gambio teilen sich denselben PHP-Interpreter auf dem Server. Es kann
immer nur **eine** PHP-Version aktiv sein. Also muss die gewaehlte Version von
**beiden** vertragen werden. Da Gambio die hoehere Anforderung hat, richtet sich
die Entscheidung nach Gambio.

| Software | Vertraegt PHP ... | Quelle |
|---|---|---|
| WordPress 6.x | 7.4+, voll 8.1, Beta 8.2/8.3 | wordpress.org/about/requirements |
| Gambio 4.x / 4.9 | **8.2 / 8.3** (8.0/8.1 abgekuendigt) | docs.gambio.de/systemvoraussetzungen |
| **Gemeinsames Ziel** | **8.2 (sicher) bzw. 8.3** | — |

## Wichtige Vorbedingung: Gambio-Version pruefen

Unser Inventar zeigt die Gambio-Version aktuell als `unknown`. **Bevor** das
PHP-Upgrade gemacht wird, muss Michael die laufende Gambio-Version feststellen
(Admin-Bereich -> Shop-Info, oder `release_info.php` auf dem Server):

- Ist Gambio **4.x / aktuell** -> PHP 8.2/8.3 ist freigegeben, Upgrade kann geplant werden.
- Ist Gambio **aelter (3.x o.ae.)** -> erst **Gambio updaten**, dann PHP. Sonst geht der Shop kaputt.

> Das ist der haeufigste Stolperstein: PHP hochziehen, waehrend der Shop noch eine
> alte Gambio-Version faehrt, die 8.2 nicht kennt -> weisse Seite / Shop offline.

## Sicherer Ablauf (Reihenfolge fuer Michael)

1. **Bestandsaufnahme:** Gambio-Version + WordPress-Version + aktive Plugins notieren.
2. **Gambio ggf. zuerst updaten**, bis es PHP 8.2/8.3 offiziell unterstuetzt.
3. **Backup** (Dateien + Datenbank) von Shop UND WordPress.
4. **Testkopie / Staging:** PHP-Version dort auf 8.2 stellen und beide Systeme klicken
   (Shop: Bestellprozess; WordPress: Login, wichtige Seiten, Formulare).
5. **Plugins/Module pruefen:** WordPress-Plugins auf 8.2-Kompatibilitaet aktualisieren;
   Gambio-Module checken.
6. **Erst dann Live** umstellen (bei Profihost meist im Kunden-Menue pro Domain waehlbar).
7. **Nachkontrolle:** Security-Scanner-Lauf -> bestaetigt die neue PHP-Version im Inventar.

## Was das mit dem Security-Scanner zu tun hat

- Der Scanner hat das EOL-Problem **sichtbar gemacht** (vorher war PHP `unknown`).
- CVE-2012-1823, das die ROT-Mail ausloeste, betrifft 7.3.33 **nicht** (2012 gefixt) —
  das war ein Fehlalarm und ist im Scanner gefiltert (PR #67).
- Nach dem PHP-Upgrade liest der naechste Scanner-Lauf automatisch die neue Version.

## Quellen

- WordPress Requirements: https://wordpress.org/about/requirements/
- WordPress PHP-Kompatibilitaet: https://make.wordpress.org/hosting/handbook/php-compatibility/
- Gambio Systemvoraussetzungen: https://docs.gambio.de/systemvoraussetzungen/
- PHP End-of-Life: https://endoflife.date/php (7.3 EOL 2021-12-06)

---

*Erstellt am 2026-05-31 · Sound-Spirit Wissensbasis · Kontext: KEV-Scanner
ROT-Mail CVE-2012-1823 + PHP-7.3-EOL-Befund.*
