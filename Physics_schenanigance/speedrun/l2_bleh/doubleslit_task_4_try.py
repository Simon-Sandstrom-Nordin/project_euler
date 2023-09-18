
# MW 2023-03-20
# Python calculation of wave interference
# length unit: mm

import numpy as np
import matplotlib.pyplot as plt

# wave parameters
wavelength = 0.0005     # mm = 5000 Ångström, approx wavelength för green laser pointer
k = 2*np.pi/wavelength

# geometry parameters
D = 2000        # distance to detector screen
W = 80          # width of detector screen
points = 1000   # number of pixels of detector screen

# slit parameters
d = .05
w = .20     # width of slit
N = 100      # number of point sources
point_sources_1 = np.linspace(-d/2-w/2, -d/2+w/2, N)    # numpy array with slit point sources
point_sources_2 = np.linspace(d/2-w/2, d/2+w/2, N)    # numpy array with slit point sources
point_sources = np.append(point_sources_1, point_sources_2)
N = N*2

# compute time averaged intensity on a detector screen
screen = np.empty(points)
intensity = np.empty(points)
for p in range(points):
    x = W * (p / (points - 1) - 0.5)
    r = np.sqrt(D ** 2 + x ** 2)
    intensity[p] = N/(2*r**2)
    screen[p] = x
    for i in range(0, N-1):
        for j in range(i+1, N):
            x1 = point_sources[i]
            x2 = point_sources[j]
            r1 = np.sqrt(D**2 + (x-x1)**2)
            r2 = np.sqrt(D**2 + (x-x2)**2)
            intensity[p] += np.cos(k*(r1-r2))/(r**2)

# normalization
intensity = intensity / intensity.max()

plt.plot(screen, intensity)
plt.xlabel('x')
plt.ylabel('intensity')
# plt.show()


# new
N = N // 2
point_sources = np.linspace(-w/2, w/2, N)    # numpy array with slit point sources
print(point_sources)

# compute time averaged intensity on a detector screen
screen = np.empty(points)
intensity = np.empty(points)
for p in range(points):
    x = W * (p / (points - 1) - 0.5)
    r = np.sqrt(D ** 2 + x ** 2)
    intensity[p] = N/(2*r**2)
    screen[p] = x
    for i in range(0, N-1):
        for j in range(i+1, N):
            x1 = point_sources[i]
            x2 = point_sources[j]
            r1 = np.sqrt(D**2 + (x-x1)**2)
            r2 = np.sqrt(D**2 + (x-x2)**2)
            intensity[p] += np.cos(k*(r1-r2))/(r**2)
# normalize intensity
max_intense = intensity.max()
for k in range(len(intensity)):
    intensity[k] = intensity[k] / max_intense

plt.plot(screen, intensity)
plt.xlabel('x')
plt.title('w = ' + str(w) + ', N = ' + str(N))
plt.legend(['Double slit', 'Single slit'])
plt.ylabel('intensity')
plt.show()
