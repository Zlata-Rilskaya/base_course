import numpy as np 
from task_1 import acceleration_of_gravity as g
from task_1 import Plancks_constant as ℏ
from task_1 import Boltzmann_constant as k
from task_1 import Euler_number as e

h = 100
alpha = np.radians(45)
beta = np.radians(35)

v = np.sqrt((g * h * np.tan(beta)**2) / (2 * np.cos(alpha)**2 * (1 - np.tan(beta) * np.tan(alpha))))
print(v)

T = 110
ε = 300

N = (2/np.sqrt(np.pi))*( ℏ / k*T**3/2 )* (e**-ε/k*T * ε**T/2)
print(N)