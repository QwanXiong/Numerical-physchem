import numpy as np
import matplotlib.pyplot as plt
import math

def f(x):
    #return np.exp(-x*x)
    return 1/x
    #return np.exp(-np.sin(x))

def Im0(N,m,a,b):

    Nnew = (N-1)*2**m+1
    h = (b-a)/(Nnew-1)
    xx = np.linspace(a,b,Nnew)
    yy = f(xx)
    yy[0] *= 0.5
    yy[-1] *= 0.5
    return np.sum(yy)*h


N = 2

a =1
b = 3


ex = math.log(b) - math.log(a)

Imn = np.zeros((6,5))
for i in range(5):
    Imn[i,0] = Im0(N,i,a,b)
for j in range(1,5):
    for i in range(j,5):
        Imn[i,j] = (4**j*Imn[i,j-1] - Imn[i-1,j-1])/(4**j-1)
for j in range(5):
    Imn[5,j] = (ex-Imn[4,j])/ex

#print(Imn)
for i in range(6):
    for j in range(5):
        if (i == 5):
            print('{:12.3e}'.format(Imn[i,j]),end=' ')
        else:
            print('{:8.6e}'.format(Imn[i,j]),end=' ')
    print('\n')

fil = open('table.txt', 'w')
for i in range(6):
    for j in range(5):
        if (i == 5):
            fil.write('{:12.3e} & '.format(Imn[i,j]) )
        else:
            fil.write('{:8.6e} & '.format(Imn[i,j]) )
    fil.write('\\\\ \n')
fil.close()
print(ex)
