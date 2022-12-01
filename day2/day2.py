import numpy as np
import pandas as pd

# df = pd.read_csv('input.csv', index_col=0)
file1 = open('input.txt', 'r')

lines = file1.readlines()

count = 0
result = np.array([])
i = 0

for line in lines:
    if line.strip().isnumeric():
        count += int(line.strip())
    else:
        result = np.append(result, count)
        count = 0
        i += 1

result.sort()
result = result[::-1]
print(result[0])
print(np.sum(result[:3]))
