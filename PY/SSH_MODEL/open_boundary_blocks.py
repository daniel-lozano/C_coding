import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as la #linear algebra
from sys import argv


sites=40
Delta=[0]
for i in range(11):
    Delta.append(i*1.0/10)
    Delta.append(-i*1.0/10)

LABELS=[]

Difference=[]
plt.figure(figsize=(10,7))
for i in range(len(Delta)):
    LABELS.append(" "+ str(Delta[i]) +" ")

for l in range(len(Delta)):

    a=1-Delta[l]
    b=1+Delta[l]

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
    #print len(vp1)
    Difference.append(abs(vp1[39]-vp1[38]))
    #print vp1[39],vp1[38]
    #print Difference[-1]


    k=np.ones(len(vp1))*Delta[l]
    plt.plot(k,vp1,"_")




#plt.xticks(rotation=90)

plt.xlim(-1.1,1.1)
plt.ylim(-2.1,2.1)
plt.title("$ \mathrm{Open\ boundary\ Blocks} $")
plt.xticks(Delta,LABELS)
plt.xlabel("$ \delta $",size=15)
plt.ylabel("$ E $", size=15)
plt.savefig("open_b.png")
plt.show()




