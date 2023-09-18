# -*- coding: utf-8 -*-
# Python simulation of a partiocle in a 1d infinite box potential
# Integrate time independent SE using the Verlet method
# Boundary conditions are found by shooting
# MW 220513

from pylab import *
import numpy as np
import matplotlib.pyplot as plt

# potential energy function
def V(x):
    y = 0.0
    #y = x**2/2 # harmonic oscillator
    return y


N_list = []
M_list = []

for k in range(1, 4+1):
    # trial energy
    E = .5 * np.pi ** 2 * 1 ** 2

    # parameters
    N = 10**k  # number of mesh points
    dx = 1 / N  # step length
    dx2 = dx ** 2  # step length squared

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
        d2psinew = 2*(V(x+dx)-E)*psi
        psi += dpsi*dx + 0.5*d2psi*dx2
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
    plt.title('Wave function plotted with grid points N = ' + str(N))
    plt.show()
    N_list.append(N)
    M_list.append(psi)

plt.close()

ln_N = []
for points in N_list:
    ln_N.append(np.log(points))
ln_M = []
for error in M_list:
    ln_M.append(np.log(error))

m, b = np.polyfit(ln_N, ln_M, 1)
print(m)
print(b)


def lin(x_lin):
    return m*x_lin + b


fig = plt.figure(num=None, figsize=(8,8), dpi=80, facecolor='w', edgecolor='k')
plt.plot(N_list, M_list, linewidth=1, color='red', linestyle="",marker="o")
plt.xscale('log')
plt.xlabel('Grid points N')
plt.yscale('log')
plt.ylabel('Error ∆')
plt.title('Error over number of grid points')
lin_N = []
for points in ln_N:
    lin_N.append(np.exp(lin(points)))
plt.plot(N_list, lin_N, linewidth=1, color='green', linestyle="-")
plt.show()
