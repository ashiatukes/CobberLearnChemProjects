
import numpy as np

actual = np.array([2, 4, 5, 4, 5, 7, 9])
predicted = np.array([2.5, 3.5, 4, 5, 6, 8, 8])

residuals = predicted - actual

mae = np.mean(np.abs(residuals))
mse = np.mean(residuals ** 2)

r2 = 1 - (
    np.sum(residuals ** 2) /
    np.sum((actual - np.mean(actual)) ** 2)
)

print("Residuals:", residuals)
print("MAE:", round(mae, 4))
print("MSE:", round(mse, 4))
print("R²:", round(r2, 4))

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

print("\nScikit-learn Verification:")
print("MAE:", round(mean_absolute_error(actual, predicted), 4))
print("MSE:", round(mean_squared_error(actual, predicted), 4))
print("R²:", round(r2_score(actual, predicted), 4))

import matplotlib.pyplot as plt
from pathlib import Path

folder = Path(__file__).resolve().parent

plt.figure(figsize=(7, 5))


# Highlight predictions with the largest errors
max_error = np.max(np.abs(residuals))

colors = [
    "red" if abs(r) == max_error else "blue"
    for r in residuals
]

plt.scatter(actual, predicted, c=colors,
            label="Predictions")


plt.plot([2, 9], [2, 9], "r--",
         label="Perfect Prediction")

plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.title("Predicted vs. Actual Values")
plt.legend()
plt.grid(True)

plt.savefig(folder / "Predicted_vs_Actual.png", dpi=300)
plt.show()

# Create residual plot
plt.figure(figsize=(7, 5))

plt.scatter(actual, residuals, color="blue")

plt.axhline(
    y=0,
    color="red",
    linestyle="--",
    label="Zero Error"
)

plt.xlabel("Actual Values")
plt.ylabel("Residuals")
plt.title("Residual Plot")
plt.legend()
plt.grid(True)

# Save graph
plt.savefig(folder / "Residual_Plot.png", dpi=300)

plt.show()

print("\nActual | Predicted | Residual")
print("-----------------------------")

for a, p, r in zip(actual, predicted, residuals):
    print(f"{a:6.1f} | {p:9.1f} | {r:8.1f}")
