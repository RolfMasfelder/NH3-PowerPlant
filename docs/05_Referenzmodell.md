# Referenzmodell

**Projekt:** NH3-PowerPlant

**Dokument:** 05_Referenzmodell.md

**Version:** 0.1 (Entwurf)

---

# 1 Ziel des Referenzmodells

Vor jeder Optimierung ist eine eindeutig definierte Ausgangsanlage erforderlich.

Das Referenzmodell beschreibt eine technisch realisierbare Grundkonfiguration, an der sämtliche späteren Varianten gemessen werden.

Es handelt sich bewusst nicht um die optimale Anlage, sondern um ein möglichst einfaches und nachvollziehbares Basismodell.

Alle späteren Änderungen werden ausschließlich gegenüber diesem Referenzmodell bewertet.

---

# 2 Anforderungen

Das Referenzmodell soll

- thermodynamisch konsistent sein,
- mit heutigen Komponenten grundsätzlich realisierbar sein,
- möglichst wenige Freiheitsgrade besitzen,
- reproduzierbare Berechnungen ermöglichen,
- als Ausgangspunkt für Variantenuntersuchungen dienen.

---

# 3 Systemgrenzen

Das Referenzmodell umfasst sämtliche Komponenten zwischen der Wärmequelle und dem elektrischen Generator.

Nicht Bestandteil des Referenzmodells sind

- wirtschaftliche Betrachtungen,
- Regelungstechnik,
- Sicherheitskonzepte,
- mechanische Konstruktion,
- Rohrleitungsdimensionierung.

Diese Themen werden erst nach Abschluss der thermodynamischen Untersuchung betrachtet.

---

# 4 Anlagenübersicht

Das Referenzmodell besteht aus folgenden Hauptkomponenten:

1. Wasserreservoir
2. Wärmepumpe
3. NH₃-Verdampfer
4. NH₃-Turbine
5. Generator
6. NH₃-Kondensator
7. Speisepumpe
8. Wasserkreislauf

Alle Komponenten arbeiten stationär.

Zeitabhängige Vorgänge werden zunächst nicht betrachtet.

---

# 5 Referenzparameter

Für alle Berechnungen der ersten Projektphase werden einheitliche Randbedingungen verwendet.

| Parameter | Wert |
|-----------|------|
| Wärmequelle | Wasser |
| Temperatur Reservoir | 8 °C |
| Austritt Wärmepumpe | 80 °C |
| Umgebungstemperatur | 20 °C |
| Arbeitsmedium ORC | NH₃ |
| Betriebsart | stationär |
| Zielgröße | 100 kW elektrische Leistung |

Diese Werte dienen ausschließlich als Referenz.

Spätere Sensitivitätsanalysen untersuchen die Auswirkungen geänderter Randbedingungen.

---

# 6 Modellannahmen

Zur Vereinfachung werden zunächst folgende Annahmen getroffen.

## Wärmequelle

Das Wasserreservoir besitzt eine konstante Temperatur.

Die entnommene Wärme verändert seine Temperatur nicht.

---

## Wärmepumpe

Die Wärmepumpe arbeitet stationär.

Der COP wird zunächst als konstanter Parameter vorgegeben.

Später wird der COP aus den tatsächlichen Betriebsbedingungen berechnet.

---

## NH₃-Kreisprozess

Der Kreisprozess arbeitet geschlossen.

Es treten keine Stoffverluste auf.

Druckverluste in Rohrleitungen werden zunächst vernachlässigt.

---

## Turbine

Der isentrope Wirkungsgrad wird zunächst vorgegeben.

Mechanische Verluste werden später ergänzt.

---

## Generator

Konstanter Wirkungsgrad.

Keine Teillastbetrachtung.

---

## Kondensator

Vollständige Kondensation.

Konstanter Kühlwassermassenstrom.

---

## Speisepumpe

Konstanter hydraulischer Wirkungsgrad.

---

# 7 Bilanzgrenzen

Für jede Komponente werden später getrennte Bilanzen erstellt.

Diese umfassen

- Massenbilanz
- Energiebilanz
- Exergiebilanz

Dadurch kann jede Komponente unabhängig bewertet werden.

---

# 8 Referenz-Betriebspunkt

Der erste Betriebspunkt dient ausschließlich der Modellvalidierung.

Dabei werden

- Temperaturen,
- Drücke,
- Enthalpien,
- Entropien,
- Massenströme

für sämtliche Zustandsgrößen bestimmt.

Dieser Betriebspunkt bildet die Grundlage aller weiteren Berechnungen.

---

# 9 Modellvereinfachungen

Folgende Effekte werden zunächst nicht berücksichtigt.

- Wärmeverluste der Rohrleitungen
- Druckverluste außerhalb der Hauptkomponenten
- Wärmeleitung innerhalb von Bauteilen
- Wärmespeicherung
- dynamisches Verhalten
- Anfahrvorgänge
- Alterung der Komponenten

Diese Vereinfachungen ermöglichen eine übersichtliche Grundstruktur des Berechnungsmodells.

Sie werden in späteren Projektphasen schrittweise aufgehoben.

---

# 10 Zielgrößen

Für jeden Simulationslauf werden mindestens folgende Größen bestimmt.

## Thermodynamik

- Druck
- Temperatur
- Enthalpie
- Entropie
- Dampfgehalt

## Energie

- Heizleistung
- Turbinenleistung
- Pumpenleistung
- Generatorleistung
- Kondensationsleistung

## Exergie

- Exergiestrom
- Exergieverlust
- Exergiewirkungsgrad

---

# 11 Bewertungskriterien

Das Referenzmodell wird anhand folgender Kriterien beurteilt.

- thermodynamische Konsistenz
- numerische Stabilität
- Reproduzierbarkeit
- Nachvollziehbarkeit
- Erweiterbarkeit

Das Referenzmodell muss nicht den höchsten Wirkungsgrad besitzen.

Es dient ausschließlich als Vergleichsbasis für alle späteren Optimierungen.

---

# 12 Weiterentwicklung

Ausgehend vom Referenzmodell werden anschließend verschiedene Anlagenvarianten entwickelt.

Hierzu gehören insbesondere

- Rückführung der Kondensationswärme,
- mehrstufige Wärmeübertrager,
- Rekuperation,
- Variation der Verdampfungs- und Kondensationstemperaturen,
- Variation des COP,
- Optimierung der Massenströme,
- Exergieoptimierung.

Jede Variante wird vollständig neu berechnet und mit dem Referenzmodell verglichen.

---

# 13 Zusammenfassung

Das Referenzmodell bildet die gemeinsame Ausgangsbasis der gesamten Untersuchung.

Durch die klare Definition aller Randbedingungen können sämtliche späteren Änderungen eindeutig bewertet werden.

Die Qualität der Untersuchung hängt entscheidend davon ab, dass alle Varianten ausschließlich auf Änderungen gegenüber diesem Referenzmodell beruhen.

Aus diesem Grund wird das Referenzmodell nach seiner Validierung nicht mehr verändert.

Erweiterungen erfolgen ausschließlich durch neue Anlagenvarianten.
