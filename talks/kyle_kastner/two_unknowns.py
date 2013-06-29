import matplotlib.pyplot as plot
import numpy as np

#Bayesian estimation of unknown mean, unknown variance on Gaussian data
total_obs = 1000
primary_mean = 5.
primary_var = 4.
x = np.sqrt(primary_var)*np.random.randn(total_obs) + primary_mean
f, axarr = plot.subplots(3)
f.suptitle("Unknown mean ($\mu=$"+`primary_mean`+"), unknown variance ($\sigma^2=$"+`primary_var`+")")
y0label = "Timeseries"
y1label = "Estimate for mean"
y2label = "Estimate for variance"
axarr[0].set_ylabel(y0label)
axarr[1].set_ylabel(y1label)
axarr[2].set_ylabel(y2label)
axarr[0].plot(x)
prior_mean = 0.
prior_var = 1.
prior_kappa = 1.
prior_v = 0.
all_mean_guess = []
all_var_guess = []
for i in range(total_obs):
    posterior_mean = (prior_kappa*prior_mean+x[i])/(prior_kappa + 1)
    posterior_var = (prior_v*prior_var + prior_kappa/(prior_kappa + 1)*(x[i]-prior_mean)**2)/(prior_v + 1)
    prior_kappa += 1
    prior_v += 1
    all_mean_guess.append(posterior_mean)
    all_var_guess.append(posterior_var)
    prior_mean = posterior_mean
    prior_var = posterior_var

axarr[1].plot(all_mean_guess)
axarr[2].plot(all_var_guess)
plot.show()
