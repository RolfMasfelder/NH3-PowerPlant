# Variantenvergleich

**Projekt:** NH3-PowerPlant

**Dokument:** 07_Variantenvergleich.md

**Version:** 0.1 (Entwurf)

---

# 1 Zielsetzung

Nach der Definition des Referenzmodells und der Entwicklung des Berechnungsmodells werden verschiedene Anlagenvarianten miteinander verglichen.

Ziel des Variantenvergleichs ist nicht die Identifikation einer einzelnen optimalen Lösung, sondern das Verständnis der Auswirkungen unterschiedlicher thermodynamischer Kopplungen auf die Gesamtanlage.

Alle Varianten werden unter identischen Randbedingungen simuliert.

Dadurch können Unterschiede eindeutig auf die jeweilige Anlagenarchitektur zurückgeführt werden.

---

# 2 Vergleichsmethodik

Alle Varianten werden mit identischen

- Stoffdaten,
- Umgebungstemperaturen,
- Wärmequellen,
- Generatorwirkungsgraden,
- Turbinenwirkungsgraden

berechnet.

Änderungen betreffen ausschließlich die jeweilige Anlagenarchitektur.

---

# 3 Referenzvariante (Variante A)

Die Referenzanlage entspricht Kapitel 05.

Eigenschaften:

- einfache Anlagenstruktur
- keine Wärmerückgewinnung
- einstufige Kondensation
- keine Rekuperation

Sie bildet den Nullpunkt sämtlicher Vergleiche.

---

# 4 Variante B

## Vorwärmung des Wärmepumpen-Quellstroms

Die Kondensationswärme des NH₃-Kreisprozesses wird über einen Wärmeübertrager genutzt, um den Quellstrom der Wärmepumpe vorzuwärmen.

Ziel:

- Erhöhung der Quellentemperatur
- Verbesserung des COP
- Reduzierung der Exergieverluste

---

# 5 Variante C

## Mehrstufige Kondensation

Die Kondensation erfolgt nicht mehr in einem einzigen Wärmeübertrager.

Mehrere Kondensationsstufen ermöglichen eine bessere Anpassung an das Temperaturprofil des Wasserkreislaufs.

Untersucht werden

- Temperaturverläufe
- Exergieverluste
- notwendige Wärmeübertragerflächen

---

# 6 Variante D

## Rekuperierte Kondensation

Zusätzlich zur mehrstufigen Kondensation werden interne Wärmeübertrager eingesetzt.

Dadurch soll

- die Temperaturdifferenz reduziert,
- die Exergievernichtung minimiert,
- der Gesamtwirkungsgrad verbessert

werden.

---

# 7 Weitere Varianten

Die Simulationssoftware soll beliebige weitere Anlagenvarianten ermöglichen.

Beispiele:

- Änderung des COP
- Variation der Verdampfungstemperatur
- Variation der Kondensationstemperatur
- Variation des Turbinenwirkungsgrades
- Variation des Generatorwirkungsgrades
- alternative Arbeitsmedien
- alternative Wärmequellen
- zusätzliche Rekuperatoren

Neue Varianten erhalten fortlaufende Kennzeichnungen.

---

# 8 Vergleichsgrößen

Für jede Variante werden identische Kenngrößen bestimmt.

## Thermodynamische Größen

- Drücke
- Temperaturen
- Massenströme
- Enthalpien
- Entropien

---

## Energetische Größen

- Heizleistung
- Turbinenleistung
- Pumpenleistung
- Generatorleistung
- Nettoleistung

---

## Exergetische Größen

- Exergiestrom
- Exergieverluste
- Exergiewirkungsgrad

---

## Wirtschaftliche Kenngrößen

Diese werden in der ersten Projektphase nicht betrachtet.

Die Software wird jedoch so aufgebaut, dass

- Investitionskosten
- Betriebskosten
- Stromgestehungskosten

später ergänzt werden können.

---

# 9 Automatisch erzeugte Vergleichstabellen

Die Vergleichstabellen werden nicht manuell erstellt.

Sie entstehen nach jedem Simulationslauf automatisch.

Geplant sind Tabellen für

- Stoffdaten
- Betriebszustände
- Energieflüsse
- Exergieflüsse
- Wirkungsgrade
- Verluste

Dadurch bleibt die Dokumentation jederzeit konsistent mit den Berechnungsergebnissen.

---

# 10 Automatisch erzeugte Diagramme

Für jede Variante werden automatisch erzeugt

- T-s-Diagramm
- p-h-Diagramm
- Sankey-Diagramm der Energieflüsse
- Sankey-Diagramm der Exergieflüsse
- Temperaturprofile der Wärmeübertrager
- COP-Diagramme
- Verlustdiagramme

Alle Diagramme werden direkt aus den Simulationsergebnissen erzeugt.

---

# 11 Bewertungsmethodik

Die Bewertung erfolgt anhand mehrerer Kriterien.

## Thermodynamische Qualität

- Energiebilanz
- Exergiebilanz
- Wirkungsgrad

## Technische Qualität

- Anlagenkomplexität
- Anzahl zusätzlicher Komponenten
- Betriebsdrücke
- Regelbarkeit

## Erweiterbarkeit

- Modularität
- Skalierbarkeit
- Eignung für andere Arbeitsmedien

Eine Gesamtbewertung ergibt sich aus der gemeinsamen Betrachtung aller Kriterien.

---

# 12 Sensitivitätsanalyse

Zusätzlich zum Variantenvergleich werden Sensitivitätsanalysen durchgeführt.

Hierbei wird jeweils nur ein Parameter verändert.

Beispiele:

- COP
- Quellentemperatur
- Vorlauftemperatur
- Turbinenwirkungsgrad
- Generatorwirkungsgrad
- Kühlwassertemperatur

Dadurch lässt sich der Einfluss einzelner Parameter auf das Gesamtsystem quantifizieren.

---

# 13 Zusammenfassung

Der Variantenvergleich stellt das zentrale Werkzeug zur Bewertung der entwickelten Anlagenarchitekturen dar.

Alle Ergebnisse beruhen auf identischen Randbedingungen und werden automatisiert aus dem Berechnungsmodell erzeugt.

Die Trennung zwischen Simulationssoftware und Dokumentation gewährleistet, dass sämtliche Tabellen, Diagramme und Bewertungen reproduzierbar sind.

Änderungen an den Eingangsparametern führen automatisch zu aktualisierten Ergebnissen, ohne dass die Dokumentation manuell angepasst werden muss.
