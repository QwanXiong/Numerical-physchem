##
##      MonteCarlo1.png and MonteCarloMA.png
##
##

import numpy as np
import matplotlib.pyplot as plt
import math

def f(x):
    return np.exp(-x*x)
    #return 1/x
    #return np.sin(x)**2
    #return np.exp(-np.sin(x))


def MCint(N):
    X=np.random.rand(1,round(N))*2.0
    Y = f(X)
    return 2.0*np.sum(Y)/N

b = 2.0
ex= math.erf(b)/2.0*math.sqrt(math.pi)
#ex = np.log(3)

NN = 10**(np.linspace(1,3,10000))
MCint_arr = np.abs((np.array([MCint(x) for x in NN]) -ex)/ex)

mean_range = 500

Mean = np.array([np.sum(MCint_arr[0:(0+mean_range)])/mean_range])
for val in range(1,MCint_arr.size-mean_range):
    Mean = np.append(Mean,np.sum(MCint_arr[val:(val+mean_range)])/mean_range)


#print(Mean)

#plt.plot(NN[::50],MCint_arr[::50],c='r',label=r"Monte-Carlo")
plt.plot(NN[0:(NN.size-mean_range)],Mean,c='b',label=r"Monte-Carlo MA")

plt.xlabel("Number of points")
plt.ylabel("Relative error of integration")
plt.title(r"$y=e^{-x^2},\; x=0..2$")
#print(booleint)
plt.legend()
plt.show()
