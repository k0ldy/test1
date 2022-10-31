import numpy as np
def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]
    
array = np.random.random(10)
print(array)
print(find_nearest(array, value=0.5))
