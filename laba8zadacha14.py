import numpy as np
a = np.array([1,2,3,4,5])
b = np.array([1,2,3,4,6])
print(np.array_equal(a,b))
print(np.allclose(a,b))
