import numpy as np
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
n = 1000
samples = [[a0, b0]]
for iteration in range(n):
    print(iteration)
    a_guess = stats.norm.rvs(loc=samples[-1][0], scale=1, size=1)
    b_guess = stats.norm.rvs(loc=samples[-1][1], scale=1, size=1)
    # print(a_guess)
    # print(b_guess)
    # print(a_guess <= 0)
    # print(b_guess <= 0)
    # Reject proposed samples if t is out of bounds
    while a_guess <= 0 or b_guess <= 0:
        # print(a_guess)
        # print(b_guess)
        # samples.append(samples[-1])
        print("out of bounds")
        a_guess = stats.norm.rvs(loc=samples[-1][0], scale=1, size=1)
        b_guess = stats.norm.rvs(loc=samples[-1][1], scale=1, size=1)

    R = likelihood(y, a_guess, b_guess) / likelihood(y, samples[-1][0], samples[-1][1])
    u = stats.uniform.rvs(size=1)
    if u < min(R, 1):
        samples.append([a_guess, b_guess])
    else:
        samples.append([samples[-1][0], samples[-1][1]])

# Histogram part(y)

a_vals = np.linspace(0.1, 50, 50)
b_vals = np.linspace(0.1, 50, 50)

print(len(a_vals))

A, B = np.meshgrid(a_vals, b_vals)
# print(A.shape[0])
# print(A.shape[1])
b_vals = b_vals[::-1]
# print(b_vals)
print(samples)
Z = np.zeros_like(A)
for sample in samples:
    for i in range(A.shape[0]-1):
        for j in range(A.shape[1]-1):
            if a_vals[i] < sample[0] <= a_vals[i+1] and b_vals[j] > sample[1] >= b_vals[j + 1]:
                    # print(a_vals[i], sample[0], a_vals[i+1])
                    # print(b_vals[i], sample[1], b_vals[i + 1])
                    # print(sample[1])
                    # print("hi")
                    Z[i, j] += 1

            # if sample[0] sample[1]:  # remember, [0] is alpha, [1] is beta
            # Z[i, j] = likelihood(y, A[i, j], B[i, j])

# Create a 2D histogram with weights from Z
hist, xedges, yedges = np.histogram2d(A.flatten(), B.flatten(), bins=(50, 50), weights=Z.flatten(), density=True)

# Plot the histogram
plt.imshow(hist, cmap='viridis', extent=[xedges.min(), xedges.max(), yedges.min(), yedges.max()])
plt.colorbar(label='Weighted Frequency')
plt.xlabel('a')
plt.ylabel('b')
plt.title('2D Histogram of Likelihood')
plt.show()
