from rdkit import Chem
from rdkit.Chem import Descriptors
import pandas as pd

# Canonical small molecules (biologically relevant)
molecules = {
    "Aspirin": "CC(=O)OC1=CC=CC=C1C(=O)O",
    "Caffeine": "Cn1cnc2c1c(=O)n(C)c(=O)n2C",
    "Paracetamol": "CC(=O)NC1=CC=C(O)C=C1",
    "Ibuprofen": "CC(C)CC1=CC=C(C=C1)C(C)C(=O)O"
}

records = []

for name, smi in molecules.items():
    mol = Chem.MolFromSmiles(smi)
    if mol is None:
        raise ValueError(f"Failed to parse SMILES for {name}")

    records.append({
        "Molecule": name,
        "MolWt": Descriptors.MolWt(mol),
        "LogP": Descriptors.MolLogP(mol),
        "HBD": Descriptors.NumHDonors(mol),
        "HBA": Descriptors.NumHAcceptors(mol),
        "TPSA": Descriptors.TPSA(mol)
    })

df = pd.DataFrame(records)
print(df.to_string(index=False))
