#!/usr/bin/python
#
# An example of Bayesian inference in action.
#
# Suppose you have a known non-linear function y = f(x) relating two random
# variables x and y. The variable y has been measured but you really want
# to know the variable x.
#
# For every value of x you can write down the distribution of y - this is the
# likelihood function p(y|x). To simplify things we are assuming a Gaussian
# likelihood with a mean and variance that depends on x. This is illustrated in
# the left panel of the plot with a blue line highlighting the conditional
# mean E[y|x].
#
# We now build up the joint distribution p(x, y) as the product of p(y|x) and
# the prior distribution p(x) on the unknown variable x. We take as p(x) = 1 to
# indicate that we are quite ignorant about x's value before we observe y.
# This is how it should be if y is a high-quality measurement of x. The joint
# pdf is shown in the middle panel as a contour plot with logarithmically
# spaced contour levels, together with the two conditional means that come into
# play (more on that soon!). The likelihood function is obtained as vertical
# slices through the joint pdf, as the left panel shows.
#
# Now you want to go in the opposite direction: for a fixed value of y you want
# to determine the distribution of x, called the posterior p(x|y). This is
# related to the joint pdf by Bayes' theorem, one version of which states that
# p(x|y) = p(x, y) / p(y). The data distribution p(y) is merely a scaling
# factor in this example that does not affect the mean, variance or shape of
# the posterior pdf and can therefore be mostly ignored. The posterior pdf is
# obtained by literally slicing the joint pdf (which happens to be equal to the
# likelihood) in the opposite (horizontal) direction, as illustrated in the
# final right panel of the plot. The posterior mean E[x|y] is indicated by a
# red line in the middle and right panels. The resulting distributions are
# *not* Gaussian and the posterior mean E[x|y] is not the same as the
# likelihood mean E[y|x] (although both cases are close matches!).
#
# An important reason to use Bayesian inference is that it produces not only an
# good estimate of x via the posterior mean E[x|y] but also an estimate of the
# uncertainty of this estimate via the posterior variance var[x|y]. This
# variance depends both on the likelihood variance and the slope of the
# non-linear function in the region of the measured y value. As can be seen in
# the right panel, the posterior distribution quickly becomes very broad for
# large values of y because both the likelihood variance increases and the
# non-linear function slope decreases with increasing x.
#
# [As an aside, the posterior mean and variance were estimated from the peak
# region of the posterior pdf via Laplace approximation - but that's another
# story...]
#
# Ludwig Schwardt
# 2 April 2013
#

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# Known Gaussian likelihood function
y_mean_poly = np.array([-9.46057773e-07,   7.97357134e-05,  -2.33606477e-03,
                         1.35757717e-02,   9.81285305e-01,   7.55670064e-02])
y_std_poly = np.array([ -1.03983346e-06,   7.12224246e-05,  -1.58714348e-03,
                         5.10456409e-03,   3.18049306e-01,   1.86474919e-02])
# Laplace approximation to posterior pdf
x_mean_poly = np.array([  3.48713751e-13,  -5.47403988e-11,   3.79337347e-09,
                         -1.52725422e-07,   3.95653738e-06,  -6.90106364e-05,
                          8.24113654e-04,  -6.71723321e-03,   3.65721645e-02,
                         -1.25640610e-01,   2.50191385e-01,   6.66814979e-01,
                          5.22707935e-03])
x_std_poly = np.array([  2.08172854e-14,  -3.51865677e-12,   2.64235598e-10,
                        -1.16011048e-08,   3.29731026e-07,  -6.34011062e-06,
                         8.35950083e-05,  -7.46810111e-04,   4.34255165e-03,
                        -1.43962515e-02,   2.53788636e-02,   2.33516467e-01,
                         5.90923630e-03])

def joint_pdf(x, y):
    """Unnormalised pdf height of joint distribution p(x, y)."""
    mean_y, std_y = np.polyval(y_mean_poly, x), np.polyval(y_std_poly, x)
    return np.exp(-0.5 * ((y - mean_y) / std_y) ** 2) / std_y

def data_pdf_max(y):
    """Approximate maximum pdf height of marginal data distribution p(y)."""
    return 1.0 / np.polyval(x_std_poly, y)

# Create grid on which to evaluate pdfs
x_grid = np.arange(2.0, 20, 0.5)
y_grid = np.arange(2., 25., 0.5)
x_grid_fine = np.arange(0.01, 25, 0.1)
y_grid_fine = np.arange(0.01, 25., 0.1)
joint = np.zeros((len(x_grid_fine), len(y_grid_fine)))
for nx, x in enumerate(x_grid_fine):
    joint[nx, :] = joint_pdf(x, y_grid_fine)
y_mean_fine = np.polyval(y_mean_poly, x_grid_fine)
x_mean_fine = np.polyval(x_mean_poly, y_grid_fine)

fig = plt.figure(1, figsize=(10, 6))
fig.clf()

ax = fig.add_subplot(1, 3, 1)
for n, xg in enumerate(x_grid):
    xslice = joint_pdf(xg, y_grid_fine)
    ax.add_patch(Polygon(np.c_[xg + 10 * xslice, y_grid_fine],
                         fc='w', closed=False, zorder=-n, alpha=0.5))
ax.plot(x_grid_fine, y_mean_fine, '-b', zorder=-1000)
ax.autoscale_view()
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_ylabel('Measured output y')
ax.set_title('Likelihood p(y|x)')
ax.axis('image')
ax.axis([0, 25, 0, 25])

ax = fig.add_subplot(1, 3, 2)
ax.contour(x_grid_fine, y_grid_fine, joint.T, 0.8 * np.logspace(-6, 1, 15),
           colors='k')
ax.plot(x_grid_fine, y_mean_fine, '-b', zorder=-1000, label='E[y | x]')
ax.plot(x_mean_fine, y_grid_fine, '-r', zorder=-1000, label='E[x | y]')
ax.autoscale_view()
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_xlabel('Desired input x')
ax.set_title('Joint pdf p(x, y)')
ax.axis('image')
ax.axis([0, 25, 0, 25])
ax.legend(loc='upper left')

ax = fig.add_subplot(1, 3, 3)
for n, yg in enumerate(y_grid):
    yslice = joint_pdf(x_grid_fine, yg)
    # Let p(x|y) = p(x, y) / p(y) and scale height of slice to correct for p(y)
    yslice *= data_pdf_max(yg) / yslice.max()
    ax.add_patch(Polygon(np.c_[x_grid_fine, yg + 10 * yslice],
                         fc='w', closed=False, zorder=-n, alpha=0.5))
ax.plot(x_mean_fine, y_grid_fine, '-r', zorder=-1000)
ax.autoscale_view()
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_title('Posterior p(x|y)')
ax.axis('image')
ax.axis([0, 25, 0, 25])

fig.subplots_adjust(wspace=0.0)
fig.savefig('bayes_in_action.pdf', bbox_inches='tight')

plt.show()
