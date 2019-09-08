import numpy as np
import matplotlib.pyplot as plt

points = np.array([(1,1), (2,4), (3,1), (4,2), (5,6), (6,3), (7,1), (8,5), (9,3)])

# get x and y vectors
x = points[:,0]
y = points[:,1]

# calculate polynomial
#z = np.polyfit(x, y, 3)    # 3 = 3rd degree polynomial fit (1 = best-fit straight line)
z = np.polyfit(x, y, 1)
#z[0] = 0.5
#z[1] = 4.0
f = np.poly1d(z)

# calculate new x's and y's
x_new = np.linspace(x[0], x[-1], 50)
y_new = f(x_new)

plt.plot(x,y,'o', x_new, y_new)
plt.xlim([x[0]-1, x[-1] + 1 ])
plt.show()
