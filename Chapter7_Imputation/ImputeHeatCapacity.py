import pandas as pd
import numpy as np

df = pd.read_csv("alkane_dataset.csv")

print(df.columns.tolist())
print("Missing heat capacity values:", df["heat capacity"].isna().sum())

print("Available heat capacity values:", df["heat capacity"].notna().sum())
known = df.dropna(
    subset=["heat capacity", "carbons", "branch number"]
)

print("Training molecules:", len(known))
from sklearn.linear_model import LinearRegression

X = known[["carbons", "branch number"]]
y = np.log(known["heat capacity"])

model = LinearRegression()
model.fit(X, y)

print("Heat capacity log-linear regression model trained!")
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import mean_absolute_error

predictions = cross_val_predict(model, X, y, cv=5)

mae = mean_absolute_error(
    known["heat capacity"],
    np.exp(predictions)
)

print("Heat capacity log-linear regression MAE:", round(mae, 4))
from sklearn.neighbors import KNeighborsRegressor

knn = KNeighborsRegressor(n_neighbors=10)

knn_predictions = cross_val_predict(knn, X, y, cv=5)

knn_mae = mean_absolute_error(
    known["heat capacity"],
    np.exp(knn_predictions)
)

print("Heat capacity KNN (k=10) MAE:", round(knn_mae, 4))
from sklearn.ensemble import RandomForestRegressor

rf = RandomForestRegressor(max_depth=15, random_state=42)

rf_predictions = cross_val_predict(rf, X, y, cv=5)

rf_mae = mean_absolute_error(
    known["heat capacity"],
    np.exp(rf_predictions)
)

print("Heat capacity Random Forest (depth=15) MAE:", round(rf_mae, 4))
ensemble_predictions = (
    np.exp(predictions)
    + np.exp(knn_predictions)
    + np.exp(rf_predictions)
) / 3

ensemble_mae = mean_absolute_error(
    known["heat capacity"],
    ensemble_predictions
)

print("Heat capacity Ensemble MAE:", round(ensemble_mae, 4))
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_predict

# Random Forest (depth=15) was our best heat capacity model
heat_predictions = np.exp(cross_val_predict(rf, X, y, cv=5))

actual_heat = known["heat capacity"]

relative_error = (
    (heat_predictions - actual_heat)
    / actual_heat
) * 100

# Bias vs. Carbons
plt.figure()
plt.scatter(known["carbons"], relative_error, alpha=0.6)
plt.axhline(0, color="red", linestyle="--")
plt.xlabel("Number of Carbons")
plt.ylabel("Relative Error (%)")
plt.title("Heat Capacity: Bias vs. Carbons")
plt.show()

# Bias vs. Branching
plt.figure()
plt.scatter(known["branch number"], relative_error, alpha=0.6)
plt.axhline(0, color="red", linestyle="--")
plt.xlabel("Number of Branches")
plt.ylabel("Relative Error (%)")
plt.title("Heat Capacity: Bias vs. Branching")
plt.show()