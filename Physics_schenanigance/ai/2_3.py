import numpy as np
import matplotlib.pyplot as plt

# wave parameters
wavelength = 0.0005  # mm = 5000 Ångström, approx wavelength for green laser pointer
k = 2 * np.pi / wavelength

# geometry parameters
d = 0.5  # separation between slits
D = 2000  # distance to detector screen
W = 20  # width of detector screen
points = 1000  # number of pixels of detector screen

# single slit parameters
w = 0.05  # width of the slit
N_values = [2, 3, 5, 10]  # number of sources

for N in N_values:
    # source positions
    source_positions = np.linspace(-w / 2, w / 2, N)

    # compute time averaged intensity on a detector screen
    screen = np.empty(points)
    intensity = np.empty(points)
    for i in range(points):
        x = W * (i / (points - 1) - 0.5)
        screen[i] = x
        r = np.sqrt(D ** 2 + x ** 2)
        interference = np.sum(np.cos(k * (r - np.sqrt(D ** 2 + (x - source_positions) ** 2))))

        r1 = np.sqrt(D ** 2 + (x - source_positions) ** 2)
        r2 = np.sqrt(D ** 2 + (x + source_positions) ** 2)

        intensity[i] = (1 + 2 * interference + np.sin(N * (k * (r1 - r2)))) / r ** 2

    plt.plot(screen, intensity, 'o', label=f'N = {N}')

plt.xlabel('x')
plt.ylabel('intensity')
plt.title('Interference Pattern - Single Slit with N Sources')
plt.legend()
plt.show()
