import numpy as np


def add(num):
    return num + 10


file1 = open('input.txt', 'r')
# file1 = open('exampleinput.txt', 'r')
lines = file1.readlines()

result = np.array([])
count = 0

for x in range(int(len(lines) / 3)):
    line1 = lines[x * 3 + 0]
    line2 = lines[x * 3 + 1]
    line3 = lines[x * 3 + 2]

    cycle = 0
    for x in line1:
        if cycle > 0:
            continue
        for y in line2:
            if cycle > 0:
                continue
            for z in line3:
                if cycle > 0:
                    continue
                if x == y == z:
                    print(x)
                    if x.isupper():
                        cycle += ord(x) - 64 + 26
                    else:
                        cycle += ord(x) - 96
                    print(cycle)

    count += cycle


print(count)

# print(result[0])
# print(np.sum(result[:3]))
