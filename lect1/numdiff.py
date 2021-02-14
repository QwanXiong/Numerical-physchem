import numpy as np
import matplotlib.pyplot as plt
import math

def f(x):
    return np.exp(x)

def fpr(x):
    return np.exp(x)

def d3(x,h):
    return (-f(x-h)+f(x+h))/2.0/h

def d5(x,h):
    return (f(x-2*h)-8.0*f(x-h)+8.0*f(x+h)-f(x+2*h))/12.0/h

def d7(x,h):
    return (-f(x-3*h)+9.0*f(x-2*h)-45.0*f(x-h)+45.0*f(x+h)-9.0*f(x+2*h)+f(x+3*h))/60.0/h

xx = 10**(np.linspace(-10,0,100))
xv = 2.0
yy3 = np.abs((d3(xv,xx)-fpr(xv))/fpr(xv))
yy5 = np.abs((d5(xv,xx)-fpr(xv))/fpr(xv))
yy7 = np.abs((d7(xv,xx)-fpr(xv))/fpr(xv))

#print(xx)
plt.loglog(xx,yy3,c='r',label=r"$n=3$")
plt.loglog(xx,yy5,c='b',label=r"$n=5$")
plt.loglog(xx,yy7,c='g',label=r"$n=7$")
plt.xlabel("Step size")
plt.ylabel("Relative error of differentiation")

plt.legend()
plt.show()
