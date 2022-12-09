import numpy as np

A = np.random.randint(-1,1,20)
print(A.shape)

A = np.reshape(A, (4,5))
print(A.shape)

print(A)

B = A.T
print(B.shape)

print(B)

P = np.dot(A,B)
print(P.shape)
print(P)
