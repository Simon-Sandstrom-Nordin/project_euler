import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("SLS22.csv")

# a. Normalize data
# run 1,2
for r in range(1, 2+1):
    run = "run " + str(r)
    df[run] = df[run]/np.max(df[run])
# trick 1-7
for t in range(1, 6+1):
    trick = "trick " + str(t)
    df[trick] = df[trick]/np.max(df[trick])

for t in range(1, 4+1):
    plt.title("Trick " + str(t))
    plt.hist(df["trick " + str(t)], density=True)
    plt.show()

# c. make i
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

# do skaters
list = []
for skater in range(0, len(df)):
    print(df["id"][skater]) # good, we can index like this
    score = 0
    make_counter = 0
    for trick_no in range(1, 4+1):
        if df["make " + str(trick_no)][skater] == 1:
            make_counter += 1
            if df["trick " + str(trick_no)][skater] > .6:
                score += 1

    try:
        print('P("Score > .6" I "Successful trick") =', score/make_counter)
        list.append(score/make_counter)
    except ZeroDivisionError:
        print("Player landed no tricks")
        list.append(0)

plt.hist(list)
plt.show()

# spridningsdiagram (scatter diagrams?)
plt.plot(df["run 1"], df["run 2"], 'ro')
plt.show()
