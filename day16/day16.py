import re
import numpy as np
from collections import defaultdict
import math
import ast
import networkx as nx
import matplotlib.pyplot as plt
from itertools import permutations


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

result = maxflow(30, 0, max_flow, sp, flowing_valves, 0, ("AA", 0))

print(result)
