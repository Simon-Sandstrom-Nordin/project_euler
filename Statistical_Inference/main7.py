import random
import statistics
from matplotlib import pyplot as plt

one_means = []
two_means = []
three_means = []
four_means = []
five_means = []
six_means = []

for counts in range(1000):

    results = []
    for k in range(4):
        r_num = random.random()
        if r_num <= 1/6:
            results.append(1)
        elif r_num <= 2/6:
            results.append(2)
        elif r_num <= 3/6:
            results.append(3)
        elif r_num <= 4/6:
            results.append(4)
        elif r_num <= 5/6:
            results.append(5)
        else:
            results.append(6)

    #plt.hist(results, bins=[1, 2, 3, 4, 5, 6])
    #plt.show()

    # count
    ones = results.count(1)
    twos = results.count(2)
    threes = results.count(3)
    fours = results.count(4)
    fives = results.count(5)
    sixes = results.count(6)
    # append
    one_means.append(ones)
    two_means.append(twos)
    three_means.append(threes)
    four_means.append(fours)
    five_means.append(fives)
    six_means.append(sixes)

print(statistics.mean(one_means))
print(statistics.mean(two_means))
print(statistics.mean(three_means))
print(statistics.mean(four_means))
print(statistics.mean(five_means))
print(statistics.mean(six_means))
