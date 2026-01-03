# Figure Captions

**Figure 1. Molecular descriptor distribution.**  
Distribution of RDKit-derived physicochemical descriptors including molecular
weight, LogP, hydrogen bond donors (HBD), hydrogen bond acceptors (HBA), and
topological polar surface area (TPSA) for the curated molecular dataset. All
descriptors were computed deterministically using RDKit.

**Figure 2. Descriptor correlation structure.**  
Pairwise Pearson correlation matrix of computed molecular descriptors.
Highly correlated descriptor pairs were identified to guide feature pruning
and reduce multicollinearity prior to QSAR modeling.

**Figure 3. QSAR model predictions versus observed values.**  
Scatter plot comparing predicted and observed target values for the linear
QSAR model. Training and test sets are shown separately to assess generalization
performance.

**Figure 4. Residual analysis of QSAR model.**  
Residuals plotted as a function of predicted activity to evaluate model bias,
heteroscedasticity, and overall fit quality.

**Figure 5. Descriptor importance in linear QSAR model.**  
Magnitude and direction of regression coefficients for retained descriptors,
illustrating relative contributions to the modeled response variable.

*Figures generated using Python (matplotlib) on 2026-01-03.*
