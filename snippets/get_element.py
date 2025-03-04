import numpy as np

def get_linear_system(k, heat_source, n):

  # Construct unit square mesh object
  mesh = get_square_mesh(start=0, stop=1, nodes=n)

  # Initialize the linear system
  A = np.zeros((n**2, n**2))
  b = np.zeros(n**2)

  for element in mesh:

    # Get element DOF numbers
    dofs = element.get_dofs()

    # Get element matrix and vector
    Ae = get_element_matrix(element, k)
    be = get_element_vector(element, heat_source)

    # Add to global matrix and vector
    A[np.ix_(dofs, dofs)] += Ae
    b[dofs] += be

  return A, b