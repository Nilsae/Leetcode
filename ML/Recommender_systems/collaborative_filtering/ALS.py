# Alternating Least Squares
# 1. Fix item factors, solve for user factors to minimize error.
# 2. Fix user factors, solve for item factors to minimize error.
# 3. Repeat until the latent embeddings converge.

# l: regularization weight 
# We are trying to minimize (R - U @ V)^2 + l(|U|^2 + |V|^2)
# = (R - U @ V).T * (R - U @ V) + l|U|^2 + l|V|^2
# if we have item factor fixed and find the best user factor:
# take the derivative with respect to U and set to zero:
# -2 V (R - U @ V) + 2 l|U| = 0
# -2VR + 2VUV + 2 lU = 0
# -2VR + U(2VV + 2 lI) = 0
# -b + A x = 0 -> solve for x, x being U



import numpy as np
import random

# Initialize user-item interaction matrix with explicit feedback
R = []
with open('explicit_ratings.txt', 'r') as file:
    users = file.readlines()
    for user in users:
        ratings = list(map(int, user.split(' ')))
        R.append(ratings)
R = np.array(R)

num_users, num_items = R.shape
num_factors = 3
lambda_reg = 0.1
num_iterations = 20

# Randomly selectively mark some entries as missing (-1)
original_R = R.copy()  # Create a copy to track original values for RMSE calculation
missing_ratio = 0.1  # Fraction of entries to exclude
num_missing = int(missing_ratio * np.count_nonzero(R != -1))
missing_indices = random.sample(list(zip(*np.where(R != -1))), num_missing)

for (u, i) in missing_indices:
    R[u, i] = -1  # Mark selected original values as missing

# Initialize user and item factors randomly
U = np.random.rand(num_users, num_factors) * 0.01
V = np.random.rand(num_items, num_factors) * 0.01

# ALS algorithm
def train_als():
    global U, V
    for iteration in range(num_iterations):
        for u in range(num_users):
            V_u = V[R[u, :] != -1, :]
            R_u = R[u, R[u, :] != -1]
            if V_u.shape[0] > 0:
                U[u] = np.linalg.solve(
                    V_u.T @ V_u + lambda_reg * np.eye(num_factors),
                    V_u.T @ R_u
                )
                
        # Update item factors
        for i in range(num_items):
            U_i = U[R[:, i] != -1, :]
            R_i = R[R[:, i] != -1, i]
            if U_i.shape[0] > 0:
                V[i, :] = np.linalg.solve(
                    np.dot(U_i.T, U_i) + lambda_reg * np.eye(num_factors),
                    np.dot(U_i.T, R_i)
                )

train_als()

# Predict the ratings
predicted_R = np.dot(U, V.T)

# Calculate RMSE for excluded items
def calculate_rmse(original_R, predicted_R, missing_indices):
    mse = np.sum([(original_R[u, i] - predicted_R[u, i]) ** 2 for (u, i) in missing_indices]) / len(missing_indices)
    return np.sqrt(mse)

rmse = calculate_rmse(original_R, predicted_R, missing_indices)

# Replace the missing values with predictions
R_filled = R.copy()
R_filled[R == -1] = predicted_R[R == -1]

print("Original Rating Matrix with Missing Values (-1):")
print(R)
print("\nPredicted Rating Matrix:")
print(R_filled)
print(f"\nRMSE for the excluded items: {rmse:.4f}")