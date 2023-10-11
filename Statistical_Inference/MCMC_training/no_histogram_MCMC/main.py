import numpy as np
import time
from scipy.special import beta
from scipy import stats
from scipy.stats import beta as beta_dist
import matplotlib.pyplot as plt


def likelihood(y, a, b):
    return np.prod(y**(a-1) * (1-y)**(b-1) / beta(a, b))


# Find values for Z by MCMC
a0 = stats.uniform.rvs(loc=1, size=1)
b0 = stats.uniform.rvs(loc=1, size=1)
y = np.array([.46, .50, .83, .58, .69, .85, .31, .54])
n = 5000
samples = [[a0, b0]]
plt.figure(1)
plt.ion()
for iteration in range(n):
    a_guess = stats.norm.rvs(loc=samples[-1][0], scale=1, size=1)
    b_guess = stats.norm.rvs(loc=samples[-1][1], scale=1, size=1)
    # Reject proposed samples if t is out of bounds
    while a_guess <= 0 or b_guess <= 0:
        a_guess = stats.norm.rvs(loc=samples[-1][0], scale=1, size=1)
        b_guess = stats.norm.rvs(loc=samples[-1][1], scale=1, size=1)
    R = likelihood(y, a_guess, b_guess) / likelihood(y, samples[-1][0], samples[-1][1])
    u = stats.uniform.rvs(size=1)
    if u < min(R, 1):
        samples.append([a_guess, b_guess])
    else:
        samples.append([samples[-1][0], samples[-1][1]])
print(len(samples))
alpha_list = []
beta_list = []
for sample in samples:
    alpha_list.append(sample[0])
    beta_list.append(sample[1])

print("mean alpha:", np.mean(alpha_list), "mean beta:", np.mean(beta_list))
print("var alpha:", np.var(alpha_list, ddof=1), "var beta:", np.var(beta_list, ddof=1))


def likelihood(x, t):
    v = 0
    for x_el in x:
        if x_el == 0:
            v += 1
    return t[0] ** v * (1 - t[0]) ** (len(x) - v)


# Markov Chain Monte Carlo (MCMC)
t0 = stats.uniform.rvs(size=1)
n = 5000
samples = [t0]
# Decenzo's my man
x = [7.8, 0.0, 0.0, 0.0, 8.6, 0.0, 7.8, 0.0, 8.7, 0.0, 9.3, 0.0, 0.0, 0.0, 0.0, 8.6, 7.1, 0.0]
for i in range(n):
    t_guess = stats.norm.rvs(loc=samples[-1], scale=1, size=1)

    # Reject proposed samples if t is out of bounds
    while t_guess <= 0 or t_guess >= 1:
        t_guess = stats.norm.rvs(loc=samples[-1], scale=1, size=1)

    R = likelihood(x, t_guess) / likelihood(x, samples[-1])
    u = stats.uniform.rvs(size=1)
    if u < min(R, 1):
        samples.append(t_guess)
    else:
        samples.append(samples[-1])
print(len(samples))

print("mean theta:", np.mean(samples))
print("var theta:", np.var(samples, ddof=1))
