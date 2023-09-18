# MW 2022-03-23
# Python simulation of damped driven pendulum

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
a_list = []
amp_list = []

for a in range(0, 15):
    # time parameters
    dt = 0.001             # time step
    dt2 = dt/2             # half of time step
    t = 0  	               # start time

    # initial conditions
    theta = np.pi/2        # initial angular position
    p = 0                  # initial angular velocity

    # model parameters (set m=g=L=1)
    omega0 = 1           # natural frequency
    omega02 = omega0**2
    gamma = 3/8          # damping coefficient
    omega = 2/3          # drive frequency
    A = a*.1             # amplitude of drive force

    position = []         # list to store angular position
    momentum = []         # list to store angular momentum
    time_list = []
    theta_list = []


    def f(theta, p, t):
        accel = -omega02*np.sin(theta) # pendulum
        accel += -gamma*p              # damping
        accel += A*np.cos(omega*t)     # drive force
        return accel


    def rk4(x, v, t):
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


    counter = 0


    def step():
        global theta_list, counter, xx, yy, t, p, theta, H, time, ene, position, momentum, time_list

        theta, p, t = rk4(theta, p, t)

        # energy
        # H = 0.5*p**2 + 1 - np.cos(theta)

        # position
        xx = (0, np.sin(theta))
        yy = (0, -np.cos(theta))

        position.append(theta)
        momentum.append(p)
        time_list.append(t)
        if theta > np.pi:
            theta -= 2*np.pi
        if theta < -np.pi:
            theta += 2*np.pi
        if (counter % 2 == 0) and (p < 0):
            counter += 1
            print(theta)
            theta_list.append(abs(theta))
        elif (counter % 2 == 1) and (p > 0):
            counter += 1
            print(abs(theta))
            theta_list.append(abs(theta))
        return None


    while counter < 200:
        step()

    a_list.append(a*.1)
    amp_list.append(abs(theta))


plt.plot(a_list, amp_list, 'o')
plt.show()
