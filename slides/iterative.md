## Direct *vs.* iterative solvers

### &nbsp;

Direct solvers:
- Solve a linear system up to machine precision
- Rely on Gaussian elimination with ${O}(N^3)$ solution time
- Are difficult to parallelize

### &nbsp;

### By accepting a small - practically insignificant - error in the solution, can we attain a faster and easier to parallelize linear solver? 

---
layout: two-cols
---

## Jacobi iterative solver

- Additive matrix decomposition:
$$\mathbf{A} = \mathbf{D}+\mathbf{L}+\mathbf{U}$$
- Reformulated linear system:
$$
\begin{array}{c}
\mathbf{A} \textbf{x} = \textbf{b}\\
\Downarrow\\
(\mathbf{D}+\mathbf{L}+\mathbf{U})\textbf{x} = \textbf{b}\\
\Downarrow\\
\textbf{x} = \mathbf{D}^{-1}\left[ \textbf{b} - (\mathbf{L}+\mathbf{U})\textbf{x} \right]
\end{array}
$$

<v-click>

- Jacobi iterations ($k=0,1,2,\ldots$):
$$
\textbf{x}^{k+1} = \mathbf{D}^{-1}\left[ \textbf{b} - (\mathbf{L}+\mathbf{U})\textbf{x}^{k} \right]
$$
- Matrix-vector products only ($O(N^2)$)

</v-click>

<v-click>

- Stopping criterion (tolerance) needed

</v-click>

::right::

<<<@/snippets/jacobi.py python {7,8|11,13,14|12,15,25}{at:1}

---
layout: two-cols
---

## Jacobi iterative solver

![CG](/images/Jacobi.png)

::right::

## &nbsp;

- Converges for diagonally dominant matrices
- Every iteration requires $O(N^2)$ operations
- Favorable scaling compared to direct solvers if the tolerance is reached in $O(1)$ iterations (independent of the system size)
- Based on matrix-vector products:
    - Efficient sparse operations
    - Suitable for parallelization
- Fast for diagonally dominant large sparse systems
---

## Stationary *vs.* Krylov subspace iterative solvers

### &nbsp;

- **Stationary methods** ➡ Matrix approximation and defect correction
    - Jacobi
    - Gauss-Seidel
    - Successive over-relaxation (SOR)
    - *Etc.*

<v-click>

- **Krylov subspace methods** ➡ Successive minimization
    - Conjugate Gradient (CG)
    - General Minimal Residual (GMRES)
    - Minimal Residual (MINRES)
    - Biconjugate Gradient Stabilized (Bi-CGSTAB)
    - *Etc.*

</v-click>

---

## Minimization for symmetric positive definite (SPD) matrices

### &nbsp;

-  Linear system:
 $$ \mathbf{A} \mathbf{x} = \mathbf{b}$$
 
- Residual:
$$\mathbf{r} = \mathbf{A} \mathbf{x} - \mathbf{b} = \mathbf{0}$$

<v-click>

- Equivalent minimization problem:
$$ \mathbf{x} = \operatornamewithlimits{argmin}_{\mathbf{y}} g(\mathbf{y})$$
 
- Minimization functional:

$$ g(\textbf{y}) = \textbf{y}^T\textbf{Ay} - 2 \textbf{y}^T\textbf{b}$$

</v-click>

---
layout: two-cols
---

## Steepest descent solver

### &nbsp;

- Minimization functional:
$$ g(\textbf{y}) = \textbf{y}^T\textbf{Ay} - 2 \textbf{y}^T\textbf{b}$$
- Steepest descent direction:
$$ \nabla g = 2 \textbf{Ay} - 2 \textbf{b} \propto \textbf{r}$$
- Iterative solution search:
$$\mathbf{x}^{k+1} = \mathbf{x}^{k} + \alpha_k \mathbf{r}_k$$
- Substitution in $g$ and minimizing:
$$\alpha_k = - \frac{\mathbf{r}_k^T \mathbf{r}_k}{\mathbf{r}_k^T \mathbf{A} \mathbf{r}_k}$$

::right::

![CG](/images/SteepestDescent.png)

---
layout: two-cols
---

## Conjugate Gradient (CG)

### &nbsp;

- Search in a direction orthogonal (conjugate) to the previous
search directions:
$$\mathbf{x}^{k+1} = \mathbf{x}^{k} + \alpha_k \mathbf{p}_k$$
- Search direction:
$$
\textbf{p}_k =
\begin{cases}
\textbf{r}_0 & k=0 \\
\textbf{r}_k -\frac{\textbf{r}_k^T  \textbf{r}_k }{ \textbf{r}_{k-1}^T \textbf{r}_{k-1}}\textbf{p}_{k-1} & k>0
\end{cases}
$$
- Search distance:
$$\alpha_k = - \frac{\mathbf{r}_k^T \mathbf{r}_k}{\mathbf{p}_k^T \mathbf{A} \mathbf{p}_k}$$

::right::

![CG](/images/ConjugateGradient.png)

---
layout: two-cols
---

## Example | CG solver

````md magic-move
<<<@/snippets/heat_sparse.py python {14-18}
<<<@/snippets/heat_cg.py python {18-25}
````

::right::

## &nbsp;

- Heat conduction problem solved using `scipy.sparse.linalg.cg`
- Optional arguments:
    - Initial guess: `x0`
    - Tolerances: `rtol`, `atol`
    - Max number of iterations: `maxiter`
    - Callback function: `callback`
    - Preconditioner: `M` 

---

## Example | CG solver

![CG](/images/CG_iterations.png)

---

## Example | Direct *vs.* CG

![CG](/images/Spsolve_vs_CG_scaling.png)

---
layout: two-cols
---

## Convergence of CG
### &nbsp;

- Solution error ($k=0,1,\ldots$):
$$\mathbf{e}^k = \mathbf{x}^k-\mathbf{x}$$
- Convergence:
$$\|\textbf{e}^k\|_{\mathbf{A}} \leq 2\left[\frac{\sqrt{\kappa(\textbf{A}})-1}{\sqrt{\kappa(\textbf{A}})+1}\right]^k \|\textbf{e}^0\|_{\mathbf{A}} $$
- Iterations to reach a fixed tolerance:
$$k_{\rm tol} = O(\sqrt{\kappa(\textbf{A})}) \log{\left(\frac{1}{\text{tol}}\right)}$$
- Condition number (SPD):
$$ \kappa (\textbf{A}) = \frac{\lambda_{\rm max}}{\lambda_{\rm min}}$$

::right::

#### &nbsp;

$$ \text{2D heat conduction: } \kappa (\textbf{A}) = O(N)$$

![CG](/images/CGconditioning.png)