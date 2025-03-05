import numpy as np
import matplotlib.pyplot as plt

# Define the 2x2 matrix A and vector b
A = np.array([[5, 1], [1, 2]])
b = np.array([-0.5, -1])

# Define the quadratic function
def f(x):
    return 0.5 * x.T @ A @ x - b.T @ x

# Define the gradient of the quadratic function
def grad_f(x):
    return A @ x - b

# Conjugate Gradient method
def steepest(A, b, x0, tol=1e-6, max_iter=100):
    x = x0
    r = b - A @ x
    p = r
    rsold = r.T @ r
    steps = [x.copy()]

    for i in range(max_iter):
        Ap = A @ p
        alpha = rsold / (p.T @ Ap)
        x = x + alpha * p
        r = r - alpha * Ap
        rsnew = r.T @ r
        steps.append(x.copy())
        if np.sqrt(rsnew) < tol:
            break
        p = r
        rsold = rsnew

    return x, steps

# Initial guess
x0 = np.array([0.5, 0.9])

# Solve the system using Conjugate Gradient method
x, steps = steepest(A, b, x0)

# Create a grid of points for plotting the energy contours
x1 = np.linspace(-1, 1, 400)
x2 = np.linspace(-1, 1, 400)
X1, X2 = np.meshgrid(x1, x2)
Z = np.array([f(np.array([x1, x2])) for x1, x2 in zip(np.ravel(X1), np.ravel(X2))])
Z = Z.reshape(X1.shape)

# Plot the energy contours
plt.figure(figsize=(6, 6))
plt.contour(X1, X2, Z, levels=20, cmap='viridis')
plt.plot(*zip(*steps), marker='o', color='r', label='Steepest descent')
plt.scatter(*zip(*steps), color='r')
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.title('Minimization of $g$')
plt.legend()
plt.grid(True)


# Conjugate Gradient method
def conjugate_gradient(A, b, x0, tol=1e-6, max_iter=100):
    x = x0
    r = b - A @ x
    p = r
    rsold = r.T @ r
    steps = [x.copy()]

    for i in range(max_iter):
        Ap = A @ p
        alpha = rsold / (p.T @ Ap)
        x = x + alpha * p
        r = r - alpha * Ap
        rsnew = r.T @ r
        steps.append(x.copy())
        if np.sqrt(rsnew) < tol:
            break
        p = r + (rsnew / rsold) * p
        rsold = rsnew

    return x, steps

# Solve the system using Conjugate Gradient method
x_cg, steps_cg = conjugate_gradient(A, b, x0)

# Plot the energy contours
plt.figure(figsize=(6, 6))
plt.contour(X1, X2, Z, levels=20, cmap='viridis')
plt.plot(*zip(*steps), marker='o', color='r', label='Steepest descent')
plt.scatter(*zip(*steps), color='r')
plt.plot(*zip(*steps_cg), marker='d', color='b', label='Conjugate gradient')
plt.scatter(*zip(*steps_cg), color='b')
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.title('Minimization of $g$')
plt.legend()
plt.grid(True)


plt.show()