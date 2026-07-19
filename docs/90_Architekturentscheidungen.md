# Architekturentscheidungen (ADR)

Dieses Dokument enthält die dauerhaft gültigen Architekturentscheidungen des Projekts.

Es orientiert sich an den *Architecture Decision Records (ADR)* nach Michael Nygard, verwendet jedoch bewusst eine kompakte Form. Nur Entscheidungen, die einer Erläuterung bedürfen, enthalten zusätzliche Abschnitte.

---

## ADR-001 – Python 3.13

**Status**

Accepted

Python 3.13 ist die verbindliche Programmiersprache des Projekts.

---

## ADR-002 – Projektstruktur

**Status**

Accepted

Der Quellcode wird fachlich in eigenständige Pakete gegliedert.

Aktuelle Struktur:

```text
core/
components/
connection/
ports/
simulation/
solver/
state/
```

Weitere Pakete werden ausschließlich nach fachlichen Gesichtspunkten ergänzt.

---

## ADR-003 – Eindeutige Identifikation

**Status**

Accepted

Alle dauerhaft existierenden Objekte besitzen einen eindeutigen `Identifier`.

Der `Identifier` dient als Primärschlüssel innerhalb des Simulationsmodells.

---

## ADR-004 – Registries

**Status**

Accepted

Objekte werden in generischen `Registry`-Klassen verwaltet.

Registries verhindern doppelte Identifier und ermöglichen einen zentralen Zugriff auf alle Objekte eines Typs.

---

## ADR-005 – Komponentenmodell

**Status**

Accepted

Alle physikalischen Geräte werden von der abstrakten Basisklasse `Component` abgeleitet.

Die eigentliche thermodynamische Berechnung erfolgt innerhalb der jeweiligen Komponente.

---

## ADR-006 – Simulationsmodell

**Status**

Accepted

Eine `Simulation` beschreibt eine vollständige thermodynamische Anlage.

Sie besitzt Registries für Komponenten, Zustände und Verbindungen.

---

## ADR-007 – Reproduzierbarkeit

**Status**

Accepted

Jeder Simulationslauf muss vollständig reproduzierbar sein.

Zu jedem Lauf werden sämtliche Eingabedaten, Ergebnisse sowie die verwendete Softwareversion dokumentiert.

---

## ADR-008 – Dokumentenerzeugung

**Status**

Accepted

Alle wissenschaftlichen Berichte werden automatisiert aus Jinja2-Templates erzeugt.

Markdown ist das führende Dokumentformat.

Weitere Ausgabeformate (PDF, HTML) werden daraus erzeugt.

---

## ADR-009 – Trennung von Infrastruktur und Thermodynamik

**Status**

Accepted

## Entscheidung

Die Softwareinfrastruktur wird vollständig entwickelt und getestet, bevor thermodynamische Modelle implementiert werden.

## Begründung

Dadurch bleiben Softwarearchitektur und thermodynamische Modellierung voneinander getrennt.

Die Infrastruktur kann unabhängig getestet werden.

Thermodynamische Modelle können später ergänzt oder ausgetauscht werden, ohne Änderungen an der grundlegenden Softwarearchitektur zu erzwingen.

Diese Entscheidung erleichtert außerdem die wissenschaftliche Nachvollziehbarkeit und reduziert das Risiko grundlegender Architekturänderungen während der Implementierung der Fachmodelle.

---

## ADR-010 – Repository als Wissensbasis

**Status**

Accepted

Das Git-Repository ist die maßgebliche Quelle für Architektur- und Modellierungsentscheidungen.

Chatverläufe dienen ausschließlich der gemeinsamen Entwicklung und werden nicht als dauerhafte Projektdokumentation betrachtet.
