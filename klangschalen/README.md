# Knowledge Base: Klangschalen + Sets

Quelle der Wahrheit fuer die **Produkttext-Pipeline (pl-sets)**. Die Pipeline ist
deterministisch (PHP): sie LIEST diese Daten, sie raet nicht.

## Dateien

| Datei | Inhalt | Pipeline-Schritt |
|-------|--------|------------------|
| `groessen-definition.yaml` | Gewicht-/Durchmesser-Klassen, Set-Kategorien, Set-Rollen | 2. Groessen-Logik |
| `wirkungs-vokabular.yaml` | Koerperzonen-Vokabular, Generik-Lexikon, HWG-Verbote, verbotene Muster | 1. Wirkungen + Sprach-/Recht-Gate |
| `text-umfang-regel.yaml` | Text-Umfang je Set-Groesse, Frage-Ueberschriften (GEO) | Block-Auswahl + Sprachregeln |

## Prinzip

Frank-Architektur: alles programmatisch als Prozessablauf in PHP. Diese Knowledge
Base ist das versionierte Daten-Asset (waechst mit jedem gepflegten Produkt), die
PHP-Pipeline der Prozess darauf. Reihenfolge im Bau:

1. Wirkungen + Groessen sammeln (diese Dateien)
2. Titel-Kandidaten erzeugen + gegen Wirkungen pruefen
3. Block-Auswahl nach Set-Groesse (klein = wenig Text, schwer = mehr)
4. Bloecke (Schnipsel) zusammenfuegen
5. Sprach-/GEO-/Kundenerwartungs-Regeln auf Ueberschriften
6. Intent-Feinschliff sprachlich
7. HTML-Ausgabe -> Weboffice

Aenderungen an Definitionen passieren HIER, nicht im Pipeline-Code.
