##
##      MC_conv_N.png and MC_conv_sqrtN.png
##
##

import numpy as np
import matplotlib.pyplot as plt
import math

rng = np.random.default_rng(2602)

def f(x):
    return (1-x**2)*np.exp(-x*x)
    #return 1/x
    #return np.sin(x)**2
    #return np.exp(-np.sin(x))
def fnu(x):
    return f(x)/np.exp(-x*x)


def MCint(N):
    X=rng.random(round(N))*10.0-5.0
    #X = rng.normal(0,1/math.sqrt(2),round(N))
    Y = f(X)
    return 10.0*np.sum(Y)/N

def MCint_NU(N):
#    X=rng.random(round(N))*2.0
    X = rng.normal(0,1/math.sqrt(2),round(N))
    Y = fnu(X)
    return math.sqrt(math.pi)*np.sum(Y)/N

#b = 2.0
#ex= math.erf(b)/2.0*math.sqrt(math.pi)
#ex = -math.exp(-4) +math.sqrt(math.pi)/4*math.erf(2)
ex = math.sqrt(math.pi)/2.0

NN = 10**(np.linspace(2,4,10000))
MCint_arr_NU = np.abs((np.array([MCint_NU(x) for x in NN]) -ex)/ex)
MCint_arr = np.abs((np.array([MCint(x) for x in NN]) -ex)/ex)

mean_range = 500

Mean_NU = np.array([np.sum(MCint_arr_NU[0:(0+mean_range)])/mean_range])
for val in range(1,MCint_arr_NU.size-mean_range):
    Mean_NU = np.append(Mean_NU,np.sum(MCint_arr_NU[val:(val+mean_range)])/mean_range)

Mean = np.array([np.sum(MCint_arr[0:(0+mean_range)])/mean_range])
for val in range(1,MCint_arr.size-mean_range):
    Mean = np.append(Mean,np.sum(MCint_arr[val:(val+mean_range)])/mean_range)


#print(Mean)

#plt.plot(NN[::50],MCint_arr[::50],c='r',label=r"Monte-Carlo")
plt.plot(NN[0:(NN.size-mean_range)],Mean_NU,c='b',label=r"Normal distribution")
plt.plot(NN[0:(NN.size-mean_range)],Mean,c='r',label=r"Uniform distribution")

#plt.plot(1/np.sqrt(NN[0:(NN.size-mean_range)]),Mean_NU,c='b',label=r"Normal distribution")
#plt.plot(1/np.sqrt(NN[0:(NN.size-mean_range)]),Mean,c='r',label=r"Uniform distribution")

plt.xlabel(r"$N$")
plt.ylabel("Relative error of integration")
plt.title(r"$y=(1-x^2)e^{-x^2},\; x=-\infty..+\infty$")
#print(booleint)
plt.legend()
plt.show()
