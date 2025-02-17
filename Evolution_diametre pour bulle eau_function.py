import pandas as pd
import matplotlib.pyplot as plt
import math as m
import numpy as np

plt.close('all')

D = 1.68e-7
beta = 14.59

d = 0.0218
r = 0.5
angle = m.asin(d/r)
co = 2*m.pi/angle


def print_radius(filename, co, D, beta, color, name, plot_theory=0):
    data_simu = pd.read_csv(filename, sep = ",",header = 0, names = ["t", "r"])

    t = np.array(data_simu["t"]) #en s

    vs = np.array(data_simu["r"])
    rs = ((vs*co*3/4/m.pi)**(1/3)) #en mm

    rt = 2*beta * np.sqrt(D*t)
    #vt3 = 4/3*(rt3**3)*m.pi/co
    t = t*1000

    if plot_theory:
        plt.plot(t, rt * 1000, "green", label="Scriven theory")
    plt.plot(t, rs*1000, label = name, color=color)
    
    #plt.plot(t, (rs-rt)/rs, label = name, color = color)

    plt.legend()
    plt.xlabel("Time t [ms]")
    plt.xlim(0.05, 0.5)
    plt.ylabel("Radius r [mm]")
    #plt.title("Radius error for different mesh refinements")
    #plt.title("Radius error for different mesh refinements")
    plt.grid(False)
    plt.show()

print_radius("bubbleInfo2502507.csv", co, D, beta, "red", "2 µm", plot_theory=1)
#print_radius("bubbleInfo300300_7.csv", co, D, beta, "blue", "1.66 µm")
print_radius("bubbleInfo4004007.csv", co, D, beta, "orange", "1.25 µm")
print_radius("bubbleInfo5005007.csv", co, D, beta, "black", "1 µm")






