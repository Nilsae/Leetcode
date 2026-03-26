import math
import numpy as np
import matplotlib.pyplot as plt


def euclidean_distance(point1, point2):
    return math.sqrt(sum((p - q) ** 2 for p, q in zip(point1, point2)))
def manhattan_distance(point1, point2):
    return sum(abs(p - q)  for p, q in zip(point1, point2))

def k_nearest_neighbors(data, query, k, distance_fn):
    neighbor_distances_and_indices = []

    for index, (point, label) in enumerate(data):
        distance = distance_fn(point, query)
        neighbor_distances_and_indices.append((distance, index))

    k_nearest_distances_and_indices = sorted(neighbor_distances_and_indices)[:k]

    k_nearest_labels = [data[i][1] for distance, i in k_nearest_distances_and_indices]

    from collections import Counter
    most_common_label = Counter(k_nearest_labels).most_common(1)[0][0]

    return most_common_label


fruits_data = [
    ((1.2, 0.4), 'Apple'),
    ((1.0, 0.5), 'Apple'),
    ((1.6, 0.7), 'Orange'),
    ((1.3, 0.3), 'Apple'),
    ((1.8, 0.8), 'Orange')
]

fruit_query = (1.4, 0.6)

predicted_type = k_nearest_neighbors(fruits_data, fruit_query, k=5, distance_fn=euclidean_distance)
print(predicted_type)

# Extract fruit features and labels
fruit_features = np.array([item[0] for item in fruits_data])
fruit_labels = np.array([item[1] for item in fruits_data])


# Create a scatter plot of apples and oranges
for fruit_type in ['Apple', 'Orange']:
    plt.scatter(
        fruit_features[fruit_labels==fruit_type, 0],
        fruit_features[fruit_labels==fruit_type, 1],
        label=fruit_type
    )

# Add the query point
plt.scatter(*fruit_query, color='red', label='query', marker='x')
plt.legend()
plt.title('Fruits Classification with kNN')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()