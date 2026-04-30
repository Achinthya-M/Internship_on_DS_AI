import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

X = np.array([
    [1, 50],
    [2, 60],
    [3, 65],
    [4, 70],
    [5, 75],
    [6, 80],
    [7, 85],
    [8, 90]
])

y = np.array([30, 40, 50, 55, 65, 70, 80, 90])

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "model.pkl")

print("Model saved successfully")