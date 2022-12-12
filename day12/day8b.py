import re
import numpy as np
from collections import defaultdict
import math

def ordoOuter(x):
    return np.array(list(map(ordo, x)))

def ordo(x):
    if x != "S" and x != "E":
        return ord(x) - 96
    if x == "S":
        return 0
    if x == "E":
        return ord("z") - 96


file1 = open('input.txt', 'r')
file1 = open('exampleinput.txt', 'r')

mapArray3 = []
i = 0
loc = (0, 0)
endloc = (0, 0)
startlocs = []
resultslocs = []

for line in file1.readlines():
    j = 0
    row = []
    for x in line.strip():
        if x == "a":
            startlocs.append((i, j))
        if x == "S":
            loc = (i, j)
            startlocs.append((i, j))
        if x == "E":
            endloc = (i, j)
        row.append(x)
        j += 1
    mapArray3.append(row)
    i += 1

for h in startlocs:
    loc = h
    mapArray = np.array(mapArray3, dtype="U5")
    mapArray2 = mapArray.copy()
    explore = []
    explore.append(loc)
    pathmap = mapArray.copy()
    mapArray = np.array(list(map(ordoOuter, mapArray)))
    pathmap[loc] = 0
    #
    for (x, y) in explore:
        # print(x, y)
        current_step = pathmap[(x, y)]
        # print(current_step)
        current_height = mapArray[(x, y)]
        if(x + 1) <= len(pathmap) - 1:
            if (mapArray[(x + 1, y)] - current_height) <= 1:
                if pathmap[(x + 1, y)].isnumeric() == False:
                    explore.append((x + 1, y))
                    pathmap[(x + 1), y] = int(current_step) + 1
                else:
                    pathmap[(x + 1, y)] = min(int(pathmap[(x + 1, y)]), (int(current_step) + 1))
        if(x - 1) >= 0:
            if (mapArray[(x - 1, y)] - current_height) <= 1:
                if pathmap[(x - 1, y)].isnumeric() == False:
                    explore.append((x - 1, y))
                    pathmap[(x - 1), y] = int(current_step) + 1
                else:
                    pathmap[(x - 1, y)] = min(int(pathmap[(x - 1, y)]), (int(current_step) + 1))
        if(y + 1) <= len(pathmap[0]) - 1:
            if (mapArray[(x, y + 1)] - current_height) <= 1:
                if pathmap[(x, y + 1)].isnumeric() == False:
                    explore.append((x, y + 1))
                    pathmap[(x, y + 1)] = int(current_step) + 1
                else:
                    pathmap[(x, y + 1)] = min(int(pathmap[(x, y + 1)]), (int(current_step) + 1))
        if(y - 1) >= 0:
            if (mapArray[(x, y - 1)] - current_height) <= 1:
                if pathmap[(x, y - 1)].isnumeric() == False:
                    explore.append((x, y - 1))
                    pathmap[(x, y - 1)] = int(current_step) + 1
                else:
                    pathmap[(x, y - 1)] = min(int(pathmap[(x, y - 1)]), (int(current_step) + 1))

    # for x in pathmap:
    #     for y in x:
    #         if len(y) == 1:
    #             print(y, end="   ")
    #         if len(y) == 2:
    #             print(y, end="  ")
    #         if len(y) == 3:
    #             print(y, end=" ")
    #     print("")


    resultslocs.append(pathmap[endloc])

    print(pathmap[endloc])

print(sorteresultslocs))