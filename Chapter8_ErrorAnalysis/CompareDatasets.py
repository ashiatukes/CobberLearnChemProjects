
import pandas as pd
from pathlib import Path
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

folder = Path(__file__).resolve().parent

datasets = [
    "dataset_low_scatter.csv",
    "dataset_high_scatter.csv",
    "dataset_positive_deviation.csv",
    "dataset_negative_deviation.csv"
]

for filename in datasets:
    df = pd.read_csv(folder / filename)

    actual = df["actual"]
    predicted = df["predicted"]

    mae = mean_absolute_error(actual, predicted)
    mse = mean_squared_error(actual, predicted)
    r2 = r2_score(actual, predicted)

    print("\nDataset:", filename)
    print("MAE:", round(mae, 4))
    print("MSE:", round(mse, 4))
    print("R²:", round(r2, 4))

    import matplotlib.pyplot as plt

    residuals = predicted - actual
    name = Path(filename).stem

    # Predicted vs. Actual
    plt.figure()
    plt.scatter(actual, predicted, color="blue")

    limits = [
        min(actual.min(), predicted.min()),
        max(actual.max(), predicted.max())
    ]

    plt.plot(limits, limits, "r--")
    plt.xlabel("Actual Values")
    plt.ylabel("Predicted Values")
    plt.title(name + ": Predicted vs. Actual")
    plt.savefig(folder / f"{name}_prediction.png", dpi=300)
    plt.show()

    # Residual plot
    plt.figure()
    plt.scatter(actual, residuals, color="purple")
    plt.axhline(0, color="red", linestyle="--")
    plt.xlabel("Actual Values")
    plt.ylabel("Residuals")
    plt.title(name + ": Residual Plot")
    plt.savefig(folder / f"{name}_residuals.png", dpi=300)
    plt.show()
