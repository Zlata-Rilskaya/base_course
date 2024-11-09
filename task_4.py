import numpy as np

N = 3
M = 5

trigonometry_array = np.sin(np.arange(N)[:, None] * N + np.arange(M) + 1)

trigonometry_array[trigonometry_array < 0] = 0

print(trigonometry_array)