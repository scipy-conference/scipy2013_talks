#!/usr/bin/env python

from ode import get_numpy_norm_f, rossler_system_factory
from runge_kutta import a_RK4

from numpy import array
from pylab import *
from mpl_toolkits.mplot3d import Axes3D

def rossler_system():
    a = 0.3980000000
    b = 2.0
    c = 4.0
    rossler = rossler_system_factory(a, b, c)

    timestep = 0.001
    x_0 = array([-1.0, -1.0, 2.0])
    t_0 = 0.0
    tolerance = 0.01
    n = 50000
    euclidean_norm = get_numpy_norm_f(2)

    ts, xs, ys, zs = [], [], [], []
    for t, (x, y, z) in a_RK4(rossler, h = timestep, x = x_0, t = t_0,
                              tol = tolerance, n = n, norm_f = euclidean_norm):
        ts.append(t)
        xs.append(x)
        ys.append(y)
        zs.append(z)

    fig = figure('Adaptive RK4 on Rossler', figsize=(22,15))
    suptitle("Figure 3: Adaptive RK4 on Rossler:\na=%.3f, b=%.2f, c=%.2f, "
             "IC = %s, tol = %.2f" %
             (a, b, c, str(list(x_0)), tolerance))

    ax = Axes3D(fig)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.scatter(xs, ys, zs, s=1)
    savefig('/Users/arp/Documents/chaotic_dynamics/assignments/5/rossler.png')
    show()

if __name__ == "__main__":
    rossler_system()
