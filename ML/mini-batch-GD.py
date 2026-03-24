# Making the batch size smaller means the model updates its parameters more frequently, using more varied subsets of the data each time.

# This introduces more "noise" into each update, which can help the model escape local minima and potentially find a better solution.
# Smaller batches also mean more updates per epoch, so the model learns faster from different parts of the data.
# too small of a batch size (like 1) might not always be best because it makes training unstable due to too much noise.





import numpy as np
from sklearn.metrics import mean_absolute_error

# Mini-Batch Gradient Descent function
def gradient_descent(X, y, learning_rate=0.01, batch_size=16, epochs=100):
    m, n = X.shape
    theta = np.random.randn(n, 1)  # random initialization

    for epoch in range(epochs):
        shuffled_indices = np.random.permutation(m)
        X_shuffled = X[shuffled_indices]
        y_shuffled = y[shuffled_indices]
        for i in range(0, m, batch_size):
            x_batch = X_shuffled[i:i + batch_size]
            y_batch = y_shuffled[i:i + batch_size]
            cur_bs = x_batch.shape[0]
            gradient = (1 / cur_bs) * x_batch.T @ (( x_batch @ theta) - y_batch)
            # print(x_batch.shape)
            # print(y_batch.shape)
            # print(gradient.shape)
            # print(theta.shape)
            theta -= learning_rate * gradient
    return theta

# Prepare sample data as per the lesson
X = np.random.rand(100, 3)
y = 5 * X[:, 0] - 3 * X[:, 1] + 2 * X[:, 2] + np.random.randn(100, 1)  # Example linear regression problem
y = y.reshape(-1, 1) 
# -1 → “figure this dimension out automatically”
# 1 → make the second dimension equal to 1 
# same as unsqueeze in pytorch -> converts (100, ) to (100, 1)

# Perform Mini-Batch Gradient Descent
theta = gradient_descent(X, y)

# Obtain predictions using the optimized parameters
predictions = X.dot(theta)

# Calculate Mean Absolute Error (MAE) to evaluate the model
mae = mean_absolute_error(y, predictions)
print(f"MAE: {mae}")







