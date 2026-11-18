from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
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
X = df[["Hydrogen Bond Donors"]]
y = df["Water Solubility"]

print(df)
# Create and train the decision tree
model = DecisionTreeClassifier(max_depth=2, random_state=42)
model.fit(X, y)

print("\nDecision tree trained successfully!")
print("Training accuracy:", model.score(X, y))
plt.figure(figsize=(12, 8))

plot_tree(
    model,
    feature_names=X.columns,
    class_names=["Not Soluble", "Soluble"],
    filled=True,
    rounded=True
)
plt.savefig("decision_tree_donors_only.png", dpi=300, bbox_inches="tight")
plt.show()