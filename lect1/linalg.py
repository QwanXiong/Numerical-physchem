import numpy as np
import matplotlib.pyplot as plt


def fun(N):
    if N < 0:
        return 0.0
    else:
        acc = 0
        for i in range(N,-1,-1):
            #print(i)
            acc += i**2
        return acc


print("[1,2]+[3,4] = ",[1,2]+[3,4])
print("[1,2] * 2 = ",[1,2]*2)
A = [i for i in range(10)]
print("A = [i for i in range(10)] = \n", A)
print("A[4] = ", A[4])
print("A[-1] = ", A[-1])
print("A[1:-1:2] = ", A[1:-1:2])
"""
Creating arrays
"""
print("\n\nCreation")
X = np.array([1,2,3])
X = np.array([[1,2],[3,4]])
print("array([[1,2],[3,4]]) = \n",X)

X = np.full((3,3),2.3)
print("\nfull((3,3),2.3) = \n",X)
X = np.zeros((3,3))
X = np.ones((3,3))
X = np.eye(3)
X = np.arange(9).reshape((3,3))
print("\narange(9).reshape((3,3)) = \n",X)

X = np.linspace(1,2,11)
print("\nlinspace(1,2,11) = \n",X)
X = np.arange(1,2,0.1)
print("\narange(1,2,0.1) = \n",X)

"""
Slicing and indexing
"""
print("\nSlicing and indexing")
Y = np.arange(1,10).reshape((3,3))
print(Y)
print("\nY[1:,1:] = \n",Y[1:,1:])
print("\nY[[1,2],[1,2]]] = \n",Y[[1,2],[1,2]])
print("\nY[np.ix_([1,2],[1,2])] = \n",Y[np.ix_([1,2],[1,2])])


print("\nY and Y[1:,1:] shares memory? ",np.shares_memory(Y,Y[1:,1:]))
print("Y and Y[np.ix_([1,2],[1,2])] shares memory? ",np.shares_memory(Y,Y[np.ix_([1,2],[1,2])]))

print("\nY < 5.0\n", Y < 5.0 )
print("\nY[Y < 5.0]\n", Y[Y < 5.0] )


"""
Matrix operations
"""
Z = np.random.randint(1,100,size=(3,3))
print("\nZ = \n",Z)
print("\nZ^{T} = \n", Z.T)
print("\ndet(Z) = ",np.linalg.det(Z))
Zinv = np.linalg.inv(Z)
print("\nZ^{-1} = \n", Zinv)
print("\nZ@Zinv = \n",Z@Zinv)
print("np.matmul(Z,Zinv) = \n",np.matmul(Z,Zinv))
print("Z.dot(Zinv) = \n",Z.dot(Zinv))



Zs = Z+Z.T
print("\nZs = Z + Z^{T}\n",Zs)
V,W = np.linalg.eigh(Zs)
print("\nEigenvalues of Zs: \n",V)
print("\nW^{T}*Zs*W = \n",W.T@Zs@W)

print("\nZ.max(axis=1) ",Z.max(axis=1))
print("Z.max(axis=0) ",Z.max(axis=0))
print("Z.sum(axis=1) ",Z.sum(axis=1))

print("W^{T} = \n",W.T)
print("W^{-1} = \n",np.linalg.inv(W))
