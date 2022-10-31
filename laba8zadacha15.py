import numpy as np
a = np.array([[0, 1], [2, 3], [4, 5], [6, 7], [9, 8]])
b = np.zeros_like(a)
b[np.arange(len(a)), a.argmax(1)] = -1
print(b)
