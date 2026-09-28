import numpy as np
import matplotlib.pyplot as plt

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
rotatable_bonds = [
    0,  # water
    0,  # ammonia
    0,  # methane
    0,  # ethanol
    0,  # acetone
    0,  # acetic acid
    0,  # benzene
    1,  # glucose
    0,  # caffeine
    2,  # serotonin
    0,  # sulfuric acid
    3   # histamine
]

matrix = []

for bond1 in rotatable_bonds:
    row = []
    for bond2 in rotatable_bonds:
        if bond1 == bond2:
            similarity = 1.0
        else:
            similarity = 1 / (1 + abs(bond1 - bond2))
        row.append(similarity)
    matrix.append(row)

matrix = np.array(matrix)

fig, ax = plt.subplots(figsize=(10, 8))

im = ax.imshow(matrix, vmin=0, vmax=1)

ax.set_xticks(np.arange(len(molecules)))
ax.set_yticks(np.arange(len(molecules)))

ax.set_xticklabels(molecules, rotation=45, ha="right")
ax.set_yticklabels(molecules)

ax.set_title("Rotatable Bonds Similarity Matrix")

plt.colorbar(im, ax=ax, label="Similarity Score")
plt.tight_layout()
plt.show()