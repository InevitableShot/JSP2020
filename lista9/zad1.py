import numpy as np


A = [[1, 2, 3, -2, -1], [3, 5, 5, -3, -9],
     [2, 3, 2, 0, -8], [2, 6, 7, -5, 1], [1, 2, 6, -4, -10]]
B = [6, 2, -5, 17, 12]
x, y, z, t, u = np.linalg.solve(A, B)

print(f'x = {x}\ny = {y}\nz = {z}\nt = {t}\nu = {u}\n')
