import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as la #linear algebra
from sys import argv


sites=int(argv[2])
delta=float(argv[1])


a=1-delta
b=1+delta

Ham1=np.zeros([sites,sites])
Ham2=np.zeros([sites,sites])
Zeros=np.zeros([sites,sites])


#llenando matriz de estados propios
for i in range(sites):
    for j in range(sites):
        if(i==j):
            Ham1[i][j]=a
            Ham2[i][j]=a
        if(i==j-1):
            Ham2[i][j]=b
        if(i==j+1):
            Ham1[i][j]=b


#impossing boundary conditions :)
Ham1[0][-1]=b
Ham2[-1][0]=b


D=np.bmat([[Zeros,Ham1],[Ham2,Zeros]])
#print D


vp1,Vp1=la.eig(D)
vp2,Vp2=la.eig(D)

vp1.sort()
vp2.sort()

k=np.linspace(0,2*np.pi,len(vp1))


print len(k),len(vp1)

plt.xlim(0,2*np.pi)
plt.ylim(-2.1,2.1)
plt.scatter(k,vp1)
plt.scatter(k,-vp2)
plt.title("$ \mathrm{Closed\ boundary\ Blocks} $")
plt.xticks([0,np.pi/2,np.pi,np.pi*3/2,2*np.pi],["0","$ \pi/2 $","$ \pi $","$ 3\pi/2 $","$ 2\pi $"])
plt.xlabel("$ \\frac{2\pi k}{N} $",size=15)
plt.ylabel("$ E $", size=15)
plt.savefig("closed_b.png")
plt.show()






