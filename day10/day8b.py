import re
import numpy as np
from collections import defaultdict


def def_value():
    return 0


file1 = open('input.txt', 'r')
# file1 = open('exampleinput.txt', 'r')
lines = file1.readlines()
count = 0

result = ""
cycle = 0

i = 1

for line in lines:

    if re.match('noop', line) is not None:
        cycle += 1
        if abs(((cycle - 1) % 40) - i) <= 1:
            result += "#"
        else:
            result += "."
        if cycle % 40 == 0:
            print(result)
            result = ""

    if re.match('addx', line) is not None:

        cycle += 1
        x = re.findall(r'-?\d+', line)
        vel = int(x[0])
        if abs(((cycle - 1) % 40) - i) <= 1:
            result += "#"
        else:
            result += "."
        if cycle % 40 == 0:
            print(result)
            result = ""
        cycle += 1
        if abs(((cycle - 1) % 40) - i) <= 1:
            result += "#"
        else:
            result += "."
        if cycle % 40 == 0:
            print(result)
            result = ""
        i += vel

