import numpy as np
import matplotlib.pyplot as plt
import math

fig=plt.figure()
X=np.linspace(-4,4,180)
plt.scatter(X ,[np.sin(x) for x in X], c='r', marker="P",label=r"$y=\sin x$" )
plt.plot(X,[np.cos(x*x) for x in X], c='g', linewidth=4.0, label=r"$y=\cos(x^2)$")
plt.xlim(-4.5,4.5)
plt.ylim(-1.5,1.5)
plt.xlabel("X-axis label")
plt.ylabel("Y-axis label")
plt.title(r"Some random plot ")
plt.legend()
plt.show()
