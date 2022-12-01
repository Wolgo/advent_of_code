import numpy as np

file1 = open('input.txt', 'r')
lines = file1.readlines()

result = np.array([])
count = 0

for line in lines:
    if line.strip().isnumeric():
        count += int(line.strip())
    else:
        result = np.append(result, count)
        count = 0

result.sort()
result = result[::-1]

print(result[0])
print(np.sum(result[:3]))
