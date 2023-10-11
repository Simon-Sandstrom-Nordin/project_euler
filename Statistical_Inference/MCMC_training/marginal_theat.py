import numpy as np
from scipy.special import gamma
from scipy import stats
from matplotlib import pyplot as plt

# prior_t = stats.beta(a=.5, b=.5)  # Jeffrey's prior for t
# prior_x = stats.beta(a=.5, b=.5)  # Jeffrey's prior for x


def likelihood(x, t):
    v = 0
    for x_el in x:
        if x_el == 0:
            v += 1
    return t[0] ** v * (1 - t[0]) ** (len(x) - v)


# def posterior(x, t):
#     return prior_t.pdf(t) * prior_x.pdf(x) * likelihood(t, x)


# Markov Chain Monte Carlo (MCMC)
t0 = stats.uniform.rvs(size=1)

plt.figure(1)

n = 10000
samples = [t0]
# Decenzo's my man
x = [.78, 0.0, 0.0, 0.0, .86, 0.0, .78, 0.0, .87, 0.0, .93, 0.0, 0.0, 0.0, 0.0, .86, .71, 0.0]
# plt.ion()
for i in range(n):
    # if i % 100 == 0:
    # plt.clf()
    t_guess = stats.norm.rvs(loc=samples[-1], scale=1, size=1)

    # Reject proposed samples if t is out of bounds
    if t_guess <= 0 or t_guess >= 1:
        samples.append(samples[-1])
        # print("t out of bounds")
    else:
        R = likelihood(x, t_guess) / likelihood(x, samples[-1])
        u = stats.uniform.rvs(size=1)
        if u < min(R, 1):
            samples.append(t_guess)
        else:
            samples.append(samples[-1])
    if i % 100 == 0:
        plt.clf()
        plt.title(f"Iteration: {i}")
        plt.hist(samples, stacked=True, density=True, alpha=0.5)
        plt.xlabel('t')
        plt.ylabel('Density')
        plt.pause(0.01)

plt.show()

#    plt.title("woa")
#    plt.pause(.001)
#    plt.hist(samples, stacked=True, density=True)

# plt.ioff()
# plt.show()
