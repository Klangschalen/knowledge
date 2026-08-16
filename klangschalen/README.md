# Knowledge Base: Klangschalen + Sets

Quelle der Wahrheit fuer die **Produkttext-Pipeline (pl-sets, Neuaufbau in PHP)**.
Die Pipeline ist deterministisch: sie LIEST diese Daten, sie raet nicht.

## Dateien

| Datei | Inhalt | Pipeline-Schritt |
|-------|--------|------------------|
| `groessen-definition.yaml` | Gewicht-/Durchmesser-Klassen, Set-Kategorien, Set-Rollen | 2. Groessen-Logik |
| `wirkungs-vokabular.yaml` | Koerperzonen, Generik-Lexikon, HWG-Verbote, verbotene Muster | 1. Wirkungen + Sprach-/Recht-Gate |
| `planetenschalen.yaml` | Planetenton + traditionelles Thema je Planet (ENTWURF, Werte pruefen) | 1. Wirkungen (Planetenschalen) |
| `titel-katalog.yaml` | 3 Titel-Bauarten + Auswahl-Regel (5 Kandidaten) | 2. Titel erzeugen + pruefen |
| `block-schnipsel.yaml` | Text-Bloecke (Schnipsel) + Reihenfolge + Include-Bedingungen | 3.-4. Block-Auswahl + Zusammenfuegen |
| `text-umfang-regel.yaml` | Text-Umfang je Set-Groesse, Frage-Ueberschriften (GEO) | 3. Block-Umfang + Sprachregeln |

## Prinzip

Frank-Architektur: alles programmatisch als Prozessablauf in PHP. Diese Knowledge
Base ist das versionierte Daten-Asset (waechst mit jedem gepflegten Produkt), die
PHP-Pipeline der Prozess darauf. Bau-Reihenfolge:

1. Wirkungen + Groessen sammeln (groessen-definition, wirkungs-vokabular, planetenschalen)
2. Titel-Kandidaten erzeugen + gegen Wirkungen pruefen (titel-katalog)
3. Block-Auswahl nach Set-Groesse (block-schnipsel + text-umfang-regel)
4. Bloecke (Schnipsel) zusammenfuegen
5. Sprach-/GEO-/Kundenerwartungs-Regeln auf Ueberschriften
6. Intent-Feinschliff sprachlich
7. HTML-Ausgabe -> Weboffice

Aenderungen an Definitionen passieren HIER, nicht im Pipeline-Code.

## Offen

- `planetenschalen.yaml`: Frequenz-/Notenwerte NICHT erfunden - aus Cousto/
  Produktdaten einsetzen (status ENTWURF). Planeten-Liste vervollstaendigen.
