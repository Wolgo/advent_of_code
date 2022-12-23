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
file2 = open('input.txt', 'r')
# file1 = open('inputb.txt', 'r')
# file2 = open('inputb.txt', 'r')


def cubing(x_scan, y_scan, heading, x_size, y_size):
    if heading == "up":
        if x_scan < x_size/3:
            print("up 1")
            new_heading = "right"
            new_x_scan = x_size / 3
            new_y_scan = y_size / 4 + x_scan
        elif x_scan < 2 * x_size / 3:
            print("up 2")
            new_heading = "right"
            new_x_scan = 0
            new_y_scan = y_size / 4 * 3 + x_scan - x_size / 3
        elif x_scan >= 2 * x_size / 3:
            print("up 3")
            new_heading = "up"
            new_x_scan = x_scan - 2 * x_size / 3
            new_y_scan = y_size - 1
        return int(new_x_scan), int(new_y_scan), new_heading
    if heading == "down":
        if x_scan < x_size/3:
            print("down 1")
            new_heading = "down"
            new_x_scan = 2 * x_size / 3 + x_scan
            new_y_scan = 0
        elif x_scan < 2 * x_size / 3:
            print("down 2")
            new_heading = "left"
            new_x_scan = x_size / 3 - 1
            new_y_scan = x_scan + y_size / 4 * 3 - x_size / 3
        elif x_scan >= 2 * x_size / 3:
            print("down 3")
            new_heading = "left"
            new_x_scan = 2 * x_size / 3 - 1
            new_y_scan = y_size / 4 + x_scan - x_size / 3 * 2
        return int(new_x_scan), int(new_y_scan), new_heading
    if heading == "right":
        if y_scan < y_size/4:
            print("right 1")
            new_heading = "left"
            new_x_scan = 2 * x_size / 3 - 1
            new_y_scan = 3 * y_size / 4 - y_scan - 1
        elif y_scan < 2 * y_size / 4:
            print("right 2")
            new_heading = "up"
            new_x_scan = x_size / 3 * 2 + y_scan - y_size / 4
            new_y_scan = y_size / 4 - 1
        elif y_scan < 3 * y_size / 4:
            print("right 3")
            new_heading = "left"
            new_x_scan = x_size - 1
            new_y_scan = 3 * y_size / 4 - y_scan - 1
        elif y_scan >= 3 * y_size / 4:
            print("right 4")
            new_heading = "up"
            new_x_scan = x_size / 3 + y_scan - y_size / 4 * 3
            new_y_scan = y_size / 4 * 3 - 1
        return int(new_x_scan), int(new_y_scan), new_heading
    if heading == "left":
        if y_scan < y_size/4:
            print("left 1")
            new_heading = "right"
            new_x_scan = 0
            new_y_scan = 3 * y_size / 4 - y_scan - 1
        elif y_scan < 2 * y_size / 4:
            print("left 2")
            new_heading = "down"
            new_x_scan = y_scan - y_size / 4
            new_y_scan = y_size / 4 * 2
        elif y_scan < 3 * y_size / 4:
            print("left 3")
            new_heading = "right"
            new_x_scan = x_size / 3
            new_y_scan = y_size / 4 * 3 - y_scan - 1
        elif y_scan >= 3 * y_size / 4:
            print("left 4")
            new_heading = "down"
            new_x_scan = x_size / 3 + y_scan - y_size / 4 * 3
            new_y_scan = 0
        return int(new_x_scan), int(new_y_scan), new_heading

lines = file1.readlines()
x_size = 0
y_size = 0

for line in lines:
    if len(line) == 1:
        break
    x_size = max(x_size, len(line) - 1)
    y_size += 1

print(x_size, y_size)
map = np.zeros((y_size, x_size))


lines = file2.readlines()
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
            x_scan = x_curr
            y_scan = y_curr
            scan_heading = heading
            if heading == "right":
                x_scan += 1
                x_scan %= x_size
            if heading == "left":
                x_scan -= 1
                x_scan %= x_size
            if heading == "up":
                y_scan -= 1
                y_scan %= y_size
            if heading == "down":
                y_scan += 1
                y_scan %= y_size
            if map[y_scan, x_scan] == 0:
                x_scan, y_scan, scan_heading = cubing(x_curr, y_curr, heading, x_size, y_size)
            if map[y_scan, x_scan] == 1:
                x_curr = x_scan
                y_curr = y_scan
                heading = scan_heading
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

