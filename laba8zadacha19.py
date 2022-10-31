import numpy as np
a = np.array([[4,3,1], [5,7,0], [9,9,3], [8,2,4]])

print(a) 
print() 

a[[0, 2]] = a[[2, 0]]
print(a)
