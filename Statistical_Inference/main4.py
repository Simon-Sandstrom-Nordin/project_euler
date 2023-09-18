# qualitative stuff
from matplotlib import pyplot as plt
from scipy.stats import nbinom
import numpy as np
fig, ax = plt.subplots(1, 1)

# data
data = [2, 3, 7, 8, 2, 4, 7, 5, 5, 7]
data.sort()

# normalization
print(data)
lin = np.linspace(0, 8, 8+1).tolist()
lin = [round(x) for x in lin]
freq = np.zeros(9)
for x in lin:
    freq[x] = data.count(x)
freq_total = sum(freq)
freq = [fre / freq_total for fre in freq]
print(data)

# parameters
n = 2
p = .2
# p = 1/7


rv = nbinom(n, p)
x = np.arange(nbinom.ppf(0.01, n, p), nbinom.ppf(0.99, n, p))
ax.vlines(x, 0, rv.pmf(x), colors='k', linestyles='-', lw=1, label='NegBin, n=' + str(n) + ", p=" + str(p))
ax.legend(loc='best', frameon=False)
# plt.show()

plt.plot(lin, freq, 'o')
plt.show()
