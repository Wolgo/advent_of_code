import re
import numpy as np
from collections import defaultdict
import math
import ast
import networkx as nx
import matplotlib.pyplot as plt
from itertools import permutations

file1 = open('input.txt', 'r')
file1 = open('exampleinput.txt', 'r')

blueprint = []
minutes = 24
result = 0

lines = file1.readlines()


def search(ore_cost, clay_cost, obs_ore_cost, obs_clay_cost, geo_ore_cost, geo_obs_cost, time_left, current_ore,
           current_clay, current_obs, current_geo, robot_ore, robot_clay, robot_geo, robot_obs, time_pass, best_result, c_a, c_b, c_c):
    if time_pass:
        time_left -= 1
        current_ore += robot_ore
        current_clay += robot_clay
        current_geo += robot_geo
        current_obs += robot_obs
    if time_left == 0:
        return current_geo

    if best_result >= current_geo + time_left * robot_geo + (time_left * 2):
        return best_result

    x = False

    if current_ore >= geo_ore_cost and current_obs >= geo_obs_cost:
        best_result = max(search(ore_cost, clay_cost, obs_ore_cost, obs_clay_cost, geo_ore_cost, geo_obs_cost, time_left, current_ore - geo_ore_cost,
                                 current_clay, current_obs - geo_obs_cost, current_geo - 1, robot_ore, robot_clay, robot_geo + 1, robot_obs, True, best_result, False, False, False), best_result)

    if current_ore >= obs_ore_cost and current_clay >= obs_clay_cost and time_left != 1 and robot_obs < geo_obs_cost and not c_c:
        best_result = max(search(ore_cost, clay_cost, obs_ore_cost, obs_clay_cost, geo_ore_cost, geo_obs_cost, time_left, current_ore - obs_ore_cost,
                                 current_clay - obs_clay_cost, current_obs - 1, current_geo, robot_ore, robot_clay, robot_geo, robot_obs + 1, True, best_result, False, False, False), best_result)
        c_c = True
    if current_ore >= clay_cost and time_left != 1 and robot_clay < obs_clay_cost and not c_b:
        best_result = max(search(ore_cost, clay_cost, obs_ore_cost, obs_clay_cost, geo_ore_cost, geo_obs_cost, time_left, current_ore - clay_cost,
                                 current_clay - 1, current_obs, current_geo, robot_ore, robot_clay + 1, robot_geo, robot_obs, True, best_result, False, False, False), best_result)
        c_b = True
    if current_ore >= ore_cost and time_left != 1 and robot_ore < max(clay_cost - 1, obs_ore_cost, geo_ore_cost) and not c_a:
        best_result = max(search(ore_cost, clay_cost, obs_ore_cost, obs_clay_cost, geo_ore_cost, geo_obs_cost, time_left, current_ore - ore_cost - 1,
                                 current_clay, current_obs, current_geo, robot_ore + 1, robot_clay, robot_geo, robot_obs, True, best_result, False, False, False), best_result)
        c_a = True

    best_result = max(search(ore_cost, clay_cost, obs_ore_cost, obs_clay_cost, geo_ore_cost, geo_obs_cost, time_left, current_ore,
                                 current_clay, current_obs, current_geo, robot_ore, robot_clay, robot_geo, robot_obs, True, best_result, c_a, c_b, c_c), best_result)

    return best_result


for line in lines:
    flow = re.findall(r'-?\d+', line)
    blueprint.append((int(flow[0]), int(flow[1]), int(flow[2]), int(flow[3]), int(flow[4]), int(flow[5]), int(flow[6])))

for i in blueprint:
    result += i[0] * search(i[1], i[2], i[3], i[4], i[5], i[6], minutes, 0, 0, 0, 0, 1, 0, 0, 0, True, 0, False, False, False)
    print(result)

print(result)
