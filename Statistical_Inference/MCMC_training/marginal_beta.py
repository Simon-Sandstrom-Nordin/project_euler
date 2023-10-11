import numpy as np
from scipy.special import gamma
from scipy.special import beta
from scipy import stats
from matplotlib import pyplot as plt


def likelihood(y, a, b):
    terms = 1
    for y_el in y:
        terms = terms * y_el**(a-1) * (1-y_el)**(b-1) / beta(a,b)
    return terms


# Markov Chain Monte Carlo (MCMC)
a0 = stats.uniform.rvs(size=1)
b0 = stats.uniform.rvs(size=1)

plt.figure(1)

n = 1000
samples = [[a0[0], b0[0]]]
y = [4.6,5.0,8.3,5.8,6.9,8.5,3.1,5.4]
# plt.ion()
for i in range(n):
    a_guess = stats.norm.rvs(loc=samples[-1][0], scale=1, size=1)
    b_guess = stats.norm.rvs(loc=samples[-1][1], scale=1, size=1)

    # Reject proposed samples if t is out of bounds
    if a_guess <= 0 or b_guess <= 0:
        samples.append(samples[-1])
        # print("t out of bounds")
    else:
        print(samples[-1][0])
        print(samples[-1][1])
        R = likelihood(y, a_guess[0], b_guess[0]) / likelihood(y, samples[-1][0], samples[-1][1])
        u = stats.uniform.rvs(size=1)
        if u < min(R, 1):
            samples.append([a_guess[0], b_guess[0]])
        else:
            samples.append([samples[-1][0], samples[-1][1]])
    if i % 100 == 0:
        plt.clf()
        plt.title(f"Iteration: {i}")
        a_vals = [sample[0] for sample in samples]
        b_vals = [sample[1] for sample in samples]
        print(a_vals)
        print(b_vals)
        plt.hist2d(a_vals, b_vals, density=True, alpha=0.5)
        plt.xlabel('t')
        plt.ylabel('Density')
        plt.pause(0.01)

plt.show()

#    plt.title("woa")
#    plt.pause(.001)
#    plt.hist(samples, stacked=True, density=True)

# plt.ioff()
# plt.show()
