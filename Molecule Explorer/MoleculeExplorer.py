# Chapter 6: Molecule Explorer
# This program uses RDKit to analyze molecules from SMILES strings.
# It generates molecular structures and calculates chemical properties.

from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import Descriptors
# Keep the program running so the user can analyze multiple molecules.
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

        print("Exact Molecular Weight:", round(exact_mw, 2))
        print("Hydrogen Bond Donors:", h_bond_donors)
        print("TPSA:", round(tpsa, 2))
        print("LogP:", round(logp, 2))
        print("Rotatable Bonds:", rotatable_bonds)

    again = input("Analyze another molecule? (yes/no): ")

    if again.lower() != "yes":
        print("Molecule Explorer finished.")
        break
