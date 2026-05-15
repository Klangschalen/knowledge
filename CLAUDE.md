# knowledge

Klangschalen-Repository. Norm-Quelle: `claude-config`-Repo (rules/, hooks/, commands/).
Diese CLAUDE.md ist ein Bootstrap-Stub: bei erster aktiver Nutzung mit projekt-spezifischem Kontext erweitern.

## Output-Vertrag - Pflicht in JEDER faktischen Antwort

Jede Antwort mit Status/Analyse/Befund/Aenderung endet im folgenden Format. Auch in Cloud-Sessions, auch ohne lokalen Hook. Vollstaendige Regel: `claude-config:rules/evidence-first.md` Abschnitt 8a.

```
RISK-LEVEL: <low | medium | high>
GEPRUEFT (wk1/wk2): <belegte Fakten, je mit evidence_ref>
UNGEPRUEFT (wk3): <was nicht verifiziert ist + welcher Check klaeren wuerde>
KONFLIKTE: <widerspruechliche Belege | keine>
URTEIL: <nur aus wk1/wk2 | oder: STOP, weil ...>
NAECHSTER SCHRITT: <GENAU EINER>
KORREKTUR: <bei Selbstkorrektur: was vorher falsch war | weglassen wenn keine>
```

Bei `low`-Aufgaben darf auf 2 Zeilen schrumpfen: `RISK-LEVEL` + `NAECHSTER SCHRITT`. Bei kreativer Texterzeugung gilt der Vertrag nicht.

## Entscheidungen mit ICE-Score

Bei JEDER Entscheidung mit mehreren Optionen: Tabelle mit ICE-Score je Option.
**ICE = Impact x Confidence x Ease / 100** (jede Achse 1-10):
- MUST: ICE >= 5.0
- SHOULD: ICE >= 3.0
- COULD: ICE >= 1.5
- WONT: ICE < 1.5

Empfehlung darunter. Nie "Soll ich...?" / "Moechtest du...?" - direkt beste Option umsetzen.
Vollstaendige Regel: `claude-config:rules/workflow-7-schritte.md` Schritt 2 + Command `/ice-score`.

## Doku-Disziplin nach jeder Code-Aenderung

Wenn Aenderungen an `rules/`, `hooks/`, `scripts/`, `commands/`, `skills/` oder `settings.json` gemacht werden, MUSS mindestens EINE Doku-Datei in derselben Branch beruehrt sein:
- CHANGELOG.md
- STATUS.md
- learnings/YYYY-MM-DD-*.md
- OFFENE-AUFGABEN.md

Erzwingung: Lokaler Stop-Hook `claude-config:hooks/doku-completeness-check.sh` warnt sonst.
