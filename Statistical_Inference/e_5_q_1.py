import numpy as np
from scipy.special import comb
from matplotlib import pyplot as plt


p = .14
r = 1


def neg_bin_pmf(k):
    return comb(k + r - 1, k) * (1 - p)**k * p**r


k_list = [0]
p_list = []
for k in k_list:
    p_list.append(neg_bin_pmf(k))
    if sum(p_list) < .95:
        k_list.append(k+1)
    else:
        pass

plt.plot(k_list, p_list, 'ro')
plt.title("Negative binomial probability density function")
plt.xlabel("Sample size")
plt.ylabel("Isolated probability")
plt.show()

print(sum(p_list))
