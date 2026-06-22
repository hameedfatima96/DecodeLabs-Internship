import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# ======================================
# FIND DATA FILE
# ======================================

folder = os.path.dirname(__file__)

print("Project Folder:")
print(folder)

print("\nFiles Found:")
print(os.listdir(folder))

# Change filename if needed
csv_file = os.path.join(folder, "employee.csv")

if not os.path.exists(csv_file):
    print("\nERROR: employee.csv not found!")
    print("Check the exact filename in your folder.")
    exit()

# ======================================
# LOAD DATASET
# ======================================

try:
    df = pd.read_csv(csv_file)
except Exception as e:
    print("\nCould not read CSV file.")
    print(e)
    exit()

print("\nDataset Loaded Successfully")
print("Shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())

# ======================================
# CHECK ATTRITION COLUMN
# ======================================

if "Attrition" not in df.columns:
    print("\nERROR: Column 'Attrition' not found.")
    print("Available columns:")
    print(df.columns.tolist())
    exit()

# ======================================
# EDA
# ======================================

plt.figure(figsize=(6, 4))

df["Attrition"].value_counts().plot(kind="bar")

plt.title("Employee Attrition Distribution")
plt.xlabel("Attrition")
plt.ylabel("Count")

plt.tight_layout()
plt.show()

# ======================================
# PREPROCESSING
# ======================================

encoder = LabelEncoder()

for column in df.columns:
    if df[column].dtype == object:
        df[column] = encoder.fit_transform(df[column])

# ======================================
# FEATURES AND TARGET
# ======================================

X = df.drop("Attrition", axis=1)
y = df["Attrition"]

# ======================================
# TRAIN TEST SPLIT
# ======================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# ======================================
# MODELS
# ======================================

models = {
    "Decision Tree": DecisionTreeClassifier(random_state=42),

    "Random Forest": RandomForestClassifier(
        n_estimators=100,
        random_state=42
    ),

    "Logistic Regression": LogisticRegression(
        max_iter=5000
    )
}

results = {}

# ======================================
# TRAIN AND EVALUATE
# ======================================

for name, model in models.items():

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    results[name] = accuracy

    print("\n" + "=" * 50)
    print(name)
    print("=" * 50)

    print(
        "Accuracy:",
        round(accuracy * 100, 2),
        "%"
    )

    print("\nClassification Report:\n")
    print(
        classification_report(
            y_test,
            predictions
        )
    )

# ======================================
# BEST MODEL
# ======================================

best_model = max(results, key=results.get)

print("\n" + "=" * 50)
print("BEST MODEL:", best_model)
print(
    "ACCURACY:",
    round(results[best_model] * 100, 2),
    "%"
)
print("=" * 50)

# ======================================
# ACCURACY CHART
# ======================================

plt.figure(figsize=(7, 5))

plt.bar(
    list(results.keys()),
    list(results.values())
)

plt.title("Model Accuracy Comparison")
plt.ylabel("Accuracy")

plt.tight_layout()
plt.show()