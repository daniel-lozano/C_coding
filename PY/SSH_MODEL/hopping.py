import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as la #linear algebra
from sys import argv


sites=40
T=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
Delta=0.5
LABELS=[]

Difference=[]

for i in range(len(T)):
    LABELS.append(" "+ str(T[i]) +" ")

for l in range(len(T)):
    t=T[l]
    a=1-Delta
    b=1+Delta

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


    D=np.bmat([[Zeros,Ham1+np.diag(np.ones(sites-1)*t,-1)+np.diag(np.ones(sites-1)*t,+1)],[Ham2,Zeros]])



    vp1,Vp1=la.eig(D)
    print len(vp1)
    Difference.append(abs(vp1[39]-vp1[38]))
    print vp1[39],vp1[38]
    print Difference[-1]


    k=np.ones(len(vp1))*T[l]
    plt.plot(k,vp1,"_")






plt.ylim(-2.1,2.1)
plt.title("$ \mathrm{Open\ boundary\ Blocks} $")
plt.xticks(T,LABELS)
plt.xlabel("$ t $",size=15)
plt.ylabel("$ E $", size=15)
plt.savefig("open_b.png")
plt.show()




