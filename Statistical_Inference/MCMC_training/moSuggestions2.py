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
n = 10000
samples = [[a0, b0]]
plt.figure(1)
plt.ion()
for iteration in range(n):
    plt.clf()
    # print(iteration)
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
    print(samples[-1])

    # Histogram part(y)
    a_vals = np.linspace(0, 14, 50)
    b_vals = np.linspace(0, 14, 50)

    A, B = np.meshgrid(a_vals, b_vals)

    b_vals = b_vals[::-1]

    Z = np.zeros_like(A)
    for sample in samples:
        for i in range(A.shape[0]-1):
            for j in range(A.shape[1]-1):
                if a_vals[i] < sample[0] <= a_vals[i+1] and b_vals[j] > sample[1] >= b_vals[j + 1]:
                        Z[i, j] += 1

    # Create a 2D histogram with weights from Z
    hist, xedges, yedges = np.histogram2d(A.flatten(), B.flatten(), bins=(14, 14), weights=Z.flatten(), density=True)

    # Plot the histogram
    plt.imshow(hist, cmap='viridis', extent=[xedges.min(), xedges.max(), yedges.min(), yedges.max()])
    plt.colorbar(label='Weighted Frequency')
    plt.xlabel('a')
    plt.ylabel('b')
    plt.title('2D Histogram of accepted MCMC samples. Accepted samples = ' + str(iteration))
    plt.pause(0.0001)
    #time.sleep(10)
