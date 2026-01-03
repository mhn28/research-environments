# Computational Methods

## Software Environment
All computational analyses were performed on a Linux-based system using a
fully reproducible conda/micromamba environment. The operating system was
Linux-6.14.0-37-generic-x86_64-with-glibc2.39 running on a x86_64 architecture. Python version 3.10.19 was used
for all cheminformatics and machine learning analyses. Where applicable,
R version Not used was available for statistical validation and visualization.

All software dependencies were installed exclusively from the conda-forge
channel, with version pinning to ensure computational reproducibility.

---

## Molecular Representation
Chemical structures were represented as Simplified Molecular Input Line
Entry System (SMILES) strings. Molecules were parsed and validated using
the RDKit cheminformatics toolkit (2025.03.6). Structures failing
sanitization were excluded prior to descriptor computation.

---

## Descriptor Calculation
Physicochemical descriptors were computed deterministically using RDKit.
The descriptor set included molecular weight, octanol–water partition
coefficient (LogP), hydrogen bond donors (HBD), hydrogen bond acceptors
(HBA), and topological polar surface area (TPSA). Descriptor functions were
explicitly defined to prevent version-dependent behavior.

---

## Data Preprocessing
Descriptor matrices were filtered to remove zero-variance features.
Pairwise correlation analysis was performed to identify highly correlated
descriptors, and redundant features were pruned to minimize
multicollinearity. All preprocessing steps were fully scripted.

---

## Dataset Construction
Processed descriptors were partitioned into training and test sets prior
to modeling. Feature scaling parameters were learned exclusively from the
training data and subsequently applied to the test data to prevent data
leakage.

A synthetic target variable was introduced solely for pipeline validation.
This response variable does not represent biological, pharmacological, or
clinical activity.

---

## QSAR Modeling
A baseline quantitative structure–activity relationship (QSAR) model was
constructed using ordinary least squares linear regression. Model training
was performed on the scaled training dataset, and predictive performance
was evaluated on an independent test set.

Model performance was assessed using coefficient of determination (R²),
root mean squared error (RMSE), and mean absolute error (MAE). Model
coefficients were examined to assess descriptor contributions and
interpretability.

---

## Reproducibility
All scripts, intermediate data products, and final outputs were tracked
using Git version control. A frozen record of the computational environment
and artifacts was preserved in `EXPERIMENT_FREEZE.json`.

---

## Date of Methods Generation
2026-01-03
