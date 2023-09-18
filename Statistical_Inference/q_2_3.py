from scipy.stats import uniform as uni
from scipy.special import gamma
import matplotlib.pyplot as plt
import numpy as np
import statistics as stats

size = 10000000
uni_list = uni.rvs(size=size)
# print(uni_list)
# uni_list.sort()
# plt.plot(uni_list, 'ro')
# plt.show()


# Exponential dist.
def inv_exp_cdf(y, la):
    return (1/la)*np.log(1/(1-y))


def exp_pdf(x, la):
    return la * np.exp(-la*x)


la = 3
exp_list = [inv_exp_cdf(u, la) for u in uni_list]
plt.hist(exp_list, density=True, color='red', alpha=.6)
x_list = np.linspace(0, 3)
exp_x = [exp_pdf(x, la) for x in x_list]
plt.xlim([0, 3])
plt.plot(x_list, exp_x, 'b-')
plt.title('Exponential distribution')
plt.show()

print("Exp. dist.")
print("Experimental mean: ", stats.mean(exp_list))
print("Theoretical mean: ", 1/la)
print("Experimental var: ", stats.variance(exp_list))
print("Theoretical var: ", 1/(la**2))


# Gamma dist.
def gamma_pdf(x, alpha, la):
    return la**alpha/gamma(alpha) * x**(alpha-1) * np.exp(-la*x)


gamma_list = np.zeros(size)
alpha = 10
for t in range(alpha):
    uni_list = uni.rvs(size=size)
    exp_list = [inv_exp_cdf(u, la) for u in uni_list]
    for k in range(len(gamma_list)):
        gamma_list[k] += exp_list[k]
plt.hist(gamma_list, density=True, color='red', alpha=.6)
x_list = np.linspace(0, 7)
gamma_x = [gamma_pdf(x, alpha, la) for x in x_list]
plt.xlim([0, 7])
plt.plot(x_list, gamma_x, 'b-')
plt.title('Gamma distribution')
plt.show()

print("Gam. dist.")
print("Experimental mean: ", stats.mean(gamma_list))
print("Theoretical mean: ", alpha/la)
print("Experimental var: ", stats.variance(gamma_list))
print("Theoretical var: ", alpha/(la**2))

# InvGamma dist.


# Inv-χ^2 dist.

