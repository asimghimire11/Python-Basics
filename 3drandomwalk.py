import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def generate_3d_random_walk(num_steps=100000):
    # Generate random steps in x, y, and z directions
    steps_x = np.random.choice([-1, 1], size=num_steps)
    steps_y = np.random.choice([-1, 1], size=num_steps)
    steps_z = np.random.choice([-1, 1], size=num_steps)

    # Calculate cumulative sum to get the random walk
    walk_x = np.cumsum(steps_x)
    walk_y = np.cumsum(steps_y)
    walk_z = np.cumsum(steps_z)

    return walk_x, walk_y, walk_z

# Set the random seed for reproducibility
np.random.seed(425)

# Generate a 3D random walk
num_steps = 1000
random_walk_x, random_walk_y, random_walk_z = generate_3d_random_walk(num_steps)

# Plot the 3D random walk
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(random_walk_x, random_walk_y, random_walk_z, label='3D Random Walk')
ax.scatter(random_walk_x[0], random_walk_y[0], random_walk_z[0], color='green', marker='o', label='Start')
ax.scatter(random_walk_x[-1], random_walk_y[-1], random_walk_z[-1], color='red', marker='x', label='End')
ax.set_title('3D Random Walk')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.legend()
plt.show()
