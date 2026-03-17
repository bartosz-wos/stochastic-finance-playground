import numpy as np
from scipy.linalg import solve_sylvester

def solve_vec(A, B, C):
    n = A.shape[0]
    m = B.shape[0]

    In = np.eye(n)
    Im = np.eye(m)
    M = np.kron(Im, A) + np.kron(B.T, In)

    vec = C.flatten(order='F')
    vec_x = np.linalg.solve(M, vec)
    return vec_x.reshape((n, m), order='F')

n, m = 3, 3
A = np.array([[2, 0, 1], [-1, 3, 0], [0, 1, 1]])
B = np.array([[1, 2, 0], [0, 1, -1], [1, 0, 2]])
C = np.array([[1, 0, 1], [1, 1, 0], [0, 0, 1]])

x_vec = solve_vec(A, B, C)
x_sc = solve_sylvester(A, B, C)
print(x_vec)
print(np.allclose(x_vec, x_sc))
