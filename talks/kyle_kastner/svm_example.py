from sklearn import svm
from sklearn import datasets as ds
from sklearn import cross_validation as cv
from sklearn import decomposition as dc
from collections import defaultdict
import matplotlib.pyplot as plot
import numpy as np

#Slightly tweak version of scikit-learn sample code
iris = ds.load_iris()

#project iris data to 2D
pca = dc.PCA(n_components=2)
pca.fit(iris.data)
X = pca.transform(iris.data)
Y = iris.target

#Normally try test_size=.2 but we want to see some errors
X_train, X_test, Y_train, Y_test = cv.train_test_split(X, Y, test_size=.9)

C = 1.0 #Margin constant
svc = svm.SVC(kernel="linear", C=C)
svc.fit(X_train,Y_train)
Y_pred = svc.predict(X_test)

#Plot decision boundaries
h=0.2
clf = svm.SVC(kernel="linear",C=C)
clf.fit(X,Y)
x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plot.pcolormesh(xx,yy,Z)

plot.scatter(X_test[:,0],X_test[:,1],c=Y_test)
plot.xlim(xx.min(), xx.max())
plot.ylim(yy.min(), yy.max())
plot.title("SVM")
plot.show()
