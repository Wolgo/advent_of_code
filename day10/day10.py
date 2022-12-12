import re
import numpy as np
from collections import defaultdict


def def_value():
    return 0


file1 = open('input.txt', 'r')
# file1 = open('exampleinput.txt', 'r')
lines = file1.readlines()
count = 0

result = 0
cycle = 0

i = 1

for line in lines:

    if re.match('noop', line) is not None:
        cycle += 1
        if cycle == 20:
            result += cycle * i
            print(i)
            print(cycle * i)
        elif (cycle - 20) % 40 == 0:
            result += cycle * i
            print(i)
            print(cycle * i)
    if re.match('addx', line) is not None:

        cycle += 1
        x = re.findall(r'-?\d+', line)
        vel = int(x[0])
        if cycle == 20:
            result += cycle * i
            print(i)
            print(cycle * i)
        elif (cycle - 20) % 40 == 0:
            result += cycle * i
            print(i)
            print(cycle * i)
        cycle += 1
        if cycle == 20:
            result += cycle * i
            print(i)
            print(cycle * i)
        elif (cycle - 20) % 40 == 0:
            result += cycle * i
            print(i)
            print(cycle * i)
        i += vel

print(result)
