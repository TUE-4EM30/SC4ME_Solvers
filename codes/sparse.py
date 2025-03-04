import numpy as np
import time, math
import tracemalloc
import scipy.sparse, scipy.sparse.linalg
import inspect

precon = False
r = 34
n = math.floor(8*2**(r/4))
N = n**2

# Start tracking memory usage
tracemalloc.start()

# Load the matrix A and vector b
A = scipy.sparse.load_npz(f'codes/A_csr_{N}.npz')
b = np.load(f'codes/b_{N}.npy')

# Record the start time
start_time = time.time()

# Solve the linear system
# u = scipy.sparse.linalg.spsolve(A, b)

# CG
res = []
def callback(xk):
    frame = inspect.currentframe().f_back
    res.append(frame.f_locals['resid'])

if precon:
    P = scipy.sparse.linalg.spilu(A, fill_factor=50)
    M = scipy.sparse.linalg.LinearOperator((N, N), P.solve)
else:
    M = None    

u, info = scipy.sparse.linalg.cg(A, b, callback=callback, M=M)

# Record the end time
end_time = time.time()

# Get the current memory usage
current, peak = tracemalloc.get_traced_memory()

# Stop tracking memory usage
tracemalloc.stop()

# Report the time taken and memory used
niter = len(res)
print(f"{N}, {niter}, {end_time - start_time:.2e}, {peak / 10**6:.2e}, {A.nnz}")

# Export the residuals to a file
if precon:
    np.save(f'codes/CGprecon_{N}.npy', res)
else:
    np.save(f'codes/CGres_{N}.npy', res)