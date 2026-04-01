import numpy as np
import matplotlib.pyplot as plt

# Create a toy dataset
np.random.seed(1)
X = np.dot(np.random.random(size=(3, 3)), np.random.normal(size=(3, 150))).T

# Standardize the dataset
X_mean = np.mean(X, axis=0)
X_std = np.std(X, axis=0)
X_stdzd = (X - X_mean) / X_std

# Compute Covariance Matrix
cov_matrix = np.cov(X_stdzd.T)

# Perform eigendecomposition
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
# vs, lambdas

# Sort eigenvalues and corresponding eigenvectors
eigen_pairs = [(np.abs(eigenvalues[i]), eigenvectors[:,i]) for i in range(len(eigenvalues))]
# or eigen_pairs = [(v, lam) for v, lam in zip(np.abs(vs), lambdas.T)]

eigen_pairs.sort(reverse=True)

# Construct the projection matrix
W = np.hstack((eigen_pairs[0][1].reshape(3,1), eigen_pairs[1][1].reshape(3,1)))

# Transform the original dataset
X_pca = X_stdzd.dot(W)

# Visualize the results
plt.scatter(X_pca[:, 0],X_pca[:, 1])
plt.title("Scatter Plot of Transformed Dataset Using PCA")
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.grid(True)
plt.show()