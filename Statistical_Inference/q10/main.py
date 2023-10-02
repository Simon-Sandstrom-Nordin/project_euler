import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

# q1, indirect sampling from N(0,1) via Exp(L)
# https://news.ycombinator.com/item?id=37701476 discord being down
L = 1


def f(Y):
    return (1/np.sqrt(2*np.pi)) * np.exp(-(Y**2) / 2)


def g(Y):
    return L * np.exp(-L*Y)

m = 0
x_lin = np.linspace(0, 100, 1000)
for x in x_lin:
    if m < f(x) / g(x):
        m = f(x) / g(x)
print(m)

accepted_samples = []
for trial in range(1000):
    Y = stats.expon.rvs(scale=1/L, size=1)
    U = stats.uniform.rvs(size=1)
    if U <= f(Y) / (m*g(Y)):
        accepted_samples.append(g(Y))

accepted_samples = accepted_samples + [-a for a in accepted_samples]

print(len(accepted_samples))
accepted_samples.sort()
print(accepted_samples)
# plt.hist(accepted_samples, bins=30, density=True)  # Use density=True for proper probability density estimation
# x = np.linspace(-max(accepted_samples), max(accepted_samples), 1000)
# plt.plot(x, f(x), 'r-', lw=2)  # Plot the standard normal density function for comparison
# plt.show()

# Manually specify the bin edges
# bin_edges = np.linspace(0, max(accepted_samples), 30)

# Plot the histogram with specified bin edges
# plt.hist(accepted_samples, bins=bin_edges, density=True)
plt.hist(accepted_samples, bins=10, stacked=True, density=True)
x = np.linspace(-max(accepted_samples), max(accepted_samples), 1000)
plt.plot(x, f(x), 'r-', lw=2)
plt.show()
