# Systementwurf

## Dokumentstatus

| Eigenschaft | Wert |
|-------------|------|
| Dokument | 04_Systementwurf.md |
| Version | 0.1 (Entwurf) |
| Bearbeitungsstand | Entwurf |
| Letzte Änderung | 17.07.2026 |
| Autor | Projekt NH3-PowerPlant |

---

# 1 Ziel des Systementwurfs

Nach der Einordnung des Standes der Technik wird im vorliegenden Kapitel die zu untersuchende Anlagenarchitektur definiert.

Der Systementwurf stellt noch keine endgültige technische Konstruktion dar. Vielmehr beschreibt er ein thermodynamisches Modell, das in den folgenden Kapiteln schrittweise untersucht und weiterentwickelt wird.

Alle späteren Berechnungen beziehen sich auf die hier definierten Komponenten, Stoffströme und Energieflüsse.

---

# 2 Grundidee

Die vorgeschlagene Anlage besteht aus zwei gekoppelten Kreisprozessen.

Der erste Kreisprozess dient der Anhebung von Umweltwärme auf ein nutzbares Temperaturniveau.

Der zweite Kreisprozess wandelt diese Wärme in mechanische beziehungsweise elektrische Energie um.

Die Besonderheit besteht darin, dass beide Kreisprozesse nicht unabhängig voneinander arbeiten, sondern über mehrere Wärmeübertrager thermisch gekoppelt werden.

---

# 3 Systemübersicht

```mermaid
flowchart LR

    A[Wasserreservoir<br>8 °C]

    --> B[Wärmepumpe]

    --> C[NH3-Verdampfer]

    --> D[Turbine]

    --> E[Generator]

    --> F[NH3-Kondensator]

    --> G[Wasserkreislauf]

    --> A
```

Die Energieversorgung erfolgt ausschließlich durch

- Umweltwärme
- elektrische Antriebsleistung der Wärmepumpe

Die Anlage besitzt keine klassische Feuerung.

---

# 4 Hauptkomponenten

## 4.1 Umweltreservoir

Das Umweltreservoir stellt die primäre Wärmequelle dar.

Annahmen:

- großes Wasservolumen
- konstante Temperatur
- praktisch unbegrenzte Wärmekapazität

Typische Beispiele:

- See
- Fluss
- Meer
- geothermisches Wasser

---

## 4.2 Wärmepumpe

Aufgabe:

Anhebung der Umweltwärme auf das Temperaturniveau des NH₃-Kreisprozesses.

Geplante Randbedingungen:

| Größe | Wert |
|--------|------|
| Quelle | 8–10 °C |
| Senke | ca. 80 °C |
| Arbeitsmedium | NH₃ (erste Projektphase) |

Die elektrische Antriebsleistung wird zunächst als externe Energie betrachtet.

Erst in späteren Projektphasen wird eine Kopplung mit dem Generator untersucht.

---

## 4.3 NH₃-Kreisprozess

Der NH₃-Kreisprozess besteht aus

- Verdampfer
- Turbine
- Kondensator
- Speisepumpe

Der Kreisprozess arbeitet vollständig geschlossen.

Seine Aufgabe besteht ausschließlich in der Umwandlung thermischer Energie in mechanische Arbeit.

---

## 4.4 Generator

Der Generator wandelt die Turbinenleistung in elektrische Energie um.

Für die erste Projektphase wird ein idealisierter Wirkungsgrad angenommen.

Spätere Kapitel berücksichtigen reale Generatorwirkungsgrade.

---

## 4.5 Wasserkreislauf

Der Wasserkreislauf besitzt im vorliegenden Konzept eine doppelte Funktion.

Einerseits dient er der Kühlung des Kondensators.

Andererseits stellt er die Wärmequelle der Wärmepumpe dar.

Diese Doppelfunktion unterscheidet das Konzept wesentlich von klassischen Kraftwerksarchitekturen.

---

# 5 Thermische Kopplung

Die Besonderheit des Systems besteht in der direkten thermischen Kopplung aller Hauptkomponenten.

Die Kondensationswärme wird nicht unmittelbar an die Umgebung abgegeben.

Stattdessen wird untersucht, in welchem Umfang sie

- den Wasserkreislauf vorwärmt,
- die Quellentemperatur der Wärmepumpe erhöht,
- den COP verbessert
- und dadurch die Gesamtbilanz beeinflusst.

Hierdurch entsteht ein thermisches Netzwerk.

---

# 6 Systemgrenzen

Zur späteren Bilanzierung werden klare Systemgrenzen definiert.

## Innerhalb des Systems

- Wärmepumpe
- NH₃-Kreisprozess
- Wasserkreislauf
- Generator
- Turbine
- Pumpen
- Wärmeübertrager

## Außerhalb des Systems

- Umweltreservoir
- elektrische Einspeisung
- Verbraucher
- Umgebung

Diese Definition ermöglicht eindeutige Energie- und Exergiebilanzen.

---

# 7 Stoffströme

Im Grundmodell werden drei Stoffkreisläufe betrachtet.

## NH₃-Kreisprozess

geschlossen

keine Stoffverluste

---

## Wärmepumpenkreis

geschlossen

Arbeitsmedium zunächst ebenfalls NH₃

---

## Wasserkreislauf

offen oder geschlossen

je nach untersuchter Anlagenvariante

---

# 8 Energieflüsse

Die wesentlichen Energieflüsse sind

- Umweltwärme
- Verdichterleistung
- Heizleistung der Wärmepumpe
- Turbinenarbeit
- Generatorleistung
- Kondensationswärme

Alle Energieflüsse werden später sowohl energetisch als auch exergetisch bilanziert.

---

# 9 Varianten des Systementwurfs

Im weiteren Projektverlauf werden mehrere Anlagenvarianten untersucht.

## Variante A

Referenzanlage

keine Rückführung der Kondensationswärme

---

## Variante B

Vorwärmung der Wärmepumpenquelle

---

## Variante C

mehrstufige Kondensation

---

## Variante D

mehrstufige Kondensation mit Rekuperation

---

Weitere Varianten können später ergänzt werden.

---

# 10 Offene Fragestellungen

Zum Zeitpunkt des Systementwurfs sind mehrere Randbedingungen bewusst noch offen.

Hierzu gehören insbesondere

- optimale Verdampfungstemperatur
- optimaler NH₃-Druck
- COP der Wärmepumpe
- Turbinenwirkungsgrad
- Massenströme
- Wärmeübertragerflächen

Diese Größen werden nicht vorgegeben, sondern im Verlauf der Berechnungen bestimmt.

---

# 11 Bedeutung des Systementwurfs

Der vorliegende Systementwurf stellt den gemeinsamen Ausgangspunkt aller weiteren Untersuchungen dar.

Änderungen an der Anlagenarchitektur werden grundsätzlich nicht innerhalb der Berechnungskapitel vorgenommen.

Stattdessen wird jede neue Architektur als eigenständige Anlagenvariante dokumentiert und anschließend vollständig neu bilanziert.

Dieses Vorgehen gewährleistet die Nachvollziehbarkeit aller späteren Ergebnisse.
