# MW 2022-03-23
# Python simulation of damped driven pendulum

import numpy as np
import matplotlib.pyplot as plt

gamma_list = []
amp_list = []

for g in range(1, 19+1):
    for k in range(5, 6):

        # time parameters
        dt = 1*10**(-k)             # time step
        # dt2 = dt/2            # half time step
        t = 0  	              # start time

        # initial conditions
        theta = np.pi/2       # initial angular position
        p = 0                 # initial angular velocity

        # model parameters (set m=g=L=1)
        omega0 = 1           # natural frequency
        omega02 = omega0**2
        gamma = .1*g          # damping coefficient
        omega = 2/3          # drive frequency
        A = .4              # amplitude of drive force

        position = []         # list to store angular position
        momentum = []         # list to store angular momentum

        def f(theta, p, t):
            accel = -omega02*np.sin(theta) # pendulum
            accel += -gamma*p              # damping
            # accel += A*np.cos(omega*t)     # drive force
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
            # H = 0.5*p**2 + 1 - np.cos(theta)

            # position
            xx = (0, np.sin(theta))
            yy = (0, -np.cos(theta))

            position.append(theta)
            momentum.append(p)

            if theta>np.pi: theta -= 2*np.pi
            if theta<-np.pi: theta += 2*np.pi

        while p <= 0:
            step()
        print(gamma)

    gamma_list.append(gamma)
    amp_list.append(abs(theta))

fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# ax.set_xscale('log')
# plt.plot(dx_list, time_list, 'o')
# plt.plot(gamma_list, amp_list, 'o')
plt.title("Amplitude [rad] at first turning point over γ [1/s], with dt = 1e-5 [s]")
plt.xlabel("γ [1/s]")
plt.ylabel("Amplitude [rad]")
plt.plot(gamma_list, amp_list, 'o')
plt.show()

print("Gamma | Amplitude")
for k in range(0, len(gamma_list)):
    print(gamma_list[k], "|", amp_list[k])

# inversion
for element in range(0, len(gamma_list)):
    gamma_list[element] = 1/gamma_list[element]
# linear interpolation between first two points
a1 = amp_list[-1]
a2 = amp_list[-2]
g1 = gamma_list[-1]
g2 = gamma_list[-2]

# gradient
k = (a2 - a1) / (g2 - g1)

# y-intercept
m = a1 - k*g1


def linear(x):
    return k*x+m


x_linspace = np.linspace(0, 2, 100+1)
plt.plot(gamma_list, amp_list, 'bo')
plt.plot(x_linspace, linear(x_linspace), 'g-')
plt.title("Amplitude [rad] at first turning point over 1/γ [s], with dt = 1e-5 [s]")
plt.xlabel("1/γ [s]")
plt.ylabel("Amplitude [rad]")
plt.show()

# now for the interpolation


def linear_int(x):
    return k*x+m    # vi hittar nollställen här


guess_low = 0
guess_high = 2

# intervallhalvering
error = 1
tol = 10**(-9)
while error > tol:
    guess_mid = (guess_low + guess_high) / 2
    if linear_int(guess_mid) * linear_int(guess_high) < 0:
        guess_low = guess_mid
    else:
        guess_high = guess_mid
    error = abs(guess_low - guess_high)

print(guess_mid)
print(1/guess_mid)
print(linear_int(guess_mid))
