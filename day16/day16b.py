import re
import numpy as np
from collections import defaultdict
import math
import ast
import networkx as nx
import matplotlib.pyplot as plt
import itertools


def maxflow(time, flow, max_flow, mov, options, best_result, current_node):
    if max_flow * time + flow < best_result:
        return best_result

    for i in options:
        new_time = time - mov[current_node[0]][i[0]] - 1
        if new_time <= 0:
            best_result = max(flow, best_result)
        new_flow = flow + i[1] * new_time
        new_options = options.copy()
        new_options.remove(i)
        if new_options != []:
            best_result = maxflow(new_time, new_flow, max_flow, mov, new_options, best_result, i)
        elif new_flow > best_result:
            best_result = new_flow

    return best_result


G = nx.Graph()

file1 = open('input.txt', 'r')
# file1 = open('exampleinput.txt', 'r')

flowing_valves = []
solution = ["AA"]
lines = file1.readlines()
max_flow = 0
for line in lines:
    valves = re.findall(r'[A-Z]{2}', line)
    flow = re.findall(r'\d+', line)
    if int(flow[0]) > 0:
        max_flow += int(flow[0])
        flowing_valves.append((valves[0], int(flow[0])))
    for i in range(1, len(valves)):
        G.add_edge(valves[0], valves[i])
print(flowing_valves)
print(solution)

sp = dict(nx.all_pairs_shortest_path_length(G))
print(sp)

result = 0
subsets = [v for a in range(len(flowing_valves)) for v in itertools.combinations(flowing_valves, a)]
subsets = set(subsets)
x = 0
for i in subsets:
    print(x, " out of ", len(subsets))
    j = set(i)
    q = list(set(flowing_valves) - j)
    max_a = 0
    max_b = 0
    for a in j:
        max_a += a[1]
    for b in q:
        max_b += b[1]

    temp_result = maxflow(26, 0, max_a, sp, list(j), 0, ("AA", 0))
    temp_result += maxflow(26, 0, max_b, sp, q, 0, ("AA", 0))
    result = max(result, temp_result)
    x += 1

print(result)
