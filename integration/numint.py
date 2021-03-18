##
##   expx2_interval.png
##
##


import numpy as np
import matplotlib.pyplot as plt
import math

def f(x):
    return np.exp(-x*x)
    #return np.sin(x)**2
    #return np.exp(-np.sin(x))

def trap(h,a,b):
    N = round((b-a)/h)
    hnew = (b-a)/(N-1)
#    print(N)
    xx = np.linspace(a,b,N)
    yy = f(xx)
    yy[0] *= 0.5
    yy[-1] *= 0.5
#    print("x",xx[-1])
    return np.sum(yy)*hnew

def simp(h,a,b):
    N = round((b-a)/2/h)*2+1
    hnew = (b-a)/(N-1)
#    print("N",N)
    xx = np.linspace(a,b,N)
    yy = f(xx)/3.0
    yy[1:-1:2] *= 4.0
    yy[2:-1:2] *= 2.0
#    print(yy)
    return np.sum(yy)*hnew

def boole(h,a,b):
    N = round((b-a)/4/h)*4+1
    hnew = (b-a)/(N-1)
#    print(N)
    xx = np.linspace(a,b,N)
    yy = f(xx)*2.0/45.0
    #yy = np.ones(N)
    yy[0] *= 7.0
    yy[-1] *= 7.0
    yy[1:-1:2] *= 32.0
    yy[2:-1:4] *= 12.0
    yy[4:-1:4] *= 14.0
#    print(yy)
    return np.sum(yy)*hnew

a = 0.0
b = 2.5
ex = math.erf(b)/2.0*math.sqrt(math.pi)-math.erf(a)/2.0*math.sqrt(math.pi)

#ex = 7.95492652101284527451321966532
hh = 10**(np.linspace(-4,-1,100))
trapint = np.abs((np.array([trap(x,a,b) for x in hh]) -ex)/ex)
simpint = np.abs((np.array([simp(x,a,b) for x in hh]) -ex)/ex)
booleint = np.abs((np.array([boole(x,a,b) for x in hh])-ex)/ex)

# trapint = np.abs((np.array([trap(x,a,b) for x in hh])))
# simpint = np.abs((np.array([simp(x,a,b) for x in hh]) ))
# booleint = np.abs((np.array([boole(x,a,b) for x in hh])))
#yy_trap = np.abs((trap(hh,a,b)-ex)/ex)
#print(trapint)
#print(simp(0.00359381,0,3))

#plt.semilogx(hh,trapint,c='r',label=r"Trapezoid")
plt.loglog(hh,trapint,c='r',label=r"Trapezoid")
plt.loglog(hh,simpint,c='b',label=r"Simpson's")
plt.loglog(hh,booleint,c='g',label=r"Boole's")
plt.xlabel("Step size")
plt.ylabel("Relative error of integration")
plt.title(r"$y=e^{-x^2},\; x=0..2.5$")
#print(booleint)
plt.legend()
plt.show()
