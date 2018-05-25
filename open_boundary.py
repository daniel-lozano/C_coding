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
        if(i+1<2*sites):
            Ham1[i][(i+1)]=a
            Ham2[i][(i+1)]=b
        if(i-1>=0):
            Ham1[i][(i-1)]=b
            Ham2[i][(i-1)]=a
    else:
        
        if(i+1<2*sites):
            Ham1[i][(i+1)%(2*sites)]=b
            Ham2[i][(i+1)%(2*sites)]=a
        if(i-1>=0):
            Ham1[i][(i-1)%(2*sites)]=a
            Ham2[i][(i-1)%(2*sites)]=b


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
plt.show()






