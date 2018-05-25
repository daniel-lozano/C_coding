import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as la #linear algebra
from sys import argv


Sites=[10,15,20,25,30,35,40,45,50]
Delta=0.1
LABELS=[]

Difference=[]

for i in range(len(Sites)):
    LABELS.append(" "+ str(Sites[i]) +" ")

for l in range(len(Sites)):

    a=1-Delta
    b=1+Delta
    sites=Sites[l]
    print sites
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


    D=np.bmat([[Zeros,Ham1],[Ham2,Zeros]])



    vp1,Vp1=la.eig(D)
    vp1.sort()
    print vp1[len(vp1)/2], vp1[len(vp1)/2-1]
    Difference.append( vp1[len(vp1)/2]-vp1[len(vp1)/2-1])
    print Difference[-1]


plt.semilogy(Sites,Difference,"o-")
#plt.xticks(Sites,LABELS)
plt.show()




