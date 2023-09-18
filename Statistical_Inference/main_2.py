from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import scipy.special
import statistics


alpha = 2
m = 1
N = 100

list_of_N = []
mean_list = []


def Finv(y):
    return m * (1-y)**(-1/alpha)


#def pdf(x):
#    return (alpha * m**alpha) / (x**(alpha+1))


uni = stats.uniform.rvs(size = N)
stickprov_100 = [Finv(u) for u in uni]
stickprov_100.sort(reverse=True)

#fig, ax = plt.subplots(1, 1)
#x = np.linspace(0, 5, 10000)
#ax.plot(x, pdf(x), 'k-', lw=2, label='täthetfunktion för $X\sim{Exp}(2)$')

#ax.hist(stickprov_100, density=True, histtype='stepfilled', alpha=0.9)
#ax.legend(loc='best', frameon=False)
#print(stickprov_100)
#plt.xlim([0,5])
#plt.show()

print(statistics.mean(stickprov_100))
list_of_N.append(N)
mean_list.append(statistics.mean(stickprov_100))

for w in range(1, 15):
    N = N * 3

    def Finv(y):
        return m * (1-y)**(-1/alpha)


    uni = stats.uniform.rvs(size = N)
    stickprov_100 = [Finv(u) for u in uni]
    stickprov_100.sort(reverse=True)

    print(statistics.mean(stickprov_100))
    list_of_N.append(N)
    mean_list.append(statistics.mean(stickprov_100))

print(alpha*m/(alpha-1))
plt.plot(list_of_N, mean_list, 'o')
plt.xscale("log")
plt.ylabel("Sample mean")
plt.xlabel("N")
plt.title("Red line is theoretically expected value")
plt.axhline(y=alpha*m/(alpha-1), color='r', linestyle='-')
plt.show()
