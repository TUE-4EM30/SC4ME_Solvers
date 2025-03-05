---
style: apple-basic
css: styles.css
mdc: true
lineNumbers: true
hideInToc: true
class: red-background
---

#  Scientific Computing for Mechanical Engineering
##  Solving linear systems in Python

---
src: ./slides/intro.md
---

---
src: ./slides/toc.md
---

<!-- table of contents -->

---
layout: center
class: red-background
---

# Direct dense matrix solvers

---
src: ./slides/linsys.md
---

<!-- slides imported from linsys.md -->

---
layout: center
class: red-background
---

# Sparse matrices

---
src: ./slides/sparse.md
---

<!-- slides imported from sparse.md -->

---
layout: center
class: red-background
---

# Iterative matrix solvers

---
src: ./slides/iterative.md
---

<!-- slides imported from iterative.md -->

---
layout: center
class: red-background
---

# Matrix conditioning

---
src: ./slides/conditioning.md
---

<!-- slides imported from conditioning.md -->

---
layout: center
class: red-background
---

# Summary

---

## Summary

### &nbsp;

<v-clicks at=0>

- Direct *vs.* iterative solvers:
    - Direct solvers work well for small (possibly dense) systems.
    - Iterative solvers are preferable when systems become big and are particularly efficient for sparse systems (matrix-vector products).
- Be aware of conditioning problems:
    - Solution can become meaningless due to floating point precision.
    - Iterative solvers might converge slowly (or not at all).
    - Use iterative solvers in combination with preconditioners.

</v-clicks>