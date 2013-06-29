# -*- coding: utf-8 -*-
# This script was created for a homework assignment in CSCI 4446: Chaotic
# Dynamics. It plots a state space diagram, omega vs theta, of the damped 
# pendulum. For the chosen parameter values, the trajectory has become chaotic,
# resulting in an interesting graphic.

import math
import numpy as np
import matplotlib.pyplot as plt

# First order system for the damped pendulum
# m is mass, l is the length of the pendulum, g is gravity, A is the
# aplitude of the driving force, beta is a damping factor related to friction
# and alpha is the drive frequency
def dpend(x, t, m, l, beta, g, A, alpha):
    y0 = x[1]
    w = alpha * t
    gamma = 1/(m*l)
    y1 = gamma*(A*math.cos(w) - beta*l*x[1] - m*g*math.sin(x[0]))
    y = np.array([[y0],[y1]])
    return y
 
# Integrator for first order systems using RK4
def rk(n, dim, x0, t0, dt, f, args):
    x = np.zeros((dim, n))
    x[:,0] = x0[:,0]
    t = t0    
    for i in range(1,n):
        v1 = f(x[:,i - 1],t, *args)
        v2 = f(x[:,i - 1] + (dt/2)*v1[:,0], t + (dt/2), *args)
        v3 = f(x[:,i - 1] + (dt/2)*v2[:,0], t + (dt/2), *args)
        v4 = f(x[:,i - 1] + dt*v3[:,0], t + dt, *args)
        x[:,i] = x[:,i - 1] + (dt/6)*(v1[:,0] + 2*v2[:,0] + 2*v3[:,0] + v4[:,0])
        t += dt
    return x
        
n = 50000 # number of time steps 
dim = 2 # dimension of state space
x0 = np.array([[3.15],[0]]) # starting point in state space
t0 = 0 # start time
dt = 0.005 #size of time step
m = 0.1 
g = 9.8 
l = 0.1
beta = 0.25
A = 1
alpha = 0.7809 * math.sqrt(g/l)
args = [m, l, beta, g, A, alpha]
x = rk(n, dim, x0, t0, dt, dpend, args)
theta = abs(np.fmod(x[0,:], 2*math.pi)) # theta is plotted modulo 2 pi
omega = x[1,:]
plt.scatter(theta, omega, s=0.5, marker = ',')
plt.title('Chaotic Trajectory in the State Space of the Damped Pendulum')
plt.xlabel(r'$\theta$ modulo 2$\pi$ (radians)')
plt.ylabel(r'$\omega$ (radians/second)')
plt.savefig('damped_pendulum.ps', orientation='landscape', dpi=600)
