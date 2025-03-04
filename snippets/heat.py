import numpy as np
import matplotlib.pyplot as plt

k  = 1.0 # Thermal conductivity
n  = 32  # Nodes in each direction

# Flower-shaped heat source
def heat_source(x, y):
    r = np.sqrt((x - 0.5)**2 + (y - 0.5)**2)
    theta = np.arctan2(y - 0.5, x - 0.5)
    return np.sin(5 * theta) * np.exp(-10 * r**2)

# Assemble the linear system
A, b = get_linear_system(k, heat_source, n)

# Solve the linear system
x = np.linalg.solve(A, b)

# Plot the final temperature distribution
plt.imshow(x.reshape((n, n)), extent=[0, 1, 0, 1],\
            origin='lower', cmap='hot')
plt.colorbar(label='Temperature')
plt.show()