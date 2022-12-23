import re
import numpy as np
from collections import defaultdict
import math
import ast
import networkx as nx
import matplotlib.pyplot as plt
from itertools import permutations


file1 = open('input.txt', 'r')
# file1 = open('exampleinput.txt', 'r')

drops = []
surface = []

lines = file1.readlines()
min_x = 0
max_x = 0
min_y = 0
max_y = 0
min_z = 0
max_z = 0
water = []

for line in lines:
    flow = re.findall(r'-?\d+', line)
    x = int(flow[0])
    y = int(flow[1])
    z = int(flow[2])

    min_x = min(x, min_x)
    max_x = max(x, max_x)
    min_y = min(y, min_y)
    max_y = max(y, max_y)
    min_z = min(z, min_z)
    max_z = max(z, max_z)


    drops.append((x, y, z))
    surface.append((x + 1, y, z))
    surface.append((x - 1, y, z))
    surface.append((x, y + 1, z))
    surface.append((x, y - 1, z))
    surface.append((x, y, z + 1))
    surface.append((x, y, z - 1))

for i in drops:
    surface = list(filter(i.__ne__, surface))

water.append((min_x - 1, min_y - 1, min_z - 1))

for i in water:
    if i[0] + 1 <= max_x + 1:
        loc = (i[0] + 1, i[1], i[2])
        if not drops.__contains__(loc):
            if not water.__contains__(loc):
                water.append(loc)
    if i[0] - 1 >= min_x - 1:
        loc = (i[0] - 1, i[1], i[2])
        if not drops.__contains__(loc):
            if not water.__contains__(loc):
                water.append(loc)
    if i[1] + 1 <= max_y + 1:
        loc = (i[0], i[1] + 1, i[2])
        if not drops.__contains__(loc):
            if not water.__contains__(loc):
                water.append(loc)
    if i[1] - 1 >= min_y - 1:
        loc = (i[0], i[1] - 1, i[2])
        if not drops.__contains__(loc):
            if not water.__contains__(loc):
                water.append(loc)
    if i[2] + 1 <= max_z + 1:
        loc = (i[0], i[1], i[2] + 1)
        if not drops.__contains__(loc):
            if not water.__contains__(loc):
                water.append(loc)
    if i[2] - 1 >= min_z - 1:
        loc = (i[0], i[1], i[2] - 1)
        if not drops.__contains__(loc):
            if not water.__contains__(loc):
                water.append(loc)

for i in surface:
    if not water.__contains__(i):
        surface = list(filter(i.__ne__, surface))

print(len(surface))
