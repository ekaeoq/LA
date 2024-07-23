import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

a1 = np.array([1, 2, 0])
d1 = np.array([1, 1, 1])
a2 = np.array([2, 3, 1])
d2 = np.array([0, 3, -1])

t_values = np.linspace(-5, 5, 100)
line1_points = a1[:, np.newaxis] + t_values * d1[:, np.newaxis]
line2_points = a2[:, np.newaxis] + t_values * d2[:, np.newaxis]

normal_vector = np.cross(d1, d2)
normal_vector = normal_vector / np.linalg.norm(normal_vector)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(line1_points[0], line1_points[1], line1_points[2], label='Line 1')
ax.plot(line2_points[0], line2_points[1], line2_points[2], label='Line 2')

intersection_point = np.array([2, 3, 1])
ax.scatter(*intersection_point, color='red', label='Intersection Point')

normal_origin = intersection_point - 5 * normal_vector
normal_end = intersection_point + 5 * normal_vector
ax.quiver(*normal_origin, *(normal_end - normal_origin), color='green', label='Normal Vector', length=5)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

plt.show()

