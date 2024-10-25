import math 
import task_1
from task_1 import acceleration_of_gravity as g

x0 = 0
y0 = 0
v0 = 15

for t in range(0, 6, 1):
    x = x0 + v0 * t
    y = y0 + v0 * t - (g * t**2 / 2)

print(x, y)
