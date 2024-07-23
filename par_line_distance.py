import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

d1 = np.array([1, 1, 1])
d2 = np.array([0, 3, -1])

n = np.cross(d1, d2)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.quiver(0, 0, 0, d1[0], d1[1], d1[2], color='blue', label='d1')
ax.quiver(0, 0, 0, d2[0], d2[1], d2[2], color='red', label='d2')

ax.quiver(0, 0, 0, n[0], n[1], n[2], color='green', label='d1 x d2')

parallelogram = np.array([
    [0, 0, 0],
    d1,
    d1 + d2,
    d2,
    [0, 0, 0]
])

ax.plot(parallelogram[:, 0], parallelogram[:, 1], parallelogram[:, 2], color='purple', linestyle='dotted', label='Parallelogram')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

plt.show()

