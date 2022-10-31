import numpy as np
m = np.random.randint(low=1, high=100, size=[3,3])
print('массив:')
print(m)
print('средние значения каждой строки матрицы')
print(m.mean(axis=1))
