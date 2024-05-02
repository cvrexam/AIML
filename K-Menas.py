from sklearn.cluster import KMeans
import numpy as np
data = np.array([[2,10],[8,4],[5,8],[7,5],[6,4]])
km = KMeans(n_clusters = 3)
km.fit(data)
cnt = km.cluster_centers_
lbls = km.labels_
print("Centroids : ",cnt)
print("Labels : ",lbls)
