import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split into training and holdout sets
X_train, X_holdout, y_train, y_holdout = train_test_split(X, y, test_size=0.2, random_state=42)
X_base, X_meta, y_base, y_meta = train_test_split(X_train, y_train, test_size=0.5, random_state=42)
# FULL DATASET (100)
# │
# ├── HOLDOUT (20) → final evaluation
# │
# └── TRAIN (80)
#       │
#       ├── BASE (40) → train base models
#       │
#       └── META (40) → train meta-model

# Initialize base models without using SVC to ensure all models are covered in the lesson
base_models = [DecisionTreeClassifier(), RandomForestClassifier()]

# Train base models and collect predictions for the meta model
base_model_preds = []
for model in base_models:
    model.fit(X_base, y_base)
    preds = model.predict(X_meta)
    base_model_preds.append(preds.reshape(-1, 1))

# Stack predictions to create a new dataset
stacked_preds = np.hstack(base_model_preds)

# Initialize and train the meta model
meta_model = LogisticRegression()
meta_model.fit(stacked_preds, y_meta)

# Get predictions from base models on the holdout set
holdout_preds = []
for model in base_models:
    model.fit(X_base, y_base)  # Retrain the models on the full base set
    preds = model.predict(X_holdout)
    holdout_preds.append(preds.reshape(-1, 1))

# Stack the predictions to create a new dataset
stacked_holdout_preds = np.hstack(holdout_preds)

# Final predictions on the holdout set
final_preds = meta_model.predict(stacked_holdout_preds)

# Calculate the accuracy
accuracy = accuracy_score(y_holdout, final_preds)
print(f'Accuracy: {accuracy*100:.2f}%')