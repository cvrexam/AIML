from sklearn_extra.cluster import KMedoids
import numpy as np
data = np.array([[2,10],[8,4],[5,8],[7,5],[6,4]])
kmed = KMedoids(n_clusters=3,random_state=0)
kmed.fit(data)
lbls = kmed.labels_
meds = kmed.medoid_indices_
print(lbls)
print(meds)
