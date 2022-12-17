import re
import numpy as np
from collections import defaultdict
import math
import ast
import networkx as nx
import matplotlib.pyplot as plt
from itertools import cycle



file1 = open('input.txt', 'r')
file1 = open('exampleinput.txt', 'r')

lines = file1.readlines()
max_flow = 0
for line in lines:
    flow = re.findall(r'[<>]', line)

print(len(flow))
cycle_length = len(flow)
cycle_count = 0
flow_iterator = cycle(flow)
field = np.zeros((10000, 7))

field[0, :] = 1
highest_rock = 0
# print(field)
rock_type = 1
rock = []
for i in range(0, 2022):

    # print(highest_rock)
    # print(i)

    if rock_type == 5:
        rock = [[highest_rock + 4, 3], [highest_rock + 4, 2], [highest_rock + 5, 3], [highest_rock + 5, 2]]
        rock_type = 1
    elif rock_type == 4:
        rock = [[highest_rock + 4, 2], [highest_rock + 5, 2], [highest_rock + 6, 2], [highest_rock + 7, 2]]
        rock_type = 5
    elif rock_type == 3:
        rock = [[highest_rock + 4, 4], [highest_rock + 4, 3], [highest_rock + 4, 2], [highest_rock + 5, 4], [highest_rock + 6, 4]]
        rock_type = 4
    elif rock_type == 2:
        rock = [[highest_rock + 4, 3], [highest_rock + 5, 3], [highest_rock + 6, 3], [highest_rock + 5, 4], [highest_rock + 5, 2]]
        rock_type = 3
    elif rock_type == 1:
        if cycle_count % cycle_length == 0:
            print(cycle_count)
        rock = [[highest_rock + 4, 4], [highest_rock + 4, 3], [highest_rock + 4, 2], [highest_rock + 4, 5]]
        rock_type = 2

    falling = True
    while falling:
        # print(highest_rock)
        # print(rock)
        wind_direction = next(flow_iterator)
        cycle_count += 1
        safe_to_move = True
        if wind_direction == "<":
            for j in rock:
                if j[1] == 0:
                    safe_to_move = False
                elif field[j[0], j[1] - 1] == 1:
                    safe_to_move = False
            if safe_to_move:
                for j in rock:
                    j[1] -= 1
        elif wind_direction == ">":
            for j in rock:
                if j[1] == 6:
                    safe_to_move = False
                elif field[j[0], j[1] + 1] == 1:
                    safe_to_move = False
            if safe_to_move:
                for j in rock:
                    j[1] += 1
        for j in rock:
            if field[j[0]-1, j[1]] == 1:
                falling = False
        if falling:
            for j in rock:
                j[0] -= 1
        elif falling is False:
            for j in rock:
                highest_rock = max(highest_rock, j[0])
                field[j[0], j[1]] = 1
            # print(field)


print(highest_rock)
