import numpy as np
import matplotlib.pyplot as plt

arr = np.array([[1, 2, 3, 4, 5],[0, 1, 2, 3, 4]])
y = [i**2 for i in arr[1]]

plt.plot(arr[0], y)
plt.xticks(arr[0])
plt.xlabel("X-Data")
plt.ylabel("Y-Data")
plt.title("Experimental plot")
plt.show()