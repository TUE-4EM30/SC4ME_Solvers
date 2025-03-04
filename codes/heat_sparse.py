import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.sparse, scipy.sparse.linalg

r   = 0.25

r = 12
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

data = np.empty(5*N)
indices = np.empty(5*N, dtype=np.int32)
indptr = np.zeros(N+1, dtype=np.int32)
for i in range(nx):
    for j in range(ny):
        index = i * ny + j
        if i == 0 or i == nx-1 or j == 0 or j == ny-1:
            indptr[index+1] = indptr[index] + 1
            data[indptr[index]:indptr[index+1]] = [1]
            indices[indptr[index]:indptr[index+1]] = [index]
        else:
            indptr[index+1] = indptr[index] + 5
            data[indptr[index]:indptr[index+1]] = [-4, 1, 1, 1, 1]
            indices[indptr[index]:indptr[index+1]] = [index, index - 1, index + 1, index - ny, index + ny]
            
A_csr = scipy.sparse.csr_matrix((data, indices, indptr), shape=(N, N))

# Create the right-hand side vector b
b = np.zeros(N)
for i in range(nx):
    for j in range(ny):
        if i != 0 and i != nx-1 and j != 0 and j != ny-1:
            b[i * ny + j] = heat_source(i * dx, j * dy) * dx**2

# Export
scipy.sparse.save_npz(f'codes/A_csr_{N}.npz', A_csr)

np.save(f'codes/b_{N}.npy', b)



# # Solve the linear system
# u = scipy.sparse.linalg.spsolve(A_csr, b)

# # Reshape the solution vector into a 2D array
# u = u.reshape((nx, ny))

# # Plot the final temperature distribution
# plt.imshow(u, extent=[0, 1, 0, 1], origin='lower', cmap='hot', interpolation='bilinear')
# plt.title(f'$N$={N}, $\epsilon$={eps}')
# plt.gca().set_xticks([])
# plt.gca().set_yticks([])
# plt.xlabel('')
# plt.ylabel('')
# plt.show()

# # Print memory usage of the sparse matrix A_csr
# print(f"{N}, {(A_csr.data.nbytes + A_csr.indices.nbytes + A_csr.indptr.nbytes) / 1024**2:.2e}")
