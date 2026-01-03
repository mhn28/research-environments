"""
Experiment 01: Cheminformatics Foundations with RDKit

This script computes core physicochemical descriptors for a reference
small molecule (caffeine) using RDKit. These descriptors are widely used
in medicinal chemistry, pharmacokinetics, and QSAR modeling.

Environment:
- Python 3.10
- RDKit (conda-forge)
- Ubuntu 24.04

Author: Mohin Sapara
"""

from rdkit import Chem
from rdkit.Chem import Descriptors

SMILES = "Cn1cnc2c1c(=O)n(C)c(=O)n2C"  # Caffeine

def main():
    mol = Chem.MolFromSmiles(SMILES)
    if mol is None:
        raise ValueError("Invalid SMILES string")

    results = {
        "MolecularWeight": Descriptors.MolWt(mol),
        "LogP": Descriptors.MolLogP(mol),
        "HBD": Descriptors.NumHDonors(mol),
        "HBA": Descriptors.NumHAcceptors(mol),
        "TPSA": Descriptors.TPSA(mol),
    }

    for name, value in results.items():
        print(f"{name}: {value:.3f}")

if __name__ == "__main__":
    main()
