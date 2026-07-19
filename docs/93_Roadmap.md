# Roadmap

## Dokumentstatus

| Eigenschaft | Wert |
|-------------|------|
| Dokument | 93_Roadmap.md |
| Version | 0.1 (Entwurf) |
| Bearbeitungsstand | Entwurf |
| Letzte Änderung | 19.07.2026 |
| Autor | Projekt NH3-PowerPlant |

---

## 1 Ziel der Roadmap

Die Roadmap beschreibt die geplante Entwicklungsreihenfolge des Projekts.

Sie verbindet die fachliche Untersuchung mit der Softwareentwicklung und legt fest, welche Voraussetzungen erfüllt sein müssen, bevor spätere Anlagenvarianten untersucht werden.

Der Schwerpunkt liegt zunächst auf einem reproduzierbaren Referenzmodell. Optimierungen und Variantenvergleiche folgen erst danach.

---

## 2 Leitprinzipien

Die Entwicklung folgt diesen Grundsätzen:

- zuerst eindeutige Begriffe und Datenverträge,
- dann einfache, überprüfbare Modelle,
- danach automatisierte Auswertung,
- erst anschließend Varianten und Optimierungen.

Jeder Entwicklungsschritt soll durch Tests, strukturierte Ergebnisdaten oder automatisch erzeugte Dokumentation überprüfbar sein.

---

## 3 Phase 1: Grundlagen konsolidieren

Ziel dieser Phase ist ein konsistenter Projekt- und Datenrahmen.

Aufgaben:

1. Abhängigkeiten im Python-Projekt korrekt einordnen.
2. README und Projektdokumentation an die aktuelle Paketstruktur anpassen.
3. Scope der ersten Projektphase festlegen.
4. Ergebnismodell definieren.
5. Begriffe zwischen Dokumentation, Templates und Quellcode vereinheitlichen.

Ergebnis dieser Phase:

- ein konsistenter Projektüberblick,
- ein dokumentierter Ergebnisdatenvertrag,
- eine klare Abgrenzung des ersten Referenzmodells.

---

## 4 Phase 2: Stoffdaten und Zustände

Ziel dieser Phase ist die reproduzierbare Berechnung thermodynamischer Zustände.

Aufgaben:

1. Stoffdaten-Schnittstelle definieren.
2. CoolProp als Stoffdatenquelle anbinden.
3. NH3 als erstes Arbeitsmedium unterstützen.
4. Ein internes Einheitensystem festlegen.
5. StatePoints aus unabhängigen Zustandspaaren ableiten.
6. Plausibilitätsprüfungen für unvollständige oder widersprüchliche Zustände ergänzen.

Ergebnis dieser Phase:

- StatePoints können mit realen Stoffdaten befüllt werden,
- Stoffdatenberechnungen sind getestet und reproduzierbar,
- manuell eingetragene Stoffwerte werden vermieden.

---

## 5 Phase 3: Einfache Komponentenmodelle

Ziel dieser Phase ist ein berechenbarer thermodynamischer Minimalprozess.

Die erste Implementierungsreihenfolge lautet:

1. Pumpe
2. Turbine
3. Verdampfer
4. Kondensator
5. Generator
6. Wärmepumpe

Jede Komponente besitzt mindestens:

- definierte Eingangs- und Ausgangszustände,
- eine Energiebilanz,
- überprüfbare Kennwerte,
- Unit-Tests.

Exergiebilanzen werden vorbereitet und ergänzt, sobald die energetischen Modelle stabil sind.

---

## 6 Phase 4: Referenzmodell Variante A

Ziel dieser Phase ist der erste vollständige Simulationslauf der Referenzanlage.

Randbedingungen:

- Wasserreservoir bei 8 °C,
- Wärmepumpen-Austritt bei 80 °C,
- NH3 als Arbeitsmedium des Kraftwerksprozesses,
- stationärer Betrieb,
- 100 kW elektrische Zielleistung,
- zunächst vorgegebene Wirkungsgrade und COP-Werte.

Aufgaben:

1. Referenzanlage aus Komponenten, Ports, Connections und StatePoints aufbauen.
2. Sequenziellen Solver für den ersten Betriebspunkt verwenden.
3. Massen- und Energiebilanzen prüfen.
4. Ergebnisdaten strukturiert speichern.
5. Reproduzierbarkeit des Laufs dokumentieren.

Ergebnis dieser Phase:

- ein lauffähiges Referenzmodell,
- ein maschinenlesbares Ergebnis,
- eine überprüfbare Ausgangsbasis für alle Varianten.

---

## 7 Phase 5: Automatische Berichtsgenerierung

Ziel dieser Phase ist die automatische Dokumentation eines Simulationslaufs.

Aufgaben:

1. Ergebnisdaten nach JSON exportieren.
2. Jinja2-Templates mit Ergebnisdaten rendern.
3. Ergebnis- und Diskussionskapitel als Markdown erzeugen.
4. Tabellen und Diagrammreferenzen aus strukturierten Daten ableiten.
5. Später PDF und HTML über Pandoc erzeugen.

Ergebnis dieser Phase:

- kein manuelles Übertragen von Berechnungsergebnissen,
- reproduzierbare Ergebnisberichte,
- klare Trennung zwischen Berechnung und Dokumentation.

---

## 8 Phase 6: Variantenvergleich

Ziel dieser Phase ist die Untersuchung der in Kapitel 07 beschriebenen Anlagenvarianten.

Varianten:

- Variante A: Referenzanlage ohne Wärmerückgewinnung,
- Variante B: Vorwärmung des Wärmepumpen-Quellstroms,
- Variante C: mehrstufige Kondensation,
- Variante D: mehrstufige Kondensation mit Rekuperation.

Vor Beginn dieser Phase muss Variante A reproduzierbar laufen.

Für Varianten mit Rückkopplungen werden iterative Solver und Konvergenzkriterien ergänzt.

---

## 9 Phase 7: Sensitivitätsanalyse und Bewertung

Ziel dieser Phase ist die systematische Bewertung der Einflussgrößen.

Untersucht werden insbesondere:

- Quellentemperatur,
- Zieltemperatur der Wärmepumpe,
- COP,
- Turbinenwirkungsgrad,
- Generatorwirkungsgrad,
- Kondensationstemperatur,
- Arbeitsmedium.

Ergebnis dieser Phase:

- Vergleichstabellen,
- Wirkungsgrad- und Verlustdiagramme,
- Energie- und Exergiebilanzen,
- Beantwortung der Forschungsfrage.

---

## 10 Nichtziele der ersten Entwicklungsphase

Nicht Bestandteil der ersten Phase sind:

- Wirtschaftlichkeitsrechnung,
- Regelungstechnik,
- Sicherheitskonzept,
- Rohrleitungsdimensionierung,
- dynamische Simulation,
- mechanische Detailkonstruktion,
- reale Anlagensteuerung.

Diese Themen können später ergänzt werden, sobald die thermodynamische Grundlage belastbar ist.
