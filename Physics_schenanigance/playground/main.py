import math as m
import matplotlib.pyplot as plt
g = 9.82


def evol(u, v):
    up = v
    vp = -g*m.sin(u)
    return [up, vp]


phi_0 = m.pi/4
phip_0 = 0
T = 10
N = 100000
h = T/N

time_list = [0]
phi_list = [phi_0]
phip_list = [phip_0]

for k in range(1, N):
    [up, vp] = evol(phi_list[-1], phip_list[-1])
    phi_list.append(phi_list[-1] + up*h)
    phip_list.append(phip_list[-1] + vp * h)
    time_list.append(time_list[-1] + h)

plt.plot(time_list, phi_list, 'r')

N = 2*N
h = T/N
phi_0 = m.pi/4
phip_0 = 0

time_list = [0]
phi_list = [phi_0]
phip_list = [phip_0]

for k in range(1, N):
    [up, vp] = evol(phi_list[-1], phip_list[-1])
    phi_list.append(phi_list[-1] + up*h)
    phip_list.append(phip_list[-1] + vp * h)
    time_list.append(time_list[-1] + h)

plt.plot(time_list, phi_list, 'b')
plt.title("Pendulum motion")
plt.ylabel("Angle from vertical [rad]")
plt.xlabel("Time [s]")
plt.show()