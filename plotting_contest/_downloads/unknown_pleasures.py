#!/usr/bin/python
#
# Create your own Unknown Pleasures album cover! See the original at
# http://en.wikipedia.org/wiki/Unknown_Pleasures
#
# The plot represents a series of pulses produced by a pulsar (or pulsating
# neutron star) and recorded by a radio telescope, stacked on top of each
# other for analysis of the pulse structure. The specific pulsar on the iconic
# cover is PSR B1919+21, the very first one discovered in 1967. You can also
# choose your own pulsar for fun!
#
# Ludwig Schwardt
# 3 April 2013
#

import numpy as np
from scipy.signal import resample, filtfilt, get_window
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# The integrated pulse profile for the original pulsar B1919+21 (the same
# pulsar used on the Unknown Pleasures cover), obtained from the EPN archive
# at http://www.jb.man.ac.uk/research/pulsar/Resources/epn/
# This is the 410 MHz version from the Lovell telescope (gl98_410.epn.asc)
pulse_profile = np.array([60.3604279, 479.295197, 1965.36938, 3677.84521,
                          3769.74854, 3510.14917, 3006.14600, 2514.34790,
                          2126.71875, 2143.31738, 2370.14624, 2517.27686,
                          2097.36572, 1361.16357, 499.311279, 152.751862])
# Alternatively, choose your own pulsar from the EPN archive, download the
# ASCII profile of choice and load it as follows:
#
# data = np.loadtxt('jnk98_673.epn.asc', skiprows=2)
# pulse_profile = np.abs(data[:,1]) / data[:,1].max()
# main_pulse = (pulse_profile >= 0.05).nonzero()[0]
# pulse_profile = pulse_profile[main_pulse[0]:main_pulse[-1]]
#
# Some famous choices (the lower frequency data sets work better in general):
# - The Vela pulsar, B0833-45 (brightest in the Southern hemisphere)
#   http://www.jb.man.ac.uk/research/pulsar/Resources/epn/epndb/B0833-45/jnk98_673.epn.asc
# - The Crab pulsar, B0531+21 (only a youthful 959 years old!)
#   http://www.jb.man.ac.uk/research/pulsar/Resources/epn/epndb/B0531+21/mh96_330.epn.asc

# Pad pulse profile with zeros and interpolate to fixed number of samples
pad = int(0.45 * len(pulse_profile))
padded_profile = np.r_[np.zeros(pad), pulse_profile, np.zeros(pad)]
profile = resample(padded_profile, 300)
profile = np.abs(profile) / profile.max()
N = len(profile)
mask = (profile >= 0.01)

# Define smoothing and non-linear operators to tweak each pulse trace
# The edge window gets rid of transient effects at the edges due to filtfilt
edge_window = get_window('hamming', 17)[:8]
edge_window = np.r_[edge_window, np.ones(N - 16), edge_window[::-1]]
# Smooth traces symmetrically with simple moving average filter
smooth = lambda x, M: filtfilt(np.ones(M) / M, [1.], x) * edge_window
# The nonlinearity increases the peakiness of traces
nonlin_knee = 1.
nonlin = lambda y: nonlin_knee * (np.exp(y / nonlin_knee) - 1)
x = np.arange(N)

# Make a figure that is exactly the size of a CD cover (12 cm x 12 cm)
fig = plt.figure(1, figsize=(12 / 2.54, 12 / 2.54))
fig.patch.set_facecolor('black')
fig.clf()
ax = fig.add_subplot(1, 1, 1)
# The CD cover has 80 pulse traces
for row in range(80):
    # The signal is positive with a mean given by the integrated pulse profile
    signal = np.zeros(len(profile))
    signal[mask] = np.random.chisquare(profile[mask])
    noise = 0.05 * np.random.chisquare(np.ones(len(profile)))
    # The signal and noise have different smoothing factors / bandwidths
    y = smooth(signal, 16) + smooth(noise, 4)
    y = nonlin(y)
    # Create overlapping traces via a manual painter's algorithm
    ax.add_patch(Polygon(np.c_[x, row + 2 * y], fc='k', ec='0.85', lw=0.8,
                         closed=False, zorder=-row, alpha=1.0))
ax.autoscale_view()
ax.axis('tight')
# Remove variability of top limit of plot due to peak amplitude of top traces
y_top = ax.get_ylim()[1]
ax.set_position([0.285, 0.22, 0.43, 0.56 * y_top / 82.])
ax.set_ylim(-0.01 * y_top, 1.01 * y_top)
ax.axis('off')

fig.savefig('unknown_pleasures.pdf', facecolor='k', edgecolor='k')

plt.show()
