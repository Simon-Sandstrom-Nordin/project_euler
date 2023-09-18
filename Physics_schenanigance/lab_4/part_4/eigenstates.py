# -*- coding: utf-8 -*-
# Python simulation of a partiocle in a 1d infinite box potential
# Integrate time independent SE using the Verlet method
# Boundary conditions are found by shooting
# MW 220513

from pylab import *
import numpy as np
import matplotlib.pyplot as plt


def energy_to_error(E):

    # parameters
    N=10000               # number of mesh points
    dx=1/N             # step length
    dx2=dx**2          # step length squared

    # potential energy function
    def V(x):
        # y = 0.0
        y = x**2/2 + x**4/2     # harmonic oscillator
        return y

    # initial values and lists
    x = 0               # initial value of position x
    psi = 0             # wave function at initial position
    dpsi = 1            # derivative of wave function at initial position
    x_tab = []          # list to store positions for plot
    psi_tab = []        # list to store wave function for plot
    x_tab.append(x)
    psi_tab.append(psi)

    for i in range(N):
        d2psi = 2*(V(x)-E)*psi
        d2psinew = 2*(V(x+dx)-E)*psi
        psi += dpsi*dx + 0.5*d2psi*dx2
        dpsi += 0.5*(d2psi+d2psinew)*dx
        x += dx
        x_tab.append(x)
        psi_tab.append(psi)

    print('E=', E, ' psi(xmax)=', psi)

    return psi


def plot(E):

    # parameters
    N=10000               # number of mesh points
    dx=1/N             # step length
    dx2=dx**2          # step length squared

    # potential energy function
    def V(x):
        # y = 0.0
        y = x**2/2 + x**4/2     # harmonic oscillator
        return y

    # initial values and lists
    x = 0               # initial value of position x
    psi = 0             # wave function at initial position
    dpsi = 1            # derivative of wave function at initial position
    x_tab = []          # list to store positions for plot
    psi_tab = []        # list to store wave function for plot
    x_tab.append(x)
    psi_tab.append(psi)

    for i in range(N):
        d2psi = 2*(V(x)-E)*psi
        d2psinew = 2*(V(x+dx)-E)*psi
        psi += dpsi*dx + 0.5*d2psi*dx2
        dpsi += 0.5*(d2psi+d2psinew)*dx
        x += dx
        x_tab.append(x)
        psi_tab.append(psi)

    print('E=', E, ' psi(xmax)=', psi)
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
    return None

# energy_guess_lower = 0.4*np.pi**2
# energy_guess_higher = 0.7*np.pi**2
energy_guess_lower = 8*np.pi**2**1
energy_guess_higher = 9.5*np.pi**2**1

# states
# 5.1316490504250565
# 19.987641904873115
# 44.67184672167343
# 79.21902882315945

tol = 10**(-8)
error = 1
while error > tol:
    low = energy_to_error(energy_guess_lower)
    high = energy_to_error(energy_guess_higher)
    mid = energy_to_error((energy_guess_lower + energy_guess_higher)/2)
    error = abs(energy_guess_higher - energy_guess_lower)
    if high * mid > 0:
        energy_guess_higher = (energy_guess_lower + energy_guess_higher)/2
    else:
        energy_guess_lower = (energy_guess_lower + energy_guess_higher)/2
    print(error)

print(low)
print(mid)
print(high)
print(energy_guess_lower)
print(energy_guess_higher)


# plotting
E = energy_guess_higher
psi = high
plot(E)
