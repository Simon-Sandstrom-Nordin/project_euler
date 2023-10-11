import numpy as np
from scipy import stats
from matplotlib import pyplot as plt


# acceptance-rejection method
# N(0,1) pdf
def s_n_pdf(x):
    return (1/np.sqrt(2*np.pi)) * np.exp(-(x**2)/2)


a = -3
b = 3
m = 1/np.sqrt(2*np.pi)  # max value of N(0,1)
accepted_samples = []
n = 10000
for k in range(n):
    u = stats.uniform.rvs(size=1)
    v = stats.uniform.rvs(loc=a, scale=abs(b-a), size=1)
    if u < s_n_pdf(v) / m:
        accepted_samples.append(v)
plt.hist(accepted_samples, stacked=True, density=True)
x_lin = np.linspace(a, b)
plt.figure(1)
plt.plot(x_lin, s_n_pdf(x_lin))
plt.title("Acceptance-rejection method for N(0,1) with n =" + str(n))
plt.show()

# Markov Chain Monte Carlo (MCMC)
initial_value = stats.uniform.rvs(size=1)
X0 = initial_value

plt.figure(2)

samples = [X0]
for i in range(n):
    plt.clf()
    y = stats.norm.rvs(loc=samples[-1], scale=1, size=1)
    R = s_n_pdf(y) / s_n_pdf(samples[-1])
    u = stats.uniform.rvs(size=1)
    if u < min(R, 1):
        samples.append(y)
    else:
        samples.append(samples[-1])
    plt.plot(x_lin, s_n_pdf(x_lin))
    plt.title("MCMC method for N(0,1) with X0 =" + str(X0) + ", n = " + str(n))
    plt.hist(samples, stacked=True, density=True)
    plt.pause(.001)
plt.show()
