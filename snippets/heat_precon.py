import numpy as np
import scipy.sparse.linalg
import inspect

k  = 1.0 # Thermal conductivity
n  = 32  # Nodes in each direction

# Flower-shaped heat source
def heat_source(x, y):
    r = np.sqrt((x - 0.5)**2 + (y - 0.5)**2)
    theta = np.arctan2(y - 0.5, x - 0.5)
    return np.sin(5 * theta) * np.exp(-10 * r**2)

# Assemble the sparse linear system
A, b = get_linear_system(k, heat_source, n)

# ILU preconditioner
P = scipy.sparse.linalg.spilu(A, fill_factor=50)
M = scipy.sparse.linalg.LinearOperator((N, N),\
                                        P.solve)

# Solve the sparse linear system using CG
x = scipy.sparse.linalg.cg(A, b, M=M)