import numpy as np
from scipy.stats import mode
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from collections import Counter


class RandomForest:
    def __init__(self, n_trees=100, max_depth=None):
        self.n_trees = n_trees
        self.max_depth = max_depth
        self.trees = []

    def bootstrapping(self, X, y):
        n_samples = X.shape[0]
        idxs = np.random.choice(n_samples, n_samples, replace=True)
        return X[idxs], y[idxs]

    def fit(self, X, y):
        np.random.seed(42)  # Ensuring reproducibility
        for _ in range(self.n_trees):
            X_, y_ = self.bootstrapping(X, y)
            tree = DecisionTreeClassifier(max_depth=self.max_depth)
            tree.fit(X_, y_)
            self.trees.append(tree)

    def predict(self, X):
        tree_preds = np.array([tree.predict(X) for tree in self.trees])
        return mode(tree_preds)[0]


# Prepare the iris dataset
iris = load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# Initialize and fit the RandomForest classifier
rf = RandomForest(n_trees=100, max_depth=2)
rf.fit(X_train, y_train)

# Predict and evaluate the accuracy
y_pred = rf.predict(X_test)
print("Accuracy: ", accuracy_score(y_test, y_pred))