# Graphical Abstract

## Conceptual Layout

The graphical abstract illustrates a reproducible cheminformatics-to-QSAR
workflow implemented in a fully controlled computational environment.

**Left panel**  
Small-molecule structures represented as SMILES strings are parsed using
RDKit to generate standardized molecular objects.

**Middle panel**  
Physicochemical descriptors (molecular weight, lipophilicity, hydrogen bond
counts, and polar surface area) are computed deterministically. Descriptor
filtering removes non-informative and redundant features to ensure numerical
stability and interpretability.

**Right panel**  
A baseline linear QSAR model is trained and evaluated as a proof-of-concept
pipeline validation step, demonstrating transparent model construction,
evaluation, and logging rather than predictive optimization.

A reproducibility layer underpins the entire workflow, highlighting
version-pinned environments, logged provenance, and auditable outputs.

---

## Suggested Caption

**Graphical Abstract.** Reproducible cheminformatics and QSAR workflow.
Small-molecule structures are converted into physicochemical descriptors
using RDKit, followed by systematic feature filtering and baseline QSAR
modeling within a version-controlled Linux environment. The framework
emphasizes transparency, reproducibility, and methodological rigor rather
than predictive performance.

*Generated automatically on 2026-01-03 as part of a reproducible computational
research pipeline.*
