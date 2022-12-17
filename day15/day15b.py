import re
import numpy as np
from collections import defaultdict
import math
import ast

def threshold(n):
    return n[1]

file1 = open('input.txt', 'r')
# file1 = open('exampleinput.txt', 'r')

sensors = []
possible_range = 21
possible_range = 4000001



lines = file1.readlines()
for line in lines:
    divider = re.findall(r'-?\d+', line)
    location = (int(divider[0]), int(divider[1]))

    location_threshold = abs(int(divider[0]) - int(divider[2])) + abs(int(divider[1]) - int(divider[3]))
    sensors.append((location, location_threshold))

i = 0
j = 0
sensors = sorted(sensors, key=threshold)

while i < possible_range:
    while j < possible_range:
        check = False
        for y in sensors:
            leftover = y[1] - (abs(y[0][0] - i) + abs(y[0][1] - j))
            if leftover >= 0:
                check = False
                j += (leftover)
                o = leftover // 4000000
                if o > 0:
                    i += o
                    j = 0
                break
            else:
                check = True
        if check:
            result = (i, j)
        j += 1
    j = 0
    i += 1
    print(i)
print(result)
print(result[0] * 4000000 + result[1])