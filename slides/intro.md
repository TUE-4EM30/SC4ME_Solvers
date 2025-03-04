---

## Solving linear systems engineering

### &nbsp;

<v-clicks at=0>

- Discretization techniques:
    -   Finite Element Method (FEM) to solve problems in solid and structural mechanics, heat transfer, electrodynamics, *etc.* on complex meshes.
    -   Finite Volume Method (FVM) to solve problems in fluid mechanics, heat transfer, *etc.* on complex meshes.
    -   Finite Difference Method (FDM) to solve all kinds of physics problems on structured grids.
    - *Etc.*
- Machine learning:
    - Linear regression to fit data points.
    - Principal Component Analyses (PCA) to reduce the dimensionality of data and models.
    - Neural Networks (NN) solve linear systems to update their weights.
    - *Etc.*

</v-clicks>

---

## Degrees of freedom (DOFs) in a typical FEM simulation

### &nbsp;

<v-clicks at=0>

- **1960s** and **1970s**: Limited computation power, restricted simulations to **hundreds of DOFs**. 
- **1980s**: More powerful mainframes and early personal computers allowed for refined simulations with **thousands of DOFs**.
- **1990s**: Widespread availability of personal computers and advancements in FE software allowed for simulations of **tens of thousands of DOFs**.
- **2000s**: Emergence of high-performance computing (HPC) and parallel processing allowed for problems in the **hundreds of thousands of DOFs**.
- **2010s**: Continued development of hardware and software allowed for simulations with **millions of thousands of DOFs**.
- **2020s**: Innovations in, for example, cloud computing and GPU acceleration continue to push the boundaries, currently solving systems of **millions of DOFs**.

</v-clicks>

---

## Example: heat conduction

![Heat conduction](/images/Flower.png)

---

## Solving using `numpy`

- How solved

---

## Solving using `numpy` (cont'd)

![Numpy](/images/Direct_scaling.png)

