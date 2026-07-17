# Berechnungsmodell

## Dokumentstatus

| Eigenschaft | Wert |
|-------------|------|
| Dokument | 06_Berechnungsmodell.md |
| Version | 0.1 (Entwurf) |
| Bearbeitungsstand | Entwurf |
| Letzte Änderung | 17.07.2026 |
| Autor | Projekt NH3-PowerPlant |

---

# 1 Zielsetzung

Das Berechnungsmodell beschreibt die mathematischen und thermodynamischen Grundlagen der Simulation.

Es definiert

- die Eingangsgrößen,
- die Zustandsgrößen,
- die Bilanzgleichungen,
- die numerische Vorgehensweise,
- sowie die Struktur der Simulationssoftware.

Alle späteren Python-Module müssen diesem Dokument entsprechen.

---

# 2 Modellphilosophie

Die Simulation verfolgt einen streng modularen Aufbau.

Jede technische Komponente besitzt

- definierte Eingangsgrößen,
- definierte Ausgangsgrößen,
- eine Energiebilanz,
- eine Exergiebilanz.

Dadurch können einzelne Komponenten unabhängig entwickelt und getestet werden.

---

# 3 Komponentenmodell

Die Referenzanlage wird in folgende Berechnungsmodule zerlegt.

```text
Reservoir

↓

Wärmepumpe

↓

Verdampfer

↓

Turbine

↓

Generator

↓

Kondensator

↓

Speisepumpe
```

Jedes Modul besitzt eindeutig definierte Ein- und Ausgangsgrößen.

---

# 4 Zustandsgrößen

Für jeden Stoffstrom werden mindestens folgende Größen gespeichert.

| Größe | Symbol | Einheit |
|--------|---------|---------|
| Druck | p | bar |
| Temperatur | T | °C |
| Enthalpie | h | kJ/kg |
| Entropie | s | kJ/(kg·K) |
| Dichte | ρ | kg/m³ |
| Dampfgehalt | x | - |
| Massenstrom | ṁ | kg/s |

Diese Größen bilden den vollständigen thermodynamischen Zustand eines Stoffstroms.

---

# 5 Stoffdaten

Alle Stoffwerte werden grundsätzlich aus einer Stoffdatenbibliothek entnommen.

Für das Projekt wird CoolProp verwendet.

Es werden keine Stoffwerte manuell eingegeben.

Dadurch bleiben sämtliche Berechnungen reproduzierbar.

---

# 6 Energiebilanzen

Für jede Komponente gilt

\[
\dot Q+\dot W+\sum \dot m h_{ein}
=
\sum \dot m h_{aus}
\]

Diese Bilanz wird für

- Wärmepumpe
- Verdampfer
- Turbine
- Kondensator
- Speisepumpe

getrennt ausgewertet.

---

# 7 Exergiebilanzen

Zusätzlich wird für jede Komponente eine Exergiebilanz erstellt.

Grundgleichung

\[
Ex = H-T_0S
\]

Die Exergiedissipation ergibt sich aus der Differenz

zwischen zu- und abgeführter Exergie.

---

# 8 Numerische Berechnung

Alle Komponenten werden iterativ berechnet.

Berechnungsreihenfolge

1. Reservoir
2. Wärmepumpe
3. Verdampfer
4. Turbine
5. Kondensator
6. Speisepumpe

Anschließend erfolgt

- Energiebilanz
- Exergiebilanz
- Konsistenzprüfung

---

# 9 Konvergenzkriterien

Eine Simulation gilt als konvergiert wenn

- Energiebilanzfehler < 0,01 %

- Massenbilanzfehler < 0,001 %

- Druckänderung < 0,001 bar

- Temperaturänderung < 0,01 K

Diese Grenzwerte können projektspezifisch angepasst werden.

---

# 10 Softwarearchitektur

Die Python-Software wird objektorientiert aufgebaut.

```text
Component

├── Reservoir

├── HeatPump

├── HeatExchanger

├── Turbine

├── Generator

├── Condenser

├── Pump
```

Jede Klasse besitzt mindestens

```python
calculate()

energy_balance()

exergy_balance()

report()
```

---

# 11 Zustandsobjekte

Zwischen den Komponenten werden keine Einzelwerte übertragen.

Stattdessen wird ein vollständiges Zustandsobjekt verwendet.

```python
StatePoint
```

Dieses enthält

- p
- T
- h
- s
- rho
- x
- mdot

Dadurch bleiben alle Komponenten unabhängig.

---

# 12 Simulation

Die Gesamtanlage wird durch eine Klasse

```python
PowerPlant
```

beschrieben.

Sie enthält

- sämtliche Komponenten,
- sämtliche Stoffströme,
- sämtliche Bilanzen.

Ein Simulationslauf besteht aus

```text
Initialisierung

↓

Iteration

↓

Konvergenzprüfung

↓

Berichterstellung
```

---

# 13 Ergebnisdaten

Nach jeder Simulation werden automatisch erzeugt

- CSV-Dateien
- Markdown-Tabellen
- Energiebilanzen
- Exergiebilanzen
- T-s-Diagramme
- p-h-Diagramme

Diese Ergebnisse bilden die Grundlage der folgenden Kapitel.

---

# 14 Validierung

Die Berechnungen werden in mehreren Stufen validiert.

1. Vergleich mit Literaturwerten

2. Vergleich mit einfachen Handrechnungen

3. Vergleich mit CoolProp

4. Konsistenz der Energiebilanz

5. Konsistenz der Exergiebilanz

Nur validierte Berechnungen werden für spätere Variantenvergleiche verwendet.

---

# 15 Zusammenfassung

Das Berechnungsmodell definiert die mathematische Grundlage des gesamten Projekts.

Durch den modularen Aufbau können

- neue Arbeitsmedien,
- zusätzliche Wärmeübertrager,
- alternative Turbinen,
- weitere Anlagenvarianten

ohne Änderungen an der Grundstruktur ergänzt werden.

Das Berechnungsmodell bildet somit die verbindliche Spezifikation der späteren Python-Implementierung.
