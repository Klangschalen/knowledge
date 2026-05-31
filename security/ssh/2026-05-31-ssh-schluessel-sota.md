---
title: "SSH-Schlüssel: Wie es heute läuft, was Rotation bedeutet, und der bessere Weg"
created: 2026-05-31
valid_from: 2026-05-31
invalid_from: null
superseded_by: null
status: active
audience: ["Frank", "Michael", "Christina"]
tags: ["ssh", "security", "sota", "schluessel-rotation", "least-privilege"]
---

# SSH-Schlüssel bei Sound-Spirit — SOTA-Analyse

> **Für wen ist das?** Für Frank (Überblick + Entscheidung), Michael (Umsetzung)
> und Christina (Verständnis). Teil 1 erklärt SSH von Grund auf, ohne Vorwissen.
> Teil 2–4 werden konkreter. Wer nur die Empfehlung will: **Teil 6**.

---

## Teil 1 — Was ist SSH überhaupt? (für absolute Einsteiger)

**SSH** (Secure Shell) ist die Art, wie sich ein Computer bei einem anderen
Computer **sicher anmeldet**, um dort Befehle auszuführen oder Dateien zu lesen.
Wenn Michael „auf den Server geht", um etwas zu reparieren, benutzt er SSH.

Statt eines Passworts benutzt man bei SSH meistens ein **Schlüsselpaar**. Das ist
das wichtigste Bild, das man verstehen muss:

| Teil | Was es ist | Wo es liegt | Bild |
|------|------------|-------------|------|
| **Privater Schlüssel** | Die geheime Hälfte | Bleibt beim, der sich anmeldet (Michaels Laptop, oder bei uns: GitHub) | Dein Hausschlüssel — gibst du **niemals** her |
| **Öffentlicher Schlüssel** | Die offene Hälfte | Liegt **auf dem Server** in einer Liste namens `authorized_keys` | Das Türschloss — darf jeder sehen |

**So läuft die Anmeldung ab (vereinfacht):**

1. GitHub (oder Michael) will sich beim Server anmelden.
2. Der Server schaut in seine Liste `authorized_keys`: „Kenne ich dieses Schloss?"
3. Der Server stellt eine Rechenaufgabe, die nur mit dem **privaten** Schlüssel
   lösbar ist.
4. GitHub löst sie mit dem privaten Schlüssel → der Server lässt rein.

Das Geniale: **Der private Schlüssel verlässt nie den Anmelder.** Es wird kein
Passwort über die Leitung geschickt. Wer nur das Türschloss (öffentlichen
Schlüssel) sieht, kann nichts damit anfangen.

> **Merksatz:** Öffentlicher Schlüssel = Schloss (darf rumliegen).
> Privater Schlüssel = Schlüssel (streng geheim).
> Wer den privaten Schlüssel hat, **kommt rein**.

---

## Teil 2 — Was wir GERADE machen (Ist-Zustand)

### 2a) Der CISA-KEV-Scanner (neu, seit heute)

Damit unser Sicherheits-Scanner in GitHub Actions die **echten Software-Versionen**
auf dem Server lesen kann (WordPress, Plugins, Gambio …), haben wir ihm einen
SSH-Zugang gegeben:

- Der private Schlüssel liegt als **GitHub-Secret** namens `PROFIHOST_SSH_KEY`.
- Der Scanner verbindet sich, **liest** ein paar Versions-Dateien, fertig.
- In unserem Python-Code ist das **nur-lesend** programmiert (`cat`, `grep`, `php -v`).

### 2b) Michaels Schlüssel (Bestand, gewachsen)

Michael nutzt SSH für **viele Systeme** — Schnittstellen, Wartung, Deployments,
Backups. In der Praxis ist oft **ein einziger, lange gültiger Schlüssel** im
Einsatz, der überall passt. Das ist bequem, aber sicherheitstechnisch der
schwächste Punkt (siehe Teil 4).

### Das versteckte Problem im Ist-Zustand

> **Wichtig — bitte einmal in Ruhe lesen:**
> „Nur-lesend" ist bei uns aktuell nur eine **Vereinbarung in unserem Code**,
> **nicht** eine Regel, die der Server erzwingt.
>
> Der Schlüssel selbst hat (sehr wahrscheinlich) **vollen Shell-Zugang**. Würde
> der GitHub-Secret jemals geleakt, könnte ein Angreifer damit eben **nicht nur
> lesen**, sondern alles tun, was der Schlüssel darf — Dateien ändern, löschen,
> Schnittstellen manipulieren.
>
> Die echte Sicherheit kommt erst, wenn **der Server** den Schlüssel einschränkt
> (Teil 6).

---

## Teil 3 — Was bedeutet „SSH rotieren"?

**Rotation = den Schlüssel regelmäßig austauschen**, so wie man ein Passwort
regelmäßig ändert. Genau das war deine Frage.

**Ablauf einer Rotation (Beispiel):**

1. Neues Schlüsselpaar erzeugen (neues Schloss + neuer Schlüssel).
2. Neues **Schloss** (öffentlichen Schlüssel) zur `authorized_keys` auf dem
   Server hinzufügen.
3. Neuen **privaten** Schlüssel überall eintragen, wo er gebraucht wird
   (z. B. GitHub-Secret aktualisieren).
4. Testen, dass alles noch läuft.
5. **Altes Schloss aus `authorized_keys` entfernen** — ab jetzt ist der alte
   Schlüssel tot.

### Warum rotieren? Der Unterschied in einem Satz

| Ohne Rotation | Mit Rotation |
|---------------|--------------|
| Ein geleakter Schlüssel funktioniert **für immer** — bis jemand zufällig merkt, dass er weg ist. | Ein geleakter Schlüssel funktioniert nur **bis zur nächsten Rotation** — danach ist er wertlos. |

Rotation **verkleinert das Zeitfenster**, in dem ein gestohlener Schlüssel
Schaden anrichten kann. Sie verhindert den Diebstahl nicht — sie sorgt dafür,
dass Diebstahl nicht ewig nachwirkt.

> **Analogie:** Ein Hotel wechselt nach jedem Gast die Türcodes. Selbst wenn ein
> Gast den Code mitnimmt, nützt er ihm beim nächsten Mal nichts mehr.

---

## Teil 4 — Die verschiedenen Techniken im Vergleich

Das ist der Kern deiner Frage: *Welche Unterschiede bestehen zwischen den
Techniken?* Hier von „bequem aber unsicher" nach „sicher aber aufwändiger":

### Technik A — Ein Schlüssel für alles (heutiger De-facto-Stand)

- **Wie:** Ein langlebiger Schlüssel, der auf allen Systemen passt.
- **Vorteil:** Maximal bequem, nur eine Sache zu merken.
- **Nachteil:** Der „Generalschlüssel". Leakt er, ist **alles** offen — und zwar
  unbegrenzt. Man weiß auch nie, *wer* gerade was gemacht hat (alle benutzen
  denselben).
- **SOTA-Bewertung:** ❌ Veraltet, gilt heute als Risiko.

### Technik B — Ein eigener Schlüssel pro Zweck (Trennung)

- **Wie:** Ein Schlüssel **nur** für den Scanner, ein anderer **nur** für
  Schnittstellen, ein dritter für Backups …
- **Vorteil:** Leakt der Scanner-Schlüssel, ist **nur der Scanner** betroffen —
  man tauscht genau diesen einen aus, der Rest läuft weiter. Man sieht auch,
  welcher Schlüssel was tut.
- **Nachteil:** Etwas mehr Verwaltung (mehrere Schlüssel statt einer).
- **SOTA-Bewertung:** ✅ Grundprinzip „Least Privilege" (so wenig Rechte wie nötig).

### Technik C — Eingeschränkter Schlüssel (forced command / restrict)

- **Wie:** In der `authorized_keys` schreibt man **vor** den Schlüssel, was er
  darf. Beispiel — dieser Schlüssel darf **nur** ein Lese-Skript ausführen,
  sonst nichts:
  ```
  command="/usr/local/bin/inventar-readonly.sh",restrict ssh-ed25519 AAAA... scanner@github
  ```
- **Vorteil:** Jetzt ist „nur-lesend" **vom Server erzwungen**, nicht nur
  Vereinbarung. Selbst mit gestohlenem Schlüssel kann ein Angreifer **nur das
  eine Skript** auslösen — keine Shell, kein Löschen, nichts.
- **Nachteil:** Skript muss einmal eingerichtet werden.
- **SOTA-Bewertung:** ✅✅ Für unseren Scanner-Fall der größte Sicherheitsgewinn.

### Technik D — Rotation (Teil 3) — kombinierbar mit B und C

- **Wie:** Schlüssel regelmäßig (z. B. quartalsweise) oder bei Verdacht tauschen.
- **Vorteil:** Begrenzt die Lebensdauer eines geleakten Schlüssels.
- **Nachteil:** Braucht einen festen Ablauf, sonst wird's vergessen.
- **SOTA-Bewertung:** ✅ Standard-Hygiene. Am stärksten zusammen mit B + C.

### Technik E — SSH-Zertifikate (CA-signiert, kurzlebig)

- **Wie:** Eine zentrale „Ausweisstelle" (Certificate Authority) signiert
  **kurzlebige** Ausweise (z. B. 8 Stunden gültig). Der Server vertraut der
  Ausweisstelle, nicht mehr einzelnen Schlüsseln.
- **Vorteil:** Kein Aufräumen von `authorized_keys` mehr; Rotation passiert
  **automatisch durch Ablauf**. Skaliert auf viele Personen/Systeme. Das ist
  der Goldstandard bei größeren Teams (Netflix, Facebook & Co. machen das so).
- **Nachteil:** Deutlich aufwändiger einzurichten; lohnt erst bei vielen
  Systemen/Personen.
- **SOTA-Bewertung:** ✅✅✅ State of the Art — aber für ein 2-Personen-Team
  vermutlich **Overkill** (noch).

### Übersichtstabelle

| Technik | Sicherheit | Aufwand | Für uns sinnvoll? |
|---------|-----------|---------|-------------------|
| A — Ein Schlüssel für alles | ❌ niedrig | sehr niedrig | nein (Risiko abbauen) |
| B — Schlüssel pro Zweck | ✅ gut | niedrig | **ja, sofort** |
| C — Eingeschränkter Schlüssel | ✅✅ sehr gut | mittel (1× Skript) | **ja, für den Scanner** |
| D — Rotation | ✅ gut | mittel (Ablauf) | **ja, quartalsweise** |
| E — SSH-Zertifikate | ✅✅✅ exzellent | hoch | später, wenn wir wachsen |

---

## Teil 5 — Wie hängt das mit dem zusammen, was wir heute gebaut haben?

Der neue CISA-KEV-Scanner braucht vom Server **nur sehr wenig**: er liest ein
paar Versions-Dateien. Das ist der **perfekte Kandidat für Technik B + C**:

- **B:** ein **eigener** Schlüssel `scanner@github`, getrennt von Michaels
  Generalschlüssel.
- **C:** dieser Schlüssel darf auf dem Server **nur ein Lese-Skript** ausführen.

Dann gilt: Selbst wenn unser GitHub-Secret jemals leakt, kann der Angreifer
**nur die Versionsnummern lesen** — also genau das, was eh in der täglichen
Mail steht. Kein Schaden möglich. Das ist ein riesiger Unterschied zum heutigen
Zustand, wo der Schlüssel (vermutlich) alles darf.

---

## Teil 6 — Empfehlung (mit ICE-Bewertung)

> **ICE = Impact × Confidence × Ease / 100** (jede Achse 1–10).
> MUST ≥ 5.0 · SHOULD ≥ 3.0 · COULD ≥ 1.5

| Maßnahme | Impact | Confidence | Ease | ICE | Stufe |
|----------|:------:|:----------:|:----:|:---:|:-----:|
| **1. Eigener, eingeschränkter Lese-Schlüssel für den Scanner** (B+C) | 9 | 9 | 7 | **5,7** | MUST |
| **2. Schlüssel pro Zweck trennen** (Michaels Generalschlüssel auflösen) | 8 | 8 | 5 | **3,2** | SHOULD |
| **3. Quartalsweise Rotation mit dokumentiertem Ablauf** (D) | 6 | 8 | 6 | **2,9** | SHOULD |
| **4. SSH-Zertifikate / CA einführen** (E) | 7 | 6 | 2 | **0,8** | WONT (noch) |

### Konkreter nächster Schritt (genau einer)

**Einen dedizierten, nur-lesenden Scanner-Schlüssel einrichten.** Ablauf für
Michael (ca. 15 Min):

1. Neues Schlüsselpaar erzeugen:
   `ssh-keygen -t ed25519 -C "scanner@github" -f scanner_key`
2. Auf dem Server ein kleines Lese-Skript ablegen, z. B.
   `/usr/local/bin/inventar-readonly.sh` (liest die Versions-Dateien aus).
3. Öffentlichen Schlüssel in `~/.ssh/authorized_keys` eintragen — **mit
   Einschränkung davor:**
   ```
   command="/usr/local/bin/inventar-readonly.sh",restrict ssh-ed25519 AAAA...scanner@github
   ```
4. Privaten Schlüssel als GitHub-Secret `PROFIHOST_SSH_KEY` hinterlegen
   (ersetzt den jetzigen, falls der Michaels Generalschlüssel war).
5. Workflow einmal manuell starten und prüfen, dass die Versionen kommen.

> Damit ist der Scanner-Zugang **sicher gekapselt**, und ihr habt nebenbei
> Technik B + C produktiv im Einsatz — die Grundlage, auf der Rotation (D)
> später trivial wird.

---

## Anhang — Glossar

| Begriff | Einfach erklärt |
|---------|-----------------|
| **SSH** | Sichere Fernanmeldung an einem anderen Computer. |
| **Schlüsselpaar** | Privat (geheim) + öffentlich (Schloss). |
| **`authorized_keys`** | Die Türschloss-Liste auf dem Server. |
| **GitHub-Secret** | Sicherer Tresor in GitHub für Passwörter/Schlüssel; im Workflow nutzbar, aber nicht auslesbar. |
| **Rotation** | Schlüssel regelmäßig austauschen. |
| **Least Privilege** | So wenig Rechte wie möglich vergeben. |
| **Forced command** | Server erzwingt, dass ein Schlüssel nur einen bestimmten Befehl darf. |
| **CA / Zertifikat** | Zentrale Ausweisstelle, die kurzlebige Zugangs-Ausweise signiert. |

---

*Erstellt am 2026-05-31 · Sound-Spirit Wissensbasis · Kontext: PR #64
(CISA-KEV SSH-Versions-Erkennung) im Repo `security-scanner-laravel`.*
