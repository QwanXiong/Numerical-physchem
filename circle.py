import numpy as np
import matplotlib.pyplot as plt



N = 2000
X=np.random.rand(1,N)*2.0-1.0
Y = np.random.rand(1,N)*2.0-1.0
M= (X*X + Y*Y < 0.5)


ax = plt.subplot(111)
box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.9])
ax.scatter(X[~M] ,Y[~M], c='b', marker="P",label=r"$x^2 + y^2 > 0.5$")
ax.scatter(X[M] ,Y[M], c='r', marker="P",label=r"$x^2 + y^2 < 0.5$")
plt.xlabel("X-axis label")
plt.ylabel("Y-axis label")
plt.title(r"Circle ")

ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.12),
          fancybox=True, shadow=True, ncol=5)
plt.show()
