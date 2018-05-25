import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as la #linear algebra
from sys import argv

sx=[[0,1],[1,0]]
sy=[[0,-1j],[1j,0]]
sz=[[1,0],[0,-1]]

print np.shape(sx), np.shape(sy), np.shape(sz)

xx=np.kron(sx,sx)
yy=np.kron(sy,sy)
zz=np.kron(sz,sz)



D=5.5 #Parametro
N=int(argv[1])
PBC=0
dim=2**N

Case_pbc=np.kron(sx,np.kron(np.eye(2**(N-2)),sx))+np.kron(sy,np.kron(np.eye(2**(N-2)),sy))+np.kron(sz,np.kron(np.eye(2**(N-2)),sz))


Ham=np.zeros((dim,dim))+PBC*Case_pbc
np.shape(Ham)

for i in range(N-1):
	
	Id1=np.eye(int(2**(i)))
	Id2=np.eye(int(2**(N-2-i)))
	Ham+=np.kron(Id1,np.kron(xx,Id2))+np.kron(Id1,np.kron(yy,Id2))+D*np.kron(Id1,np.kron(zz,Id2))
	


w,v=la.eig(Ham)
dot=np.linspace(1,len(w),len(w))
w.sort()
print len(w)

for i in range(len(w)):
	print w[i]



