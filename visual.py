import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_vectors(vectors, colors, labels, title):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    for vector, color, label in zip(vectors, colors, labels):
        ax.quiver(0, 0, 0, vector[0], vector[1], vector[2], color=color, label=label, arrow_length_ratio=0.1)
    
    max_val = np.max(np.abs(vectors)) + 1
    ax.set_xlim([-max_val, max_val])
    ax.set_ylim([-max_val, max_val])
    ax.set_zlim([-max_val, max_val])
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    ax.set_title(title)
    
    ax.legend()
    plt.show()

def main():
    A = np.array([2, 1, -1])
    B = np.array([3, -1, 4])
    
    C = np.cross(A, B)
    
    vectors = [A, B, C]
    colors = ['r', 'b', 'g']
    labels = ['Vector A (2, 1, -1)', 'Vector B (3, -1, 4)', 'A x B (Cross Product)']
    
    plot_vectors(vectors, colors, labels, "Vectors A, B, and Their Cross Product")
    
if __name__ == "__main__":
    main()

