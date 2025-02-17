import matplotlib.pyplot as plt
import math as m
import numpy as np

plt.close('all')

d = 0.002
r = 0.1  #lenght of the domaine
angle = m.asin(d/r)   #angle of axisymmetry
co = 2*m.pi/angle/10 #to get the entire volume


dT = [1.5, 2, 2.5, 3]
time = [0.225, 0.241, 0.410, 0.905]
volume = np.array([2.87e-14, 4.02e-14,5.97e-14, 8e-14])
radius = ((volume*co*3/4/m.pi)**(1/3))

sigma = [10, 20, 30, 40]
t = [0.275, 0.40,0.410, 0.945]
v = np.array([5.77e-14, 5.9e-14, 5.97e-14, 9e-14])
r = ((v*co*3/4/m.pi)**(1/3))


# Plot each on a different graph
fig1, axs1 = plt.subplots(1,2, figsize=(10, 10))

# First graph
axs1[0].plot(dT, time, marker='o')
axs1[0].set_xlabel("Superheat [K]")
axs1[0].set_ylabel("Detachment time [ms]")
axs1[0].set_title("Detachment time vs Superheat")

# Second graph
axs1[1].plot(dT, radius, marker='o', color='green')
axs1[1].set_xlabel("Superheat [K]")
axs1[1].set_ylabel("Bubble radius [m]")
axs1[1].set_title("Bubble radius vs Superheat ")


# Plot each on a different graph
fig2, axs2 = plt.subplots(1,2, figsize=(10, 10))
# Third graph
axs2[0].plot(sigma, t, marker='o', color='orange')
axs2[0].set_xlabel("Contact angle")
axs2[0].set_ylabel("Detachment time [ms]")
axs2[0].set_title("Detachment time vs Contact angle")

# Fourth graph
axs2[1].plot(sigma, r, marker='o', color='red')
axs2[1].set_xlabel("Contact angle")
axs2[1].set_ylabel("Bubble radius [m]")
axs2[1].set_title("Bubble radius vs Contact angle")

# Adjust layout
plt.tight_layout()
plt.show()