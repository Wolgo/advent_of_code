import numpy as np

def add(num):
    return num + 10

file1 = open('input.txt', 'r')
# file1 = open('exampleinput.txt', 'r')
lines = file1.readlines()

result = np.array([])
count = 0

for line in lines:
    line = line.strip()
    print(line)
    ind = int(len(line) / 2)
    print(line[0:ind])
    print(line[ind + 1: int(len(line))])
    # print(ord("A"))
    cycle = 0
    for x in line[0:ind]:
        if cycle > 0:
            continue
        for y in line[ind: int(len(line))]:
            if cycle > 0:
                continue
            if x == y:
                print(x)
                if x.isupper():
                    cycle += ord(x) - 64 + 26
                else:
                    cycle += ord(x) - 96
                print(cycle)

    count += cycle




result.sort()
result = result[::-1]
#
# addTen = np.vectorize(add)
# result = addTen(result)

print(count)

# print(result[0])
# print(np.sum(result[:3]))
