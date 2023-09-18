# MW 2022-03-23
# Python simulation of damped driven pendulum

import numpy as np
import matplotlib.pyplot as plt

theta_list = []
gamma_list = []
amp_list = []
dx_list = []
time_list = []


# functions
def f(theta, p, t):
    accel = -omega02 * np.sin(theta)  # pendulum
    # accel += -gamma*p              # damping
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

    if theta > np.pi: theta -= 2 * np.pi
    if theta < -np.pi: theta += 2 * np.pi


for th in range(1, 11):
    for k in range(5, 6):

        # time parameters
        dt = 1*10**(-k)             # time step
        # dt2 = dt/2            # half time step
        t = 0  	              # start time

        # theta = np.pi / 2  # original theta
        theta = .1 * th * np.pi/2       # initial angular position
        p = 0                 # initial angular velocity

        # model parameters (set m=g=L=1)
        omega0 = 1           # natural frequency
        omega02 = omega0**2
        # gamma = .1*g          # damping coefficient
        omega = 2/3          # drive frequency
        A = .4              # amplitude of drive force


        position = []         # list to store angular position
        momentum = []         # list to store angular momentum

        while p <= 0:
            step()
        # print(t * 2)  # twice half-period
        dx_list.append(dt)
        #amp_list.append(abs(theta))
        time_list.append(2*t)
        print("dt:", dt)
        print("Period:", 2 * t)

    # gamma_list.append(1/gamma)
    # amp_list.append(abs(theta))
    theta_list.append(abs(theta))

fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# ax.set_xscale('log')

# task 1
plt.plot(theta_list, time_list, 'bo')
plt.xlabel('Initial angle θ [rad]')
# plt.xscale('log')

# add numeric integration, series expansion, harmonic oscillator approximation
# integral from MATLAB:
int_list = [6.292888488002469, 6.322163735574268, 6.371516346195520, 6.441816615157760, 6.534345229832613, 6.650863833964514,
            6.793719452125099, 6.965996937706756, 7.171742687611157,  7.416298709205909]
plt.plot(theta_list, int_list, '-k')

# Series exp.
def series_exp(th0):
    return 2*np.pi*(1 + (1/16)*th0**2 + (11/3072)*th0**4)
th0_linspace = np.linspace(theta_list[0], theta_list[-1])
plt.plot(th0_linspace, series_exp(th0_linspace), '-r')

# Harmonic osc. approx.
def harmonic_approx(th0):
    return 2*np.pi
plt.plot(th0_linspace, [harmonic_approx(th0) for th0 in th0_linspace], '-g')

plt.ylabel('Period time [s]')
plt.title('Period time [s] over initial angle θ [rad], with dt = 1e-5 [s]')
# plt.plot(gamma_list, amp_list, 'o')
# plt.plot(theta_list, time_list, 'o')

#legend
plt.legend(['Measured data', 'Numeric integration',
            'Series approximation', 'Harmonic oscillator approximation'])

plt.show()

print("Initial angle θ [rad] | Period time [s]")
for k in range(0, len(dx_list)):
    print(str(round((k+1)*.1, 1)) + " * π/2 ≈", theta_list[k], "|", time_list[k])
