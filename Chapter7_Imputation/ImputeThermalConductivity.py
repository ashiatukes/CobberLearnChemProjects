import pandas as pd
import numpy as np

df = pd.read_csv("alkane_dataset.csv")

print(df.columns.tolist())
print("Missing thermal conductivity values:", df["thermal conductivity"].isna().sum())

print("Available thermal conductivity values:", df["thermal conductivity"].notna().sum())
known = df.dropna(
    subset=["thermal conductivity", "carbons", "branch number"]
)

print("Training molecules:", len(known))
from sklearn.linear_model import LinearRegression

X = known[["carbons", "branch number"]]
y = np.log(known["thermal conductivity"])

model = LinearRegression()
model.fit(X, y)

print("Thermal conductivity log-linear regression model trained!")
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import mean_absolute_error

predictions = cross_val_predict(model, X, y, cv=5)

mae = mean_absolute_error(
    known["thermal conductivity"],
    np.exp(predictions)
)

print("Thermal conductivity log-linear regression MAE:", round(mae, 4))
from sklearn.neighbors import KNeighborsRegressor

knn = KNeighborsRegressor(n_neighbors=10)

knn_predictions = cross_val_predict(knn, X, y, cv=5)

knn_mae = mean_absolute_error(
    known["thermal conductivity"],
    np.exp(knn_predictions)
)

print("Thermal conductivity KNN (k=10) MAE:", round(knn_mae, 4))
from sklearn.ensemble import RandomForestRegressor

rf = RandomForestRegressor(max_depth=15, random_state=42)

rf_predictions = cross_val_predict(rf, X, y, cv=5)

rf_mae = mean_absolute_error(
    known["thermal conductivity"],
    np.exp(rf_predictions)
)

print("Thermal conductivity Random Forest (depth=15) MAE:", round(rf_mae, 4))
ensemble_predictions = (
    np.exp(predictions)
    + np.exp(knn_predictions)
    + np.exp(rf_predictions)
) / 3

ensemble_mae = mean_absolute_error(
    known["thermal conductivity"],
    ensemble_predictions
)

print("Thermal conductivity Ensemble MAE:", round(ensemble_mae, 4))
import matplotlib.pyplot as plt

actual = known["thermal conductivity"]
predicted = np.exp(knn_predictions)

plt.scatter(actual, predicted, alpha=0.6)

plt.plot(
    [actual.min(), actual.max()],
    [actual.min(), actual.max()],
    "r--"
)

plt.xlabel("Actual Thermal Conductivity")
plt.ylabel("Predicted Thermal Conductivity")
plt.title("Thermal Conductivity: KNN Prediction Quality")

plt.show()
import matplotlib.pyplot as plt

# KNN (k=10) was one of our best models
thermal_predictions = np.exp(knn_predictions)

actual_thermal = known["thermal conductivity"]

relative_error = (
    (thermal_predictions - actual_thermal)
    / actual_thermal
) * 100

# Bias vs. Carbons
plt.figure()
plt.scatter(known["carbons"], relative_error, alpha=0.6)
plt.axhline(0, color="red", linestyle="--")
plt.xlabel("Number of Carbons")
plt.ylabel("Relative Error (%)")
plt.title("Thermal Conductivity: Bias vs. Carbons")
plt.show()

# Bias vs. Branching
plt.figure()
plt.scatter(known["branch number"], relative_error, alpha=0.6)
plt.axhline(0, color="red", linestyle="--")
plt.xlabel("Number of Branches")
plt.ylabel("Relative Error (%)")
plt.title("Thermal Conductivity: Bias vs. Branching")
plt.show()
# Thermal Conductivity Bias Analysis — KNN (k=10)

thermal_predictions = np.exp(
    cross_val_predict(knn, X, y, cv=5)
)

actual_thermal = known["thermal conductivity"]

relative_error = (
    (thermal_predictions - actual_thermal)
    / actual_thermal
) * 100

# Bias vs. Carbons
plt.figure()
plt.scatter(known["carbons"], relative_error, alpha=0.6)
plt.axhline(0, color="red", linestyle="--")
plt.xlabel("Number of Carbons")
plt.ylabel("Relative Error (%)")
plt.title("Thermal Conductivity: Bias vs. Carbons")
plt.show()

# Bias vs. Branching
plt.figure()
plt.scatter(known["branch number"], relative_error, alpha=0.6)
plt.axhline(0, color="red", linestyle="--")
plt.xlabel("Number of Branches")
plt.ylabel("Relative Error (%)")
plt.title("Thermal Conductivity: Bias vs. Branching")
plt.show()