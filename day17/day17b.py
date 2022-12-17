import re
import numpy as np
from collections import defaultdict
import math
import ast
import networkx as nx
import matplotlib.pyplot as plt
from itertools import cycle

file1 = open('input.txt', 'r')
# file1 = open('exampleinput.txt', 'r')

lines = file1.readlines()
max_flow = 0
for line in lines:
    flow = re.findall(r'[<>]', line)

cycle_length = len(flow)
cycle_count = 0
flow_iterator = cycle(flow)
field = np.zeros((10000000, 7))

field[0, :] = 1
highest_rock = 0
# print(field)
rock_type = 1
rock = []
bicyle = []
hi_ro = []
tricky = 0
magic_number = 28 # Start of cycle example
magic_number = 14 # Start of cycle puzzle. Yeah, i did manually find this :)
i_0 = 0
i_1 = 0
h_0 = 0
h_1 = 0
for i in range(0, 10000000):

    # print(highest_rock)
    # print(i)
    hi_ro.append(highest_rock)

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
        else:
            bicyle.append(cycle_count)
            print(bicyle)
            if cycle_count == magic_number and tricky == 0:
                tricky = 1
                print(highest_rock)
                i_0 = i
                print(i)
                h_0 = highest_rock
            elif cycle_count == magic_number and tricky == 1:
                tricky = 2
                y = bicyle.index(magic_number)
                print(highest_rock)
                i_1 = i
                h_1 = highest_rock
                print(i)
                print(h_0)
                print((h_1 - h_0) * ((1000000000000 - i_0) // (i_1 - i_0)) + h_0 + hi_ro[i_0 + (1000000000000 - i_0) % (i_1 - i_0)] - hi_ro[i_0])
                exit()
            # print(hi_ro)
        rock = [[highest_rock + 4, 4], [highest_rock + 4, 3], [highest_rock + 4, 2], [highest_rock + 4, 5]]
        rock_type = 2

    falling = True
    while falling:
        # print(highest_rock)
        # print(rock)
        wind_direction = next(flow_iterator)
        cycle_count += 1
        cycle_count = cycle_count % cycle_length
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
