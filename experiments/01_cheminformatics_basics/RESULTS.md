# Results

## Descriptor Computation and Filtering
A total of five RDKit-derived physicochemical descriptors were computed for
each molecule, including molecular weight, LogP, hydrogen bond donors (HBD),
hydrogen bond acceptors (HBA), and topological polar surface area (TPSA).
Descriptors exhibiting zero variance or high pairwise correlation were removed,
yielding a reduced and numerically stable feature set for modeling.

## Exploratory Descriptor Analysis
Pairwise correlation analysis revealed moderate interdependencies among selected
descriptors, consistent with known physicochemical relationships. Feature
filtering reduced multicollinearity and improved interpretability without
introducing stochastic variability.

## QSAR Model Development
A baseline linear regression model was trained using the filtered descriptor
matrix. To validate the computational pipeline in the absence of experimentally
measured activities, a synthetic target variable was introduced solely for
methodological verification.

## Model Performance


## Model Interpretability
Among retained descriptors, molecular weight, LogP, and hydrogen bond acceptor
count exhibited the largest absolute regression coefficients, suggesting that
bulk physicochemical properties dominate the modeled response in this baseline
linear formulation.

## Reproducibility Statement
All analyses were executed in a fully reproducible computational environment,
with fixed software versions and deterministic descriptor calculations.
All figures, tables, and metrics were generated programmatically on 2026-01-03.
