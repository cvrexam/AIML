import kmedoids
import numpy as np

# Generate some random data
data = np.array([[2,10],[8,4],[5,8],[7,5],[6,4]])

# Compute the k-medoids clustering
km = kmedoids.KMedoids(n_clusters=5, random_state=0)
c = km.fit(data)

# Get the clusters and medoids
clusters = c.labels_
medoids = km.medoid_indices_

print("Clusters:", clusters)
print("Medoids:", medoids)