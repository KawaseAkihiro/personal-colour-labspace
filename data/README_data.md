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
  Unique row identifier (e.g., `S000001`).

### sRGB colour representation
- `rgb_hex` (string)  
  sRGB colour encoded as a hex string in the form `#RRGGBB` (lowercase hex is used in this release).

- `r`, `g`, `b` (integer)  
  sRGB channel values in the range [0, 255].

### CIE L\*a\*b\* representation
- `L_star` (float)  
  CIE L\* (lightness), typically in the range [0, 100].

- `a_star` (float)  
  CIE a\* (green–red axis).

- `b_star` (float)  
  CIE b\* (blue–yellow axis).

**Note:** CIE L\*a\*b\* values are provided directly in the dataset to ensure reproducibility without requiring users to implement RGB→CIELAB conversion.

### Labels
Labels are provided in ASCII/English for international interoperability.

- `tone2_label` (categorical string)  
  Binary tone label. Values:
  - `yellow`
  - `blue`

- `season_label` (categorical string)  
  Seasonal label. Values include standard seasons and ambiguous categories:
  - `spring`, `summer`, `autumn`, `winter`
  - `spring_autumn`, `summer_winter`

Ambiguous categories indicate that the original label assignment permitted two possible seasons and the dataset encodes that ambiguity explicitly.

## Anonymisation statement
This public dataset does not contain direct personal identifiers. Any potentially identifying fields (e.g., usernames, URLs, channel names, or precise timestamps) were excluded prior to release.

## Contact
For questions or reuse inquiries, please contact the corresponding author listed in the associated paper.
