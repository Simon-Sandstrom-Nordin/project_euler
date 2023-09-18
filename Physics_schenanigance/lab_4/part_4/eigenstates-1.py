# -*- coding: utf-8 -*-
# Python simulation of a partiocle in a 1d infinite box potential
# Integrate time independent SE using the Verlet method
# Boundary conditions are found by shooting
# MW 230519

from pylab import *
import numpy as np
import matplotlib.pyplot as plt

# trial energy
E=0.5*np.pi**2

# for loop
error = 1
tol = 1e-10
iter = 1
max_iter = 10
prev_value = 10000
while error > tol and iter < max_iter:
    # parameters
    N=10000 * 10**iter     # number of mesh points
    dx=1/N              # step length
    dx2=dx**2           # step length squared

    # potential energy function
    def V(x):
        # y = 0.0
        y = x**2/2 + x**4/2     # anharmonic harmonic oscillator
        return y


    # initial values and lists
    x = 0               # initial value of position x
    psi = 0             # wave function at initial position
    dpsi = 1            # derivative of wave function at initial position
    x_tab = []          # list to store positions for plot
    psi_tab = []        # list to store wave function for plot
    x_tab.append(x)
    psi_tab.append(psi)

    for i in range(N) :
        d2psi = 2*(V(x)-E)*psi
        psi += dpsi*dx + 0.5*d2psi*dx2
        d2psinew = 2*(V(x+dx)-E)*psi
        dpsi += 0.5*(d2psi+d2psinew)*dx
        x += dx
        x_tab.append(x)
        psi_tab.append(psi)

    print('E=',E,' psi(xmax)=',psi)

    plt.close()
    plt.figure(num=None, figsize=(8,8), dpi=80, facecolor='w', edgecolor='k')
    plt.plot(x_tab, psi_tab, linewidth=1, color='red')
    #plt.xlim(0, 1)
    #limit=1.e-9
    #plt.ylim(0, limit)
    #plt.ylim(-limit, limit)
    #plt.autoscale(False)
    plt.xlabel('x')
    plt.ylabel('$\psi$')
    #plt.savefig('psi.pdf')
    plt.show()

    iter += 1
    if iter == max_iter:
        print("Max iterations hit")
