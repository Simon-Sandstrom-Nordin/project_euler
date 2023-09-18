# MW 2022-03-23
# Python simulation of damped driven pendulum

import numpy as np
import matplotlib.pyplot as plt

gamma_list = []
for g in range(1, 9):
    for k in range(0, 1):

        # time parameters
        dt = 0.0001*10**(-k)             # time step
        dt2 = dt/2            # half time step
        t = 0  	              # start time

        # initial conditions
        theta = np.pi/2       # initial angular position
        p = 0                 # initial angular velocity

        # model parameters (set m=g=L=1)
        omega0 = 1           # natural frequency
        omega02 = omega0**2
        gamma = 3/8          # damping coefficient
        omega = 2/3          # drive frequency
        A = a*.1              # amplitude of drive force

        position = []         # list to store angular position
        momentum = []         # list to store angular momentum

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

        def step():
            global xx, yy, t, p, theta, H, time, ene, position, momentum

            theta, p, t = rk4(theta, p, t)

            # energy
            #H = 0.5*p**2 + 1 - np.cos(theta)

            # position
            xx = (0, np.sin(theta))
            yy = (0, -np.cos(theta))

            position.append(theta)
            momentum.append(p)

            if theta>np.pi: theta -= 2*np.pi
            if theta<-np.pi: theta += 2*np.pi

        while p <= 0:
            step()
        print(t * 2)  # twice half-period

    gamma_list.append(1/gamma)
    amp_list.append(abs(theta))

plt.plot(gamma_list, amp_list, 'o')
plt.show()
