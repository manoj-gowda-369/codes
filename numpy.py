import numpy as np

 A = np.array([
    [2, 1, 3],
    [1, 0, 2],
    [4, 1, 8]

])
det_A = np.linalg.det(A)
print("Determinant of A:", det_A)
if det_A != 0:
    A_inv = np.linalg.inv(A)
 print("\nInverse of A:\n", A_inv)
 identity_check = np.dot(A, A_inv)
 print("\nA * A_inv (should be Identity):\n", identity_check)

