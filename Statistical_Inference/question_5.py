import random
import statistics

from matplotlib import pyplot as plt

Bin_list = []
Hypergeom_list = []
NegBin_list = []
max_iter = 100000
negbin_r_list = []

for iteration in range(max_iter):

    # Bin(8, 2/3)
    n = 8
    p = 2/3
    successes = 0
    for k in range(n):
        uniform_number = random.random()
        if uniform_number <= p:
            successes += 1
    Bin_list.append(successes)

    # Hypergeom
    N = 10
    n = 8
    s = 4   # successes in population
    successes = 0
    for k in range(n):
        uniform_number = random.random()
        if uniform_number <= s/N:
            successes += 1
            s -= 1
        N -= 1
    Hypergeom_list.append(successes)

    # NegBin(5,1/3)
    n = 8
    p = 1/3
    failures = 0
    success_counter = 0
    while True:
        uniform_number = random.random()
        if uniform_number <= p:
            failures += 1
        else:
            success_counter += 1
        if success_counter >= n-failures:
            break
    NegBin_list.append(failures)
    negbin_r_list.append(success_counter)

#plt.plot(Bin_list, 'r-')
#plt.plot(Hypergeom_list, 'b-')
#plt.plot(NegBin_list, 'g-')
#plt.ylabel("No. of successful (failing in case of NegBin) draws")
#plt.xlabel("Iteration")
#plt.show()

## HIstograms
import numpy as np
from scipy import stats

fig, ax = plt.subplots(1, 1)
x = np.arange(0,10, step=1)

plt.hist(Bin_list, density=True)
ax.plot(x, stats.binom.pmf(x, n=8, p=2/3), 'ro', ms=5, label='binom pmf')
ax.vlines(x, 0, stats.binom.pmf(x, n=8, p=2/3), colors='b', lw=4, alpha=0.5)
# ax.hist(stats.norm.rvs(size=10000, loc=0, scale=1), density=True)
# plt.savefig("sim_ex.pdf", bbox_inches='tight')
plt.show()

fig, ax = plt.subplots(1, 1)
x = np.arange(0,10, step=1)

plt.hist(Hypergeom_list, density=True)
ax.plot(x, stats.hypergeom.pmf(x, M=10, n=4, N=8), 'ro', ms=5, label='binom pmf')
ax.vlines(x, 0, stats.hypergeom.pmf(x, M=10, n=4, N=8), colors='b', lw=4, alpha=0.5)
# ax.hist(stats.norm.rvs(size=10000, loc=0, scale=1), density=True)
# plt.savefig("sim_ex.pdf", bbox_inches='tight')
plt.show()

fig, ax = plt.subplots(1, 1)
x = np.arange(0,10, step=1)

plt.hist(NegBin_list, density=True)
ax.plot(x, stats.nbinom.pmf(x, n=8, p=2/3), 'ro', ms=5, label='binom pmf')
ax.vlines(x, 0, stats.nbinom.pmf(x, n=8, p=2/3), colors='b', lw=4, alpha=0.5)
# ax.hist(stats.norm.rvs(size=10000, loc=0, scale=1), density=True)
# plt.savefig("sim_ex.pdf", bbox_inches='tight')
plt.show()

# sample mean
# bin_mean = sum(bi/len(Bin_list) for bi in Bin_list)
bin_mean = statistics.mean(Bin_list)
hypergeom_mean = statistics.mean(Hypergeom_list)
NegBin_mean = statistics.mean(NegBin_list)

# bin_var = sum((bi - bin_mean)**2 / (len(bin_mean)-1) for bi in Bin_list)
bin_var = statistics.variance(Bin_list)
hypergeom_var = statistics.variance(Hypergeom_list)
NegBin_var = statistics.variance(NegBin_list)

# theoretical mean
bin_theo_mean = 8 * (2/3)
hyper_theo_mean = 8 * (4/10)
NegBin_theo_mean = 0
for k in range(len(negbin_r_list)):
    r = negbin_r_list[k]
    NegBin_theo_mean += r*(1/3)/(1-1/3)
NegBin_theo_mean = NegBin_theo_mean / len(negbin_r_list)
##
bin_theo_var = 8 * (2/3) * (1/3)
hyper_theo_var = 8 * (4/10) * ((10 - 4)/10) * (10 - 8)/(10-1)
NegBin_theo_var = 0
NegBin_theo_var = -1
#for k in range(len(negbin_r_list)):
#    r = negbin_r_list[k]
#    NegBin_theo_var += r*(1/3)/((1-1/3)**2)
#NegBin_theo_var = NegBin_theo_var / len(negbin_r_list)
# r= statistics.mean(negbin_r_list)
# NegBin_theo_var = r*(1/3)/((1-1/3)**2)

print("Number of iterations:", max_iter)
print("Bin sample mean:", bin_mean, "Theoretical mean:", bin_theo_mean)
print("Hypergeom sample mean:", hypergeom_mean, "Theoretical mean:", hyper_theo_mean)
print("NegBin sample mean:", NegBin_mean, "Theoretical mean:", NegBin_theo_mean)
##
print("Bin sample variance:", bin_var, "Theoretical variance:", bin_theo_var)
print("Hypergeom sample variance:", hypergeom_var, "Theoretical variance:", hyper_theo_var)
print("NegBin sample variance:", NegBin_var, "Theoretical variance:", NegBin_theo_var)

# sample variance

# sample histogram and pdf possibly
