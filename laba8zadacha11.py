import numpy as np
m = np.random.randint(low=4, high=7, size=[5,5])
m[(m > 4) & (m < 7)] *=-1
print(m)
