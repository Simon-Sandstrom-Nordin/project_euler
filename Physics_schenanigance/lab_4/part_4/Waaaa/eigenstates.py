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
    N=10**5               # number of mesh points
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


energy_guess_lower =  12
energy_guess_higher = 30

#energy_guess_lower =  0.6961758207571827
#energy_guess_higher = 0.696175820757183
# energy_guess_lower = 0.4*np.pi**2
# energy_guess_higher = 0.6*np.pi**2
# energy_guess_lower = 0.4*np.pi**2*3.9**2
# energy_guess_higher = 0.7*np.pi**2*4.1**2

# states
# 4.934802312473049
# 19.739210588790634
# 44.41322884867447
# 78.95686378434979

# with N = 10**7
# low: 0.6961758207571827
# high:0.696175820757183

tol = 10**(-15)
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

# WIth N = 10^(8)
# E= 0.6961758207571827  psi(xmax)= -72229361.03588428
# E= 0.696175820757183  psi(xmax)= -72229527.20962073