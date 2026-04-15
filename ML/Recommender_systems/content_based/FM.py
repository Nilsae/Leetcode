import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from data_extraction import extract_dataset

class SimpleFactorizationMachine:
    def __init__(self, n_factors, n_features, learning_rate=0.01, epochs=100, reg=0.01):
        self.n_factors = n_factors
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.reg = reg
        
        self.w0 = 0
        self.W = np.zeros(n_features)
        self.V = np.random.normal(0, 0.1, (n_features, n_factors))

    def fit(self, X, y):
        m, n = X.shape
        for epoch in range(self.epochs):
            for i in range(m):
                linear_terms = self.w0 + np.dot(X[i], self.W)
                interaction_term = sum(
                    (np.dot(X[i], self.V[:, f]) ** 2 - np.dot(X[i] ** 2, self.V[:, f] ** 2)) / 2
                    for f in range(self.n_factors))
                predictions = linear_terms + interaction_term
                err = predictions - y[i]
                
                self.w0 -= self.learning_rate * err
                self.W -= self.learning_rate * (err * X[i] + self.reg * self.W)
                
                for f in range(self.n_factors):
                    V_f = self.V[:, f]
                    self.V[:, f] -= self.learning_rate * (
                        err * (X[i] @ V_f - X[i] ** 2 * V_f) / 2 + self.reg * V_f)

    def predict(self, X):
        m, n = X.shape
        y_pred = np.zeros(m)
        for i in range(m):
            linear_terms = self.w0 + np.dot(X[i], self.W)
            # - First term (dot(...)**2) captures all interactions (including self-interactions)
            # - Second term subtracts self-interactions (i == j)
            # - Division by 2 removes double counting (i,j and j,i)
            # Result equals: sum_{i<j} <v_i, v_j> * x_i * x_j
            interaction_term = sum(
                (np.dot(X[i], self.V[:, f]) ** 2 - np.dot(X[i] ** 2, self.V[:, f] ** 2)) / 2 
                for f in range(self.n_factors))
            y_pred[i] = linear_terms + interaction_term
        return y_pred


# Extract dataset
df = extract_dataset()

# Split dataset into train and test
X = df.drop(columns=['rating']).values
y = df['rating'].values
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.4, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# Hyperparameter tuning
best_mae = float('inf')
best_params = (0, 0, 0)
learning_rates = [0.001, 0.01]
n_factors_list = [2, 3]
reg_list = [0.01, 0.1]

for lr in learning_rates:
    for n_factors in n_factors_list:
        for reg in reg_list:
            fm_model = SimpleFactorizationMachine(n_factors = n_factors, n_features = len(X[0]), learning_rate=lr, reg=reg)
            fm_model.fit(X_train, y_train)
            y_val_pred = fm_model.predict(X_val)
            mae = np.mean(abs((y_val - y_val_pred)))
            print(f'Parameters: lr={lr}, n_factors={n_factors}, reg={reg} ==> MAE={mae:.4f}')
            
            if mae < best_mae:
                best_mae = mae
                best_params = (lr, n_factors, reg)

print(f'Best Parameters: lr={best_params[0]}, n_factors={best_params[1]}, reg={best_params[2]} with MAE={best_mae:.4f}')

# Train final model with best parameters
best_lr, best_n_factors, best_reg = best_params
final_model = SimpleFactorizationMachine(n_factors=best_n_factors, n_features=X_train.shape[1], 
                                         learning_rate=best_lr, epochs=1000, reg=best_reg)
final_model.fit(X_train, y_train)
y_pred = final_model.predict(X_test)

# Evaluate model using Mean Absolute Error
mae = np.mean(abs((y_test - y_pred)))
print(f'Test Mean Absolute Error: {mae:.4f}')