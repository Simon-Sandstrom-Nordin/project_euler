# MW 2022-03-23
# Python simulation of damped driven pendulum

import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_yscale('log')
plt.title("Amplitude [rad] at turning points over time [s], with dt = 1e-5 [s]")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude [rad]")

for count in range(1, 2+1):

    amp_list = []
    time_list = []

    t = 0  # start time

    # initial conditions
    theta = np.pi / 2  # initial angular position
    p = 0  # initial angular velocity
    dt = 10**(-4) / (10*count)
    # model parameters (set m=g=L=1)
    omega0 = 1  # natural frequency
    omega02 = omega0 ** 2
    gamma = 1  # damping coefficient
    omega = 2 / 3  # drive frequency
    A = .4  # amplitude of drive force

    position = []  # list to store angular position
    momentum = []  # list to store angular momentum


    def f(theta, p, t):
        accel = -omega02 * np.sin(theta)  # pendulum
        accel += -gamma * p  # damping
        # accel += A*np.cos(omega*t)     # drive force
        return accel


    def rk4(x, v, t):
        xk1 = dt * v
        vk1 = dt * f(x, v, t)
        xk2 = dt * (v + vk1 / 2)
        vk2 = dt * f(x + xk1 / 2, v + vk1 / 2, t + dt / 2)
        xk3 = dt * (v + vk2 / 2)
        vk3 = dt * f(x + xk2 / 2, v + vk2 / 2, t + dt / 2)
        xk4 = dt * (v + vk3)
        vk4 = dt * f(x + xk3, v + vk3, t + dt)
        x += (xk1 + 2 * xk2 + 2 * xk3 + xk4) / 6
        v += (vk1 + 2 * vk2 + 2 * vk3 + vk4) / 6
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

        if theta > np.pi:
            theta -= 2 * np.pi
        if theta < -np.pi:
            theta += 2 * np.pi


    for counter in range(1, 10):
        # time parameters
        if counter % 2 == 0:
            while p <= 0:
                step()
        else:
            while p > 0:
                step()
        time_list.append(t)
        amp_list.append(abs(theta))

    if count == 1:
        plt.plot(time_list, amp_list, 'bo-')
    elif count == 2:
        plt.plot(time_list, amp_list, 'ro')
    print("Time [s] | Amplitude [rad]")
    for k in range(0, len(amp_list)):
        print(time_list[k], "|", amp_list[k])
plt.show()


# linear* interpolation between first two points
# a1 = np.log(amp_list[0])
# a2 = np.log(amp_list[1])
# t1 = time_list[0]
# t2 = time_list[1]
# gradient
# k = (a2 - a1) / (t2 - t1)
# y-intercept
# m = amp_list[0] - k*t1
C = (amp_list[1] / (amp_list[2]**(time_list[1]/time_list[2]))) ** ((1 - time_list[1]/time_list[2])**(-1))
alpha = (1/time_list[2]) * np.log(amp_list[2] / C)


def linear(x):
    return C*np.exp(alpha*x)


fig = plt.figure()
x_linspace = np.linspace(0, 30, 100+1)
#ax = fig.add_subplot(1, 1, 1)
#ax.set_yscale('log')
plt.plot(x_linspace, linear(x_linspace), 'g-')
plt.plot(time_list, amp_list, 'ro')
plt.title("Amplitude [rad] at turning points over time [s], with dt = 1e-5 [s]")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude [rad]")
plt.show()

# now for the interpolation


def linear_int(x):
    return C*np.exp(alpha*x) - amp_list[0]/2    # vi hittar nollställen här


guess_low = 0
guess_high = 5

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
print(linear_int(guess_mid))
