# Ergebnismodell

## Dokumentstatus

| Eigenschaft | Wert |
|-------------|------|
| Dokument | 96_Ergebnismodell.md |
| Version | 0.1 (Entwurf) |
| Bearbeitungsstand | Entwurf |
| Letzte Änderung | 19.07.2026 |
| Autor | Projekt NH3-PowerPlant |

---

## 1 Ziel des Ergebnismodells

Das Ergebnismodell definiert, welche Daten ein Simulationslauf erzeugt.

Es bildet den Vertrag zwischen

- thermodynamischer Berechnung,
- Speicherung der Ergebnisse,
- Validierung,
- Tabellen- und Diagrammerzeugung,
- automatischer Berichtsgenerierung.

Alle Berichte, Tabellen und Diagramme werden ausschließlich aus diesem Ergebnismodell abgeleitet.

---

## 2 Grundsätze

Ein Simulationsergebnis ist vollständig strukturiert und maschinenlesbar.

Es enthält keine manuell ergänzten Berechnungsergebnisse.

Jeder Simulationslauf muss später mit denselben Eingabedaten reproduzierbar sein.

Das Ergebnismodell speichert deshalb neben numerischen Ergebnissen auch Metadaten zur Ausführung.

---

## 3 Oberste Struktur

Ein Ergebnis besteht mindestens aus folgenden Bereichen:

```text
SimulationResult
├── run
├── configuration
├── parameters
├── state_points
├── components
├── balances
├── efficiencies
├── validation
├── figures
└── report
```

Diese Struktur kann später erweitert werden, ohne bestehende Ergebnisdateien ungültig zu machen.

---

## 4 Run-Metadaten

Der Bereich `run` beschreibt den Simulationslauf.

Pflichtfelder:

| Feld | Bedeutung |
|------|-----------|
| id | eindeutige Laufkennung |
| timestamp | Zeitpunkt des Simulationslaufs |
| project_version | Version des Python-Pakets |
| simulation_name | Name der Simulation |
| variant | untersuchte Anlagenvariante |
| description | kurze Beschreibung des Laufs |

Optionale Felder:

- Git-Commit,
- Git-Branch,
- Python-Version,
- verwendete Stoffdatenbibliothek,
- verwendete Template-Version.

---

## 5 Konfiguration

Der Bereich `configuration` enthält die Eingabedaten des Simulationslaufs.

Hierzu gehören insbesondere:

- Arbeitsmedien,
- Randbedingungen,
- Wirkungsgrade,
- COP-Werte,
- Zielgrößen,
- Solver-Einstellungen,
- Konvergenzkriterien.

Die Konfiguration muss ausreichen, um den Simulationslauf später erneut auszuführen.

---

## 6 Parameter

Der Bereich `parameters` enthält die für den Bericht relevanten Eingangsgrößen.

Jeder Parameter besitzt mindestens:

| Feld | Bedeutung |
|------|-----------|
| name | Anzeigename |
| symbol | Formelzeichen, falls vorhanden |
| value | numerischer oder textueller Wert |
| unit | Einheit |
| source | Herkunft des Werts |

Diese Daten speisen die Parametertabellen der Ergebnisdokumentation.

---

## 7 StatePoints

Der Bereich `state_points` enthält alle thermodynamischen Zustände.

Jeder StatePoint besitzt mindestens:

| Feld | Bedeutung |
|------|-----------|
| identifier | eindeutige Kennung |
| fluid | Arbeitsmedium |
| pressure | Druck |
| temperature | Temperatur |
| enthalpy | spezifische Enthalpie |
| entropy | spezifische Entropie |
| density | Dichte |
| mass_flow | Massenstrom |
| vapor_quality | Dampfgehalt |

Interne Berechnungen verwenden ein einheitliches Einheitensystem.

Berichte dürfen Werte in technisch üblichen Einheiten darstellen, müssen diese Umrechnung jedoch aus den gespeicherten Daten ableiten.

---

## 8 Komponenten

Der Bereich `components` enthält die Ergebnisse einzelner Anlagenkomponenten.

Jede Komponente besitzt mindestens:

| Feld | Bedeutung |
|------|-----------|
| identifier | eindeutige Kennung |
| type | Komponententyp |
| input_states | referenzierte Eingangszustände |
| output_states | referenzierte Ausgangszustände |
| heat_flow | Wärmestrom |
| power | mechanische oder elektrische Leistung |
| efficiency | Wirkungsgrad, falls anwendbar |
| status | Berechnungsstatus |

Komponentenspezifische Kennwerte können zusätzlich ergänzt werden.

---

## 9 Bilanzen

Der Bereich `balances` enthält Energie-, Massen- und Exergiebilanzen.

Für jede Bilanz werden gespeichert:

| Feld | Bedeutung |
|------|-----------|
| target | Komponente oder Gesamtsystem |
| balance_type | energy, mass oder exergy |
| inputs | Summe der Eingangsströme |
| outputs | Summe der Ausgangsströme |
| residual | Bilanzfehler |
| relative_error | relativer Bilanzfehler |
| passed | Ergebnis der Prüfung |

Diese Daten bilden die Grundlage der Konsistenzprüfung.

---

## 10 Wirkungsgrade

Der Bereich `efficiencies` enthält abgeleitete Bewertungsgrößen.

Beispiele:

- Turbinenwirkungsgrad,
- Pumpenwirkungsgrad,
- Generatorwirkungsgrad,
- COP der Wärmepumpe,
- thermischer Wirkungsgrad,
- Netto-Wirkungsgrad,
- Exergiewirkungsgrad.

Jeder Eintrag enthält Name, Wert, Einheit und Bezugsgröße.

---

## 11 Validierung

Der Bereich `validation` enthält alle Prüfungen eines Simulationslaufs.

Beispiele:

- Massenbilanz erfüllt,
- Energiebilanz erfüllt,
- Exergiebilanz erfüllt,
- Druckbereich plausibel,
- Temperaturbereich plausibel,
- Dampfgehalt im gültigen Bereich,
- Konvergenzkriterien erfüllt.

Jede Prüfung besitzt mindestens:

| Feld | Bedeutung |
|------|-----------|
| name | Name der Prüfung |
| result | passed, failed oder warning |
| message | kurze Beschreibung |
| value | geprüfter Wert, falls vorhanden |
| limit | Grenzwert, falls vorhanden |

---

## 12 Abbildungen und Tabellen

Der Bereich `figures` enthält Referenzen auf automatisch erzeugte Abbildungen.

Geplante Abbildungen:

- T-s-Diagramm,
- p-h-Diagramm,
- Sankey-Diagramm Energie,
- Sankey-Diagramm Exergie,
- Temperaturprofile,
- Verlustdiagramme.

Tabellen werden aus den Bereichen `parameters`, `state_points`, `components`, `balances` und `efficiencies` erzeugt.

---

## 13 Berichtsdaten

Der Bereich `report` enthält Textbausteine und Zusammenfassungen, die direkt in Templates eingesetzt werden.

Beispiele:

- summary,
- interpretation,
- thermodynamic_discussion,
- exergy_discussion,
- hypothesis_result,
- outlook_items.

Diese Texte dürfen keine neuen numerischen Ergebnisse einführen. Sie interpretieren ausschließlich vorhandene Ergebnisdaten.

---

## 14 Bezug zu den Templates

Das Template `08_Ergebnisse.md.j2` erwartet insbesondere:

- `run`,
- `parameters`,
- `state_table`,
- `energy_table`,
- `exergy_table`,
- `efficiency_table`,
- `figures`,
- `validation`,
- `summary`.

Das Template `09_Diskussion.md.j2` erwartet zusätzlich:

- `goals`,
- `thermodynamic_discussion`,
- `exergy_discussion`,
- `heatpump_discussion`,
- `condenser_discussion`,
- `comparison_discussion`,
- `sensitivity_discussion`,
- `hypothesis_result`,
- `outlook_items`,
- `discussion_summary`.

Die spätere Python-Implementierung muss diese Daten entweder direkt liefern oder aus dem strukturierten Simulationsergebnis ableiten.

---

## 15 Speicherformate

Das primäre Speicherformat ist JSON.

Weitere Ausgabeformate können aus dem JSON-Ergebnis abgeleitet werden.

Geplante Dateien pro Simulationslauf:

```text
results/<run-id>/
├── config.json
├── manifest.json
├── result.json
├── data/
├── figures/
├── tables/
├── report.md
├── report.pdf
└── report.html
```

Frühere Simulationsläufe werden nicht überschrieben.
