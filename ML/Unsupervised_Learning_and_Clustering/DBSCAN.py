# DBSCAN: Density-Based Spatial Clustering of Applications with Noise


import numpy as np
import matplotlib.pyplot as plt


# Euclidean distance function
def euclidean_distance(a, b):
    return np.linalg.norm(a - b)


# DBSCAN algorithm function
def dbscan(data, Eps, MinPts):
    point_label = [0] * len(data)
    point_count = []
    core = []
    noncore = []

    for i in range(len(data)):
        point_count.append([])
        for j in range(len(data)):
            if euclidean_distance(data[i], data[j]) <= Eps:
                point_count[i].append(j)

        if len(point_count[i]) >= MinPts:
            core.append(i)
        else:
            noncore.append(i)

    ID = 1
    for point in core:
        if point_label[point] == 0:
            point_label[point] = ID
            queue = []
            for x in point_count[point]:
                if point_label[x] == 0:
                    point_label[x] = ID
                    if x in core:
                        queue.append(x)

            while queue:
                neighbours = point_count[queue.pop(0)]
                for y in neighbours:
                    if point_label[y] == 0:
                        point_label[y] = ID
                        if y in core:
                            queue.append(y)
            ID += 1

    return point_label


# Toy dataset
data_points = np.array([
    [1, 2], [1, 3], [2, 2], [8, 7], [8, 8], [25, 80],
    [24, 79], [25, 81], [80, 25], [81, 26], [79, 24], [89, 90]
])

# Run DBSCAN
labels = dbscan(data_points, Eps=8, MinPts=3)

# Plot the results
colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
for i in range(len(labels)):
    plt.scatter(data_points[i][0], data_points[i][1], s=100, c=colors[labels[i] % len(colors)])

plt.show()