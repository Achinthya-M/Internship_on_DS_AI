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
from sklearn.preprocessing import LabelEncoder
data = {
    "Transmission": ["Automatic", "Manual", "Automatic", "Manual", "Automatic"],
    "Color": ["Red", "Blue", "Green", "Red", "Blue"]
}
df = pd.DataFrame(data)
print("Original Data:")
print(df)
le = LabelEncoder()
df["Transmission"] = le.fit_transform(df["Transmission"])
df = pd.get_dummies(df, columns=["Color"], drop_first=True)
print("Encoded Data:")
print(df)

#task 2
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler
data={"Age":[22,25,30,35,40,45,50],"Salary":[20000,25000,40000,50000,60000,80000,100000]}
df=pd.DataFrame(data)
print("Original Data:")
print(df)
standard_scaler=StandardScaler()
df_standardized=pd.DataFrame(standard_scaler.fit_transform(df),columns=df.columns)
print("Standardized Data (StandardScaler):")
print(df_standardized)
minmax_scaler=MinMaxScaler()
df_normalized=pd.DataFrame(minmax_scaler.fit_transform(df),columns=df.columns)
print("\nNormalized Data (MinMaxScaler):")
print(df_normalized)
plt.figure(figsize=(15,5))
plt.subplot(1,3,1)
plt.hist(df["Salary"],bins=5,edgecolor="black")
plt.title("Before Scaling")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.grid(True)
plt.subplot(1,3,2)
plt.hist(df_standardized["Salary"],bins=5,edgecolor="black")
plt.title("After StandardScaler")
plt.xlabel("Standardized Salary")
plt.ylabel("Frequency")
plt.grid(True)
plt.subplot(1,3,3)
plt.hist(df_normalized["Salary"],bins=5,edgecolor="black")
plt.title("After MinMaxScaler")
plt.xlabel("Normalized Salary (0 to 1)")
plt.ylabel("Frequency")
plt.grid(True)
plt.tight_layout()
plt.show()


#task 3
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score
data={"Experience":[0,1,2,3,4,5,6,7,8,9,10],"Salary":[20000,23000,28000,36000,47000,61000,78000,98000,121000,147000,176000]}
df=pd.DataFrame(data)
X=df[["Experience"]]
y=df["Salary"]
linear_model=LinearRegression()
linear_model.fit(X,y)
y_pred_linear=linear_model.predict(X)
r2_linear=r2_score(y,y_pred_linear)
poly=PolynomialFeatures(degree=2)
X_poly=poly.fit_transform(X)
poly_model=LinearRegression()
poly_model.fit(X_poly,y)
y_pred_poly=poly_model.predict(X_poly)
r2_poly=r2_score(y,y_pred_poly)
plt.figure(figsize=(12,5))
plt.suptitle("Linear vs Polynomial Regression")
plt.subplot(1,2,1)
plt.scatter(X,y,label="Actual Data")
plt.plot(X,y_pred_linear,label="Linear Fit")
plt.title("Linear Regression Fit")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.legend()
plt.grid(True)
plt.subplot(1,2,2)
plt.scatter(X,y,label="Actual Data")
plt.plot(X,y_pred_poly,label="Polynomial Fit (Degree=2)")
plt.title("Polynomial Regression Fit (Degree=2)")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
print("R² Score using Original Linear Feature:",round(r2_linear,4))
print("R² Score using Polynomial Features (degree=2):",round(r2_poly,4))
if r2_poly>r2_linear:
    print("\nPolynomial features improved the model by capturing the curve in the data.")
else:
    print("\nPolynomial features did not improve the model.")
    
    
    
    
    
    
    
    
    
    
    
    



































