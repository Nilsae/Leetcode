import matplotlib.pyplot as plt

# Toy dataset with 2D points
data = [(2,3), (5,3.4), (1.3,1), (3,4), (2,3.5), (7,5)]

# k-Means settings
k = 2  
centers = [data[0], data[3]]  # Fixed initial centers selection.

# Definition of Euclidean distance
def distance(point1, point2):
    return ((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)**0.5

# k-Means algorithm
def k_means(data, centers, k):
    while True:
        clusters = [[] for _ in range(k)]

        # Assign data points to the closest center
        for point in data:
            distances = [distance(point, center) for center in centers]
            index = distances.index(min(distances))
            clusters[index].append(point)

            # or : 
            # min_d = distance(point, centers[0])
            # closest_center_idx = 0
            # for idx, center in enumerate(centers):
            #     if distance(point, center) < min_d:
            #         min_d = distance(point, center)
            #         closest_center_idx = idx
            # clusters[closest_center_idx].append(point)

        # Update centers to be the mean of points in a cluster
        new_centers = []
        for cluster in clusters:
            if len(cluster) == 0:  # We only expect valid clusters with our data.
                continue
            center = (sum([point[0] for point in cluster])/len(cluster), 
                      sum([point[1] for point in cluster])/len(cluster))
            new_centers.append(center)

        # Break loop if centers don't change significantly
        if max([distance(new, old) for new, old in zip(new_centers, centers)]) < 0.0001:
            break
        else:
            centers = new_centers
    return clusters, centers

clusters, centers = k_means(data, centers, k)

# Visualization of the clusters
colors = ['r', 'g', 'b', 'y', 'c', 'm']
fig, ax = plt.subplots()

# Plot points
for i, cluster in enumerate(clusters):
    for point in cluster:
        ax.scatter(*point, color=colors[i])

# Plot centers
for i, center in enumerate(centers):
    ax.scatter(*center, color='black', marker='x', s=300)

ax.set_title('Clusters and their centers')
plt.show()