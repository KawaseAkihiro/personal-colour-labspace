# personal-colour-labspace

This repository provides an anonymised dataset and minimal reproducible code accompanying the paper
**“Personal Colour between Perceptual Space and Social Practice”** (accepted; in proofreading).

It enables reproducibility of the classification analysis of personal-colour labels from colour coordinates.

## Repository structure
- `data/lab_samples.csv` — anonymised sample-level dataset (RGB and CIE L\*a\*b\*)
- `data/README_data.md` — data dictionary / codebook
- `run_pipeline.py` — minimal runnable script to load and validate the dataset
- `requirements.txt` — Python dependencies
- `config.example.yml` — configuration template (paths and random seed)
- `.gitignore` — excludes generated outputs and local config

## Data summary
Each row corresponds to one colour sample. The dataset includes:
- sRGB values (`rgb_hex`, `r`, `g`, `b`)
- CIE L\*a\*b\* coordinates (`L_star`, `a_star`, `b_star`)
- two personal-colour label types:
  - `tone2_label` (binary tone)
  - `season_label` (seasonal label; includes ambiguous categories such as `spring_autumn`)

See `data/README_data.md` for full details.

## Quick start
1. Create a Python environment and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
2. Create a local config file:
   ```bash
   cp config.example.yml config.yml
3. Run:
   ```bash
   python run_pipeline.py

## Reproducibility notes
- The repository is designed to avoid machine-specific absolute paths (e.g., personal Google Drive directories).
- Random seeds are controlled via `config.yml` (default: `seed: 42`).
- The dataset provides both RGB and CIE L\*a\*b\* values to make downstream analyses independent of implementation-specific conversion details.

## License and citation
- Code license: MIT License (see `LICENSE`)
- Data license: CC BY 4.0 (see `data/LICENSE`)
- Citation: Please cite the Zenodo Concept DOI (all versions): https://doi.org/10.5281/zenodo.18646259

