import numpy as np
import matplotlib.pyplot as plot


N = 1000
upper_lim = 10 #Upper bound for data, where points will be random from 0 to upper_lim
noise_var = B = 4 #Add Gaussian noise

xs = np.sort(upper_lim*np.random.rand(N,1), axis=0)
#Generating function
ys = np.square(xs) - 4*xs + 1
wm = ys + B*np.random.randn(N,1)

c = iter(['rx', 'b', 'g', 'k'])
plot.figure()
plot.title("Linear Regression")
plot.plot(wm, c.next())

def gen_dft(m, n, N):
    return np.exp(1j*-2*m*n/N)

def gen_polynomial(x, m, N=None):
    return np.power(x, m)

for i in ["line","polynomial","dft"]:
    N_basis = 3 if i != "line" else 2
    basis_func = np.vectorize(gen_dft) if i == "dft" else np.vectorize(gen_polynomial)
    basis = basis_func(np.arange(N)[:,np.newaxis], np.arange(N_basis),N).T

    test_data = t = np.dot(basis,wm)
    #Calculate the Moore-Penrose pseudoinverse using the following formula
    #maximum_likelihood = wml = np.linalg.inv(basis.T*basis)*basis.T*t
    #Direct calculation appears to have numerical instability issues...
    #Luckily the pinv method calculates Moore-Penrose pseudo inverse using SVD, which largely avoids the numerical issues
    maximum_likelihood = wml = np.dot(np.linalg.pinv(basis),t)
    plot.plot(np.real(wml),c.next())
plot.show()
