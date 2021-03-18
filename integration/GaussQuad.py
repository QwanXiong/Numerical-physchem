import numpy as np
import matplotlib.pyplot as plt
import math

def f(x):
    return np.exp(-x*x)

N = 3

a = lambda j: (2*j-1)/j
b = lambda j: 0
c = lambda j:(j-1)/j

alpha = lambda j: -b(j)/a(j)
beta = lambda j: math.sqrt(c(j+1)/a(j)/a(j+1));

J = np.zeros((N,N))
J[0,0] = alpha(1)
J[0,1] = beta(1)
J[N-1,N-1] = alpha(N)
J[N-1,N-2] = beta(N-1)

for j in range(2,N):
    J[j-1,j-2] = beta(j-1);
    J[j-1,j-1] = alpha(j);
    J[j-1,j] = beta(j);

#print(J)

V,Vec = np.linalg.eigh(J)
W = 2.0*Vec[0,:]**2
#print(W@f(V))
print('k           exact         gaussian quadrature ' )
for k in range(1,2*N+1):
    fun = lambda x:(x-1)**k
    print('{0:} {1:20.13f} {2:20.13f} '.format(k, W@fun(V), (-1)**k*2**(k+1)/(k+1)))

print(J)
