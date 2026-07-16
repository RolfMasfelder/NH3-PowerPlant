# Projektidee

## Dokumentstatus

| Eigenschaft | Wert |
|-------------|------|
| Dokument | 00_Projektidee.md |
| Version | 0.1 (Entwurf) |
| Bearbeitungsstand | Entwurf |
| Letzte Änderung | 15.07.2026 |
| Autor | Projekt NH3-PowerPlant |

---

## 1 Motivation

Die Energieversorgung moderner Industriegesellschaften basiert heute überwiegend auf thermischen Kraftwerken, Wasserkraft, Windenergie, Photovoltaik sowie verschiedenen Formen der Nutzung geothermischer Energie. Thermische Kraftwerke arbeiten dabei nahezu ausschließlich nach dem gleichen Grundprinzip:

1. Bereitstellung von Wärme auf hohem Temperaturniveau.
2. Verdampfung eines Arbeitsmediums.
3. Expansion des Arbeitsmediums in einer Turbine.
4. Umwandlung der mechanischen Energie in elektrische Energie durch einen Generator.
5. Abführung der verbleibenden Wärme über einen Kondensator.

Die Bereitstellung der Wärme erfolgt klassisch durch

- fossile Brennstoffe,
- Kernenergie,
- Solarthermie,
- Biomasse oder
- natürliche geothermische Wärme.

Allen Verfahren gemeinsam ist die Notwendigkeit einer möglichst hochtemperierten Wärmequelle.

---

## 2 Ausgangsidee

Dieses Projekt entstand aus einem Gedankenexperiment.

Die zentrale Frage lautet:

> Kann eine Wärmepumpe die Rolle der klassischen Feuerung übernehmen und damit den thermodynamischen Kreisprozess eines Kraftwerks antreiben?

Dabei wird bewusst auf fossile Brennstoffe, Kernenergie oder direkte Verbrennungsprozesse verzichtet.

Die Wärme soll ausschließlich einem sehr großen natürlichen Reservoir entnommen werden, beispielsweise

- einem See,
- dem Meer,
- einem Fluss,
- dem Erdreich oder
- einem anderen großvolumigen Wärmespeicher.

Die Wärmepumpe hebt diese Umweltwärme auf ein höheres Temperaturniveau an. Diese Wärme treibt anschließend einen geschlossenen NH₃-Kreisprozess an, dessen Turbine einen elektrischen Generator antreibt.

Ein Teil oder die gesamte erzeugte elektrische Leistung soll wiederum die Wärmepumpe versorgen.

---

## 3 Warum dieses Konzept ungewöhnlich ist

Auf den ersten Blick erscheint eine solche Anlage widersprüchlich.

Eine Wärmepumpe benötigt elektrische Energie.

Diese elektrische Energie soll jedoch gerade durch den nachgeschalteten Kreisprozess erzeugt werden.

Damit entsteht scheinbar ein geschlossener Kreislauf

Reservoir → Wärmepumpe → NH₃-Kreisprozess → Turbine → Generator → Wärmepumpe

dessen Energiebilanz kritisch hinterfragt werden muss.

Die klassische Thermodynamik legt zunächst nahe, dass ein solcher Kreislauf aufgrund des zweiten Hauptsatzes keinen elektrischen Energieüberschuss erzeugen kann.

Diese Aussage beantwortet jedoch noch nicht die wesentlich interessantere Frage:

> Wie nahe kann eine derartige Anlagenarchitektur an die theoretischen thermodynamischen Grenzen herangeführt werden?

Genau diese Fragestellung bildet den Ausgangspunkt der vorliegenden Untersuchung.

---

## 4 Zielsetzung

Ziel dieses Projektes ist ausdrücklich **nicht** der Nachweis eines Perpetuum Mobile.

Ebenso wenig soll versucht werden, bekannte thermodynamische Gesetze zu widerlegen.

Stattdessen soll untersucht werden,

- welche Anlagenarchitektur sich aus der Kombination einer Wärmepumpe mit einem NH₃-Kreisprozess ergibt,
- welche thermodynamischen Randbedingungen dabei auftreten,
- welche Energie- und Exergieströme innerhalb der Anlage entstehen,
- welche Verluste auftreten,
- welche Komponenten diese Verluste dominieren,
- und ob durch geeignete Wärmeführung sowie interne Wärmerückgewinnung eine signifikante Verbesserung gegenüber klassischen Anlagen erreicht werden kann.

Die Untersuchung versteht sich daher als **ergebnisoffene Machbarkeitsstudie**.

---

## 5 Grundannahmen

Für die erste Projektphase werden bewusst vereinfachte Randbedingungen gewählt.

Arbeitsmedium des Kraftwerks:

- Ammoniak (NH₃)

Wärmequelle:

- großes Wasserreservoir

Temperatur der Wärmequelle:

- etwa 8…10 °C

Zieltemperatur nach der Wärmepumpe:

- zunächst 80 °C

Elektrische Zielgröße:

- Referenzanlage mit 100 kW Generatorleistung

Alle späteren Berechnungen können auf andere Temperaturbereiche oder Leistungen skaliert werden.

---

## 6 Zentrale Fragestellungen

Im Verlauf der Studie sollen insbesondere folgende Fragen beantwortet werden.

## Thermodynamik

- Welche theoretischen Grenzen setzt der zweite Hauptsatz?
- Welche Rolle spielt die Exergie gegenüber der Energiebilanz?
- Welche Kreisprozesse eignen sich für niedrige Temperaturniveaus?

## Wärmepumpe

- Welcher COP ist unter realistischen Bedingungen erreichbar?
- Welche Arbeitsmedien sind geeignet?
- Welche Temperaturhübe sind wirtschaftlich sinnvoll?

## NH₃-Kreisprozess

- Welche Drücke ergeben sich?
- Welche Turbinentechnologien sind geeignet?
- Welche Massenströme werden benötigt?

## Wärmeübertrager

- Welche Verluste entstehen im Kondensator?
- Wie wirkt sich eine mehrstufige Kondensation aus?
- Kann die Kondensationswärme zur Vorwärmung der Wärmequelle genutzt werden?

## Gesamtsystem

- Wo entstehen die größten Exergieverluste?
- Welche Anlagenvariante besitzt den höchsten Gesamtwirkungsgrad?
- Welche Optimierungsansätze ergeben sich daraus?

---

## 7 Arbeitsweise

Das Projekt wird vollständig reproduzierbar aufgebaut.

Alle Berechnungen werden mit nachvollziehbaren Modellen durchgeführt.

Der Bericht enthält ausschließlich Ergebnisse, deren Herleitung dokumentiert ist.

Hierzu gehören

- thermodynamische Stoffdaten,
- Python-Skripte,
- Berechnungstabellen,
- Energie- und Exergiebilanzen,
- Fließbilder,
- T-s-Diagramme,
- p-h-Diagramme sowie
- Sensitivitätsanalysen.

Das Repository dient dabei als zentrale Entwicklungsumgebung.

Der vorliegende Bericht bildet die technische Dokumentation des Projektes.

---

## 8 Projektphasen

Das Projekt gliedert sich in mehrere aufeinander aufbauende Schritte.

1. Thermodynamische Grundlagen
2. Auslegung einer Referenzanlage
3. Entwicklung eines Berechnungsmodells
4. Vergleich verschiedener Anlagenarchitekturen
5. Optimierung der Wärmeführung
6. Exergieanalyse
7. Bewertung der Ergebnisse

Jede Projektphase endet mit einer vollständigen Energiebilanz sowie einer Exergiebilanz.

Die Ergebnisse bilden jeweils die Grundlage der folgenden Entwicklungsstufe.

---

## 9 Schlussbemerkung

Dieses Projekt verfolgt bewusst einen ingenieurwissenschaftlichen Ansatz.

Ausgangspunkt ist kein fertiges Anlagenkonzept, sondern ein Gedankenexperiment, dessen technische Tragfähigkeit systematisch untersucht werden soll.

Alle Berechnungen erfolgen ergebnisoffen.

Sollte sich zeigen, dass einzelne Teilkonzepte thermodynamisch nicht realisierbar sind, werden diese dokumentiert und analysiert. Ebenso werden Optimierungsmöglichkeiten untersucht, die sich aus einer geschickten Kopplung von Wärmepumpe, NH₃-Kreisprozess und Wärmeübertragern ergeben.

Das Ziel besteht nicht im Nachweis einer vorgefassten These, sondern im Aufbau eines nachvollziehbaren thermodynamischen Modells, das eine fundierte Bewertung der vorgeschlagenen Anlagenarchitektur ermöglicht.
