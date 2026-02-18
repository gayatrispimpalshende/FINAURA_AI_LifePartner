import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# -----------------------------
# Generate Synthetic Dataset
# -----------------------------
np.random.seed(42)

data_size = 400

age = np.random.randint(22, 60, data_size)
income = np.random.randint(20000, 150000, data_size)
monthly_expense = np.random.randint(10000, 120000, data_size)
medical_percent = np.random.randint(5, 50, data_size)
savings_percent = np.random.randint(5, 60, data_size)
life_event = np.random.randint(0, 4, data_size)  # 0 None, 1 Marriage, 2 Baby, 3 Job Change
app_active_time = np.random.randint(0, 2, data_size)  # 0 Morning, 1 Night

target = []

for i in range(data_size):
    if medical_percent[i] > 30:
        target.append(0)  # Insurance
    elif savings_percent[i] > 40:
        target.append(1)  # Investment
    elif monthly_expense[i] > income[i]:
        target.append(2)  # Loan
    else:
        target.append(3)  # Savings Plan

df = pd.DataFrame({
    "age": age,
    "income": income,
    "monthly_expense": monthly_expense,
    "medical_percent": medical_percent,
    "savings_percent": savings_percent,
    "life_event": life_event,
    "app_active_time": app_active_time,
    "target": target
})

X = df.drop("target", axis=1)
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", accuracy)

joblib.dump(model, "finaura_model.pkl")

print("Model saved as finaura_model.pkl")
