import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse.csgraph import minimum_spanning_tree
from sklearn.neighbors import kneighbors_graph

data = np.genfromtxt("data.csv", delimiter = ",", skip_header = 1)

metric = "euclidean" # see the sklearn.DistanceMetric class for options
metric_params = None
n_neighbors = 20

# Calculate the k-nearest neighbors graph
G = kneighbors_graph(data, n_neighbors = n_neighbors, mode = 'distance', 
                     metric = metric, metric_params = metric_params)

zero_fix = G.data[G.data > 0].min() * 1.e-8
G.data[G.data == 0] = zero_fix

# Calculate the MST of this graph
MST = minimum_spanning_tree(G, overwrite = True)

MST[MST == zero_fix] = 0

lmin = MST[MST > 0].min() # May need to check that this is a true value and not rounding error
lmax = MST[MST > 0].max()
persist = np.zeros(len(data))
degree = MST.getnnz(1)
for i in range(len(data)):
    # Approximate MST means that some nodes are not connected to MST
    if degree[i] > 0: persist[i] = MST[i][MST[i] > 0.].min()
    
persist = (persist - lmin) / (lmax - lmin)
print np.where(persist < 0).shape
idx = np.argsort(persist)

print persist[idx]

