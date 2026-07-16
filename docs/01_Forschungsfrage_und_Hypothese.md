# Forschungsfrage und Hypothese

## Dokumentstatus

| Eigenschaft | Wert |
|-------------|------|
| Dokument | 01_Forschungsfrage_und_Hypothese.md |
| Version | 0.1 (Entwurf) |
| Bearbeitungsstand | Entwurf |
| Letzte Änderung | 15.07.2026 |
| Autor | Projekt NH3-PowerPlant |

---

## 1 Einleitung

Das vorliegende Projekt entstand aus einer zunächst ungewöhnlich erscheinenden Fragestellung:

> Kann eine Wärmepumpe innerhalb eines thermodynamischen Kreisprozesses die Funktion der klassischen Feuerung übernehmen?

Diese Fragestellung unterscheidet sich grundlegend von der klassischen Betrachtung einer Wärmepumpe als Verbraucher elektrischer Energie. Stattdessen wird die Wärmepumpe als integraler Bestandteil einer Wärmekraftmaschine betrachtet.

Das Projekt verfolgt ausdrücklich nicht das Ziel, bekannte thermodynamische Gesetze in Frage zu stellen. Vielmehr soll untersucht werden, welche Möglichkeiten sich ergeben, wenn Wärmepumpe, Kreisprozess und Wärmerückgewinnung konsequent als Gesamtsystem entwickelt werden.

---

## 2 Wissenschaftliche Ausgangslage

Thermische Kraftwerke nutzen eine Wärmequelle mit möglichst hoher Temperatur, um einen Kreisprozess anzutreiben.

Die maximale Effizienz wird durch den Carnot-Wirkungsgrad begrenzt.

Eine Wärmepumpe dagegen nutzt mechanische oder elektrische Arbeit, um Wärme von einem niedrigen auf ein höheres Temperaturniveau anzuheben.

Beide Systeme werden in der Technik üblicherweise unabhängig voneinander betrachtet.

Eine direkte Kopplung erfolgt bislang hauptsächlich

- zur Nutzung industrieller Abwärme,
- in Geothermieanlagen,
- bei Organic-Rankine-Cycles (ORC),
- sowie in einigen Forschungsprojekten zur Kraft-Wärme-Kopplung.

Gemeinsam ist diesen Anlagen, dass die Wärmepumpe lediglich vorhandene Wärmequellen verbessert oder zusätzliche Abwärme nutzbar macht.

Sie übernimmt jedoch nicht die Rolle des eigentlichen Wärmeerzeugers innerhalb eines geschlossenen Kraftwerksprozesses.

---

## 3 Forschungsfrage

Aus dieser Überlegung ergibt sich die eigentliche Forschungsfrage.

> Welche thermodynamischen Eigenschaften besitzt eine Kraftwerksarchitektur, deren primäre Wärmequelle aus einer Wärmepumpe besteht, die ihre Energie einem großvolumigen Niedertemperaturreservoir entzieht?

Hieraus ergeben sich mehrere Teilfragen.

### 3.1 Kreisprozess

Welcher thermodynamische Kreisprozess eignet sich für Vorlauftemperaturen von etwa 80 °C?

Ist Ammoniak (NH₃) als Arbeitsmedium geeignet?

Welche Alternativen existieren?

---

### 3.2 Wärmepumpe

Welche Leistungszahl (COP) ist unter realistischen Betriebsbedingungen erreichbar?

Welchen Einfluss besitzt die Temperatur des Reservoirs?

Welchen Einfluss besitzt die Kondensationstemperatur?

---

### 3.3 Wärmeübertragung

Welche Verluste entstehen im Verdampfer?

Welche Verluste entstehen im Kondensator?

Wie wirken sich mehrstufige Wärmeübertrager aus?

---

### 3.4 Turbine

Welche Turbinenkonzepte eignen sich für niedrige Verdampfungsdrücke?

Welche Leistungen können bei moderaten Temperaturen erreicht werden?

---

### 3.5 Gesamtsystem

Welche Komponente bestimmt den Gesamtwirkungsgrad?

Wo entstehen die größten Exergieverluste?

Welche Optimierungsansätze besitzen das größte Potential?

---

## 4 Die eigentliche Hypothese

Die Untersuchung basiert auf folgender Arbeitshypothese.

> **Eine konsequent thermisch gekoppelte Anlagenarchitektur aus Wärmepumpe, NH₃-Kreisprozess und interner Wärmerückgewinnung kann die Exergieausnutzung gegenüber einer konventionellen Niedertemperatur-Kraftwerksanlage verbessern, ohne die thermodynamischen Hauptsätze zu verletzen.**

Diese Formulierung enthält bewusst keine Aussage darüber,

- dass elektrische Überschüsse entstehen,
- dass ein autarker Betrieb möglich ist,
- oder dass bekannte Wirkungsgradgrenzen überschritten werden.

Die Hypothese beschränkt sich ausschließlich auf die Verbesserung der Nutzung vorhandener Energie.

---

## 5 Präzisierung der Hypothese

Die allgemeine Hypothese lässt sich in mehrere überprüfbare Einzelhypothesen aufteilen.

### H1

Die Rückführung der Kondensationswärme reduziert die Exergieverluste des Gesamtsystems.

---

### H2

Eine mehrstufige Wärmeübertragung reduziert die irreversiblen Verluste im Kondensator.

---

### H3

Eine optimierte Wasserführung erhöht die effektive Quellentemperatur der Wärmepumpe.

---

### H4

Die Verbesserung der Quellentemperatur erhöht den real erreichbaren COP der Wärmepumpe.

---

### H5

Die Verbesserung des COP kompensiert einen Teil der Verluste des NH₃-Kreisprozesses.

---

### H6

Die größte Optimierungsreserve liegt nicht in der Turbine, sondern in der thermischen Kopplung der einzelnen Wärmeübertrager.

---

## 6 Nullhypothese

Der wissenschaftliche Vergleich erfordert eine Nullhypothese.

Diese lautet:

> **Die vorgeschlagene thermische Kopplung führt gegenüber einer klassischen ORC-Anlage zu keiner signifikanten Verbesserung der exergetischen Gesamtbilanz.**

Alle späteren Berechnungen werden gegen diese Nullhypothese bewertet.

---

## 7 Bewertungsgrößen

Zur Überprüfung der Hypothesen werden mehrere Kenngrößen verwendet.

## Energiebilanz

- Wärmeströme
- elektrische Leistung
- mechanische Leistung

---

## Exergiebilanz

- Exergieverluste
- Exergiewirkungsgrad
- lokale Exergiedissipation

---

## Kreisprozess

- Turbinenwirkungsgrad
- Pumpenarbeit
- Verdampfungsleistung
- Kondensationsleistung

---

## Wärmepumpe

- COP
- Temperaturhub
- Verdampfungstemperatur
- Kondensationstemperatur

---

## Gesamtsystem

- Nettoleistung
- Gesamtwirkungsgrad
- exergetischer Gesamtwirkungsgrad
- Sensitivität gegenüber Temperaturänderungen

---

## 8 Untersuchungsstrategie

Die Untersuchung erfolgt schrittweise.

### Phase 1

Thermodynamische Grundlagen

---

### Phase 2

Referenzanlage

Klassischer NH₃-Kreisprozess ohne Wärmerückgewinnung.

---

### Phase 3

Variante B

Nutzung der Kondensationswärme zur Vorwärmung des Wärmepumpen-Quellstroms.

---

### Phase 4

Variante C

Mehrstufige Kondensation.

---

### Phase 5

Variante D

Mehrstufige Kondensation mit interner Rekuperation.

---

### Phase 6

Vergleich aller Varianten anhand

- Energie
- Exergie
- Wirkungsgrad
- technischer Realisierbarkeit

---

## 9 Abgrenzung

Nicht Bestandteil dieser Untersuchung sind zunächst

- wirtschaftliche Bewertungen,
- Investitionskosten,
- Amortisationszeiten,
- Genehmigungsfragen,
- Sicherheitsbetrachtungen,
- Detailkonstruktionen einzelner Komponenten.

Diese Themen können in einer späteren Projektphase ergänzt werden.

---

## 10 Eigene Anmerkung

Obwohl die Untersuchung von einer ungewöhnlichen Grundidee ausgeht, verfolgt sie ausdrücklich einen klassischen ingenieurwissenschaftlichen Ansatz.

Es wird weder versucht, den Energieerhaltungssatz noch den zweiten Hauptsatz der Thermodynamik zu umgehen.

Vielmehr soll untersucht werden, ob durch eine systematische Betrachtung aller Energie- und Exergieströme bisher wenig beachtete Optimierungspotentiale sichtbar werden.

Die eigentliche wissenschaftliche Fragestellung lautet daher nicht:

> *Kann ein selbstlaufendes Kraftwerk gebaut werden?*

sondern

> *Welche thermodynamischen Grenzen besitzt eine Kraftwerksarchitektur, bei der Wärmepumpe, Kreisprozess und Wärmerückgewinnung nicht getrennt, sondern als gemeinsames System entwickelt werden?*

Diese Fragestellung bildet den Leitgedanken aller folgenden Kapitel.
