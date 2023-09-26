import numpy as np
import math
import matplotlib.pyplot as plt

g=4.300917e-3
massdarkmatter=4e10
massobservabel=1e10
radiusinitial=1e3
radiusfinal=50e3
samplingfrequency=1e3

radius=np.linspace(radius-initial ,radius-final,sampling-frquency)

d=(mi/voli)*np.exp(-s*(r-rm))
mc=d*4*np.pi*(r**2)*(rf-ri)/l
m=np.cumsum(mc)

v=np.sqrt(g*m/(k*r))



#print("r=",r)
#print("v=",v)

plt.plot(r, v)
plt.title("Approximated classical m33 rotation curve")
plt.xlabel("Distance from galaxy center (Km)")
plt.ylabel("Velocity of star (Km/s)")
plt.show()
