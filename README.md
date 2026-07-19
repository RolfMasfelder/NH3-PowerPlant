# NH3-PowerPlant

Simulation und Auslegung eines Kraftwerks-/Energiekonzepts auf Basis von Ammoniak (NH3) als Energieträger.

## Dokumentstatus

| Eigenschaft | Wert |
|-------------|------|
| Version | 0.1 (Entwurf) |
| Bearbeitungsstand | Entwurf |
| Letzte Änderung | 15.07.2026 |
| Autor | Projekt NH3-PowerPlant |

## Über das Projekt

Dieses Projekt untersucht die Nutzung von Ammoniak (NH3) als CO2-freien Energieträger und Brennstoff für
Kraftwerksprozesse. Es enthält Modelle, Berechnungen und Auswertungen zu Erzeugung, Speicherung und
energetischer Verwertung von Ammoniak.

> **Status:** Frühes Entwicklungsstadium (Work in Progress). API und Struktur können sich noch ändern.

## Einzuhalten

- [PEP 8](https://peps.python.org/pep-0008/) – Style Guide for Python Code

Beispiele:

Jede Datei enthält genau eine öffentliche Klasse.
Keine Datei wird länger als etwa 300 Zeilen. Wenn sie darüber wächst, ist das ein Signal, sie aufzuteilen.
Jede öffentliche Methode erhält einen Docstring im NumPy-Stil.
Alle Klassen bekommen von Anfang an Typannotationen und werden mit mypy --strict getestet.
Alle Unit-Tests spiegeln die Paketstruktur wider (tests/unit/components/test_component.py usw.).

## Projektstruktur

```txt
NH3-PowerPlant/
├── docs/          # Dokumentation, Konzepte, Spezifikationen
├── src/           # Python-Quellcode (Modelle, Simulationen, Tools)
├── templates/     # Jinja2-Templates für Ergebnisberichte
├── data/          # Roh- und Verarbeitungsdaten
├── images/        # Grafiken, Diagramme, Abbildungen
├── tests/         # Automatisierte Tests
├── references/    # Literatur, Quellen, Normen
├── notebooks/     # Jupyter Notebooks für Analysen und Prototyping
├── README.md
├── LICENSE
└── CHANGELOG.md
```

## Vorgehensweise

1. Konzept in Markdown festhalten.
2. Datenmodell daraus ableiten.
3. Python-Klassen implementieren.
4. Tests schreiben.
5. Dokumentation automatisch erzeugen.

mit "5. Dokumentation" ist die Dokumentation der Simulationsergebnisse gemeint, nicht die Projektdokumentation.

## Voraussetzungen

- Python 3.13
- virtuelles Python-Environment, zum Beispiel `venv/`

## Installation

```bash
git clone https://github.com/RolfMasfelder/NH3-PowerPlant.git
cd NH3-PowerPlant
python3 -m venv venv
source venv/bin/activate
pip install -e ".[dev]"
```

Optionale Abhängigkeiten für Analysen und Notebooks:

```bash
pip install -e ".[analysis,notebook]"
```

## Nutzung

_Wird ergänzt, sobald erste lauffähige Module verfügbar sind._

## Tests

```bash
source venv/bin/activate
pytest tests/
```

## Mitwirken

Beiträge sind willkommen! Bitte lies vor einem Pull Request die [CONTRIBUTING.md](CONTRIBUTING.md) (folgt).
Für größere Änderungen bitte zunächst ein Issue eröffnen, um das Vorhaben zu besprechen.

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz – siehe [LICENSE](LICENSE) für Details.

## Changelog

Änderungen werden in [CHANGELOG.md](CHANGELOG.md) dokumentiert.
