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

# Number of sources
N = 100

# source positions
w = .05  # width of pre-slit
source_positions = np.linspace(-w / 2, w / 2, N)

# compute time averaged intensity on a detector screen
screen = np.empty(points)
intensity = np.empty(points)
for point in range(points):
    x = W * (point / (points - 1) - 0.5)
    screen[point] = x
    r = np.sqrt(D**2 + x**2)
    combined_interference = 0
    for i in range(0, N-2):
        for j in range(i+1, N):
            xi = source_positions[i]
            xj = source_positions[j]
            ri = np.sqrt(D ** 2 + (x - xi) ** 2)
            rj = np.sqrt(D ** 2 + (x - xj) ** 2)
            combined_interference += np.cos(k*(abs(r-ri)-abs(r-rj)))
    intensity[point] = (N/2 + combined_interference)/r**2
plt.plot(screen, intensity, 'o')
plt.xlabel('x')
plt.ylabel('intensity')
plt.show()
