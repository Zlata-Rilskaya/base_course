import numpy as np
from task_1 import acceleration_of_gravity as g

x0= 0
y0 = 0
V0 = 50

t = np.arange(0, 6, 0.2)

x = x0 + V0*t
y = y0 + V0*t - g*t**2/2

h = [t,x,y]
b = np.array(h)
print(h)


