# Modellierungsentscheidungen

Dieses Dokument beschreibt die fachlichen Modellierungsentscheidungen des Projekts.

Im Gegensatz zu den Architekturentscheidungen (ADR) werden hier keine Softwareentwurfsentscheidungen dokumentiert, sondern die Abbildung thermodynamischer Systeme auf das Simulationsmodell.

---

# MD-001 – Komponentenmodell

Eine thermodynamische Anlage besteht aus einer Menge von Komponenten.

Komponenten repräsentieren reale technische Geräte, beispielsweise

- Wärmepumpe
- Verdampfer
- Turbine
- Kondensator
- Pumpe
- Wärmetauscher
- Generator

Jede Komponente besitzt einen eindeutigen `Identifier`.

Die eigentliche thermodynamische Berechnung einer Komponente erfolgt innerhalb der Komponente.

---

# MD-002 – Ports

Komponenten besitzen Ports.

Ein Port beschreibt einen definierten Anschluss einer Komponente.

Typische Ports sind beispielsweise

- NH3.in
- NH3.out
- Water.in
- Water.out
- Electrical.in
- Electrical.out

Ports dienen ausschließlich der Beschreibung der Anlagenstruktur.

Sie führen selbst keine thermodynamischen Berechnungen durch.

---

# MD-003 – Connections

Komponenten werden über Connections miteinander verbunden.

Eine Connection beschreibt den Materialfluss zwischen genau zwei Ports.

Eine Connection besitzt

- einen Identifier
- einen Quell-Port
- einen Ziel-Port
- genau einen StatePoint

Connections gehören zur Simulation und nicht zu einzelnen Komponenten.

Dadurch kann die vollständige Anlagenstruktur zentral beschrieben und analysiert werden.

---

# MD-004 – StatePoint

Ein StatePoint beschreibt ausschließlich den thermodynamischen Zustand eines Stoffstromes.

Ein StatePoint enthält ausschließlich Zustandsgrößen, beispielsweise

- Druck
- Temperatur
- Enthalpie
- Entropie
- Dichte
- Massenstrom
- Dampfgehalt

Ein StatePoint beschreibt keine Beziehungen zwischen Komponenten.

Ein StatePoint besitzt derzeit einen Identifier. Dieser dient der eindeutigen Identifikation während der Entwicklung und wird vorerst beibehalten.

---

# MD-005 – Simulation

Eine Simulation beschreibt genau eine thermodynamische Anlage.

Sie besitzt Registries für

- Komponenten
- Connections
- StatePoints

Weitere Registries können später ergänzt werden.

Die Simulation bildet den zentralen Container des gesamten Anlagenmodells.

---

# MD-006 – Registry

Alle dauerhaft existierenden Objekte werden über Registries verwaltet.

Registries verhindern doppelte Identifier.

Registries bilden den zentralen Zugriffspunkt für Objekte eines Typs.

Komponenten besitzen deshalb keine direkten Referenzen auf andere Komponenten.

Die Anlagenstruktur ergibt sich ausschließlich aus den Connections.

---

# MD-007 – Solver

Der Solver steuert die Berechnung einer Simulation.

Der Solver enthält keine thermodynamischen Modelle.

Die thermodynamischen Berechnungen erfolgen ausschließlich innerhalb der Komponenten.

Der Solver bestimmt lediglich Reihenfolge und Ablauf der Berechnung.

---

# MD-008 – Thermodynamische Zustände

Thermodynamische Zustände werden ausschließlich durch StatePoints beschrieben.

Connections transportieren StatePoints.

Komponenten lesen die StatePoints ihrer Eingangs-Connections und erzeugen daraus die StatePoints ihrer Ausgangs-Connections.

Dadurch ergibt sich ein durchgängiger Materialfluss durch die gesamte Anlage.

---

# MD-009 – Anlagenstruktur

Die Anlagenstruktur wird vollständig durch

- Komponenten
- Ports
- Connections

beschrieben.

Die Thermodynamik ist davon unabhängig.

Dadurch kann die Anlagenstruktur validiert werden, bevor thermodynamische Berechnungen durchgeführt werden.

---

# MD-010 – Trennung von Struktur und Berechnung

Die Beschreibung der Anlage und die Berechnung der Anlage sind zwei getrennte Aufgaben.

Die Klassen

- Simulation
- Component
- Port
- Connection
- StatePoint

beschreiben ausschließlich das Modell der Anlage.

Die eigentlichen thermodynamischen Berechnungen erfolgen erst durch die später implementierten Komponentenmodelle.

Diese Trennung ermöglicht eine unabhängige Entwicklung der Softwarearchitektur und der thermodynamischen Modelle.

---

# MD-011 – Entwicklungsstrategie

Die Entwicklung erfolgt schrittweise.

Zunächst werden

- Datenmodell
- Infrastruktur
- Solver

vollständig aufgebaut und getestet.

Erst anschließend werden thermodynamische Modelle implementiert.

Dadurch bleibt jeder Entwicklungsschritt nachvollziehbar und reproduzierbar.
