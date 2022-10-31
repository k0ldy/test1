import numpy as np
m = np.zeros([8, 8])
m[::2, ::2] = 1
m[1::2, 1::2] = 1
print(m)
