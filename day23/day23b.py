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

for round in range(1, 10001):
    print(elves)
    someone_moving = False
    for elf in elves:
        moving = False
        if elves.__contains__((elf[0] - 1, elf[1] - 1)) or elves.__contains__((elf[0] - 1, elf[1])) or elves.__contains__((elf[0] - 1, elf[1] + 1)) or elves.__contains__((elf[0], elf[1] - 1)) or elves.__contains__((elf[0], elf[1] + 1)) or elves.__contains__((elf[0] + 1, elf[1] - 1)) or elves.__contains__((elf[0] + 1, elf[1])) or elves.__contains__((elf[0] + 1, elf[1] + 1)):
            for x in check_order:
                if x == "N" and not moving:
                    if not elves.__contains__((elf[0] - 1, elf[1] - 1)) and not elves.__contains__((elf[0], elf[1] - 1)) and not elves.__contains__((elf[0] + 1, elf[1] - 1)):
                        proposed_directions.append((elf[0], elf[1] - 1))
                        moving = True
                        someone_moving = True
                elif x == "S" and not moving:
                    if not elves.__contains__((elf[0] - 1, elf[1] + 1)) and not elves.__contains__((elf[0], elf[1] + 1)) and not elves.__contains__((elf[0] + 1, elf[1] + 1)):
                        proposed_directions.append((elf[0], elf[1] + 1))
                        moving = True
                        someone_moving = True
                elif x == "W" and not moving:
                    if not elves.__contains__((elf[0] - 1, elf[1] - 1)) and not elves.__contains__((elf[0] - 1, elf[1])) and not elves.__contains__((elf[0] - 1, elf[1] + 1)):
                        proposed_directions.append((elf[0] - 1, elf[1]))
                        moving = True
                        someone_moving = True
                elif x == "E" and not moving:
                    if not elves.__contains__((elf[0] + 1, elf[1] - 1)) and not elves.__contains__((elf[0] + 1, elf[1])) and not elves.__contains__((elf[0] + 1, elf[1] + 1)):
                        proposed_directions.append((elf[0] + 1, elf[1]))
                        moving = True
                        someone_moving = True
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

    if not someone_moving:
        print(round)
        exit()

    elves = new_elves
    proposed_directions = []
    dir_change = check_order[0]
    check_order.remove(dir_change)
    check_order.append(dir_change)

