# personal-colour-labspace

[![DOI](https://zenodo.org/badge/1158264019.svg)](https://doi.org/10.5281/zenodo.18646259)

**Languages:** [English](README.md) | [日本語](README_ja.md) | Deutsch (diese Seite) | [한국어](README_ko.md)

Dieses Repository stellt einen anonymisierten Datensatz sowie minimalen, reproduzierbaren Code bereit, die den Beitrag
**„Personal Colour between Perceptual Space and Social Practice“** (angenommen; im Korrekturprozess) begleiten.

Es ermöglicht die Reproduzierbarkeit der Klassifikationsanalyse von Personal-Colour-Labels anhand von Farbkoordinaten.

## Repository-Struktur
- `data/lab_samples.csv` — anonymisierter Datensatz auf Sample-Ebene (RGB und CIE L\*a\*b\*)
- `data/README_data.md` — Datenbeschreibung / Codebook
- `run_pipeline.py` — minimales ausführbares Skript zum Laden und Validieren des Datensatzes
- `requirements.txt` — Python-Abhängigkeiten
- `config.example.yml` — Konfigurationsvorlage (Pfade und Zufalls-Seed)
- `.gitignore` — schließt erzeugte Outputs und lokale Konfiguration aus

## Datenübersicht
Jede Zeile entspricht einem Farbsample. Der Datensatz enthält:
- sRGB-Werte (`rgb_hex`, `r`, `g`, `b`)
- CIE L\*a\*b\*-Koordinaten (`L_star`, `a_star`, `b_star`)
- zwei Typen von Personal-Colour-Labels:
  - `tone2_label` (binärer Ton)
  - `season_label` (Saison-Label; enthält mehrdeutige Kategorien wie `spring_autumn`)

Weitere Details sind in `data/README_data.md` beschrieben.

## Schnellstart
1. Eine Python-Umgebung erstellen und Abhängigkeiten installieren:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. Eine lokale Konfigurationsdatei erstellen:
   ```bash
   cp config.example.yml config.yml
   ```
3. Ausführen:
   ```bash
   python run_pipeline.py
   ```

## Hinweise zur Reproduzierbarkeit
- Das Repository ist so konzipiert, dass maschinenspezifische absolute Pfade vermieden werden (z. B. persönliche Google-Drive-Verzeichnisse).
- Zufalls-Seeds werden über `config.yml` gesteuert (Standard: `seed: 42`).
- Der Datensatz enthält sowohl RGB- als auch CIE L\*a\*b\*-Werte, um nachgelagerte Analysen unabhängig von implementierungsspezifischen Konvertierungsdetails zu machen.

## License and citation
- Code-Lizenz: MIT License (siehe `LICENSE`)
- Daten-Lizenz: CC BY 4.0 (siehe `data/LICENSE`)
- Zitierung: Bitte zitieren Sie den Zenodo Concept DOI (alle Versionen): https://doi.org/10.5281/zenodo.18646259

