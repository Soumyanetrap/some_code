import numpy as np

arr = np.random.uniform(0, 1, 100)

h1 = arr[0:50]
h2 = arr[50:]
print(h1, h1.shape)
print(h2, h2.shape)
print(abs(np.mean(h1) - np.mean(h2)))