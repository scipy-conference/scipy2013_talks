# Construct a covariance matrix with a correlation length of 15% of its extent
import numpy as np
import math
num_evals=100
l = 15.0 # make scale equal to 25 (out of 125) cum Co2
a = np.zeros((num_evals,num_evals))
for i in range(0,num_evals):
    for j in range (i,num_evals):
        a[i][j] = math.exp(-((i-j)/l)**2)
        a[j][i] = a[i][j]
    a[i][i] += 0.0001 # special sauce
cc = np.linalg.cholesky(a).T
plot(cc) # Plot rendered in plotly, see https://plot.ly/demos/cholesky/
