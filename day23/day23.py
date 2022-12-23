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
# file1 = open('small_example.txt', 'r')

elves = []
proposed_directions = []
check_order = ["N", "S", "W", "E"]

lines = file1.readlines()

i = 0
for line in lines:
    j = 0
    for x in line:
        if x == "#":
            elves.append((j, i))
        j += 1
    i += 1

for round in range(0, 10):
    print(elves)
    for elf in elves:
        moving = False
        if elves.__contains__((elf[0] - 1, elf[1] - 1)) or elves.__contains__((elf[0] - 1, elf[1])) or elves.__contains__((elf[0] - 1, elf[1] + 1)) or elves.__contains__((elf[0], elf[1] - 1)) or elves.__contains__((elf[0], elf[1] + 1)) or elves.__contains__((elf[0] + 1, elf[1] - 1)) or elves.__contains__((elf[0] + 1, elf[1])) or elves.__contains__((elf[0] + 1, elf[1] + 1)):
            for x in check_order:
                if x == "N" and not moving:
                    if not elves.__contains__((elf[0] - 1, elf[1] - 1)) and not elves.__contains__((elf[0], elf[1] - 1)) and not elves.__contains__((elf[0] + 1, elf[1] - 1)):
                        proposed_directions.append((elf[0], elf[1] - 1))
                        moving = True
                elif x == "S" and not moving:
                    if not elves.__contains__((elf[0] - 1, elf[1] + 1)) and not elves.__contains__((elf[0], elf[1] + 1)) and not elves.__contains__((elf[0] + 1, elf[1] + 1)):
                        proposed_directions.append((elf[0], elf[1] + 1))
                        moving = True
                elif x == "W" and not moving:
                    if not elves.__contains__((elf[0] - 1, elf[1] - 1)) and not elves.__contains__((elf[0] - 1, elf[1])) and not elves.__contains__((elf[0] - 1, elf[1] + 1)):
                        proposed_directions.append((elf[0] - 1, elf[1]))
                        moving = True
                elif x == "E" and not moving:
                    if not elves.__contains__((elf[0] + 1, elf[1] - 1)) and not elves.__contains__((elf[0] + 1, elf[1])) and not elves.__contains__((elf[0] + 1, elf[1] + 1)):
                        proposed_directions.append((elf[0] + 1, elf[1]))
                        moving = True
        if not moving:
            proposed_directions.append(elf)

    i = 0
    new_elves = []
    for elf in elves:
        if proposed_directions.count(proposed_directions[i]) > 1:
            new_elves.append(elf)
        else:
            new_elves.append(proposed_directions[i])
        i += 1

    elves = new_elves
    proposed_directions = []
    dir_change = check_order[0]
    check_order.remove(dir_change)
    check_order.append(dir_change)

max_x = elves[0][0]
min_x = elves[0][0]
max_y = elves[0][1]
min_y = elves[0][1]

for elf in elves:
    max_x = max(elf[0], max_x)
    min_x = min(elf[0], min_x)
    max_y = max(elf[1], max_y)
    min_y = min(elf[1], min_y)

print(min_x, max_x, min_y, max_y)

print(abs(max_x + 1 - min_x) * abs(max_y + 1 - min_y) - len(elves))
