import numpy as np

def jacobi(A, b, x, tol):
  r = np.linalg.norm(A.dot(x) - b)
  print(f'Iteration {0}: r={r:3.2e}')                                                                                                                                                                   
    
  D  = np.diag(A)     # Diagonal
  LU = A - np.diag(D) # Lower + Upper

  # Iterations
  k = 0                                                                                                                                                           
  while r > tol:
    k += 1
    x = (b - LU.dot(x)) / D
    r = np.linalg.norm(A.dot(x) - b)
    print(f'{k}, {r:3.2e}')                                                                                                                                                                   

  return x

A = np.array([[ 5.,-2., 3],
              [-3., 9., 1],
              [ 2.,-1, -7]])
b = np.array([-1, 2., 3.])

sol = jacobi(A, b, np.zeros(b.size), 1e-9)

print(sol)