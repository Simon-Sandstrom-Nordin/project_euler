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

print(df)
