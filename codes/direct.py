import numpy as np
import time, math
import tracemalloc

r = 17
n = math.floor(8*2**(r/4))
N = n**2

# Start tracking memory usage
tracemalloc.start()

# Load the matrix A and vector b
A = np.load(f'codes/A_{N}.npy')
b = np.load(f'codes/b_{N}.npy')

# Record the start time
start_time = time.time()

# Solve the linear system
u = np.linalg.solve(A, b)

# Record the end time
end_time = time.time()

# Get the current memory usage
current, peak = tracemalloc.get_traced_memory()

# Stop tracking memory usage
tracemalloc.stop()

# Report the time taken and memory used
print(f"{N}, {end_time - start_time:.2e}, {peak / 10**6:.2e}")
