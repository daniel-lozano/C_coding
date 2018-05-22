import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as la #linear algebra
from sys import argv


sites=int(argv[2])
delta=float(argv[1])


a=1-delta
b=1+delta

Ham1=np.zeros([2*sites,2*sites])
Ham2=np.zeros([2*sites,2*sites])
DIAG=np.diag(np.ones(sites))


#llenando matriz de estados propios
for i in range(2*sites):
    
    if(i%2==0):
        Ham1[i][(i+1)%(2*sites)]=a
        Ham1[i][(i-1)%(2*sites)]=b
        Ham2[i][(i+1)%(2*sites)]=b
        Ham2[i][(i-1)%(2*sites)]=a
    else:
        Ham1[i][(i-1)%(2*sites)]=a
        Ham1[i][(i+1)%(2*sites)]=b
        Ham2[i][(i-1)%(2*sites)]=b
        Ham2[i][(i+1)%(2*sites)]=a

vp1,Vp1=la.eig(Ham1)
vp2,Vp2=la.eig(Ham2)

vp1.sort()
vp2.sort()

k=np.linspace(0,2*np.pi,len(vp1))


print len(k),len(vp1)

plt.xlim(0,2*np.pi)
plt.ylim(-2.1,2.1)
plt.scatter(k,vp1)
plt.scatter(k,-vp2)
plt.title("$ \mathrm{Closed\ boundary} $")
plt.xticks([0,np.pi/2,np.pi,np.pi*3/2,2*np.pi],["0","$ \pi/2 $","$ \pi $","$ 3\pi/2 $","$ 2\pi $"])
plt.xlabel("$ \\frac{2\pi k}{N} $",size=15)
plt.ylabel("$ E $", size=15)
plt.savefig("closed.png")
plt.show()






