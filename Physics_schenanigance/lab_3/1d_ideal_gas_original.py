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
L0 = 10.0 # length of container
L = L0 / 10

V = L # volume = length of container for d=1
N = 100 # number of particles
T = 1.0 # initial temperature
dt = 0.1 # time step
t = 0.0 # initial time
v0 = .1

# initial state
x = L*np.random.random(N) # initial random positions, distributed uniformly in container
y = np.zeros(N)
vx = np.sqrt(T)*np.random.randn(N) # initial random velocities, Maxwell distributed
#vy = np.zeros(N)

# Result lists
ti=[]
pr=[]
prt=[]
nl=[]
nr=[]

# set up the figure and animation elements
fig = plt.figure(figsize=(10,10),dpi=80)
ax1 = plt.subplot(311,aspect='equal', autoscale_on=False, xlim=(0, L), ylim=(-1,1))
gas, = ax1.plot([], [], 'bo', ms=2)
ax2 = plt.subplot(312, autoscale_on=False, xlim=(0, 100), ylim=(0, 2*N*T/L))
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
    global x,vx,t,P,Pt,ti,pr,nl,nr,L,V, v0
    x += vx*dt 
    t += dt
    Pt = 0.0 # pressure at timestep t
    # collision with walls: reverse velocity and distance to wall
    nleft = 0
    nright = 0
    for i in range(N):
        if x[i] < 0.0:
            x[i] = -x[i]
            vx[i] = -vx[i] 
        if x[i] > L:
            x[i] = 2.0*L-x[i]
            vx[i] = -vx[i]
            Pt += 2.0*np.abs(vx[i])/dt # pressure at time t
            P += 2.0*np.abs(vx[i]) # sum of all pressure changes               
        if x[i]<L/2.0: nleft += 1
        if x[i]>L/2.0: nright += 1
    # calculate temperature from x-component of velocity: T/2=v**2/2 
    #v2=0.0
    #for i in range(N):
    #    v2 += vx[i]**2
    #T = v2/N
    ti.append(t)
    nl.append(nleft)
    nr.append(nright)
    prt.append(Pt) # pressure at time t
    pr.append(P/t) # time average of pressure

    L += v0
    V = L

    # set up the figure and animation elements
    fig = plt.figure(figsize=(10, 10), dpi=80)
    ax1 = plt.subplot(311, aspect='equal', autoscale_on=False, xlim=(0, L), ylim=(-1, 1))
    gas, = ax1.plot([], [], 'bo', ms=2)
    ax2 = plt.subplot(312, autoscale_on=False, xlim=(0, 100), ylim=(0, 2 * N * T / L))
    pressure, = ax2.plot([], [], lw=1, color='b')
    plt.xlabel('time t')
    plt.ylabel('pressure P')
    ax3 = plt.subplot(313, autoscale_on=False, xlim=(0, 100), ylim=(0, N))
    numleft, = ax3.plot([], [], lw=1, color='b')
    numright, = ax3.plot([], [], lw=1, color='r')
    plt.xlabel('time t')
    plt.ylabel('particle numbers on left and right side')
                    

# calculations
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
    #pressure.set_data(ti, prt) # pressure at time t
    numleft.set_data(ti, nl)
    numright.set_data(ti, nr)
    return gas,pressure,numleft,numright

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=600, interval=10, blit=True, repeat=True)

# save animation to file
#anim.save("animation.mp4", writer=animation.FFMpegWriter(fps=30))

plt.show()
