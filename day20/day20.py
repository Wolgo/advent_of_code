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



for line in lines:
    flow = re.findall(r'-?\d+', line)
    org_list.append([int(flow[0]), i])
    mixed_list.append([int(flow[0]), i])
    i += 1

# print(mixed_list)
for x in org_list:
    j = mixed_list.index(x)
    mixed_list.remove(x)
    new_index = (j + x[0]) % len(mixed_list)
    mixed_list.insert(new_index, x)
    # print(mixed_list)

iterator = cycle(mixed_list)
j = 0
found_zero = False
result = 0
while True:
    current = iterator.__next__()
    # print(current)
    if found_zero:
        j += 1
        if j % 1000 == 0:
            result += current[0]
            print(current[0])
        if j == 3000:
            print(result)
            exit()
    if current[0] == 0:
        found_zero = True


