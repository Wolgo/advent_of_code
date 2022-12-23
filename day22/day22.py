import re
import numpy as np
from collections import defaultdict
import math
import ast
import networkx as nx
import matplotlib.pyplot as plt
from itertools import permutations
from itertools import cycle

file1 = open('input.txt', 'r')
# file1 = open('exampleinput.txt', 'r')

org_list = []
mixed_list = []
i = 0

lines = file1.readlines()
dict = {}

x_size = 0
y_size = 0

for line in lines:
    if len(line) == 1:
        break
    x_size = max(x_size, len(line) - 1)
    y_size += 1

print(x_size)
print(y_size)

map = np.zeros((y_size, x_size))


file1 = open('input.txt', 'r')
# file1 = open('exampleinput.txt', 'r')
lines = file1.readlines()
i = 0

for line in lines:
    j = 0
    for x in line:
        if x == ".":
            map[i, j] = 1
        if x == "#":
            map[i, j] = 2
        j += 1
    i += 1
    if i == y_size:
        break


loc = np.where(map == 1)
y_curr = loc[0][0]
x_curr = loc[1][0]
heading = "right"
# print(map)
path = re.findall(r'\d+|[LR]', lines[y_size + 1])
for i in path:
    print(i)
    if i.isnumeric():
        x = int(i)
        for j in range(0, x):
            if heading == "right":
                x_scan = x_curr + 1
                x_scan %= x_size
                while map[y_curr, x_scan] == 0:
                    x_scan += 1
                    x_scan %= x_size
                if map[y_curr, x_scan] == 1:
                    x_curr = x_scan
            if heading == "left":
                x_scan = x_curr - 1
                x_scan %= x_size
                while map[y_curr, x_scan] == 0:
                    x_scan -= 1
                    x_scan %= x_size
                if map[y_curr, x_scan] == 1:
                    x_curr = x_scan
            if heading == "up":
                y_scan = y_curr - 1
                y_scan %= y_size
                while map[y_scan, x_curr] == 0:
                    y_scan -= 1
                    y_scan %= y_size
                if map[y_scan, x_curr] == 1:
                    y_curr = y_scan
            if heading == "down":
                y_scan = y_curr + 1
                y_scan %= y_size
                while map[y_scan, x_curr] == 0:
                    y_scan += 1
                    y_scan %= y_size
                if map[y_scan, x_curr] == 1:
                    y_curr = y_scan
    elif i == "R":
        if heading == "right":
            heading = "down"
        elif heading == "down":
            heading = "left"
        elif heading == "left":
            heading = "up"
        elif heading == "up":
            heading = "right"
    elif i == "L":
        if heading == "right":
            heading = "up"
        elif heading == "down":
            heading = "right"
        elif heading == "left":
            heading = "down"
        elif heading == "up":
            heading = "left"
    print(y_curr, x_curr)

heading_value = 0
if heading == "right":
    heading_value = 0
elif heading == "down":
    heading_value = 1
elif heading == "left":
    heading_value = 2
elif heading == "up":
    heading_value = 3
print(1000 * (y_curr + 1) + 4 * (x_curr + 1) + heading_value)

