import numpy as np
import time
from scipy.special import beta
from scipy import stats
from scipy.stats import beta as beta_dist
import matplotlib.pyplot as plt

for skater in skaters:
    X_outcomes = []
    for row in range(0, len(df)):
        try:
            if df_alt["id"][row] == skater:
                for trick_no in range(1, 6 + 1):
                    # if pd.notna(df_alt["trick " + str(trick_no)][row]):  # Check if 'id' is not NaN
                    if df_alt["trick " + str(trick_no)][row] > 0:
                        X_outcomes.append(df_alt["trick " + str(trick_no)][row])
        except KeyError:
            # print("hi")
            pass
    X_outcomes = np.array(X_outcomes)


    def likelihood(y, a, b):
        return np.prod(y ** (a - 1) * (1 - y) ** (b - 1) / beta(a, b))


    # Sample values by MCMC
    a0 = stats.uniform.rvs(loc=1, size=1)
    b0 = stats.uniform.rvs(loc=1, size=1)
    n = 5000
    samples = [[a0, b0]]
    plt.figure(1)
    plt.ion()
    for iteration in range(n - 1):
        a_guess = stats.norm.rvs(loc=samples[-1][0], scale=1, size=1)
        b_guess = stats.norm.rvs(loc=samples[-1][1], scale=1, size=1)
        # Reject proposed samples if t is out of bounds
        while a_guess < 0 or b_guess < 0:
            a_guess = stats.norm.rvs(loc=samples[-1][0], scale=1, size=1)
            b_guess = stats.norm.rvs(loc=samples[-1][1], scale=1, size=1)
        R = likelihood(X_outcomes, a_guess, b_guess) / likelihood(X_outcomes, samples[-1][0], samples[-1][1])
        u = stats.uniform.rvs(size=1)
        if u < min(R, 1):
            samples.append([a_guess, b_guess])
        else:
            samples.append([samples[-1][0], samples[-1][1]])

    alpha_list = []
    beta_list = []
    for sample in samples:
        alpha_list.append(sample[0])
        beta_list.append(sample[1])

    print(skater)
    print("Samples:", len(samples))

    print("mean alpha:", np.mean(alpha_list), "mean beta:", np.mean(beta_list))
    print("var alpha:", np.var(alpha_list, ddof=1), "var beta:", np.var(beta_list, ddof=1))


    def likelihood(x, t):
        v = 0
        for x_el in x:
            if x_el != 0:
                v += 1
        if v == 0:
            print("LOSER")
        return t ** v * (1 - t) ** (len(x) - v)


    # Markov Chain Monte Carlo (MCMC)
    t0 = stats.uniform.rvs(size=1)
    n = 5000
    samples = [t0]
    # Decenzo's my man
    for i in range(n - 1):
        t_guess = stats.norm.rvs(loc=samples[-1], scale=1, size=1)

        # Reject proposed samples if t is out of bounds
        while t_guess <= 0 or t_guess >= 1:
            t_guess = stats.norm.rvs(loc=samples[-1], scale=1, size=1)

        R = likelihood(X_outcomes, t_guess) / likelihood(X_outcomes, samples[-1])
        u = stats.uniform.rvs(size=1)
        if u < min(R, 1):
            samples.append(t_guess)
        else:
            samples.append(samples[-1])

    print("mean theta:", np.mean(samples))
    print("var theta:", np.var(samples, ddof=1))