import math as m
from matplotlib import pyplot as plt
import numpy as np
from scipy import stats
from scipy.special import comb

def likelihood(y_vec, prob):
    log_like = 0
    for index in range(len(y_vec)):
        total = y_vec[index][0]
        y = y_vec[index][1]
        log_like += np.log(comb(total, y) * prob**y * (1-prob)**(total-y))
    return m.exp(log_like)


def normalize_data(data):
    total = sum(data)
    return [x / total for x in data]


def trapezoidal_rule_discrete(x_values, y_values):
    """
    Approximates the definite integral of a set of discrete data points using the trapezoidal rule.

    :param x_values: List of x values.
    :param y_values: List of corresponding y values.
    :return: Approximation of the definite integral.
    """
    n = len(x_values)
    h = x_values[1] - x_values[0]

    integral = 0.5 * (y_values[0] + y_values[-1])
    integral += sum(y_values[1:-1])

    return h * integral

plt.figure(1)
y_data = [[12, 8], [21, 4], [26, 13], [13, 5], [13, 5], [14, 7], [20, 12]]
p_lin = np.linspace(0, 1, 101)
p_lin = p_lin[1:]
p_lin = p_lin[:len(p_lin)-1]
l_data = []
for p in p_lin:
    l_data.append(likelihood(y_data, p))
plt.plot(p_lin, l_data, 'r-o')
plt.show()
for j in range(len(y_data)):
    plt.clf()
    y_data_sliced = y_data[:j]
    p_lin = np.linspace(0, 1, 101)
    p_lin = p_lin[1:]
    p_lin = p_lin[:len(p_lin) - 1]
    l_data = []
    for p in p_lin:
        l_data.append(likelihood(y_data_sliced, p))

    plt.title(f"Iteration: {j}")
    plt.xlabel('t')
    plt.ylabel('Density')

    # Normalize the likelihood data
    l_data_normalized = normalize_data(l_data)

    # Calculate the step size
    step_size = p_lin[1] - p_lin[0]

    # Sum of normalized probabilities
    total_prob = sum(l_data_normalized) * step_size

    # Normalize again to ensure the total probability is 1
    l_data_normalized = [x / total_prob for x in l_data_normalized]

    plt.plot(p_lin, l_data_normalized, 'r-o')
    plt.pause(1)

    # Use trapezoidal rule to approximate the integral
    result = trapezoidal_rule_discrete(p_lin, l_data_normalized)
    print(f"Approximated integral: {result}")

plt.show()

#plt.figure(2)
p0 = stats.uniform.rvs(size=1)
samples = [p0]
n = 1000
for i in range(n):
    t_guess = stats.norm.rvs(loc=samples[-1], scale=.5, size=1)

    # Reject proposed samples if t is out of bounds
    while t_guess <= 0 or t_guess >= 1:
        t_guess = stats.norm.rvs(loc=samples[-1], scale=.5, size=1)

    R = likelihood(y_data, t_guess) / likelihood(y_data, samples[-1])
    u = stats.uniform.rvs(size=1)
    if u < min(R, 1):
       samples.append(t_guess)
    else:
       samples.append(samples[-1])

plt.title(f"Iteration: {n}")
plt.hist(samples, stacked=True, density=True, alpha=0.5)
plt.xlabel('t')
plt.ylabel('Density')
plt.show()
print(np.mean(samples))
print(np.var(samples))
