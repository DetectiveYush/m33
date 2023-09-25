import numpy as np
import math
import matplotlib.pyplot as plt

g=4.300917e-3
m2=1e10
k=1
rm=10e3
v1=50
r1=1e3
m3=5e10

m1=(v1**2)*k*rm/g
m=m2
#print (m1)
vol=(4/3)*math.pi*(rm**3)
d=m/vol
dd=(m3-m)/vol

v=[]
vd=[]
rtest=[1e3,3e3,5e3,8e3, 10e3, 20e3,30e3,40e3,50e3]
r=np.linspace(1e3,50e3,100)


for i in r:
    if i<=rm:
        mi=(4/3)*math.pi*(i**3)*d
    else:
        mi=m
    md=(4/3)*math.pi*(i**3)*dd
    #print("r=",i,",m=",mi)
    vi=math.sqrt(g*(mi)/(k*i))
    v.append(vi)
    vdi=math.sqrt((vi**2)+(g*md/i))
    vd.append(vdi)


#print("r=",r)
#print("v=",v)

#Now we'll model with Dark matter (constant density)

#vd=math.sqrt((v**2)+(gm3/r))

plt.plot(r, v)
plt.title("Approximated classical m33 rotation curve")
plt.xlabel("Distance from galaxy center (ly)")
plt.ylabel("Velocity of star (Km/s)")
plt.savefig("rotation_curve.png")
#plt.show()

plt.plot(r, vd)
plt.title("Approximated m33 rotation curve with Dark matter")
plt.xlabel("Distance from galaxy center (ly)")
plt.ylabel("Velocity of star (Km/s)")
plt.savefig("rotation_curve_dark_matter.png")
plt.show()


