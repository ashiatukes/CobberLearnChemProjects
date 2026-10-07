import pandas as pd
from sklearn.tree import DecisionTreeClassifier
data = {
    "Molecule": [
        "Molecule 1", "Molecule 2", "Molecule 3", "Molecule 4",
        "Molecule 5", "Molecule 6", "Molecule 7", "Molecule 8",
        "Molecule 9", "Molecule 10"
    ],
    "Molecular Weight": [180, 250, 80, 300, 150, 400, 90, 200, 130, 275],
    "Hydrogen Bond Donors": [5, 2, 1, 1, 4, 3, 0, 2, 3, 1],
    "Hydrogen Bond Acceptors": [6, 3, 2, 2, 5, 4, 1, 3, 4, 2],
    "Water Solubility": [1, 0, 1, 0, 1, 0, 1, 0, 0, 1]
}

df = pd.DataFrame(data)
X = df[["Molecular Weight", "Hydrogen Bond Donors", "Hydrogen Bond Acceptors"]]
y = df["Water Solubility"]

print(df)i