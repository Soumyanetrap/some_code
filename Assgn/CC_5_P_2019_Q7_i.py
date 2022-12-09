import numpy as np
import math as mt

x = np.random.uniform(0,1,50)

mean = np.mean(x)

msq = np.mean([i**2 for i in x])

rf = mt.sqrt(msq - mean**2)/mean
print("Relative Fluctuation:", rf)