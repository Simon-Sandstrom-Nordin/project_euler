import math as m
from scipy import stats
from matplotlib import pyplot as plt
import numpy as np

rv = stats.gamma.rvs(a=4, scale=1/(2 + 2*2.01 + 3*3.82), size=10000)
print(rv)
plt.hist(rv, density=True)
plt.show()


#def xp(x, theta):
#    return theta*m.exp(-theta*x)
counter = 0
for r in rv:
    if r > .3:
        counter += 1
print(counter/len(rv))


#x_means = []
#for r in rv:
#    x_outcomes = stats.expon.rvs(scale=r, size=10000)
#    x_means.append(np.mean(x_outcomes))


#plt.hist(x_means)
#plt.show()
#print(x_means)
#print(np.mean(x_means))
# print("mwah")
