import numpy as np
import matplotlib.pyplot as plot

#Bayesian estimation of unknown variance for Gaussian distributed data
total_obs = 1000
primary_mean = known_mean = 5
primary_var = 4
x = np.sqrt(primary_var)*np.random.randn(total_obs) + primary_mean
all_a = []
all_b = []
all_prec_guess = []
all_prec_doubt = []
prior_a=1/2.+1
prior_b=1/2.*np.sum((x[0]-primary_mean)**2)
f,axarr = plot.subplots(3)
f.suptitle("Known mean ($\mu=$"+`known_mean`+"), unknown variance ($\sigma^2=$"+`primary_var`+"; $\lambda$="+`1./primary_var`+")")
y0label = "Timeseries"
y1label = "Estimate for precision"
y2label = "Doubt in estimate"
axarr[0].set_ylabel(y0label)
axarr[1].set_ylabel(y1label)
axarr[2].set_ylabel(y2label)

axarr[0].plot(x)
for i in range(1,total_obs):
    posterior_a=prior_a+1/2.
    posterior_b=prior_b+1/2.*np.sum((x[i]-known_mean)**2)
    all_a.append(posterior_a)
    all_b.append(posterior_b)
    all_prec_guess.append(posterior_a/posterior_b)
    all_prec_doubt.append(posterior_a/(posterior_b**2))
    prior_a=posterior_a
    prior_b=posterior_b

axarr[1].plot(all_prec_guess)
axarr[2].plot(all_prec_doubt)
plot.show()
