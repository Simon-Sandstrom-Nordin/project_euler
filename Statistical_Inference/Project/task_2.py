import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("SLS22.csv")

# Normalize data
# run 1,2
for r in range(1, 2+1):
    run = "run " + str(r)
    df[run] = df[run]/np.max(df[run])
    plt.title("Run " + str(r))
    plt.hist(df[run], density=True)
    plt.show()

# trick 1-7
for t in range(1, 6+1):
    trick = "trick " + str(t)
    df[trick] = df[trick]/np.max(df[trick])

# for t in range(1, 4+1):
#    plt.title("Trick " + str(t))
#    plt.hist(df["trick " + str(t)], density=True)
#    plt.show()


# make i
def f(x):
    if x == 0:
        return 0
    else:
        return 1


for k in range(1, 4+1):
    make = df["trick " + str(k)].apply(f)
    make.name = "make " + str(k)  # Assign the name directly here
    df = pd.concat([df, make], axis=1)  # Use df[cols] to include all columns

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

print(df)
for skater in range(0, len(df)):
    print(df["run 1"][skater], df["run 2"][skater])

plt.title("Run 1 vs run 2 for each skater")
plt.plot(df["run 1"], df["run 2"], 'ro')
plt.show()

# (a)
theta_parameters = []
for skater in range(0, len(df)):
    print(df["id"][skater])         # good, we can index like this
    score = 0
    make_counter = 0
    for trick_no in range(1, 4+1):
        if df["make " + str(trick_no)][skater] == 1:
            make_counter += 1
    theta_parameters.append(make_counter/4)     # out of a total of four makes
plt.hist(theta_parameters)
plt.show()

# (b) gamma parameters
alpha_parameters = []
beta_parameters = []
for skater in range(0, len(df)):
    # print(df["id"][skater])         # good, we can index like this
    Z_outcomes = []
    for trick_no in range(1, 4+1):
        if df["make " + str(trick_no)][skater] == 1:
            Z_outcomes.append(df["trick " + str(trick_no)][skater])
    Z_mean = np.mean(Z_outcomes)
    Z_usv = np.var(Z_outcomes, ddof=True)   # unbiased sample variance
    # https://statproofbook.github.io/P/beta-mome.html
    alpha_parameters.append(Z_mean * (Z_mean * (1 - Z_mean) / Z_usv - 1))
    beta_parameters.append((1 - Z_mean) * (Z_mean * (1 - Z_mean) / Z_usv - 1))

# print(alpha_parameters)
# print(beta_parameters)
# alpha_parameters = np.nan_to_num(alpha_parameters, nan=np.mean(alpha_parameters), posinf=np.mean(alpha_parameters), neginf=np.mean(alpha_parameters))
# beta_parameters = np.nan_to_num(beta_parameters, nan=np.mean(beta_parameters), posinf=np.mean(alpha_parameters), neginf=np.mean(alpha_parameters))
# print(alpha_parameters)
# print(beta_parameters)

# same fix... it didn't work last time tho
alpha_adjusted = []
for a in range(len(alpha_parameters)-1, 0-1, -1):
    if ~np.isinf(alpha_parameters[a]) and ~np.isnan(alpha_parameters[a]):
        alpha_adjusted.append(alpha_parameters[a])
adjusted_mean_a = np.mean(alpha_adjusted)
alpha_adjusted.reverse()
print(alpha_adjusted)
beta_adjusted = []
for b in range(len(beta_parameters)-1, 0-1, -1):
    if ~np.isinf(beta_parameters[b]) and ~np.isnan(beta_parameters[b]):
        beta_adjusted.append(beta_parameters[b])
adjusted_mean_b = np.mean(beta_adjusted)
beta_adjusted.reverse()
print(beta_adjusted)

alpha_parameters_X = np.nan_to_num(alpha_parameters, nan=adjusted_mean_a, posinf=adjusted_mean_a, neginf=adjusted_mean_a)
beta_parameters_X = np.nan_to_num(beta_parameters, nan=adjusted_mean_b, posinf=adjusted_mean_b, neginf=adjusted_mean_b)

plt.hist(alpha_parameters_X, color='r', density=True)
plt.hist(beta_parameters_X, color='b', density=True)
plt.show()

# (c)
alpha_parameters = []
beta_parameters = []
for skater in range(0, len(df)):
    Y_outcomes = []
    for run_no in range(1, 2+1):
        Y_outcomes.append(df["run " + str(run_no)][skater])
    Y_mean = np.mean(Y_outcomes)
    Y_usv = np.var(Y_outcomes, ddof=True)   # unbiased sample variance
    if Y_usv == 0:
        print("Warning!")
        print(Y_mean * (Y_mean * (1 - Y_mean) / Y_usv - 1))
        print((1 - Y_mean) * (Y_mean * (1 - Y_mean) / Y_usv - 1))

    # https://statproofbook.github.io/P/beta-mome.html
    alpha_parameters.append(Y_mean * (Y_mean * (1 - Y_mean) / Y_usv - 1))
    beta_parameters.append((1 - Y_mean) * (Y_mean * (1 - Y_mean) / Y_usv - 1))

plt.title("my own test")
print("testing")
print(alpha_parameters)
print(beta_parameters)

# plt.hist(alpha_parameters, color='r', density=True)
# plt.hist(beta_parameters, color='b', density=True)
# same fix... it didn't work last time tho
alpha_adjusted = []
for a in range(len(alpha_parameters)-1, 0-1, -1):
    if ~np.isinf(alpha_parameters[a]) and ~np.isnan(alpha_parameters[a]):
        alpha_adjusted.append(alpha_parameters[a])
adjusted_mean_a = np.mean(alpha_adjusted)
alpha_adjusted.reverse()
print(alpha_adjusted)
beta_adjusted = []
for b in range(len(beta_parameters)-1, 0-1, -1):
    if ~np.isinf(beta_parameters[b]) and ~np.isnan(beta_parameters[b]):
        beta_adjusted.append(beta_parameters[b])
adjusted_mean_b = np.mean(beta_adjusted)
beta_adjusted.reverse()
print(beta_adjusted)

alpha_parameters_Y = np.nan_to_num(alpha_parameters, nan=adjusted_mean_a, posinf=adjusted_mean_a, neginf=adjusted_mean_a)
beta_parameters_Y = np.nan_to_num(beta_parameters, nan=adjusted_mean_b, posinf=adjusted_mean_b, neginf=adjusted_mean_b)

plt.plot(alpha_parameters_Y, beta_parameters_Y, 'ro')
plt.show()

# (d) simulate 5000 cups

# for cup in range(5000):

# indexed after skaters (for the final we need to keep all this sht for when we recalculate the total grades)
grade_list = []
for skater in range(0, len(df)):
    Y1 = 0
    Y2 = 0
    X1 = 0
    X2 = 0
    X3 = 0
    X4 = 0

    Y1 = stats.beta.rvs(a=alpha_parameters_Y[skater], b=beta_parameters_Y[skater], size=1)
    Y2 = stats.beta.rvs(a=alpha_parameters_Y[skater], b=beta_parameters_Y[skater], size=1)
    thetas = stats.bernoulli.rvs(p=theta_parameters[skater], size=4)
    # print(thetas)
    if thetas[0] == 1:
        X1 = stats.beta.rvs(a=alpha_parameters_X[skater], b=beta_parameters_X[skater], size=1)
    if thetas[1] == 1:
        X2 = stats.beta.rvs(a=alpha_parameters_X[skater], b=beta_parameters_X[skater], size=1)
    if thetas[2] == 1:
        X3 = stats.beta.rvs(a=alpha_parameters_X[skater], b=beta_parameters_X[skater], size=1)
    if thetas[3] == 1:
        X4 = stats.beta.rvs(a=alpha_parameters_X[skater], b=beta_parameters_X[skater], size=1)

    # calculate total grade
    topX = [X1, X2, X3, X4]
    topX.sort()
    topX = topX[2:]
    topY = max(Y1, Y2)
    grade = sum(topX) + topY

    grade_list.append(grade)

Y1 = []
Y2 = []
X1 = []
X2 = []
X3 = []
X4 = []
