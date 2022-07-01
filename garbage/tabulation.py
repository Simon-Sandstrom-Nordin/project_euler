import math

from matplotlib import pyplot as plt

x = []
for k in range(48, 55 + 1):
    x.append(k)

y = [2, 4, 6, 9, 6, 7, 0, 1]

average = 0
for k in range(0, len(y)):
    average += x[k] * y[k]
average = average / sum(y)
print("Average value is", average)
deviation = 0
for k in x:
    deviation += (k - average)**2
deviation = deviation / (sum(y) - 1)
deviation = math.sqrt(deviation)
print("Standard deviation is", deviation)
print("This means that 34.1 % * 2 = 68.2 % of observations "
      "fall within the interval", average, "±", deviation,
      "= [", average - deviation, ",", average + deviation, "]")

plt.title("dot plot")
plt.plot(x, y, 'o')
plt.show()

plt.title("tab drab")
plt.bar(x, y)
plt.show()
