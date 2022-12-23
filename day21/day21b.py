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

def sub(i, dict):
    if isinstance(dict[i], float) or isinstance(dict[i], int) or dict[i] == "humn":
        return dict[i]
    else:
        a = sub(dict[i][0], dict)
        b = sub(dict[i][2], dict)
        if (isinstance(a, int) or isinstance(a, float)) and (isinstance(b, int) or isinstance(b, float)):
            if dict[i][1] == "+":
                return a + b
            elif dict[i][1] == "-":
                return a - b
            elif dict[i][1] == "*":
                return a * b
            elif dict[i][1] == "/":
                return a / b
        return (a, dict[i][1], b)


def reduce(x):
    print(x)
    if isinstance(x, float) or isinstance(x, int):
        return x
    a = x[0]
    c = x[2]
    if a == "humn":
        return c

    if isinstance(a[0], float) or isinstance(a[0], int):
        if a[1] == "+":
            return reduce((a[2], "=", c - a[0]))
        if a[1] == "-":
            return reduce((a[2], "=", a[0] - c))
        if a[1] == "*":
            return reduce((a[2], "=", c / a[0]))
        if a[1] == "/":
            return reduce((a[2], "=", a[0] / c))

    if isinstance(a[2], float) or isinstance(a[2], int):
        if a[1] == "+":
            return reduce((a[0], "=", c - a[2]))
        if a[1] == "-":
            return reduce((a[0], "=", a[2] + c))
        if a[1] == "*":
            return reduce((a[0], "=", c / a[2]))
        if a[1] == "/":
            return reduce((a[0], "=", a[2] * c))

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

dict["humn"] = "humn"
dict["root"] = (dict["root"][0], "=", dict["root"][2])
print(reduce(sub("root", dict)))
