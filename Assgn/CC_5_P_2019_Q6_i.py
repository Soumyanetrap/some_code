import numpy as np
from math import sqrt, cos, sin, pi

from scipy.integrate import simps
from scipy.special import jn, fresnel


x = np.random.uniform(0 , 4.5, 20)
x.sort()
print(x)

I = simps(jn(2.5,x))
print(I)

S,C = fresnel(3/sqrt(pi))

I_true = sqrt(2/pi)*(18*sqrt(2)/27.0*cos(4.5) - 4*sqrt(2)/27.0*sin(4.5)+sqrt(2*pi)*S)

print(I_true)