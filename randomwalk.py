import numpy as np
import matplotlib.pyplot as plt

def generate_random_walk(num_steps=1000):
    # Generate random steps in both x and y directions
    steps_x = np.random.choice([-1, 1], size=num_steps)
    steps_y = np.random.choice([-1, 1], size=num_steps)

    # Calculate cumulative sum to get the random walk
    walk_x = np.cumsum(steps_x)
    walk_y = np.cumsum(steps_y)

    return walk_x, walk_y

# Set the random seed for reproducibility
np.random.seed(42)

# Generate a random walk
num_steps = 1000
random_walk_x, random_walk_y = generate_random_walk(num_steps)

# Plot the random walk
plt.plot(random_walk_x, random_walk_y, label='Random Walk')
plt.scatter(random_walk_x[0], random_walk_y[0], color='green', marker='o', label='Start')
plt.scatter(random_walk_x[-1], random_walk_y[-1], color='red', marker='x', label='End')
plt.title('2D Random Walk')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.show()
