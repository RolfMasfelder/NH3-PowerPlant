docs/

00_Projektidee.md
01_Forschungsfrage_und_Hypothese.md
02_Thermodynamische_Grundlagen.md
03_Stand_der_Technik_gekoppelter_thermischer_Kreisprozesse.md
04_Systementwurf.md
05_Referenzmodell.md
06_Berechnungsmodell.md
07_Variantenvergleich.md

08_Ergebnisse.md ersetzt durch templates/08_Ergebnisse.md.j2
09_Diskussion.md ersetzt durch templates/09_Diskussion.md.j2

10_Ausblick.md
99_Glossar.md



NH3-PowerPlant
│
├── pyproject.toml
├── pytest.ini
├── README.md
├── LICENSE
├── .gitignore
│
├── src/
│   └── nh3powerplant/
│       ├── __init__.py
│       ├── version.py
│       │
│       ├── simulation/
│       │   └── __init__.py
│       │
│       ├── components/
│       │   └── __init__.py
│       │
│       ├── fluids/
│       │   └── __init__.py
│       │
│       ├── state/
│       │   └── __init__.py
│       │
│       ├── reporting/
│       │   └── __init__.py
│       │
│       ├── documentation/
│       │   └── __init__.py
│       │
│       ├── manifest/
│       │   └── __init__.py
│       │
│       ├── config/
│       │   └── __init__.py
│       │
│       └── utils/
│           └── __init__.py
│
└── tests/
    ├── __init__.py
    └── test_import.py

    src/
    nh3powerplant/
        state/
            __init__.py
            phase.py
            statepoint.py
