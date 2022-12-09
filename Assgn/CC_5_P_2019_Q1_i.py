import numpy as np
import random
import math

array = np.random.uniform(0, 2, 50)
print(array.shape)

mean = np.mean(array)
msq = np.mean([i**2 for i in array])

print("Mean:",mean)
print("Mean Square",msq)

std = math.sqrt(msq - mean**2)
print("Standard Deviation:", std)