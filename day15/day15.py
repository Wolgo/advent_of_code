import re
import numpy as np
from collections import defaultdict
import math
import ast

file1 = open('input.txt', 'r')
# file1 = open('exampleinput.txt', 'r')

sensors = []
row = 10
row = 2000000
result = set([])
known_beacons = set([])

lines = file1.readlines()
for line in lines:
    divider = re.findall(r'-?\d+', line)
    location = (int(divider[0]), int(divider[1]))
    if int(divider[3]) == row:
        known_beacons.add(int(divider[2]))

    location_threshold = abs(int(divider[0]) - int(divider[2])) + abs(int(divider[1]) - int(divider[3]))
    sensors.append((location, location_threshold))

print(known_beacons)

print(sensors)

for y in sensors:
    leftover = y[1] - abs(y[0][1] - row)
    if leftover > 0:
        result.update(range(y[0][0] - leftover, y[0][0] + leftover + 1))

result = list(result - known_beacons)
print(result)
print(len(result))

