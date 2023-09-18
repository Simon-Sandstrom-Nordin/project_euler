import random
import statistics

import numpy as np
from matplotlib import pyplot as plt
from scipy import stats

# 1. Generate two uniformly distributed samples
uni_samples_1 = []
uni_samples_2 = []
N = 10000

for k in range(N):
    uniform_number_1 = random.random()
    uni_samples_1.append(uniform_number_1)
    uniform_number_2 = random.random()
    uni_samples_2.append(uniform_number_2)

# print(uni_samples_1)
# plt.hist(uni_samples_1)
# plt.show()

# 2. Transform these (Box-Muller method) to a ~N(0,1)
Z0_samples = []
Z1_samples = []

for k in range(N):
    U1 = uni_samples_1[k]
    U2 = uni_samples_2[k]

    Z0 = np.sqrt(-2*np.log(U1)) * np.cos(2*np.pi*U2)
    Z1 = np.sqrt(-2*np.log(U1)) * np.sin(2*np.pi*U2)

    Z0_samples.append(Z0)
    Z1_samples.append(Z1)

fig, ax = plt.subplots(1, 1)
x = np.linspace(-20, 20, 100)

plt.hist(Z0_samples, density=True)
ax.plot(x, stats.norm.pdf(x, loc=0, scale=1))
# ax.hist(stats.norm.rvs(size=10000, loc=0, scale=1), density=True)
# plt.savefig("sim_ex.pdf", bbox_inches='tight')
plt.show()

# plt.hist(Z1_samples)
# plt.show()

# 3. Transform these to a ~N(my, sigma^2) by Y = x*my + sigma
theta = 3
var = 25

for k in range(N):
    Z0_samples[k] = Z0_samples[k] * np.sqrt(var) + theta

fig, ax = plt.subplots(1, 1)
x = np.linspace(-100, 100, 10000)

plt.hist(Z0_samples, density=True)
ax.plot(x, stats.norm.pdf(x, loc=theta, scale=np.sqrt(var)))
# ax.hist(stats.norm.rvs(size=10000, loc=0, scale=1), density=True)
# plt.savefig("sim_ex.pdf", bbox_inches='tight')
plt.show()

# plt.hist(Z1_samples)
# plt.show()

# print point estimators
print("Mean:", statistics.mean(Z0_samples))
print("Var:", statistics.variance(Z0_samples))
