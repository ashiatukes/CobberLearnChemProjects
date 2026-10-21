
import numpy as np
import pandas as pd
from pathlib import Path

# Save CSV files in the Chapter 8 folder
folder = Path(__file__).resolve().parent

# Reproducible simulated data
rng = np.random.default_rng(42)
actual = np.linspace(10, 100, 50)

datasets = {
    "dataset_low_scatter.csv":
        actual + rng.normal(0, 2, 50),

    "dataset_high_scatter.csv":
        actual + rng.normal(0, 15, 50),

    "dataset_positive_deviation.csv":
        actual + 10 + rng.normal(0, 2, 50),

    "dataset_negative_deviation.csv":
        actual - 10 + rng.normal(0, 2, 50)
}

for filename, predicted in datasets.items():
    df = pd.DataFrame({
        "actual": actual,
        "predicted": predicted
    })

    df.to_csv(folder / filename, index=False)
    print(f"Created: {filename}")

print("All four simulated datasets created!")
