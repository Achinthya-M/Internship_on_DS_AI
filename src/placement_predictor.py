import time
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, f1_score
X, y = make_classification(n_samples=1000, n_features=20, weights=[0.9, 0.1], random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Baseline Accuracy:", accuracy_score(y_test, y_pred))
print("Baseline F1:", f1_score(y_test, y_pred))
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10]
}
start = time.time()
grid_acc = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, scoring='accuracy', cv=3)
grid_acc.fit(X_train, y_train)
grid_time = time.time() - start
start = time.time()
grid_f1 = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, scoring='f1', cv=3)
grid_f1.fit(X_train, y_train)
grid_f1_time = time.time() - start
param_dist = {
    'n_estimators': range(10, 500),
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10, 15]
}
start = time.time()
rand = RandomizedSearchCV(RandomForestClassifier(random_state=42), param_dist, n_iter=20, scoring='f1', cv=3, random_state=42)
rand.fit(X_train, y_train)
rand_time = time.time() - start
print("\nGrid (Accuracy) Best Params:", grid_acc.best_params_)
print("Grid (F1) Best Params:", grid_f1.best_params_)
print("Random Search Best Params:", rand.best_params_)
print("\nTime Taken:")
print("Grid Search:", grid_time)
print("Grid F1:", grid_f1_time)
print("Random Search:", rand_time)
from sklearn.metrics import f1_score
y_pred_grid_acc = grid_acc.predict(X_test)
y_pred_grid_f1 = grid_f1.predict(X_test)
y_pred_rand = rand.predict(X_test)
print("\nFinal Model Comparison (F1 Score):")
print("Baseline F1:", round(f1_score(y_test, y_pred), 2))
print("Grid (Accuracy) F1:", round(f1_score(y_test, y_pred_grid_acc), 2))
print("Grid (F1) F1:", round(f1_score(y_test, y_pred_grid_f1), 2))
print("Random Search F1:", round(f1_score(y_test, y_pred_rand), 2))