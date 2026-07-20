# Berechnungskonzept (Entwurf)

**Status:** Draft

## Zielsetzung

Dieses Dokument beschreibt das geplante Berechnungskonzept der Simulationssoftware. Es stellt keine Implementierung dar, sondern definiert die fachlichen Leitlinien für die spätere Entwicklung.

Die Berechnung soll stationäre thermodynamische Kreisprozesse reproduzierbar simulieren und die Grundlage für wissenschaftlich belastbare Untersuchungen bilden.

---

# 1. Grundprinzip

Die Simulationssoftware trennt konsequent zwischen

* Anlagenstruktur
* thermodynamischer Berechnung
* Dokumentenerzeugung

Dadurch können diese Bereiche unabhängig voneinander entwickelt, getestet und erweitert werden.

---

# 2. Anlagenmodell

Eine Anlage besteht aus folgenden Objekten:

* Simulation
* Component
* Port
* Connection
* StatePoint

Die Beziehungen zwischen diesen Objekten sind in den Modellierungsentscheidungen beschrieben.

Die Anlagenstruktur ist vollständig definiert, bevor eine Berechnung beginnt.

---

# 3. Aufgabenverteilung

## Simulation

Die Klasse `Simulation` verwaltet sämtliche Objekte einer Anlage.

Sie enthält keine thermodynamischen Gleichungen.

Für einfache, bereits geordnete Modelle kann `Simulation.calculate()` alle registrierten Komponenten einmal in Einfügereihenfolge berechnen und anschließend die ausgehenden Connections der jeweiligen Komponente aktualisieren.

Dieser Ablauf ist ein deterministischer Einzeldurchlauf. Mehrfache Aufrufe von `Simulation.calculate()` propagieren Zustände erneut durch vorhandene Rückführungen, ersetzen aber keine Konvergenzprüfung.

---

## Solver

Der Solver steuert ausschließlich den Berechnungsablauf.

Er

* bestimmt die Reihenfolge der Berechnung,
* erkennt gegebenenfalls Iterationen,
* beendet die Berechnung nach Erreichen der Konvergenz.

Für nichtlineare oder rückgekoppelte Modelle mit Konvergenzkriterium bleibt der Solver zuständig. Er kann dazu später wiederholt `Simulation.calculate()` oder komponentenspezifische Berechnungsschritte aufrufen.

Der Solver enthält keine Gleichungen für einzelne Komponenten.

---

## Component

Jede Komponente implementiert ihr eigenes thermodynamisches Modell.

Eine Komponente

* liest die Zustände ihrer Eingangs-Connections,
* berechnet ihre Energiebilanz,
* bestimmt die Zustände ihrer Ausgangs-Connections.

Die Komponente besitzt das vollständige Wissen über ihr physikalisches Verhalten.

---

## Connection

Connections transportieren Stoffströme zwischen Komponenten.

Eine Connection besitzt genau einen StatePoint.

Connections führen keine thermodynamischen Berechnungen durch. Sie übertragen den StatePoint des Quellports auf den Zielport.

---

## StatePoint

StatePoints beschreiben ausschließlich thermodynamische Zustände.

Typische Zustandsgrößen sind

* Druck
* Temperatur
* Enthalpie
* Entropie
* Dichte
* Massenstrom
* Dampfgehalt

Ein StatePoint besitzt keine Kenntnis über die Anlagenstruktur.

---

# 4. Stoffwerte

Die Berechnung der Stoffwerte erfolgt mit CoolProp.

CoolProp dient ausschließlich als Stoffdatenbibliothek.

Die eigentlichen Bilanzgleichungen werden nicht an CoolProp delegiert, sondern innerhalb der jeweiligen Komponenten implementiert.

Dadurch bleiben sämtliche Berechnungsschritte nachvollziehbar und überprüfbar.

---

# 5. Komponentenmodelle

Alle Komponenten besitzen dieselbe äußere Schnittstelle.

Die innere Berechnung ist komponentenspezifisch.

Beispiele:

* Turbine
* Verdichter
* Pumpe
* Verdampfer
* Kondensator
* Wärmetauscher
* Wärmepumpe

Neue Komponenten können ergänzt werden, ohne den Solver ändern zu müssen.

---

# 6. Arbeitsmedien

Das erste Referenzarbeitsmedium ist NH₃.

Die Software soll so aufgebaut werden, dass weitere Arbeitsmedien später ergänzt werden können.

Die Auswahl des Arbeitsmediums darf keine Änderungen an der Simulationsarchitektur erfordern.

---

# 7. Berechnungsablauf

Der grundsätzliche Ablauf einer Berechnung lautet:

1. Einlesen der Konfiguration
2. Aufbau der Anlagenstruktur
3. Konsistenzprüfung
4. Initialisierung der StatePoints
5. Durchführung der Simulation
6. Konvergenzprüfung
7. Ausgabe der Ergebnisse
8. Erstellung der Dokumentation

---

# 8. Ergebnisse

Die Simulation erzeugt ausschließlich strukturierte Daten.

Hierzu gehören insbesondere

* StatePoints
* Komponentenkennwerte
* Energiebilanzen
* Wirkungsgrade
* Verlustleistungen

Diese Daten bilden die einzige Grundlage für sämtliche Tabellen, Diagramme und Berichte.

Es werden keine Berechnungsergebnisse manuell in Dokumente übernommen.

---

# 9. Reproduzierbarkeit

Jeder Simulationslauf wird vollständig dokumentiert.

Zu jedem Lauf gehören mindestens

* config.json
* manifest.json
* numerische Ergebnisse
* Diagramme
* automatisch erzeugte Berichte

Ein Simulationslauf muss zu einem späteren Zeitpunkt mit identischen Eingangsdaten reproduzierbar sein.

---

# 10. Erweiterbarkeit

Die Softwarearchitektur ist so ausgelegt, dass

* neue Komponenten,
* neue Arbeitsmedien,
* neue Solver,
* neue Auswerteverfahren

ergänzt werden können, ohne bestehende Komponenten grundlegend ändern zu müssen.

Die langfristige Wartbarkeit besitzt Vorrang vor einer möglichst kompakten Implementierung.

---

# 11. Ziel

Das Projekt soll eine nachvollziehbare und reproduzierbare wissenschaftliche Simulationsumgebung für gekoppelte thermodynamische Kreisprozesse bereitstellen.

Die physikalischen Modelle sollen transparent implementiert sein, sodass sämtliche Berechnungsschritte überprüft und dokumentiert werden können.
