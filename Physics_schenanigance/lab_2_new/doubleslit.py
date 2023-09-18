# MW 2023-03-20
# Python calculation of wave interference
# length unit: mm

import numpy as np
import matplotlib.pyplot as plt

# wave parameters
wavelength = 0.0005 # mm = 5000 Ångström, approx wavelength för green laser pointer
k = 2*np.pi/wavelength

# geometry parameters
d = 0.5 # separation between slits
D = 4000 # distance to detector screen
W = 20 # width of detector screen
points = 10000000 # number of pixels of detector screen

print("Wavelength is:", wavelength)
print("Separation between slits is:", d)
print("Distance to detector screen is:", D)
print("Distance between points is:", d/points)

# source positions
x1 = d/2
x2 = -d/2

# compute time averaged intensity on a detector screen
screen = np.empty(points)
intensity = np.empty(points)
for i in range(points):
    x = W*(i/(points-1)-0.5)
    screen[i] = x
    r = np.sqrt(D**2 + x**2)
    r1 = np.sqrt(D**2 + (x-x1)**2)
    r2 = np.sqrt(D**2 + (x-x2)**2)
    intensity[i] = (1 + np.cos(k*(r1-r2)))/r**2
plt.xlabel('x')
plt.ylabel('intensity')

intensity_lowered = intensity - intensity[0]/2
plt.plot(screen, intensity_lowered, 'b-')

index_list = []
index = 0
for counter in range(0, 2+1):
    while intensity_lowered[index] * intensity_lowered[index+1] > 0:
        index += 1
    if counter != 1:
        index_list.append(index)
    index += 1

for k in index_list:
    # print(k)
    # print(intensity_lowered[k])
    pass

# index_list[0] is first root
index_1 = index_list[0]
# index_list[1] is one period later
index_2 = index_list[1]
# linear int. y = k*x + m
k1 = (intensity_lowered[index_1]-intensity_lowered[index_1+1])/(screen[index_1]-screen[index_1+1])
m1 = intensity_lowered[index_1] - k1 * screen[index_1]


def linear_1(x_lin):
    return k1*x_lin + m1


k2 = (intensity_lowered[index_2]-intensity_lowered[index_2+1])/(screen[index_2]-screen[index_2+1])
m2 = intensity_lowered[index_2] - k2 * screen[index_2]


def linear_2(x_lin):
    return k2*x_lin + m2


x_lin_1 = np.linspace(screen[index_1], screen[index_1+1], num=100)
x_lin_2 = np.linspace(screen[index_2], screen[index_2+1], num=100)
plt.plot(x_lin_1, linear_1(x_lin_1), 'r-')
plt.plot(x_lin_2, linear_2(x_lin_2), 'g-')

plt.show()


# bisection method to find roots (thnx GPT)
def bisection_method(f, a, b, epsilon):
    """
    Bisection method to find the root of a function f within the interval [a, b]
    with a given tolerance epsilon.
    """
    if f(a) * f(b) > 0:
        raise ValueError("The function values at the interval endpoints must have opposite signs.")

    while (b - a) > epsilon:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2


tol = 1e-12
# Apply bisection method to find roots of linear_1
root_1 = bisection_method(linear_1, screen[index_1], screen[index_1 + 1], epsilon=tol)

# Apply bisection method to find roots of linear_2
root_2 = bisection_method(linear_2, screen[index_2], screen[index_2 + 1], epsilon=tol)

print("Tolerance for bisection method is: ", tol)
print("Root 1:", root_1)
print("Root 2:", root_2)
print("Period is:", root_2-root_1)
print("Theoretical period is:", wavelength * D / d)
