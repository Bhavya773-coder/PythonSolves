import numpy as np
from sklearn.neighbors import NearestNeighbors

# Example dataset: 5 points in 2D space
data = np.array([
    [1, 2],
    [2, 3],
    [3, 4],
    [5, 5],
    [7, 8]
])

# Number of neighbors to find
k = 3

# The point for which to find the nearest neighbors
query_point = np.array([[3, 3]])

# Create and fit the KNN model
knn = NearestNeighbors(n_neighbors=k, algorithm='auto')
knn.fit(data)

# Find the K nearest neighbors
distances, indices = knn.kneighbors(query_point)

# Output the results
print(f"The {k} nearest neighbors to the point {query_point[0]} are at indices {indices[0]} with distances {distances[0]}")

# Print the actual nearest neighbors
nearest_neighbors = data[indices[0]]
print(f"Nearest neighbors: \n{nearest_neighbors}")
