import numpy as np
 A = np.array([
   [2, 1, 3],
    [1, 0, 2],
    [4, 1, 8]
])
  
 eigenvalues, eigenvectors = np.linalg.eig(A)
 print("Eigenvalues:")
for i, val in enumerate(eigenvalues):
    print(f"λ{i+1} =", val)
  print("\nEigenvectors (each column corresponds to an eigenvalue):")
  for i in range(len(eigenvectors)):
 print(f"v{i+1} =", eigenvectors[:, i])
