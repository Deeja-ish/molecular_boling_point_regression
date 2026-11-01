# DATA EXPLORATION RECORD

## Executive Summary

This dataset contains synthetic molecular descriptors used to predict molecular boiling point. The target variable is `boiling_point_c`. The dataset has 5,000 rows and no duplicate rows.

Author: Khadija Goni  
Date: 2026-11-01  
Project: Molecular Boiling Point Regression

---

## Column Analysis

### molecule_id

- Data type: String
- Description: Unique identifier for each molecule.
- Observations: 5,000 unique values, no missing values.
- Modeling decision: Use as identifier only, not as a model feature.

---

### molecular_weight

- Data type: Float
- Description: Molecular weight of each molecule.
- Observations: No missing values. Distribution is approximately uniform.
- Modeling decision: Keep as numeric feature.

---

### logP

- Data type: Float
- Description: Hydrophobicity proxy. Negative values indicate more hydrophilic molecules, while positive values indicate more hydrophobic molecules.
- Observations: 144 missing values, approximately 2.88%. Negative values are valid and not errors.
- Proposed solution: Impute missing values using median. Keep negative values unchanged.

---

### tpsa

- Data type: Float
- Description: Topological Polar Surface Area. It estimates the surface contribution from polar atoms and is useful for molecular property prediction.
- Observations: 141 missing values, approximately 2.82%. No negative values. Distribution is approximately uniform.
- Proposed solution: Impute missing values using median.

---

### hbd

- Data type: Integer
- Description: Number of hydrogen bond donors.
- Observations: Values range from 0 to 5. No missing values.
- Modeling decision: Keep as numeric feature.

---

### hba

- Data type: Integer
- Description: Number of hydrogen bond acceptors.
- Observations: Values range from 0 to 9. No missing values.
- Modeling decision: Keep as numeric feature.

---

### rotatable_bonds

- Data type: Integer
- Description: Number of rotatable bonds, representing molecular flexibility.
- Observations: Values range from 0 to 14. 164 missing values.
- Proposed solution: Impute missing values using median. Optionally create a missing indicator column such as `rotatable_bonds_missing`.

---

### aromatic_rings

- Data type: Integer
- Description: Number of aromatic rings in the molecule.
- Observations: Values range from 0 to 4. No missing values.
- Modeling decision: Keep as numeric feature.

---

### boiling_point_c

- Data type: Float
- Description: Target variable. Boiling point of the molecule in Celsius.
- Observations: No missing values. Negative values are present and are physically valid because some molecules boil below 0°C.
- Modeling decision: Keep as target variable. Do not remove or convert negative values.

---
**Correlation** : There is a weak correation between the features and the target the only variable that shows strong correlation with the target is the TPSA(Topological Polar Surface Area) of about 0.71.

## Final Cleaning Decisions

1. Keep negative `logP` values.
2. Keep negative `boiling_point_c` values.
3. Impute missing `logP`, `tpsa`, and `rotatable_bonds` using median.
4. Optionally add missing indicator columns for features with missing values.
6. Use `molecule_id` only as an identifier, not as a predictive feature.