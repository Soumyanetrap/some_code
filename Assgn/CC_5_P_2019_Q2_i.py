import matplotlib.pyplot as plt

import math as mt

x = [i for i in range(0,10)]
y1 = [i**2 for i in x]
y2 = [mt.exp(i/2) for i in x]
y3 = [5*i for i in x]

plt.plot(x, y1, label="y=x^2")
plt.plot(x, y2, label="y=e^(x/2)")
plt.plot(x, y3, label="y=5x")
plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.title("My Graph")
plt.show()