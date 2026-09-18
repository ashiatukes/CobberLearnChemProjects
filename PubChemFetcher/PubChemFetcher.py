# This script uses PubChemPy to retrieve molecular properties
# from PubChem using a compound's name.
# Retrieve molecular properties from PubChem

import pubchempy as pcp

name = input("Enter a molecule name: ").strip()

properties = [
    "MolecularWeight",
    "MolecularFormula",
    "SMILES",
    "HBondDonorCount",
    "HBondAcceptorCount",
    "XLogP"
]

try:
    results = pcp.get_properties(properties, name, "name")

    if results:
        molecule = results[0]

        print("\nResults for:", name)
        print("Molecular weight:", molecule.get("MolecularWeight"))
        print("Molecular formula:", molecule.get("MolecularFormula"))
        print("SMILES:", molecule.get("SMILES", "Not available"))
        print("H-bond donors:", molecule.get("HBondDonorCount"))
        print("H-bond acceptors:", molecule.get("HBondAcceptorCount"))
        print("XLogP:", molecule.get("XLogP"))

    else:
        print("No molecule found.")

except pcp.PubChemPyError as error:
    print("PubChem returned an error:", error)


