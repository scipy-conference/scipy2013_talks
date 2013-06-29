import numpy as np
import matplotlib.pyplot as plot

#Bayesian estimation of unknown mean, Gaussian distributed data
total_obs = 1000
primary_mean = 5.
primary_var = known_var = 4.
x = np.sqrt(primary_var)*np.random.randn(total_obs) + primary_mean
f, axarr = plot.subplots(3)
f.suptitle("Unknown mean ($\mu=$"+`primary_mean`+"), known variance ($\sigma^2=$"+`known_var`+")")
y0label = "Timeseries"
y1label = "Estimate for mean"
y2label = "Doubt in estimate"
axarr[0].set_ylabel(y0label)
axarr[1].set_ylabel(y1label)
axarr[2].set_ylabel(y2label)
axarr[0].plot(x)
prior_mean = 0.
prior_var = 1000000000000.
all_mean_guess = []
all_mean_doubt = []
for i in range(total_obs):
    posterior_mean_doubt = 1./(1./known_var+1./prior_var)
    posterior_mean_guess = (prior_mean/prior_var+x[i]/known_var)*posterior_mean_doubt
    all_mean_guess.append(posterior_mean_guess)
    all_mean_doubt.append(posterior_mean_doubt)
    prior_mean=posterior_mean_guess
    prior_var=posterior_mean_doubt

axarr[1].plot(all_mean_guess)
axarr[2].plot(all_mean_doubt)
plot.show()
