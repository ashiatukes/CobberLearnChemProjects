from pathlib import Path
import matplotlib.pyplot as plt

# Number of carbon atoms
carbons = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Boiling points in Celsius
boiling_points = [
    -161.5, -88.6, -42.1, -0.5, 36.1,
    68.7, 98.4, 125.6, 150.8, 174.1
]

# Create the scatter plot
plt.scatter(carbons, boiling_points)

# Label the graph
plt.title("Boiling Points of Linear Alkanes")
plt.xlabel("Number of Carbon Atoms")
plt.ylabel("Boiling Point (°C)")

# Display the graph
plt.savefig(Path(__file__).resolve().parent / "AlkaneBoilingPoints.png", dpi=300, bbox_inches="tight")

plt.show()
plt.show()
