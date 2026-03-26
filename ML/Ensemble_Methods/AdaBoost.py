import numpy as np
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

class AdaBoost:
    def __init__(self, S=10, learning_rate=1):
        self.S = S
        self.learning_rate = learning_rate
        self.models = []
        self.model_weights = []

    def fit(self, X, y):
        M, N = X.shape
        W = np.ones(M) / M
        y = y * 2 - 1

        for _ in range(self.S):
            h = DecisionTreeClassifier(max_depth=1)
            h.fit(X, y, sample_weight=W)

            pred = h.predict(X)
            error = W.dot(pred != y)
            if error > 0.5:
                break

            beta = self.learning_rate * np.log((1 - error) / error)
            # This calculates how much trust to give the current weak learner.
            # error = weighted training error of the tree
            # If error is small → beta is large → model is important
            # If error ≈ 0.5 → beta ≈ 0 → model is useless
            W = W * np.exp(beta * (pred != y))
            # (pred != y) → boolean array
            # correct → 0
            # wrong → 1
            # So:
            # correct → multiply by 
            # exp(0)=1
            # wrong → multiply by exp(beta)
            W = W / W.sum() # normalize

            self.models.append(h)
            self.model_weights.append(beta)

    def predict(self, X):
        Hx = 0
        for h, beta in zip(self.models, self.model_weights):
            Hx += beta * h.predict(X)
        return (Hx > 0) * 1 

# Synthetic dataset creation, training and prediction
data = make_classification(n_samples=200, n_features=5, n_informative=3, n_redundant=2, random_state=1)
X = data[0]
y = data[1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
ada = AdaBoost(S=10, learning_rate=0.5)
ada.fit(X_train, y_train)
predictions = ada.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print('AdaBoost accuracy:', accuracy)