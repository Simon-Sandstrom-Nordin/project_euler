from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import scipy.special

alpha = 1
m = 1
N = 1000000


def Finv(y):
    return m * (y)**(-1/alpha)


uni = stats.uniform.rvs(size = N)
stickprov_100 = [Finv(u) for u in uni]

plt.plot(stickprov_100, uni, 'go')


alpha = 2


def Finv(y):
    return m * (y)**(-1/alpha)


uni = stats.uniform.rvs(size = N)
stickprov_100 = [Finv(u) for u in uni]

plt.plot(stickprov_100, uni, 'bo')

alpha = 3


def Finv(y):
    return m * (y)**(-1/alpha)


uni = stats.uniform.rvs(size = N)
stickprov_100 = [Finv(u) for u in uni]

plt.plot(stickprov_100, uni, 'ro')

alpha = 3


def Finv(y):
    return m * (y)**(-1/alpha)


uni = stats.uniform.rvs(size = N)
stickprov_100 = [Finv(u) for u in uni]

plt.plot(stickprov_100, uni, 'ro')


alpha = 100


def Finv(y):
    return m * (y)**(-1/alpha)


uni = stats.uniform.rvs(size = N)
stickprov_100 = [Finv(u) for u in uni]

plt.plot(stickprov_100, uni, 'ko')
plt.title("alpha: " + "various" + ", m: " + str(m) + ", N = " + str(N))
plt.xlim([0,5])
plt.show()