import numpy as np
arr = np.array([2, 0,  1, 5,
                4, 1, 9])
print(arr)
sorted_index_array = np.argsort(arr)
sorted_array = arr[sorted_index_array]
  
print(sorted_array)
n = 1
rslt = sorted_array[-n : ]
print("{} НАИБОЛЬШЕЕ:".format(n), rslt[0])
