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
D = 2000 # distance to detector screen
W = 20 # width of detector screen
points = 1000 # number of pixels of detector screen

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
plt.plot(screen,intensity)
plt.xlabel('x')
plt.ylabel('intensity')
plt.show()

counter = 1
while intensity[counter] > intensity[counter+1]:
    counter += 1
print(counter)
print(intensity[counter-1])
print(intensity[counter])
print(intensity[counter+1])
print(screen[counter-1])
print(screen[counter])
print(screen[counter+1])
x_one_b = screen[counter-1]
x_one = screen[counter]
x_one_a = screen[counter+1]

counter += 1
while intensity[counter] < intensity[counter+1]:
    counter += 1
print(counter)
print(intensity[counter-1])
print(intensity[counter])
print(intensity[counter+1])
print(screen[counter-1])
print(screen[counter])
print(screen[counter+1])

counter += 1
while intensity[counter] > intensity[counter+1]:
    counter += 1
print(counter)
print(intensity[counter-1])
print(intensity[counter])
print(intensity[counter+1])
print(screen[counter-1])
print(screen[counter])
print(screen[counter+1])
x_two_b = screen[counter-1]
x_two = screen[counter]
x_two_a = screen[counter+1]

est = abs(abs(x_one) - abs(x_two))
print(est)
error_1 = abs(abs(x_one_b) - abs(x_one_a))
error_2 = abs(abs(x_two_b) - abs(x_two_a))
e_tot = error_1 + error_2
print(e_tot)
print(wavelength * D / d)
print((est + e_tot, est - e_tot))
