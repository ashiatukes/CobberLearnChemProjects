import matplotlib.pyplot as plt
import math
from pathlib import Path

# Data collected from PubChem
molecules = ["ibuprofen", "aspirin", "acetaminophen", "morphine"]

xlogp = [3.5, 1.2, 0.5, 0.8]
tpsa = [37.3, 63.6, 49.3, 52.9]

# Create a similarity matrix
def make_matrix(values, scale, title, filename):
    matrix = []

    for value1 in values:
        row = []

        for value2 in values:
            similarity = math.exp(
                -abs(value1 - value2) / scale
            )
            row.append(similarity)

        matrix.append(row)

    fig, ax = plt.subplots(figsize=(6, 5))

    image = ax.imshow(matrix, vmin=0, vmax=1)

    ax.set_xticks(range(len(molecules)))
    ax.set_yticks(range(len(molecules)))

    ax.set_xticklabels(molecules)
    ax.set_yticklabels(molecules)

    ax.set_title(title)

    for i in range(len(molecules)):
        for j in range(len(molecules)):
            ax.text(
                j, i,
                f"{matrix[i][j]:.2f}",
                ha="center",
                va="center"
            )

    fig.colorbar(image, ax=ax, label="Similarity Score")
    fig.tight_layout()

    output = Path(__file__).with_name(filename)
    plt.savefig(output, dpi=300)

    print(f"{title}: water vs caffeine = {matrix[0][1]:.2f}")


# Generate XLogP matrix
make_matrix(
    xlogp,
    1.0,
    "XLogP Similarity Matrix",
    "XLogPMatrix.png"
)

# Generate TPSA matrix
make_matrix(
    tpsa,
    50.0,
    "TPSA Similarity Matrix",
    "TPSAMatrix.png"
)

plt.show()