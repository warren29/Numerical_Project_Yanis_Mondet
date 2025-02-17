import pandas as pd
import matplotlib.pyplot as plt
import math as m
import numpy as np

plt.close('all')


d = 0.002 
r = 0.2  #lenght of the domaine
angle = m.asin(d/r)   #angle of axisymmetry
co = 2*m.pi/angle/10 #to get the entire volume

def BL_therm(R, dT, rhol, Cpl, rhov, h):
    Ja = dT* rhol * Cpl / (rhov*h)
    beta = Ja * m.sqrt(3/m.pi)
    #print(beta)
    delta_th = R/beta
    return delta_th, beta

D = 0.104/(1377.5*1280) #R134a
beta = BL_therm(50e-6, 2.5, 1377.5, 1280, 5.19, 144350)[1] #for R and dT

def print_radius(filename, co, D, beta, plot_theory, name, color):
    data_simu = pd.read_csv(filename, sep = ",",header = 0, names = ["t", "r"])

    t = np.array(data_simu["t"]) #en s

    vs = np.array(data_simu["r"])
    rs = ((vs*co*3/4/m.pi)**(1/3)) #en mm

    rt = 2*beta * np.sqrt(D*(t))
    ti = (0.00005 / (2*beta))**2/D
    print(ti)
    #vt3 = 4/3*(rt3**3)*m.pi/co
    t = t*1000

    if plot_theory:
        plt.plot(t-ti*1000, rt * 1000, "green", label="Scriven theory")
    plt.plot(t-ti*1000, rs*1000, label = name, color = color)
    
    #plt.plot(t, (rs-rt)/rs, label = name, color = color)

    plt.legend()
    plt.xlabel("Time t [ms]")
    #plt.xlim(0.05, 0.5)
    plt.ylabel("Radius r [mm]")
    #plt.title("Radius error for different mesh refinements")
    #plt.title("Radius error for different mesh refinements")
    plt.grid(False)
    plt.show()

    


print(BL_therm(50e-6, 2.5, 1377.5, 1280, 5.19, 144350))

print_radius("bubbleInfoR134a1microMULES.csv", co, D, beta, plot_theory=1, name="Surface tension with MULES", color = 'orange')
print_radius("bubbleInfoR134a1microMULESwithouttension.csv", co, D, beta, plot_theory=0, name= "No surface tension with MULES", color = 'blue')
print_radius("bubbleInfoR134a1microIsoAdvectionWithoutTension.csv", co, D, beta, plot_theory=0, name= "No surface tension with IsoAdvection", color = "red")

