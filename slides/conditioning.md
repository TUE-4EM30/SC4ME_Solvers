## CG convergence
### &nbsp;
- With infinite precision, for an $N$ dimensional system, CG converges in $N$ iterations at most!
- CG can be interpreted as a direct solution algorithm.
- Reaches a small tolerance in $k_{\rm tol} \ll N$ iterations for well-conditioned systems (small $\kappa$):
$$k_{\rm tol} = O(\sqrt{\kappa(\textbf{A})}) \log{\left(\frac{1}{\text{tol}}\right)}$$
- If the matrix $\textbf{A}$ is ill-conditioned (large $\kappa$), the method is highly susceptible to rounding errors:
$$\|\textbf{e}^k\|_{\mathbf{A}} \leq 2\left[\frac{\sqrt{\kappa(\textbf{A}})-1}{\sqrt{\kappa(\textbf{A}})+1}\right]^k \|\textbf{e}^0\|_{\mathbf{A}} $$

---
layout: two-cols-header
---

## Understanding the condition number | Binary numbers

::left::

<v-clicks at=0>

- Integers: $\texttt{\small 16-bits signed}$
    - Range: $-2^{15} \geq x \geq 2^{15} - 1$
    - Spacing: $1$
- Float/double: $\texttt{\small 64-bits}$
    - Exponent range: $10^{-308}$ - $10^{308}$
    - Fraction range: 15-17 significant digits
    - Relative spacing (eps): $2^{-53} \approx 1 \cdot 10^{-16}$

</v-clicks>

## &nbsp;
## &nbsp;
## &nbsp;

::right::

<v-clicks at=0>

![int](/images/int16.png){width=80%}

![int](/images/double.png){width=80%}

</v-clicks>

---

## Understanding the condition number | Perturbation sensitivity

### &nbsp;

- Due to machine precision, there is always a loss of significance because of rounding errors.
- Consider a machine precision perturbation of the right-hand-side vector:
$$ 
\begin{align*}
\mathbf{A}\left(\mathbf{x}+\widetilde{\mathbf{x}}\right) &= \left(\mathbf{b}+\widetilde{\mathbf{b}}\right)  & \qquad \| \widetilde{\mathbf{b}} \| / \| \mathbf{b} \| &\approx {\rm eps} 
\end{align*}
$$

<v-click>

- Corresponding perturbation of the solution vector:
$$
\begin{align*}
    & \frac{\|\widetilde{\mathbf{x}}\|}{\|\mathbf{x}\|} =\frac{\| \mathbf{A}^{-1} \widetilde{\mathbf{b}}\|}{\|\mathbf{x}\|} \frac{\| \mathbf{A} \mathbf{x} \|}{\| \mathbf{b} \|} \leq \frac{\| \mathbf{A}^{-1} \| \|  \widetilde{\mathbf{b}}\|}{\|\mathbf{x}\|} \frac{\| \mathbf{A} \| \| \mathbf{x} \|}{\| \mathbf{b} \|} = { \| \mathbf{A} \| \| \mathbf{A}^{-1} \| } \frac{ \|  \widetilde{\mathbf{b}}\| }{\| \mathbf{b} \|} = \kappa({\textbf{A}}) \, \text{eps}
\end{align*}
$$

- Condition number (SPD):
$$
\kappa (\mathbf{A}) =  \| \mathbf{A} \| \| \mathbf{A}^{-1} \|  = \frac{\lambda_{\rm max}}{\lambda_{\rm min}}
$$

- When $\kappa(\mathbf{A})$ becomes very large ($O(\text{eps}^{-1})$), rounding errors lead to large solution errors.

</v-click>

---

## Ill-conditioned systems of equations

### &nbsp;

- A system is called *ill-conditioned* when the condition number is large ($O(\text{eps}^{-1})$).
- A singular matrix has an infinite condition number.
- Typical cases of ill-conditioned systems:
    - Large (FE/FV/FD) systems
    - Higher-order methods
    - Meshes with distorted elements
    - Multi-physics problems
    - *Etc.*

---

## Matrix preconditioning

### &nbsp;

- Original linear system with $\kappa(\mathbf{A}) \gg 1$:
$$ \mathbf{A}\mathbf{x} = \mathbf{b} $$

- Equivalent preconditioned systems:

    <v-click at=0>

    - Left preconditioning ➡ Consider a matrix $\mathbf{L}$ such that $\kappa(\mathbf{LA}) \ll \kappa(\mathbf{A})$:
    $$\mathbf{L} \mathbf{A} \mathbf{x} = \mathbf{L} \mathbf{b}$$

    </v-click>

    <v-click at=1>

    - Right preconditioning ➡ Consider a matrix $\mathbf{R}$ such that $\kappa(\mathbf{AR}) \ll \kappa(\mathbf{A})$:
    $$\begin{array}{cc} \mathbf{A} \mathbf{R} \mathbf{y} = \mathbf{b} & \mathbf{x} = \mathbf{R} \mathbf{y} \end{array}$$

    </v-click>

    <v-click at=2>

    - Left and right preconditioning ➡ Consider matrices $\mathbf{L}$ and $\mathbf{R}$ such that $\kappa(\mathbf{LAR}) \ll \kappa(\mathbf{A})$:
    $$\begin{array}{cc} \mathbf{L}\mathbf{A} \mathbf{R} \mathbf{y} = \mathbf{L}\mathbf{b} &  \mathbf{x} = \mathbf{R} \mathbf{y} \end{array}$$

    </v-click>

---

## Preconditioning strategies

### &nbsp;

- Using the inverse matrix $\mathbf{A}^{-1}$ ($O(N^4)$) as a preconditioner $\mathbf{L}$ results in optimal conditioning:
$$ \kappa(\mathbf{LA}) = \kappa(\mathbf{A}^{-1} \mathbf{A}) = \kappa(\mathbf{I}) = 1 $$

<v-click>

- A good preconditioner provides a computationally cheap approximation of the inverse:


    - Jacobi preconditioning ($O(N)$):
    $$ \mathbf{D} \approx \mathbf{A} $$

    - Incomplete LU preconditioning ($O(N^2)$):
    $$ \mathbf{LU} \approx \mathbf{A} $$

    - *Etc.*

</v-click>

---
layout: two-cols
---

## Example | Preconditioned CG

<<<@/snippets/heat_precon.py python {17-23}

::right::

## &nbsp;

- Incomplete LU computed using `scipy.linal.sparse.spilu`
- Optional arguments:
    - Tolerance for dropping entries: `drop_tol`
    - Upper limit to LU fill in: `fill_factor`
    - *Etc.*
- Optimization required to balance:
    - Cost of preconditioner
    - Increased efficiency of solver

---

## Example | Preconditioned CG

![Preconditioned CG](/images/Preconditioning_iterations.png)

---

## Example | Preconditioned CG

![Preconditioned CG scaling](/images/Preconditioning_scaling.png)