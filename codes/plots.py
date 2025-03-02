import numpy as np
import matplotlib.pyplot as plt

# Load the data from the CSV file
data = np.loadtxt('codes/direct.csv', delimiter=',', comments='//')
data_sp = np.loadtxt('codes/sparse.csv', delimiter=',', comments='//')

# Extract columns
dofs = data[:, 0]
time = data[:, 1]
memory = data[:, 2]

dofs_sp = data_sp[:, 0]
time_sp = data_sp[:, 1]
memory_mat_sp = data_sp[:, 2]
memory_tot_sp = data_sp[:, 3]

#########################
# Direct solver results #
#########################

# Create the log-log plots
plt.figure(figsize=(12, 6))

# Plot time vs. DOFs
plt.subplot(1, 2, 1)
plt.loglog(dofs, time, marker='o', linestyle='-', color='b', label='Time')
# Add scaling line with a rate of 3
plt.loglog(dofs, 0.01*time[0] * (dofs / dofs[0])**3, linestyle='--', color='k', label='$O(N^3)$')
plt.xlabel('$N$')
plt.ylabel('Time [s]')
plt.grid(True, which="both", ls="--")
plt.legend()

# Plot memory vs. DOFs
plt.subplot(1, 2, 2)
plt.loglog(dofs, memory, marker='o', linestyle='-', color='r', label='Memory')
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
plt.loglog(dofs_sp, time_sp, marker='o', linestyle='-', color='b', label='Time')
# Add scaling line with a rate of 2
plt.loglog(dofs_sp, 0.00001*time_sp[0] * (dofs_sp / dofs_sp[0])**2, linestyle='--', color='k', label='$O(N^2)$')
plt.xlabel('$N$')
plt.ylabel('Time [s]')
plt.grid(True, which="both", ls="--")
plt.legend()

# Plot memory vs. DOFs
plt.subplot(1, 2, 2)
plt.loglog(dofs_sp, memory_mat_sp, marker='.', linestyle='--', color='r', label='Memory (Matrix)')
plt.loglog(dofs_sp, memory_tot_sp, marker='o', linestyle='-', color='r', label='Memory (Total)')
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
plt.loglog(dofs, time, marker='o', linestyle='-', color='b', label='Dense')
plt.loglog(dofs_sp, time_sp, marker='d', linestyle='--', color='b', label='Sparse')
plt.xlabel('$N$')
plt.ylabel('Time [s]')
plt.grid(True, which="both", ls="--")
plt.legend()

# Plot memory vs. DOFs
plt.subplot(1, 2, 2)
plt.loglog(dofs, memory, marker='o', linestyle='-', color='r', label='Dense')
plt.loglog(dofs_sp, memory_tot_sp, marker='d', linestyle='--', color='r', label='Sparse')
plt.xlabel('$N$')
plt.ylabel('Memory [MB]')
plt.grid(True, which="both", ls="--")
plt.legend()
plt.tight_layout()


# Show the plots
plt.show()