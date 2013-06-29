from sklearn import decomposition as dc
from sklearn import datasets as ds
import matplotlib.pyplot as plot
import numpy as np

boston = ds.load_boston()
houses = boston.data

#Plot the unnormalized 2D projection
pca = dc.PCA(n_components=2)
pca.fit(houses)
reduced = pca.transform(houses)
plot.scatter(reduced[:,0],reduced[:,1])
plot.title("Unnormalized PCA")

#Normalize and plot the 2D projection
houses -= np.mean(houses, axis=0)
houses /= np.var(houses, axis=0)
pca.fit(houses)
reduced = pca.transform(houses)
plot.figure()
plot.scatter(reduced[:,0],reduced[:,1])
plot.title("Normalized PCA")
plot.show()
