class CustomError(Exception):
    pass

# MW 2022-03-23
# Python simulation of damped driven pendulum

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# .01: 3.709999999999965
# .001: 3.7089999999997025
# .0001: 3.7089999999997025

# time parameters
dt = 0.1             # time step
dt2 = dt/2            # half time step
t = 0  	              # start time

# initial conditions
theta = np.pi/2       # initial angular position
p = 0                 # initial angular velocity
counter = 0

# model parameters (set m=g=L=1)
omega0 = 1           # natural frequency
omega02 = omega0**2
gamma = 3/8            # damping coefficient
omega = 2/3          # drive frequency
A = .4              # amplitude of drive force

position = []         # list to store angular position
momentum = []         # list to store angular momentum
time = []

# set up the figure and the plot element to animate
fig = plt.figure(figsize=(10,14),dpi=80)
ax1 = plt.subplot(211, aspect='equal', autoscale_on=False, xlim=(-1.1,1.1), ylim=(-1.1,1.1))
pendulum, = ax1.plot([], [], c='r', lw=10)
ax1.axis('off')
ax2 = plt.subplot(212, aspect='equal', autoscale_on=False, xlim=(-np.pi, np.pi), ylim=(-3, 3))
phaseportrait, = ax2.plot([], [], 'bo', markersize=0.5)# c='black', lw=0)
ax2.set_xlabel(r'$\theta$')
ax2.set_ylabel(r'p')


def f(theta, p, t):
    accel = -omega02*np.sin(theta) # pendulum
    accel += -gamma*p              # damping
    accel += A*np.cos(omega*t)     # drive force
    return accel


def rk4(x, v, t):   # Runge-Kutta 4
    xk1 = dt*v
    vk1 = dt*f(x, v, t)
    xk2 = dt*(v+vk1/2)
    vk2 = dt*f(x+xk1/2, v+vk1/2, t+dt/2)
    xk3 = dt*(v+vk2/2)
    vk3 = dt*f(x+xk2/2, v+vk2/2, t+dt/2)
    xk4 = dt*(v+vk3)
    vk4 = dt*f(x+xk3, v+vk3, t+dt)
    x += (xk1+2*xk2+2*xk3+xk4)/6
    v += (vk1+2*vk2+2*vk3+vk4)/6
    t += dt
    return x, v, t


def step():
    global counter, list_change, xx, yy, t, p, theta, H, time, ene, position, momentum, amplitude, time

    theta, p, t = rk4(theta, p, t)

    # break for period
    if ((-1)**counter)*p > 0:
        counter += 1
        print(counter)
        if counter > 12:
            fig2 = plt.figure()
            ax = fig2.add_subplot()
            ax.set_yscale('log')
            res = [abs(ele) for ele in position]
            plt.plot(time, res)
            plt.show()
            raise EOFError
            return False

    # energy
    # H = 0.5*p**2 + 1 - np.cos(theta)

    # position
    xx = (0, np.sin(theta))
    yy = (0, -np.cos(theta))

    time.append(t)
    position.append(theta)
    momentum.append(p)

    #if theta>np.pi: theta -= 2*np.pi
    #if theta<-np.pi: theta += 2*np.pi


def init():
    pendulum.set_data([], [])
    phaseportrait.set_data([], [])
    return pendulum, phaseportrait


def animate(i):
    result = step()
    if result is False:
        return
    pendulum.set_data(xx, yy)
    phaseportrait.set_data(position, momentum)
    return pendulum, phaseportrait,


anim = animation.FuncAnimation(fig, animate, init_func=init,
                                frames=600, interval=1, blit=True, repeat=True)
plt.show()

pos = 0
pos_list = []
try:
    while True:
        if position[pos+1] > position[pos]:
            while position[pos+1] > position[pos]:
                pos += 1
            pos_list.append(pos)
        else:
            while position[pos+1] < position[pos]:
                pos += 1
            pos_list.append(pos)

except IndexError:
    pass

print(pos_list)

for p in pos_list:
    print("pos:", p)
    print(position[p-1])
    print(position[p])
    print(position[p+1])

time_amp = [time[0]]
list_amp = [position[0]]
for p in pos_list:
    time_amp.append(time[p])
    list_amp.append(position[p])
list_amp = [abs(el) for el in list_amp]
print(list_amp)

plt.plot(time_amp, list_amp, 'o')
plt.show()

# linear interpolation
t1 = time_amp[0]
t2 = time_amp[1]
a1 = list_amp[0]
a2 = list_amp[1]

A = np.array([[t1, 1], [t2, 1]])
A_inv = np.linalg.inv(A)
r = np.array([[a1], [a2]])

print(A)
print(A_inv)
print(A @ A_inv, A_inv @ A)
print(A_inv @ r)
coeff = A_inv @ r

# y = kx + m
# position[0]/ 2 = k*tau + m
# => tau = position[0]/(2*k) - m
tau = (position[0]/2 - coeff[1]) / coeff[0]
print(tau)
