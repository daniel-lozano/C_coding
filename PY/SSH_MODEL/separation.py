import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as la #linear algebra
from sys import argv


Sites=[10,15,20,25,30,35,40,45,50]

Delta=[0,0.1,0.2,0.3,0.4,0.5]
LABELS=[]




for i in range(len(Sites)):
    LABELS.append(" "+ str(Sites[i]) +" ")

for m in range(len(Delta)):
    Difference=[]
    for l in range(len(Sites)):

        a=1-Delta[m]
        b=1+Delta[m]
        sites=Sites[l]
        
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
        #    print vp1[len(vp1)/2], vp1[len(vp1)/2-1]
        Difference.append( vp1[len(vp1)/2]-vp1[len(vp1)/2-1])
        #    print Difference[-1]


    plt.semilogy(Sites,Difference,"o-",label="$ \delta= $"+str(Delta[m]))
#plt.xticks(Sites,LABELS)
plt.legend()
plt.show()




