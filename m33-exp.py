import numpy as np
import math
import matplotlib.pyplot as plt

g=4.300917e-3
m3=3.2e9
m2=4.8e9
k=0.31
rm=8e3
vi=25
ri=1e3
vf=28
rf=50e3
l=100

mi=(vi**2)*k*ri/g
mf=(vf**2)*k*rf/g
voli=(4/3)*np.pi*ri**3
volf=(4/3)*np.pi*rf**3
s=rf*(np.log(mf*voli/(mi*volf)))/(rf-ri)

rtest=[1e3,3e3,5e3,8e3, 10e3, 20e3,30e3,40e3,50e3]
r=np.linspace(ri,rf,l)

d=(mi/voli)*np.exp(s*(r-ri)/rf)
mc=d*4*np.pi*r**2*(rf-ri)/l
m=np.cumsum(mc)

v=np.sqrt(g*m/(k*r))



#print("r=",r)
#print("v=",v)

plt.plot(r, v)
plt.title("Approximated classical m33 rotation curve")
plt.xlabel("Distance from galaxy center (Km)")
plt.ylabel("Velocity of star (Km/s)")
plt.show()
