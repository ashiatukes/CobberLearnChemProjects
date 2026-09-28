from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import Descriptors

while True:
    smiles = input("Enter a SMILES string: ")

    molecule = Chem.MolFromSmiles(smiles)

    if molecule is None:
        print("Invalid SMILES string.")
    else:
        Draw.MolToFile(molecule, "molecule.png")

        exact_mw = Descriptors.ExactMolWt(molecule)
        h_bond_donors = Descriptors.NumHDonors(molecule)
        tpsa = Descriptors.TPSA(molecule)
        logp = Descriptors.MolLogP(molecule)
        rotatable_bonds = Descriptors.NumRotatableBonds(molecule)

        print("Exact Molecular Weight:", exact_mw)
        print("Hydrogen Bond Donors:", h_bond_donors)
        print("TPSA:", tpsa)
        print("LogP:", logp)
        print("Rotatable Bonds:", rotatable_bonds)

    again = input("Analyze another molecule? (yes/no): ")

    if again.lower() != "yes":
        print("Molecule Explorer finished.")
        break
