# Berichtsgenerierung (Entwurf)

**Status:** Draft

## Zielsetzung

Die Dokumentation eines Simulationslaufes wird vollständig automatisiert erzeugt.

Manuell geschriebene Ergebnisberichte sind nicht vorgesehen.

Alle Tabellen, Diagramme und numerischen Werte stammen ausschließlich aus den Ergebnissen der Simulation.

---

# 1. Grundprinzip

Die Dokumentenerzeugung ist vollständig von der eigentlichen Berechnung getrennt.

Der Ablauf lautet:

```text
Simulation
        │
        ▼
Ergebnisdaten (JSON, CSV)
        │
        ▼
Jinja2-Templates
        │
        ▼
Markdown
        │
        ▼
Pandoc
        │
        ▼
PDF / HTML
```

---

# 2. Ergebnisse als Datenquelle

Die Simulation erzeugt ausschließlich strukturierte Daten.

Beispielsweise

* Komponentenkennwerte
* StatePoints
* Energiebilanzen
* Temperaturprofile
* Wirkungsgrade
* Diagrammdaten

Diese Daten werden in maschinenlesbaren Formaten gespeichert.

---

# 3. Templates

Die Dokumentation basiert auf Jinja2-Templates.

Templates enthalten

* Text
* Tabellen
* Platzhalter
* Schleifen
* Bedingungen

Sie enthalten keine Berechnungen.

---

# 4. Markdown

Markdown ist das führende Dokumentformat.

Alle automatisch erzeugten Dokumente werden zunächst als Markdown erstellt.

Markdown-Dateien werden nicht manuell bearbeitet.

Bearbeitet werden ausschließlich die Templates.

---

# 5. Pandoc

Pandoc erzeugt aus den Markdown-Dateien weitere Ausgabeformate.

Geplant sind insbesondere

* PDF
* HTML

Weitere Formate können später ergänzt werden.

---

# 6. Ergebnisverzeichnis

Jeder Simulationslauf erhält ein eigenes Verzeichnis.

Beispiel:

```text
results/
└── 2026-07-19_18-42-15/
    ├── config.json
    ├── manifest.json
    ├── data/
    ├── figures/
    ├── tables/
    ├── report.md
    ├── report.pdf
    └── report.html
```

Frühere Simulationsläufe werden niemals überschrieben.

---

# 7. Reproduzierbarkeit

Alle Dokumente entstehen ausschließlich aus

* den Eingabedaten,
* den Simulationsergebnissen,
* den verwendeten Templates.

Eine manuelle Nachbearbeitung ist nicht vorgesehen.

---

# 8. Dokumentstruktur

Die wissenschaftliche Dokumentation orientiert sich an der Struktur des Projektverzeichnisses.

Einzelne Kapitel können aus eigenen Templates erzeugt werden.

Beispiele:

* Ergebnisse
* Diskussion
* Zusammenfassung

Dadurch können einzelne Kapitel unabhängig weiterentwickelt werden.

---

# 9. Ziel

Die Dokumentenerzeugung ist Bestandteil der Simulationsumgebung.

Jeder Simulationslauf soll automatisch einen vollständigen, nachvollziehbaren und reproduzierbaren Bericht erzeugen, dessen Inhalt ausschließlich auf den berechneten Ergebnissen basiert.
