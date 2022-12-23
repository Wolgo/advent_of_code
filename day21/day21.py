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


for line in lines:
    flow = re.findall(r'[a-z\d]{4}|[\+\-\/\*]|\d+', line)
    if len(flow) == 2:
        dict[flow[0]] = int(flow[1])
    if len(flow) == 4:
        dict[flow[0]] = (flow[1], flow[2], flow[3])

while True:
    for i in dict:
        if i == "root":
            if isinstance(dict[i], int) or isinstance(dict[i], float):
                print(dict[i])
                exit()
        if isinstance(dict[i], tuple):
            a = dict[dict[i][0]]
            b = dict[dict[i][2]]
            if (isinstance(a, int) or isinstance(a, float)) and (isinstance(b, int) or isinstance(b, float)):
                if dict[i][1] == "+":
                    dict[i] = a + b
                elif dict[i][1] == "-":
                    dict[i] = a - b
                elif dict[i][1] == "*":
                    dict[i] = a * b
                elif dict[i][1] == "/":
                    dict[i] = a / b
