import numpy as np
import math
import matplotlib.pyplot as plt

g=4.300917e-3
m3=0.8e8
m2=1e9
k=1
rm=8e3
v1=25
r1=1e3


m1=(v1**2)*k*rm/g
m=m2

vol=(4/3)*math.pi*(rm**3)
d=m/vol

v=[]
rtest=[1e3,3e3,5e3,8e3, 10e3, 20e3,30e3,40e3,50e3]
r=np.linspace(1e3,50e3,100)


for i in r:
    if i<=8e3:
        mi=(4/3)*math.pi*(i**3)*d
    else:
        mi=m1
    #print("r=",i,",m=",mi)
    vi=math.sqrt(g*(mi)/(k*i))
    v.append(vi)


#print("r=",r)
#print("v=",v)

plt.plot(r, v)
plt.title("Approximated classical m33 rotation curve")
plt.xlabel("Distance from galaxy center (ly)")
plt.ylabel("Velocity of star (Km/s)")
plt.show()
