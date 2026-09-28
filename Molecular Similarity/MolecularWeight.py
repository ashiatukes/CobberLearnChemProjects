import pubchempy as pcp
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Molecules from the textbook
molecules = [
    "water",
    "ammonia",
    "methane",
    "ethanol",
    "acetone",
    "acetic acid",
    "benzene",
    "glucose",
    "caffeine",
    "serotonin",
    "sulfuric acid",
    "histamine"
]
# Reference molecular weights in g/mol
# Rounded values for our independent comparison

weights = [
    18.02,   # water
    17.03,   # ammonia
    16.04,   # methane
    46.07,   # ethanol
    58.08,   # acetone
    60.05,   # acetic acid
    78.11,   # benzene
    180.16,  # glucose
    194.19,  # caffeine
    176.22,  # serotonin
    98.08,   # sulfuric acid
    111.15   # histamine
]

for name, weight in zip(molecules, weights):
    print(f"{name}: {weight:.2f} g/mol")


# Our own comparison formula:
# Similarity = smaller weight / larger weight
matrix = []

for weight1 in weights:
    row = []

    for weight2 in weights:
        similarity = min(weight1, weight2) / max(weight1, weight2)
        row.append(similarity)

    matrix.append(row)

matrix = np.array(matrix)

# Create the similarity matrix
fig, ax = plt.subplots(figsize=(12, 10))

image = ax.imshow(matrix, vmin=0, vmax=1)

ax.set_xticks(range(len(molecules)))
ax.set_yticks(range(len(molecules)))

ax.set_xticklabels(molecules, rotation=90)
ax.set_yticklabels(molecules)

ax.set_title("Molecular Weight Similarity Matrix")

fig.colorbar(image, ax=ax, label="Similarity Score")
fig.tight_layout()

# Save the graph in your project folder
output = Path(__file__).with_name("MolecularWeightMatrix.png")

plt.savefig(output, dpi=300)
plt.show()