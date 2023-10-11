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

y_data = np.array([.46, .50, .83, .58, .69, .85, .31, .54])

# Markov Chain Monte Carlo (MCMC)
a0 = stats.uniform.rvs(size=1)
b0 = stats.uniform.rvs(size=1)


n = 1000
samples = [[a0, b0]]

for i in range(n):
    a_guess = stats.norm.rvs(loc=samples[-1][0], scale=1, size=1)[0]
    b_guess = stats.norm.rvs(loc=samples[-1][1], scale=1, size=1)[0]

    # Reject proposed samples if t is out of bounds
    if a_guess <= 0 or b_guess <= 0:
        samples.append(samples[-1])
        print("out of bounds")
    else:
        R = likelihood(y_data, a_guess, b_guess) / likelihood(y_data, samples[-1][0], samples[-1][1])
        u = stats.uniform.rvs(size=1)
        if u < min(R, 1):
            samples.append([a_guess, b_guess])
        else:
            samples.append([samples[-1][0], samples[-1][1]])

# Filter out invalid samples
a_vals = [sample[0] for sample in samples if sample[0] > 0 and sample[1] > 0]
b_vals = [sample[1] for sample in samples if sample[0] > 0 and sample[1] > 0]

# Create a 2D histogram of the sampled data
hist, xedges, yedges = np.histogram2d(a_vals, b_vals, bins=(50, 50))

# (Previous code remains the same)

# Filter out invalid samples
a_vals = np.array([sample[0] for sample in samples if sample[0] > 0 and sample[1] > 0])
b_vals = np.array([sample[1] for sample in samples if sample[0] > 0 and sample[1] > 0])

# Create a 2D histogram of the sampled data
hist, xedges, yedges = np.histogram2d(a_vals, b_vals, bins=(50, 50))

plt.imshow(hist, cmap='viridis', extent=[xedges.min(), xedges.max(), yedges.min(), yedges.max()])
plt.colorbar(label='Frequency')
plt.xlabel('a')
plt.ylabel('b')
plt.title('2D Histogram of Sampled Data')

plt.show()
