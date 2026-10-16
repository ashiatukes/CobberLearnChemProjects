import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
df = pd.read_csv("alkane_dataset.csv")

print(df.head())
print(df.columns.tolist())

print("Missing viscosity values:", df["viscosity"].isna().sum())
print("Available viscosity values:", df["viscosity"].notna().sum())
known = df.dropna(
        subset=["viscosity", "carbons", "branch number"]
    )

print("Training molecules:", len(known))
X = known[["carbons", "branch number"]]
y = np.log(known["viscosity"])

model = LinearRegression()
model.fit(X, y)

print("Log-linear regression model trained!")
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import mean_absolute_error

predictions = cross_val_predict(model, X, y, cv=5)
actual_viscosity = np.exp(y)
predicted_viscosity = np.exp(predictions)
mae = mean_absolute_error(actual_viscosity, predicted_viscosity)

print("Log-linear regression MAE:", round(mae, 4))
from sklearn.neighbors import KNeighborsRegressor
knn = KNeighborsRegressor(n_neighbors=10)
knn_predictions = cross_val_predict(knn, X, np.exp(y), cv=5)

knn_mae = mean_absolute_error(np.exp(y), knn_predictions)

print("KNN (k=10) MAE:", round(knn_mae, 4))
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor(max_depth=15, random_state=42)

rf.fit(X, known["viscosity"])

print("Random Forest (depth=15) model trained!")
rf_predictions = cross_val_predict(rf, X, known["viscosity"], cv=5)

rf_mae = mean_absolute_error(known["viscosity"], rf_predictions)

print("Random Forest (depth=15) MAE:", round(rf_mae, 4))
ensemble_predictions = (
    predicted_viscosity + knn_predictions + rf_predictions
) / 3

ensemble_mae = mean_absolute_error(
    known["viscosity"], ensemble_predictions
)

print("Ensemble MAE:", round(ensemble_mae, 4))
import matplotlib.pyplot as plt
plt.scatter(known["viscosity"], predicted_viscosity)

plt.xlabel("Actual Viscosity")
plt.ylabel("Predicted Viscosity")
plt.title("Log-Linear Regression: Prediction Quality")
plt.plot([0, 1.2], [0, 1.2], "r--", label="Perfect Prediction")
plt.legend()
plt.show()
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_predict

# Use your trained log-linear regression model
# Change "model" if your regression variable has another name
predicted_viscosity = ensemble_predictions

actual_viscosity = known["viscosity"]

relative_error = (
    (predicted_viscosity - actual_viscosity)
    / actual_viscosity
) * 100

# Bias vs. Carbons
plt.figure()
plt.scatter(known["carbons"], relative_error, alpha=0.6)
plt.axhline(0, color="red", linestyle="--")
plt.xlabel("Number of Carbons")
plt.ylabel("Relative Error (%)")
plt.title("Viscosity: Bias vs. Carbons")
plt.show()

# Bias vs. Branching
plt.figure()
plt.scatter(known["branch number"], relative_error, alpha=0.6)
plt.axhline(0, color="red", linestyle="--")
plt.xlabel("Number of Branches")
plt.ylabel("Relative Error (%)")
plt.title("Viscosity: Bias vs. Branching")
plt.show()