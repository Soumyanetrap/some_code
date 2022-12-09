import numpy as np
from math import sin, cos, pi

th = 35*pi/180
R = np.array([[cos(th), -sin(th), 0],[sin(th), cos(th), 0],[0, 0, 1]])
x = np.array([2,1,3])

print(R@x)