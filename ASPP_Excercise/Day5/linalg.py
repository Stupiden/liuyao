import numpy as np
from scipy import linalg

# a. Define matrix A
A = np.array([
    [1, -2, 3],
    [4, 5, 6],
    [7, 1, 9]
], dtype=float)

# b. Define vector b
b = np.array([1, 2, 3], dtype=float)

print("A =")
print(A)
print("\nb =")
print(b)

# c. Solve A x = b
x = linalg.solve(A, b)

print("\nSolution x of A x = b:")
print(x)

check = A @ x

print("A @ x =")
print(check)

print("\nOriginal b =")
print(b)

print("\nCheck result:")
print(np.allclose(check, b))

B = np.random.rand(3, 3)
X = linalg.solve(A, B)
print("\nSolution X =")
print(X)

eigenvalues, eigenvectors = linalg.eig(A)

print("Eigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)

# g. Inverse and determinant
A_inv = linalg.inv(A)
det_A = linalg.det(A)

print("Inverse of A:")
print(A_inv)

print("\nDeterminant of A:")
print(det_A)

# h. Norms of A with different orders
print("\nNorms of A:")
print("Frobenius norm:", linalg.norm(A))
print("1-norm:", linalg.norm(A, 1))
print("Infinity norm:", linalg.norm(A, np.inf))
print("2-norm:", linalg.norm(A, 2))