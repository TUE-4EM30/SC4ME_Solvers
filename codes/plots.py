import numpy as np
import matplotlib.pyplot as plt
import scipy.sparse
from colors import tol_cset

# Load the color scheme
cset = tol_cset('high-contrast')

# Load the data from the CSV file
data = np.loadtxt('codes/direct.csv', delimiter=',', comments='//')
data_sp = np.loadtxt('codes/sparse.csv', delimiter=',', comments='//')
data_cg = np.loadtxt('codes/cg.csv', delimiter=',', comments='//')
data_p  = np.loadtxt('codes/precon.csv', delimiter=',', comments='//')

# Extract columns
dofs = data[:, 0]
time = data[:, 1]
memory = data[:, 2]

dofs_sp = data_sp[:, 0]
time_sp = data_sp[:, 1]
memory_mat_sp = data_sp[:, 2]
memory_tot_sp = data_sp[:, 3]
nnz_sp = data_sp[:, 4]

dofs_cg = data_cg[:, 0]
iter_cg = data_cg[:, 1]
time_cg = data_cg[:, 2]
memory_cg = data_cg[:, 3]

dofs_p = data_p[:, 0]
iter_p = data_p[:, 1]
time_p = data_p[:, 2]
memory_p = data_p[:, 3]

#########################
# Direct solver results #
#########################

# Create the log-log plots
plt.figure(figsize=(12, 6))

# Plot time vs. DOFs
plt.subplot(1, 2, 1)
plt.loglog(dofs, time, marker='o', linestyle='-', color=cset.blue, label='Time')
# Add scaling line with a rate of 3
plt.loglog(dofs, 0.01*time[0] * (dofs / dofs[0])**3, linestyle='--', color=cset.black, label='$O(N^3)$')
plt.xlabel('$N$')
plt.ylabel('Time [s]')
plt.grid(True, which="both", ls="--")
plt.legend()

# Plot memory vs. DOFs
plt.subplot(1, 2, 2)
plt.loglog(dofs, memory, marker='o', linestyle='-', color=cset.yellow, label='Memory')
# Add scaling line with a rate of 2
plt.loglog(dofs, 0.1*memory[0] * (dofs / dofs[0])**2, linestyle='--', color='k', label='$O(N^2)$')
plt.xlabel('$N$')
plt.ylabel('Memory [MB]')
plt.grid(True, which="both", ls="--")
plt.legend()
plt.tight_layout()

#########################
# Sparse results        #
#########################

# Create the log-log plots
plt.figure(figsize=(12, 6))

# Plot time vs. DOFs
plt.subplot(1, 2, 1)
plt.loglog(dofs_sp, time_sp, marker='o', linestyle='-', color=cset.blue, label='Time')
# Add scaling line with a rate of 2
plt.loglog(dofs_sp, 0.00001*time_sp[0] * (dofs_sp / dofs_sp[0])**2, linestyle='--', color='k', label='$O(N^2)$')
plt.xlabel('$N$')
plt.ylabel('Time [s]')
plt.grid(True, which="both", ls="--")
plt.legend()

# Plot memory vs. DOFs
plt.subplot(1, 2, 2)
plt.loglog(dofs_sp, memory_mat_sp, marker='.', linestyle='--', color=cset.yellow, label='Memory (Matrix)')
plt.loglog(dofs_sp, memory_tot_sp, marker='o', linestyle='-', color=cset.yellow, label='Memory (Total)')
# Add scaling line with a rate of 1
plt.loglog(dofs_sp, 0.5*memory_mat_sp[0] * (dofs_sp / dofs_sp[0]), linestyle='--', color='k', label='$O(N)$')
plt.xlabel('$N$')
plt.ylabel('Memory [MB]')
plt.grid(True, which="both", ls="--")
plt.legend()
plt.tight_layout()

#########################
# Combined results        #
#########################

# Create the log-log plots
plt.figure(figsize=(12, 6))

# Plot time vs. DOFs
plt.subplot(1, 2, 1)
plt.loglog(dofs, time, marker='o', linestyle='-', color=cset.blue, label='Dense')
plt.loglog(dofs_sp, time_sp, marker='s', linestyle='--', color=cset.blue, label='Sparse')
plt.xlabel('$N$')
plt.ylabel('Time [s]')
plt.grid(True, which="both", ls="--")
plt.legend()

# Plot memory vs. DOFs
plt.subplot(1, 2, 2)
plt.loglog(dofs, memory, marker='o', linestyle='-', color=cset.yellow, label='Dense')
plt.loglog(dofs_sp, memory_tot_sp, marker='s', linestyle='--', color=cset.yellow, label='Sparse')
plt.xlabel('$N$')
plt.ylabel('Memory [MB]')
plt.grid(True, which="both", ls="--")
plt.legend()
plt.tight_layout()

#########################
# CG iterations         #
#########################

# Create the log-log plots
plt.figure(figsize=(12, 6))

# Plot iterations
plt.subplot(1, 2, 1)
res = np.load('codes/CGres_1024.npy')
plt.loglog(np.arange(res.size), res, linestyle='-', color=cset.blue, label='$N=1024$')
res = np.load('codes/CGres_16384.npy')
plt.loglog(np.arange(res.size), res, linestyle='-', color=cset.yellow, label='$N=16384$')
res = np.load('codes/CGres_262144.npy')
plt.loglog(np.arange(res.size), res, linestyle='-', color=cset.red, label='$N=262144$')
res = np.load('codes/CGres_4194304.npy')
plt.loglog(np.arange(res.size), res, linestyle='-', color=cset.black, label='$N=4194304$')

# plt.loglog(dofs_cg, 0.1*dofs_cg[0] * (dofs_cg / dofs_cg[0])**0.5, linestyle='--', color='k', label='$O(\sqrt{N})$')
plt.xlabel('Iteration')
plt.ylabel('Resdiual')
plt.grid(True, which="both", ls="--")
plt.legend()
plt.tight_layout()

# Plot time vs. DOFs
plt.subplot(1, 2, 2)
plt.loglog(dofs_cg, iter_cg, marker='o', linestyle='-', color=cset.blue, label='CG iterations')
plt.loglog(dofs_cg, 0.1*dofs_cg[0] * (dofs_cg / dofs_cg[0])**0.5, linestyle='--', color='k', label='$O(\sqrt{N})$')
plt.xlabel('$N$')
plt.ylabel('Iterations')
plt.grid(True, which="both", ls="--")
plt.legend()
plt.tight_layout()

#########################
# CG iterations 2        #
#########################

# Create the log-log plots
plt.figure(figsize=(6, 6))


# Plot time vs. DOFs
plt.subplot(1, 1, 1)
plt.loglog(dofs_cg, iter_cg, marker='o', linestyle='-', color=cset.blue, label='CG iterations')
plt.loglog(dofs_cg, 0.1*dofs_cg[0] * (dofs_cg / dofs_cg[0])**0.5, linestyle='--', color='k', label='$O(\sqrt{N})$')
plt.xlabel('$N$')
plt.ylabel('Iterations')
plt.grid(True, which="both", ls="--")
plt.legend()
plt.tight_layout()

#########################
# spsolve vs cg         #
#########################

# Create the log-log plots
plt.figure(figsize=(12, 6))

start = 7

# Plot time vs. DOFs
plt.subplot(1, 2, 1)
plt.loglog(dofs_sp[start:], time_sp[start:], marker='s', linestyle='--', color=cset.blue, label='Sparse / Direct')
plt.loglog(dofs_sp[start:], 0.03*time_sp[start] * (dofs_sp[start:] / dofs_sp[start])**2, linestyle='--', color='k', label='$O(N^2)$')
plt.loglog(dofs_cg[start:], time_cg[start:], marker='o', linestyle='-', color=cset.blue, label='Sparse / Iterative')
plt.loglog(dofs_sp[start:], 0.05*time_sp[start] * (dofs_sp[start:] / dofs_sp[start])**(1.5), linestyle='-', color='k', label=r'$O(N^{\frac{3}{2}})$')
plt.xlabel('$N$')
plt.ylabel('Time [s]')
plt.grid(True, which="both", ls="--")
plt.legend()

# Plot memory vs. DOFs
plt.subplot(1, 2, 2)
plt.loglog(dofs_sp[start:], memory_tot_sp[start:], marker='s', linestyle='--', color=cset.yellow, label='Sparse / Direct')
plt.loglog(dofs_cg[start:], memory_cg[start:], marker='o', linestyle='-', color=cset.yellow, label='Sparse / Iterative')
plt.xlabel('$N$')
plt.ylabel('Memory [MB]')
plt.grid(True, which="both", ls="--")
plt.legend()
plt.tight_layout()

#########################
# Precon                #
#########################

# Create the log-log plots
plt.figure(figsize=(12, 6))

start = 7

# Plot time vs. DOFs
plt.subplot(1, 2, 1)
plt.loglog(dofs_cg[start:-2], time_cg[start:-2], marker='s', linestyle='--', color=cset.blue, label='CG')
plt.loglog(dofs_p[start:], time_p[start:], marker='o', linestyle='-', color=cset.blue, label='CG / Preconditioned')
plt.loglog(dofs_sp[start:], 0.05*time_sp[start] * (dofs_sp[start:] / dofs_sp[start])**(1.5), linestyle='-', color='k', label=r'$O(N^{\frac{3}{2}})$')
plt.xlabel('$N$')
plt.ylabel('Time [s]')
plt.grid(True, which="both", ls="--")
plt.legend()

# Plot memory vs. DOFs
plt.subplot(1, 2, 2)
plt.loglog(dofs_cg[start:-2], memory_cg[start:-2], marker='s', linestyle='--', color=cset.yellow, label='CG')
plt.loglog(dofs_p[start:], memory_p[start:], marker='o', linestyle='-', color=cset.yellow, label='CG / Preconditioned')
plt.xlabel('$N$')
plt.ylabel('Memory [MB]')
plt.grid(True, which="both", ls="--")
plt.legend()
plt.tight_layout()

#########################
# Precon iterations     #
#########################

# Create the log-log plots
plt.figure(figsize=(12, 6))

# Plot iterations
plt.subplot(1, 2, 1)
res = np.load('codes/CGres_1024.npy')
pres = np.load('codes/CGprecon_1024.npy')
plt.loglog(np.arange(res.size), res, linestyle='--', color=cset.blue, label='$N=1024$')
plt.loglog(np.arange(pres.size), pres, linestyle='-', color=cset.blue, label='$N=1024$ (Preconditioned)')
res = np.load('codes/CGres_16384.npy')
pres = np.load('codes/CGprecon_16384.npy')
plt.loglog(np.arange(res.size), res, linestyle='--', color=cset.yellow, label='$N=16384$')
plt.loglog(np.arange(pres.size), pres, linestyle='-', color=cset.yellow, label='$N=16384$ (Preconditioned)')
res = np.load('codes/CGres_262144.npy')
pres = np.load('codes/CGprecon_262144.npy')
plt.loglog(np.arange(res.size), res, linestyle='--', color=cset.red, label='$N=262144$')
plt.loglog(np.arange(pres.size), pres, linestyle='-', color=cset.red, label='$N=262144$ (Preconditioned)')
res = np.load('codes/CGres_4194304.npy')
pres = np.load('codes/CGprecon_4194304.npy')
plt.loglog(np.arange(res.size), res, linestyle='--', color=cset.black, label='$N=4194304$')
plt.loglog(np.arange(pres.size), pres, linestyle='-', color=cset.black, label='$N=4194304$ (Preconditioned)')

plt.xlabel('Iteration')
plt.ylabel('Resdiual')
plt.grid(True, which="both", ls="--")
plt.legend(loc='upper right')
plt.tight_layout()

# Plot time vs. DOFs
plt.subplot(1, 2, 2)
plt.loglog(dofs_cg, iter_cg, marker='s', linestyle='--', color=cset.blue, label='CG iterations')
plt.loglog(dofs_p, iter_p, marker='o', linestyle='-', color=cset.blue, label='CG iterations (Preconditioned)')
# plt.loglog(dofs_cg, 0.1*dofs_cg[0] * (dofs_cg / dofs_cg[0])**0.5, linestyle='--', color='k', label='$O(\sqrt{N})$')
plt.xlabel('$N$')
plt.ylabel('Iterations')
plt.grid(True, which="both", ls="--")
plt.legend()
plt.tight_layout()

#########################
# Sparsity              #
#########################

# Create the log-log plots
plt.figure(figsize=(12, 6))

# Sparsity pattern
A = scipy.sparse.load_npz(f'codes/A_csr_{64}.npz')
plt.subplot(1, 2, 1)
plt.spy(A, markersize=5, color=cset.blue)
plt.xlabel('Sparsity pattern $N=64$')
plt.tight_layout()

# Plot time vs. DOFs
plt.subplot(1, 2, 2)
plt.loglog(dofs_sp, nnz_sp, marker='o', linestyle='-', color=cset.blue, label='Nonzeros')
# Add scaling line with a rate of 1
plt.loglog(dofs_sp, dofs_sp[0] * (dofs_sp / dofs_sp[0]), linestyle='--', color='k', label='$O(N)$')
plt.xlabel('$N$')
plt.ylabel('Nonzeros')
plt.grid(True, which="both", ls="--")
plt.legend()
plt.tight_layout()

#########################
# Jacobi                #
#########################

jacobi = np.loadtxt('codes/jacobi.csv', delimiter=',', comments='//')

# Create the log-log plots
plt.figure(figsize=(6, 6))

# Plot iterations
plt.subplot(1, 1, 1)
plt.loglog(jacobi[:,0], jacobi[:,1], linestyle='-', color=cset.blue)

plt.xlabel('Iteration')
plt.ylabel('Resdiual')
plt.grid(True, which="both", ls="--")
plt.tight_layout()

# Show the plots
plt.show()