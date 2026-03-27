# Increasing the batch_size generally leads to more stable and accurate centroid estimates.

# While it does require more computation per iteration, it often converges in fewer steps than smaller batches.



import numpy as np
import matplotlib.pyplot as plt

def euclidean_dist(a, b):
    # calculate the Euclidean distance between data points
    return np.sqrt(np.sum((a - b) ** 2, axis=1))

def initialize_centers(data, k):
    # initialize k centroids randomly from the data
    idx = np.random.choice(len(data), size=k, replace=False)
    return data[idx, :]

def mini_batch_kMeans(data, k, iterations=100, batch_size=20):
    # mini-batch k-means clustering algorithm
    centers = initialize_centers(data, k)
    for _ in range(iterations):
        idx = np.random.choice(len(data), size=batch_size, replace=False)
        batch = data[idx, :]
        distances = np.array([euclidean_dist(center, batch) for center in centers])
        labels = np.argmin(distances, axis=0)
        for i in range(k):
            centers[i] = np.mean(batch[labels == i], axis=0) if len(batch[labels == i]) > 0 else centers[i]
    return centers

# Prepare the data
np.random.seed(42)
data = np.vstack([
    np.random.normal(loc=[2, 2], scale=0.5, size=(100, 2)),
    np.random.normal(loc=[-2, -2], scale=0.5, size=(100, 2))
])

# Apply the algorithm
centers = mini_batch_kMeans(data, k=2)

# Plot data and clusters
plt.scatter(data[:, 0], data[:, 1], s=50)
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.5)
plt.title('Mini-Batch K-Means Clustering')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.show()