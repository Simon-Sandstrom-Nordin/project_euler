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
L = 10.0/10 # length of container
V = L # volume = length of container for d=1
N = 100000 # number of particles
T = 1.0 # initial temperature
dt = 0.1 # time step
t = 0.0 # initial time
# v0 = np.sqrt(T)
v0 = np.sqrt(T)/10
# v0 = .5
T0 = T

# initial state
x = L*np.random.random(N)/L # initial random positions, distributed uniformly in container
y = np.zeros(N)
vx = np.sqrt(T)*np.random.randn(N) # initial random velocities, Maxwell distributed
#vy = np.zeros(N)

# Result lists
ti=[]
pr=[]
prt=[]
nl=[]
nr=[]
time_list = []
kinetic_energy_list = []


# set up the figure and animation elements
fig = plt.figure(figsize=(10,10),dpi=80)
ax1 = plt.subplot(311,aspect='equal', autoscale_on=False, xlim=(0, L*10), ylim=(-1,1))
gas, = ax1.plot([], [], 'bo', ms=2)
lines, = ax1.plot([],[], 'r-', lw=2)
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
    global x,vx,t,P,Pt,ti,pr,nl,nr,L,T,time_list,kinetic_energy_list, plt
    x += vx*dt 
    t += dt
    Pt = 0.0 # pressure at timestep t
    # collision with walls: reverse velocity and distance to wall
    nleft = 0
    nright = 0
    for i in range(N) :
        if x[i] < 0.0 : 
            x[i] = -x[i]
            vx[i] = -vx[i] 
        if x[i] > L :  
            x[i] = 2.0*L-x[i]
            vx[i] = 2*v0-vx[i]
            Pt += 2.0*np.abs(vx[i]-v0)/dt # pressure at time t
            P += 2.0*np.abs(vx[i]-v0) # sum of all pressure changes
        if x[i]<L/2.0 : nleft += 1
        if x[i]>L/2.0 : nright += 1
    # calculate temperature from x-component of velocity: T/2=v**2/2 
    v2=0.0
    for i in range(N) :
        v2 += vx[i]**2
    T = v2/N
    ti.append(t)
    nl.append(nleft)
    nr.append(nright)
    prt.append(Pt) # pressure at time t
    pr.append(P/t) # time average of pressure
    L += v0*dt
    time_list.append(t)

    KE = 0  # kinetic energy
    for i in range(N):
        KE += (1/2) * vx[i]**2

    kinetic_energy_list.append(KE)
    if L > 10:
        plt.close()



# calculations
#for i in range(1000) : step()
#print P
                                                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
# initialization
def init():
    gas.set_data([], [])
    lines.set_data([], [])
    pressure.set_data([], [])
    numleft.set_data([], [])
    numright.set_data([], [])
    return gas,pressure,numleft,numright

# animation function
def animate(i):
    global L
    step()
    gas.set_data(x, y)
    lines.set_data(L, [-1,1])
    pressure.set_data(ti, pr) # time average of pressure
    #pressure.set_data(ti, prt) # pressure at time t
    numleft.set_data(ti, nl)
    numright.set_data(ti, nr)
    return gas, lines,pressure,numleft,numright

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=600, interval=10, blit=True, repeat=True)

# save animation to file
#anim.save("animation.mp4", writer=animation.FFMpegWriter(fps=30))

plt.show()

#print("T =", T)
#print("P/t =", P/t)
#print("V =", V)
#print("N =", N)

#print("alternative form of the ideal gas law,"
#      "pV = NkT, where N is the number of molecules\n"
#      "and k is Boltzman's constant, is used. "
#      "Units have been chosen such that k = 1.")
#plt.plot(time_list, law_list, 'r')
#plt.title("PV - NkT over time")
#plt.ylabel("PV - NkT")
#plt.xlabel("Time [s]")
#plt.show()
#print(dt*100*v0)


plt.plot(time_list, kinetic_energy_list, 'r')
plt.title("Kinetic energy over time, v0 = sqrt(T)/10")
plt.ylabel("Kinetic energy [J]")
plt.xlabel("Time [s]")
plt.show()
print("Difference in kinetic energy from beginning to end of expansion:")
print(kinetic_energy_list[-1] - kinetic_energy_list[0], "Joule")
