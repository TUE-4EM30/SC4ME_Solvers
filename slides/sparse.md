## Sparse matrices in engineering

### &nbsp;

- Discretization techniques:
    - Finite Element Method (FEM) ➡ Basis functions "interact" only locally.
    - Finite Volume Method (FVM) ➡ Cell fluxes only "interact" with neighbors.
    - Finite Difference Method (FDM) ➡ Stencils only involve neighboring grid points.
    - *Etc.*
- Machine learning:
    - Feature-representation matrices.
    - Networks with local interactions.
    - *Etc.*

---

## Example | Sparsity pattern

![Numpy](/images/Sparsity.png)


---

## Sparse matrix formats

### &nbsp;

- When the number of non-zero values scales linearly with the size of the matrix ($nnz = O(N)$), a dense matrix (`numpy.array`) with $O(N^2)$ memory complexity is not a good choice. 

<v-space>

- Variety of sparse matrix formats with $nnz=O(N)$ memory complexity:
    - Diagonal (DIA) format
    - Compressed sparse row/column (CSR/CSC) formats
    - Coordinate (COO) format
    - Dictionary of keys (DOK) format
    - List of lists (LIL) format

![Sparse matrices](/images/SparseMatrices.png){width=70%}

</v-space>

---
layout: two-cols
---

## Coordinate (COO) format

$$
   \mathbf{A} = \left[\begin{array}{ccccc}
    \colorbox{lightgreen}{1} & \colorbox{orange}{3}  & \square & \square & \square\\
    \square   & \colorbox{yellow}{2} & \square & \square & \square\\
    \square  & \square  & \square & \colorbox{lightblue}{4} & \square\\
    \square   & \square   & \square  & \square & \square\\
    \square  & \square  & \square & \colorbox{magenta}{1}   & \square\\
  \end{array}\right]
$$

### &nbsp;

```py
import scipy.sparse

row_indices = [0, 4, 0, 1, 2, 0]
col_indices = [0, 3, 1, 1, 3, 1]
values      = [1, 1, 1, 2, 4, 2]

A = scipy.sparse.coo_matrix(
        (values, (row_indices, col_indices)), 
        shape=(5, 5)
    )
```

::right::

### &nbsp;

$$
\begin{align*}
\texttt{row\_indices} &= \left[ \begin{array}{cccccc} \colorbox{lightgreen}{0} & \colorbox{magenta}{4} & \colorbox{orange}{0} & \colorbox{yellow}{1} & \colorbox{lightblue}{2} & \colorbox{orange}{0} \end{array} \right] \\
 \texttt{col\_indices} &= \left[ \begin{array}{cccccc} \colorbox{lightgreen}{0} & \colorbox{magenta}{3} & \colorbox{orange}{1} & \colorbox{yellow}{1} & \colorbox{lightblue}{3} & \colorbox{orange}{1} \end{array} \right]\\
 \texttt{values} &= \underbrace{\left[ \begin{array}{cccccc} \colorbox{lightgreen}{1}& \colorbox{magenta}{1} & \colorbox{orange}{1} & \colorbox{yellow}{2} & \colorbox{lightblue}{4} & \colorbox{orange}{2} \end{array} \right]}_{\texttt{nnz}}
\end{align*}
$$

## &nbsp;

- Fast construction (append arrays) 
- Allows for duplicate entries (FE assembly)
- Fast matrix-vector product ($O(\texttt{nnz})$)
- Inefficient slicing
- Suboptimal storage efficiency

---
layout: two-cols
---

## Compressed sparse row (CSR)

$$
   \mathbf{A} = \left[\begin{array}{ccccc}
    \colorbox{lightgreen}{1} & \colorbox{orange}{3}  & \square & \square & \square\\
    \square   & \colorbox{yellow}{2} & \square & \square & \square\\
    \square  & \square  & \square & \colorbox{lightblue}{4} & \square\\
    \square   & \square   & \square  & \square & \square\\
    \square  & \square  & \square & \colorbox{magenta}{1}   & \square\\
  \end{array}\right]
$$

### &nbsp;

```py
import scipy.sparse

row_offsets = [0, 2, 3, 4, 4, 5]
col_indices = [0, 1, 1, 3, 3]
values      = [1, 3, 2, 4, 1]

A = scipy.sparse.csr_matrix(
        (values, col_indices, row_offsets), 
        shape=(5, 5)
    )
```

::right::

## &nbsp;

$$
\begin{align*}
\texttt{row\_offsets} &= \overbrace{ \left[ \begin{array}{cccccc} 0 & 2 & 3 & 4 & 4 & 5 \end{array} \right] }^{{N+1}}\\
 \texttt{col\_indices} &= \left[ \begin{array}{ccccc} \colorbox{lightgreen}{0} & \colorbox{orange}{1} & \colorbox{yellow}{1} & \colorbox{lightblue}{3} & \colorbox{magenta}{3} \end{array} \right]\\
 \texttt{values} &= \underbrace{\left[ \begin{array}{ccccc} \colorbox{lightgreen}{1} & \colorbox{orange}{3} & \colorbox{yellow}{2} & \colorbox{lightblue}{4} & \colorbox{magenta}{1} \end{array} \right]}_{\texttt{nnz}}
\end{align*}
$$

### &nbsp;

- Not suitable for construction due to changes in sparsity pattern (reallocation of memory)
- Very fast matrix-vector product due to data locality
- Fast row slicing
- Good storage efficiency

---
layout: two-cols
---

## Diagonal (DIA) format

$$
   \mathbf{A} = \left[\begin{array}{ccccc}
    \colorbox{lightgreen}{1} & \colorbox{orange}{3}  & \square & \square & \square\\
    \square   & \colorbox{yellow}{2} & \square & \square & \square\\
    \square  & \square  & \square & \colorbox{lightblue}{4} & \square\\
    \square   & \square   & \square  & \square & \square\\
    \square  & \square  & \square & \colorbox{magenta}{1}   & \square\\
  \end{array}\right]
$$

### &nbsp;

```py
import numpy as np
import scipy.sparse

offsets = [0, 1, -1]
values  = np.array([[1, 2, 0, 0, 0],
                    [0, 3, 0, 4, 0],
                    [0, 0, 0, 1, 0]])

A = scipy.sparse.dia_matrix(
        (values, offsets), 
        shape=(5, 5)
    )
```

::right::

## &nbsp;

$$
\begin{align*}
\texttt{offsets} &= \overbrace{ \left[ \begin{array}{ccc} 0 & 1 & -1 \end{array} \right] }^{\texttt{n}_{\rm diag}}\\
 \texttt{values} &= \left[ \begin{array}{ccccc} \colorbox{lightgreen}{1} &  \colorbox{yellow}{2} & \square & \square & \square \\ \blacksquare & \colorbox{orange}{3} & \square & \colorbox{lightblue}{4} & \square \\ \square & \square & \square & \colorbox{magenta}{1}  & \blacksquare \end{array} \right]
\end{align*}
$$

### &nbsp;

- Very fast and efficient when the matrix is diagonal
- Unnecessary memory allocation (in particular for large offsets)
- Poor choice when the matrix is not entirely diagonal

---
layout: two-cols
---

## Example | Sparse matrices

- Code of example

---

## Solving a sparse system

![Numpy](/images/Sparse_scaling.png)
<!-- - Still something else needed -->

---

## Solving a sparse system

![Numpy](/images/Direct_vs_Sparse_scaling.png)
<!-- - Still something else needed -->

