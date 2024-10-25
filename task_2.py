import numpy as np 

import task_1
from task_1 import acceleration_of_gravity as g

h = 100
alpha = np.radians(45)
beta = np.radians(35)
g = 9.8

v = np.sqrt((g * h * np.tan(beta)**2) / (2 * np.cos(alpha)**2 * (1 - np.tan(beta) * np.tan(alpha))))
print(v)

import numpy as np  

import task_1
from task_1 import ℏ
from task_1 import k
from task_1 import e

T = 200
k = 1,380649 * 10**23
ε = 300
N = (2/np.sqrt(np. pi))*( ℏ / k*T^1,5 )* (e**-ε/k*T * ε**T//2)

print(N)