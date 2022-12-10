import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

C = A@B

D = B.T@A.T

print(C.T)
print(D)
#since both matrix (AB)^T and B^TA^T are equal, we conclude (AB)^T = B^TA^T