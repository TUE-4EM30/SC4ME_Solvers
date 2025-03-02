import numpy as np
import math
import matplotlib.pyplot as plt

r = 18
n = math.floor(8*2**(r/4))

# Parameters
nx, ny = n, n  # Number of grid points in x and y directions
dx, dy = 1.0 / (nx - 1), 1.0 / (ny - 1)  # Grid spacing

# Heat source
def heat_source(x, y):
    # Flower shape function
    r = np.sqrt((x - 0.5)**2 + (y - 0.5)**2)
    theta = np.arctan2(y - 0.5, x - 0.5)
    return np.sin(5 * theta) * np.exp(-10 * r**2)

# Create the coefficient matrix A
N = nx * ny
A = np.zeros((N, N))

for i in range(nx):
    for j in range(ny):
        index = i * ny + j
        if i == 0 or i == nx-1 or j == 0 or j == ny-1:
            A[index, index] = 1  # Boundary conditions
        else:
            A[index, index] = -4
            A[index, index - 1] = 1
            A[index, index + 1] = 1
            A[index, index - ny] = 1
            A[index, index + ny] = 1

# Create the right-hand side vector b
b = np.zeros(N)
for i in range(nx):
    for j in range(ny):
        if i != 0 and i != nx-1 and j != 0 and j != ny-1:
            b[i * ny + j] = heat_source(i * dx, j * dy) * dx**2

# Export the matrix A and vector b as NumPy arrays
np.save(f'codes/A_{N}.npy', A)
np.save(f'codes/b_{N}.npy', b)

# # Solve the linear system
# u = np.linalg.solve(A, b)

# # Reshape the solution vector into a 2D array
# u = u.reshape((nx, ny))

# # Plot the final temperature distribution
# plt.imshow(u, extent=[0, 1, 0, 1], origin='lower', cmap='hot', interpolation='bilinear')
# plt.title(f'N={N}')
# plt.gca().set_xticks([])
# plt.gca().set_yticks([])
# plt.xlabel('')
# plt.ylabel('')
# plt.show()