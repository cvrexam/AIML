import numpy as np
from scipy.spatial.distance import euclidean, minkowski, jaccard
p1 = np.array([2,7])
p2 = np.array([7,4])
eu_dist = euclidean(p1,p2)
mi_dist = minkowski(p1,p2)
jc_srce = jaccard(p1,p2)
print(eu_dist)
print(mi_dist)
print(jc_srce)
