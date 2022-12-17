import numpy as np

field = np.ones((3, 3))
field[1, :] = 2
field[2, :] = 3
print(field)
field = np.roll(field, -3)
field[2:,:] = 0
print(field)