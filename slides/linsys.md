---
layout: two-cols
---

## Linear systems of equations

- Equations form:
$$
\begin{align*} 
 &E_1: & 4 x_1 - x_2 + x_3 &= 8 \\
 &E_2: & 2 x_1 + 5 x_2 + 2 x_3 &= 3 \\
 &E_3: & x_1 + 2 x_2 + 4 x_3 &= 11
\end{align*}
$$
- Matrix form:
$$
\left[ \begin{array}{ccc} 4 & -1 & 1 \\ 2 & 5 & 2 \\ 1 & 2 & 4 \end{array} \right] \left( \begin{array}{c} x_1 \\ x_2 \\ x_3 \end{array} \right) = \left( \begin{array}{c} 8 \\ 3 \\ 11 \end{array} \right)
$$
- Augmented matrix form:
$$
\left[ \begin{array}{ccc} 4 & -1 & 1 \\ 2 & 5 & 2 \\ 1 & 2 & 4 \end{array} \right|  \left. \begin{array}{c} 8 \\ 3 \\ 11 \end{array} \right]
$$

---

## A note on the solvability of linear systems

### &nbsp;

<v-clicks at=0>

- In this lecture we assume:
    - As many linear equations as unknowns (DOFs).
    - The equations are *linearly independent*: each of the equations cannot be written as a linear combination of the others.

- Consequently, the linear system $\mathbf{A} \mathbf{x} = \mathbf{b}$:
    - Has a *unique solution*.
    - Is invertible: $\mathbf{A}^{-1}$ existst.
    - The determinant of $\mathbf{A}$ is non-zero.
    - All eigenvalues of $\mathbf{A}$ are non-zero.

- Always establish that your system is indeed solvable. **Do not ignore “matrix is singular” errors/warnings!**

</v-clicks>

---

## Direct solving using Gaussian elimination

### &nbsp;

- Elimination steps:
$$
\left[ \begin{array}{ccc} 4 & -1 & 1 \\ 2 & 5 & 2 \\ 1 & 2 & 4 \end{array} \right|  \left. \begin{array}{c} 8 \\ 3 \\ 11 \end{array} \right]
\Rightarrow
\left[ \begin{array}{ccc} 4 & -1 & 1 \\ 0 & \frac{11}{2} & \frac{3}{2} \\ 0 & \frac{9}{4} & \frac{15}{4} \end{array} \right|  \left. \begin{array}{c} 8 \\ -1 \\ 9 \end{array} \right]
\Rightarrow
\left[ \begin{array}{ccc} 4 & -1 & 1 \\ 0 & \frac{11}{2} & \frac{3}{2} \\ 0 & 0 & \frac{69}{22} \end{array} \right|  \left. \begin{array}{c} 8 \\ -1 \\ \frac{207}{22} \end{array} \right]
$$

<v-click>

- Solution and back-substitution steps:
$$
\left[ \begin{array}{ccc} 4 & -1 & 1 \\ 0 & \frac{11}{2} & \frac{3}{2} \\ 0 & 0 & 1 \end{array} \right|  \left. \begin{array}{c} 8 \\ -1 \\ 3 \end{array} \right]
\Rightarrow
\left[ \begin{array}{ccc} 4 & -1 & 1 \\ 0 & \frac{11}{2} & 0 \\ 0 & 0 & 1 \end{array} \right|  \left. \begin{array}{c} 8 \\ -\frac{11}{2} \\ 3 \end{array} \right]
\Rightarrow
\left[ \begin{array}{ccc} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right|  \left. \begin{array}{c} 1 \\ -1 \\ 3 \end{array} \right]
$$

</v-click>

---

## Analysing complexity | Elimination steps

### &nbsp;

Using $E_i$, with $i=1,\ldots,N-1$, eliminate $x_i$ from all equations $E_j$, with $j=i+1,\ldots,N$:
$$
\begin{align*}
 A_{jk} &\leftarrow A_{jk} - \frac{A_{ji}}{A_{ii}} A_{ik}   
 & b_{j} &\leftarrow b_{j} - \frac{A_{ji}}{A_{ii}} b_{i}   
 & &\text{for } k = i,\ldots,N  
\end{align*}
$$

<v-click>

- Number of additions/subtractions:
$$
\sum_{i=1}^{N-1} (N-i)(N-i+1) = \frac{N^3-N}{3} = O(N^3)
$$

</v-click>

<v-click>

- Number of multiplications/divisions:
$$
\sum_{i=1}^{N-1} (N-i)(N-i+2) = \frac{2N^3+3N^2-5N}{6} = O(N^3)
$$

</v-click>

---

## Analysing complexity | Back-substitution steps

### &nbsp;

Solve $x_i$ for $i=N,\ldots,1$ by back-substitution of the solved coefficients $x_j$, with $j=i+1,\ldots,N$:
$$
\begin{align*}
b_i \leftarrow \frac{1}{A_{ii}}\left( b_i - \sum_{j=i+1}^{N} A_{ij} x_j \right)
\end{align*}
$$

<v-click>

- Number of additions/subtractions:
$$
\sum_{i=1}^{N-1} (N-i) = \frac{N^2-N}{2} = O(N^2)
$$

</v-click>

<v-click>

- Number of multiplications/divisions:
$$
1 + \sum_{i=1}^{N-1} (N-i+1) = \frac{N^2+N}{2} = O(N^2)
$$

</v-click>

---

## Analysing complexity | Gaussian elimination

### &nbsp;

- Floating-point operations:
    - Elimination steps: $O(N^3)$ additions/subtractions and multiplications/divisions
    - Back-substitution steps: $O(N^2)$ additions/subtractions and multiplications/divisions
- Memory allocation:
    - Dense matrix storage: $O(N^2)$
    - All operations can be done in place

---

## Example | Direct dense matrix solving

![Numpy](/images/Direct_scaling.png)