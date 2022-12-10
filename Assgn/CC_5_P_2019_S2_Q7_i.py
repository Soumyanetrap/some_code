import numpy as np

A = np.array([[1, -2],[4, 5]])
I = np.eye(A.shape[0])
eq = A@A -6*A + 13*I
print(eq)

#Since value of eq = 0, the matrix satisfies its characteristic polynomial equated to zero