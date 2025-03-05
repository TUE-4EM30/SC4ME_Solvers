## Solving linear systems engineering

### &nbsp;

<v-clicks at=0>

- **Discretization techniques:**
    -   Finite Element Method (FEM) ➡ Solid and structural mechanics, heat transfer, electrodynamics, *etc.* ➡ Complex meshes
    -   Finite Volume Method (FVM) ➡ Fluid mechanics, heat transfer, *etc.* ➡ Complex meshes
    -   Finite Difference Method (FDM) ➡ Physics problems ➡ Structured grids
    - *Etc.*
- **Machine learning:**
    - Linear regression to fit data points
    - Principal Component Analyses (PCA) to reduce the dimensionality of data and models
    - Neural Networks (NN) solve linear systems to update their weights
    - *Etc.*

</v-clicks>

---

## Degrees of freedom (DOFs) in a typical FEM simulation

### &nbsp;

<v-clicks at=0>

- **1960s** and **1970s**: Limited computation power, restricted simulations to **hundreds of DOFs**. 
- **1980s**: More powerful mainframes and early personal computers allowed for refined simulations with **thousands of DOFs**.
- **1990s**: Widespread availability of mainframes and personal computers and advancements in FE software allowed for simulations of **tens of thousands of DOFs**.
- **2000s**: Emergence of high-performance computing (HPC) and parallel processing allowed for problems in the **hundreds of thousands of DOFs**.
- **2010s**: Continued development of hardware and software allowed for simulations with **millions of DOFs**.
- **2020s**: Innovations in, for example, cloud computing and GPU acceleration continue to push the boundaries, currently solving systems of **tens of millions of DOFs**.

</v-clicks>

---

## Example | Heat conduction

![Heat conduction](/images/Flower.png)

- Given the conductivity, $k$, and heat source, $s$, find the temperature, $T$, such that:
$$
\begin{align*}
-\nabla \cdot k \nabla T &= s & &\text{in }\Omega \\
T &= 0 & &\text{on }\partial \Omega
\end{align*}
$$
- Partial differential equation (PDE) discretized using $N$ nodes, with one DOF (temperature) per node.

---
layout: two-cols
---

## Direct solving using `numpy`

````md magic-move
<<<@/snippets/heat.py python {*|13-14}
<<<@/snippets/get_element.py python {*}
<<<@/snippets/heat.py python {16-17}
````

::right::

## &nbsp;

- Discretized linear system: $\mathbf{A}\mathbf{x} = \mathbf{b}$
- Conductivity matrix: $\mathbf{A} \in \mathbb{R}^{N\times N}$
```py {*}{lines: false}
In [1]: type(A)
Out[1]: numpy.ndarray

In [2]: A.shape
Out[2]: (1024, 1024)

In [3]: A.dtype
Out[3]: dtype('float64')
```

- Heat source vector: $\mathbf{b} \in \mathbb{R}^{N}$

<v-click at=3>

- Temperature solution vector: 
$$\mathbf{x} = [T_1, T_2, \ldots, T_N] \in \mathbb{R}^N$$

- Direct solver: `numpy.linalg.solve` 

</v-click>

---

## Direct solving using `numpy` | Analysis

![Numpy](/images/Direct_scaling.png)

---

## Direct solving using `numpy` | Analysis

### &nbsp;

- Simulation time scales with $O(N^3)$:
    - Can we explain?
    - Can we improve?

- Memory (RAM) allocation scales with $O(N^2)$:
    - Can we explain?
    - Can we improve?