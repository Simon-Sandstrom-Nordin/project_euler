import statistics
from scipy import stats
from matplotlib import pyplot as plt

data = [2, 3, 7, 8, 2, 4, 7, 5, 5, 7]
t_bar = statistics.mean(data)
N0 = 100
p_list = []
N_list = []

for iteration in range(1, 13):
    N = N0 * 2**iteration
    counter = 0
    for k in range(0, N):
        generated_sample = stats.nbinom.rvs(n=2, p=1/7, size=10)
        T_bar = generated_sample.mean()
        if T_bar <= t_bar:
            counter += 1
    p = counter / N
    print('Out of', N, "random sets of samples,", counter, "had a mean lower than or equal to question's sample's mean"
                                                           " making p = ", p)
    p_list.append(p)
    N_list.append(N)

plt.plot(N_list, p_list, 'b-o')
plt.ylabel("P(T_bar <= t_bar), T_bar = NegBin(2,1/7) sample mean, t_bar = question's sample mean")
plt.xlabel('Sample size from NegBin(2,1/7)')
plt.title("P(T_bar <= t_bar) over Sample size of NegBin distribution")
plt.show()

for probability_index in range(len(p_list)):
    print("Probability at N =", N_list[probability_index], "is p =", p_list[probability_index])

