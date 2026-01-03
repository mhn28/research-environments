# QSAR Dataset Card — Experiment 01

## Dataset Name
qsar_dataset.csv

## Objective
Provide a model-ready, interpretable descriptor matrix for QSAR method development.

## Feature Space
- RDKit physicochemical descriptors
- Deterministic computation
- Zero-variance features removed

## Target Variable
- Column: target_activity
- Status: Placeholder (to be populated with experimental or curated data)

## Intended Use
- Classical QSAR (linear, tree-based, kernel methods)
- Descriptor interpretability studies
- Baseline ML benchmarking

## Prohibited Use
- Clinical inference
- Regulatory decision-making
- Model deployment without experimental validation

## Environment
- OS: Ubuntu 24.04 LTS
- Python: 3.10 (conda-forge)
- RDKit: conda-forge build

## Provenance
Generated as Step 8.1 in a reproducible cheminformatics workflow.