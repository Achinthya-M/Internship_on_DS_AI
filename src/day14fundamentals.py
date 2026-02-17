# Import Libraries
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, MinMaxScaler, StandardScaler, PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Create Dataset (Salary Prediction Example)
# In real projects: df = pd.read_csv("dataset.csv")
data = {
    "Age": [25,30,35,40,28,32,45,50,23,36,29,41],
    "Experience": [1,3,7,10,2,5,15,20,1,8,4,12],
    "Education_Level": ["Bachelors","Masters","PhD","PhD","Bachelors","Masters",
                        "PhD","Masters","Bachelors","Masters","Bachelors","PhD"],
    "Department": ["IT","HR","IT","Finance","HR","IT","Finance","Finance","HR","IT","HR","Finance"],
    "Salary": [30000,40000,50000,65000,42000,48000,80000,90000,28000,52000,46000,70000]
}
df = pd.DataFrame(data)

# Inspect Dataset & Identify Feature Types
print("\nDataset Info:")
print(df.info())
# Separate target variable
target = "Salary"
# Identify numerical & categorical columns
numerical_cols = ["Age", "Experience"]
categorical_cols = ["Education_Level", "Department"]

# ENCODING CATEGORICAL VARIABLES
# Label Encoding → for ORDINAL categories (Education Level has order)
le = LabelEncoder()
df["Education_Level_Encoded"] = le.fit_transform(df["Education_Level"])
# One-Hot Encoding → for NOMINAL categories (Department has no order)
df = pd.get_dummies(df, columns=["Department"], drop_first=True)
# Drop original categorical column after encoding
df = df.drop("Education_Level", axis=1)
print("\nDataset after encoding:")
print(df.head())

# Prepare Feature Matrix (X) and Target (y)
X = df.drop(target, axis=1)
y = df[target]
# Train-Test Split BEFORE scaling (to avoid data leakage)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# BASELINE MODEL (Before Scaling & Polynomial Features)
model = LinearRegression()
model.fit(X_train, y_train)
baseline_preds = model.predict(X_test)
baseline_score = r2_score(y_test, baseline_preds)
print("\nBaseline Model R² Score:", baseline_score)

# FEATURE SCALING
# Standard Scaling (mean=0, std=1)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
# Train model on scaled features
scaled_model = LinearRegression()
scaled_model.fit(X_train_scaled, y_train)
scaled_preds = scaled_model.predict(X_test_scaled)
scaled_score = r2_score(y_test, scaled_preds)
print("Model Score After Scaling:", scaled_score)

# POLYNOMIAL FEATURES (Non-linear relationships)
poly = PolynomialFeatures(degree=2, include_bias=False)
X_train_poly = poly.fit_transform(X_train_scaled)
X_test_poly = poly.transform(X_test_scaled)
# Train model on engineered features
poly_model = LinearRegression()
poly_model.fit(X_train_poly, y_train)
poly_preds = poly_model.predict(X_test_poly)
poly_score = r2_score(y_test, poly_preds)
print("Model Score After Polynomial Features:", poly_score)

# FINAL COMPARISON
print("\n===== PERFORMANCE COMPARISON =====")
print("Before Feature Engineering :", baseline_score)
print("After Scaling             :", scaled_score)
print("After Polynomial Features :", poly_score)
# FINAL FEATURE MATRIX READY FOR ML PIPELINES
print("\nFinal Feature Shape:", X_train_poly.shape)
print("\nFeature Engineering Completed Successfully!")

#task 1
import pandas as pd
df = pd.DataFrame({
    "Transmission": ["Automatic", "Manual", "Manual", "Automatic", "Manual"],
    "Color": ["Red", "Blue", "Green", "Red", "Blue"]
})
df["Transmission"] = df["Transmission"].map({"Manual": 0, "Automatic": 1})
df = pd.get_dummies(df, columns=["Color"], drop_first=True)
print(df)

#task 2
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler
df = pd.DataFrame({
    "Age": [22, 25, 28, 30, 35, 40, 45, 50],
    "Salary": [25000, 30000, 45000, 50000, 65000, 80000, 100000, 120000]
})
standard_scaler = StandardScaler()
minmax_scaler = MinMaxScaler()
df_standardized = pd.DataFrame(
    standard_scaler.fit_transform(df),
    columns=df.columns
)
df_normalized = pd.DataFrame(
    minmax_scaler.fit_transform(df),
    columns=df.columns
)
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.hist(df["Salary"], bins=6)
plt.title("Salary Before Scaling")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.subplot(1, 2, 2)
plt.hist(df_standardized["Salary"], bins=6)
plt.title("Salary After StandardScaler")
plt.xlabel("Scaled Salary")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

#task 3
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
np.random.seed(42)
X = np.arange(1, 51).reshape(-1, 1)
y = 3*(X[:, 0]**2) + 5*X[:, 0] + 10 + np.random.normal(0, 200, size=50)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)
y_pred_linear = linear_model.predict(X_test)
r2_linear = r2_score(y_test, y_pred_linear)
poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X)
X_train_p, X_test_p, y_train_p, y_test_p = train_test_split(X_poly, y, test_size=0.2, random_state=42)
poly_model = LinearRegression()
poly_model.fit(X_train_p, y_train_p)
y_pred_poly = poly_model.predict(X_test_p)
r2_poly = r2_score(y_test_p, y_pred_poly)
print("R² Score (Original Features):", r2_linear)
print("R² Score (Polynomial Features degree=2):", r2_poly)



































