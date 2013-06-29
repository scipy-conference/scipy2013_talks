import numpy as np
import matplotlib.pyplot as plot
import math
from sklearn import datasets

X,y = datasets.make_regression(n_samples=1000,n_features=1,n_informative=1,noise=15,bias=1000)
#Ensure y array is 2D
y = y[:,np.newaxis]

#Add bias terms
X = np.hstack((np.ones((X.shape[0],1)), X))

#Initialize theta to zeros
theta = np.zeros((X.shape[1],1))
alpha = 0.01
iters = 1000

def linear_cost(theta,X,y):
    m = y.shape[0]
    return 1./(2.*m)*np.sum((np.dot(X,theta)-y)**2.)

def linear_cost_grad(theta,X,y):
    m = y.shape[0]
    return 1./m*np.dot(X.T,(y-np.dot(X,theta)))

def gradient_descent(theta,X,y,alpha,iters):
    m = y.shape[0]
    all_cost = []
    print theta.shape
    for i in range(iters):
        all_cost.append(linear_cost(theta,X,y))
        theta += float(alpha)*linear_cost_grad(theta,X,y)
    return theta,all_cost

#Perform linear reagression via gradient descent
theta,all_cost = gradient_descent(theta,X,y,alpha,iters)
plot.figure()
plot.title("Cost vs. number of iterations")
plot.plot(range(len(all_cost)),all_cost)
plot.figure()
plot.title("Linear Regression")

#Use only the linear term
plot.plot(X[:,1], y, 'rx')
plot.plot(X[:,1], np.dot(X,theta))
plot.show()
