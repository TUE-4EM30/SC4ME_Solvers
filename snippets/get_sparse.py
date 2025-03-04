def get_linear_system(k, heat_source, n):

  # Initialize data structures
  mesh = get_square_mesh(start=0, stop=1, nodes=n)
  row_indices, col_indices, values = [], [], []
  b = np.zeros(n**2)

  for element in mesh:
    dofs = element.get_dofs()
    Ae = get_element_matrix(element, k)
    be = get_element_vector(element, heat_source)

    # Add to data structures
    for i in range(len(dofs)):
      for j in range(len(dofs)):
        values.append(Ae[i, j])
        row_indices.append(dofs[i])
        col_indices.append(dofs[j])
        b[dofs[i]] += be[i]

    # Create the sparse matrix in COO format
    A = scipy.sparsse.coo_matrix((values,\
      (row_indices, col_indices)), shape=(n**2, n**2))

    return A.tocsr(), b