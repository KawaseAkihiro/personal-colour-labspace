# Codebook for `lab_samples.csv`

## Overview
`lab_samples.csv` is an anonymised, sample-level dataset used for the classification of personal-colour labels from colour coordinates.

The dataset is intended for open access and reuse. It contains no direct personal identifiers (e.g., usernames, URLs, channel names, or precise timestamps).

## Unit of observation
Each row represents one colour sample used in the analysis.

## File format
- Encoding: UTF-8
- Delimiter: comma (CSV)
- Header: first row contains column names
- Numeric fields use `.` as decimal separator

## Columns

### Identifiers
- `sample_id` (string)  
  Unique row identifier in the form `S000001`.

### sRGB colour representation
- `rgb_hex` (string)  
  sRGB colour encoded as a hex string in the canonical form `#RRGGBB` (lowercase hex).

- `r`, `g`, `b` (integer)  
  sRGB channel values in the range [0, 255].

### CIE L\*a\*b\* representation
- `L_star` (float)  
  CIE L\* (lightness). In this release, values are constrained to the theoretical range [0, 100].

- `a_star` (float)  
  CIE a\* (green–red axis).

- `b_star` (float)  
  CIE b\* (blue–yellow axis).

**Range handling:** `L_star` is clamped to [0, 100] to avoid floating-point rounding artefacts slightly above 100.0.

### Labels (ASCII / English)
Labels are provided in ASCII/English for international interoperability.

- `tone2_label` (categorical string)  
  Tone label with possible multi-membership:
  - `yellow`
  - `blue`
  - `yellow_blue` (multi-membership; the sample belongs to both tone categories)

- `season_label` (categorical string)  
  Seasonal label with possible multi-membership:
  - Single season: `spring`, `summer`, `autumn`, `winter`
  - Two-season combinations: `spring_summer`, `spring_autumn`, `spring_winter`, `summer_autumn`, `summer_winter`, `autumn_winter`
  - Three-season combinations: `spring_summer_autumn`, `spring_summer_winter`, `spring_autumn_winter`, `summer_autumn_winter`
  - Four-season combination: `spring_summer_autumn_winter`

**Multi-membership encoding:** When a sample belongs to multiple categories, labels are concatenated with underscores (e.g., `yellow_blue`, `spring_autumn`, `spring_summer_autumn_winter`).  
To ensure a canonical representation, the order of seasons is fixed as: `spring`, `summer`, `autumn`, `winter`.

## Anonymisation statement
This public dataset does not contain direct personal identifiers. Any potentially identifying fields (e.g., usernames, URLs, channel names, or precise timestamps) were excluded prior to release.

## Recommended usage notes
Depending on the research question, users may:
- treat multi-membership labels as explicit categories (e.g., `yellow_blue`), or
- convert them into multi-label targets (e.g., one-vs-rest indicators), or
- filter multi-membership rows for analyses requiring mutually exclusive classes.

## Contact
For questions or reuse inquiries, please contact the corresponding author listed in the associated paper.
