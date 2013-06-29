import numpy as np
import scipy.optimize as opt
from scipy.io import loadmat
import matplotlib.pyplot as plot
from matplotlib import cm

def sigmoid(X):
    return 1./(1.+np.exp(-X))

def logistic_cost(theta, X, y):
    m = y.shape[0]
    if len(theta.shape) < 2:
        theta = theta[:,np.newaxis]
    h = sigmoid(np.dot(X,theta))
    #THE LINES BELOW DO NOT WORK VERY WELL
    #POSSIBLE NUMERICAL ISSUES?
    #Direct versions with distributed minus
    #return np.ravel(1./m*np.sum(-y*np.log(h) - (1.-y)*np.log(1.-h)))
    #return np.ravel(1./m*(np.dot(-y.T,np.log(h)) - np.dot((1.-y.T),np.log(1.-h))))

    #PARAMETERIZATIONS THAT WORK
    #return np.ravel(-1./m*(np.dot(y.T,np.log(h)) + np.dot((1.-y).T,np.log(1.-h))))
    #Chose this one since it seems the most direct
    return np.ravel(-1./m*np.sum(y*np.log(h) + (1.-y)*np.log(1.-h)))

def logistic_cost_grad(theta, X, y):
    m = y.shape[0]
    if len(theta.shape) < 2:
        theta = theta[:,np.newaxis]
    h = sigmoid(np.dot(X,theta))
    return np.ravel(1./m*np.dot(X.T,h-y))

def logistic_cost_reg(theta, X, y, l=.1):
    m = y.shape[0]
    if len(theta.shape) < 2:
        theta = theta[:,np.newaxis]
    reg = l/(2.*m)*np.sum(theta[1:,:]**2.)
    return np.ravel(logistic_cost(theta,X,y) + reg)

def logistic_cost_reg_grad(theta, X, y, l=.1):
    m = y.shape[0]
    if len(theta.shape) < 2:
        theta = theta[:,np.newaxis]
    reg = float(l)/m*np.sum(np.vstack((np.zeros(1), theta[1:,:])))
    return np.ravel(logistic_cost_grad(theta,X,y) + reg)

#Perform classification of MNIST digits
from sklearn import datasets
digits = datasets.load_digits()
X = digits.data
plotdim = 4
randind = np.random.randint(X.shape[0],size=(plotdim,plotdim))
f1, axarr = plot.subplots(plotdim,plotdim)
for i in range(plotdim):
    for j in range(plotdim):
        axarr[i,j].get_xaxis().set_visible(False)
        axarr[i,j].get_yaxis().set_visible(False)
#Digits are 8x8 images
for i in range(plotdim):
    for j in range(plotdim):
        axarr[i,j].imshow(X[randind[i,j],:].reshape(8,8), cmap=cm.gray)

#These digits are randomly ordered, if given an ORDERED set
#of training data make sure to randomize before splitting
#Normalize between 0 and 1
X = digits.data/255.

#Subtract the mean, though it doesn't appear to make a big difference
X = X - np.mean(X)
y = digits.target.T[:,np.newaxis]

#Add bias terms
X = np.hstack((np.ones((X.shape[0],1)), X))

#Expect 10 labels for digits
num_labels = np.amax(y)-np.amin(y)+1
all_theta = np.zeros((X.shape[1],num_labels))

for c in range(num_labels):
    #Initialize theta to zeros and pass into optimization routine
    theta0 = np.zeros((X.shape[1],))
    #fmin_cg requires the cost and cost_grad functions to return flattened 1D arrays!
    #theta = opt.fmin_cg(logistic_cost, theta0, fprime=logistic_cost_grad, args=(X, (y == c)), maxiter=50)
    #Use regularized cost function
    theta = opt.fmin_cg(logistic_cost_reg, theta0, fprime=logistic_cost_reg_grad, args=(X, (y == c)), maxiter=50)
    all_theta[:,c] = theta

#We can use the builtin check_grad function to perform numerical gradient
#checking, ensuring the gradient code is correct for the cost
#print opt.check_grad(logistic_cost, logistic_cost_grad, theta, X, y)
h = sigmoid(np.dot(X, all_theta))
pred = np.argmax(h,axis=1)[:,np.newaxis]
print "Classification accuracy(%):" + `100*np.sum((y == pred))/float(len(y))`

for i in range(plotdim):
    for j in range(plotdim):
        ind = randind[i,j]
        if y[ind] == pred[ind]:
            text_color = 'g'
        else:
            text_color = 'r'
        axarr[i,j].set_title("Label=" + `pred[ind,:][0]`,color=text_color)
plot.suptitle("Overall classification accuracy(%):" + `round(100*np.sum((y == pred))/float(len(y)),2)`)
plot.show()
