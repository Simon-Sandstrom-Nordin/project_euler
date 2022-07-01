import math

from matplotlib import pyplot as plt

A = [1058, 1045, 942, 1044, 1047, 1029, 980, 980, 988, 983,
     977, 982, 974, 900, 908, 928, 940, 954, 940, 945, 936]
B = [180, 186, 174.5, 188, 180, 185, 185, 184, 184, 189,
     183.5, 181, 186, 177, 180.5, 178.5, 175.5, 182, 182, 177, 175]

average_A = sum(A) / len(A)
average_B = sum(B) / len(B)

covariance = 0
for k in range(0, len(A)):
    covariance += (A[k] - average_A) * (B[k] - average_B)
covariance = covariance / (len(A) - 1)
print("covariance is", covariance)

point_estimate_variance_A = 0
for k in A:
    point_estimate_variance_A += (k - average_A)**2
point_estimate_variance_A = point_estimate_variance_A / (len(A)-1)
point_estimate_variance_A = math.sqrt(point_estimate_variance_A)

point_estimate_variance_B = 0
for k in B:
    point_estimate_variance_B += (k - average_B)**2
point_estimate_variance_B = point_estimate_variance_B / (len(A)-1)
point_estimate_variance_B = math.sqrt(point_estimate_variance_B)

correlation_coefficient = covariance / (point_estimate_variance_A*point_estimate_variance_B)
print("correlation coefficient is", correlation_coefficient)

plt.plot(A, B, 'ro')
plt.show()
