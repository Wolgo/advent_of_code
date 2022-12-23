import re
import numpy as np
from collections import defaultdict
import math
import ast
import networkx as nx
import matplotlib.pyplot as plt
from itertools import permutations


file1 = open('input.txt', 'r')
file1 = open('exampleinput.txt', 'r')

drops = []
surface = []

lines = file1.readlines()

for line in lines:
    flow = re.findall(r'-?\d+', line)
    x = int(flow[0])
    y = int(flow[1])
    z = int(flow[2])

    drops.append((x, y, z))
    surface.append((x + 1, y, z))
    surface.append((x - 1, y, z))
    surface.append((x, y + 1, z))
    surface.append((x, y - 1, z))
    surface.append((x, y, z + 1))
    surface.append((x, y, z - 1))

for i in drops:
    surface = list(filter((i).__ne__, surface))

print(len(surface))