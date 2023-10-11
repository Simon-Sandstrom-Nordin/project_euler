import numpy as np
from scipy.special import beta
from scipy import stats
from scipy.stats import beta as beta_dist
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


def likelihood(y, a, b):
    result = 1
    for y_el in y:
        result = result * y_el**(a-1) * (1-y_el)**(b-1) / beta(a, b)
    return result


a_vals = np.linspace(0.1, 30, 100)
b_vals = np.linspace(0.1, 30, 100)

A, B = np.meshgrid(a_vals, b_vals)

y = np.array([.46, .50, .83, .58, .69, .85, .31, .54])

Z = np.zeros_like(A)

# Markov Chain Monte Carlo (MCMC)
a0 = stats.uniform.rvs(size=1)
b0 = stats.uniform.rvs(size=1)

plt.figure(1)

n = 1000
samples = [[a0, b0]]
# y = [4.6,5.0,8.3,5.8,6.9,8.5,3.1,5.4]
# plt.ion()
for iteration in range(n):
    a_guess = stats.norm.rvs(loc=samples[-1][0], scale=1, size=1)[0]
    b_guess = stats.norm.rvs(loc=samples[-1][1], scale=1, size=1)[0]

    # Reject proposed samples if t is out of bounds
    if a_guess <= 0 or b_guess <= 0:
        samples.append(samples[-1])
        print("out of bounds")
    else:
        R = likelihood(y, a_guess, b_guess) / likelihood(y, samples[-1][0], samples[-1][1])
        u = stats.uniform.rvs(size=1)
        if u < min(R, 1):
            samples.append([a_guess, b_guess])
        else:
            samples.append([samples[-1][0], samples[-1][1]])
    if iteration % 100 == 0:
        plt.clf()
        # fill in values for Z
        for i in range(A.shape[0]):
            for j in range(A.shape[1]):
                Z[i, j] = likelihood(y, A[i, j], B[i, j])

        # Create a 2D histogram
        hist, xedges, yedges = np.histogram2d(A.flatten(), B.flatten(), bins=(50, 50), weights=Z.flatten())
        a_vals = [sample[0] for sample in samples]
        b_vals = [sample[1] for sample in samples]
        plt.imshow(hist, cmap='viridis', extent=[xedges.min(), xedges.max(), yedges.min(), yedges.max()])
        plt.colorbar(label='Frequency')
        plt.xlabel('a')
        plt.ylabel('b')
        plt.title('2D Histogram of Likelihood ' + f"Iteration: {i}")
        # plt.show()
        plt.pause(0.01)

plt.show()
# for i in range(A.shape[0]):
#    for j in range(A.shape[1]):
#        Z[i, j] = likelihood(y, A[i, j], B[i, j])
