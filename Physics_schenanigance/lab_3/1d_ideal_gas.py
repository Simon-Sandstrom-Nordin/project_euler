"""
One-dimensional ideal gas simulation with animation
Calculates pressure from particle collisions with container wall
MW 220422
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

# set up simulation parameters (assume constants k=1, m=1)
P = 0.0 # initial value of time averaged pressure
L = 10.0 # length of container
V = L**2 # volume = length of container for d=1
N = 200 # number of particles
T = 2.0 # initial temperature
dt = 0.1 # time step
t = 0.0 # initial time


def positive_or_negative(N):
    array = np.random.random(N)
    for k in range(0, N):
        if np.random.random() < 0.5:
            array[k] = 1
        else:
            array[k] = -1
    return array


# initial state
x = L*np.random.random(N) # initial random positions, distributed uniformly in container
y = np.multiply(np.random.random(N), positive_or_negative(N))
vx = np.sqrt(T)*np.random.randn(N) # initial random velocities, Maxwell distributed
vy = np.sqrt(T)*np.random.randn(N)

# Result lists
ti=[]
pr=[]
prt=[]
nl=[]
nr=[]

# set up the figure and animation elements
fig = plt.figure(figsize=(10,10),dpi=80)
ax1 = plt.subplot(311,aspect='equal', autoscale_on=False, xlim=(0, L), ylim=(-L/2,L/2))
gas, = ax1.plot([], [], 'bo', ms=2)
ax2 = plt.subplot(312, autoscale_on=False, xlim=(0, 100), ylim=(0, 2*2*N*T/L))
pressure, = ax2.plot([], [], lw=1, color='b')
plt.xlabel('time t')
plt.ylabel('pressure P')
ax3 = plt.subplot(313, autoscale_on=False, xlim=(0, 100), ylim=(0, N))
numleft, = ax3.plot([], [], lw=1, color='b')
numright, = ax3.plot([], [], lw=1, color='r')
plt.xlabel('time t')
plt.ylabel('particle numbers on left and right side')

# one time step
def step() :
    global x,vx,y,vy,t,P,Pt,ti,pr,nl,nr
    x += vx*dt
    y += vy * dt
    t += dt
    Pt = 0.0 # pressure at timestep t
    # collision with walls: reverse velocity and distance to wall
    nleft = 0
    nright = 0
    for i in range(N) :
        # x values
        if x[i] < 0.0 : 
            x[i] = -x[i]
            vx[i] = -vx[i]
        if x[i] > L :
            x[i] = 2.0*L-x[i]
            vx[i] = -vx[i]
            Pt += 2.0*np.abs(vx[i])/dt # pressure at time t
            P += 2.0*np.abs(vx[i]) # sum of all pressure changes               
        if x[i]<L/2.0 : nleft += 1
        if x[i]>L/2.0 : nright += 1
        # y values
        if y[i] < -L/2:
            y[i] = -L-y[i]
            vy[i] = -vy[i]
        if y[i] > L/2:
            y[i] = L-y[i]
            vy[i] = -vy[i]
            Pt += 2.0 * np.abs(vy[i]) / dt  # pressure at time t
            P += 2.0 * np.abs(vy[i])  # sum of all pressure changes

    # calculate temperature from x-component of velocity: T/2=v**2/2 
    #v2=0.0
    #for i in range(N) :
    #    v2 += vx[i]**2
    #T = v2/N
    ti.append(t)
    nl.append(nleft)
    nr.append(nright)
    prt.append(Pt) # pressure at time t
    pr.append(P/t) # time average of pressure
                    

time_list = []
law_list = []
# calculations
for i in range(1000):
    step()
    if i % 10 == 0: # append at one second intervals, dt=.1
        time_list.append(t)
        law_list.append((P / t) * V - N * 1 * T)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
# initialization
def init():
    gas.set_data([], [])
    pressure.set_data([], [])
    numleft.set_data([], [])
    numright.set_data([], [])
    return gas,pressure,numleft,numright

# animation function
def animate(i):
    step() 
    gas.set_data(x, y)
    pressure.set_data(ti, pr) # time average of pressure
    # pressure.set_data(ti, prt) # pressure at time t
    numleft.set_data(ti, nl)
    numright.set_data(ti, nr)
    return gas,pressure,numleft,numright

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=600, interval=10, blit=True, repeat=True)

# save animation to file
#anim.save("animation.mp4", writer=animation.FFMpegWriter(fps=30))

plt.show()

plt.plot(time_list, law_list, 'r')
plt.title("PV - NkT over time")
plt.ylabel("PV - NkT")
plt.xlabel("Time [s]")
plt.show()
