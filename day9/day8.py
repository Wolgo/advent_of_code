import re
import numpy as np
from collections import defaultdict


def def_value():
    return 0


file1 = open('input.txt', 'r')
# file1 = open('exampleinput.txt', 'r')
lines = file1.readlines()
count = 0

i = 0
list = []
dicta = defaultdict(def_value)
pos_x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
pos_y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for line in lines:
    vel_x = 0
    vel_y = 0

    if re.match('U.+', line) is not None:
        x = re.findall(r'\d+', line)
        vel_y = -1
    if re.match('D.+', line) is not None:
        x = re.findall(r'\d+', line)
        vel_y = +1
    if re.match('R.+', line) is not None:
        x = re.findall(r'\d+', line)
        vel_x = +1
    if re.match('L.+', line) is not None:
        x = re.findall(r'\d+', line)
        vel_x = -1
    for i in range(0, int(x[0])):
        pos_x[0] += vel_x
        pos_y[0] += vel_y
        for z in range(1, len(pos_y)):
            if pos_x[z - 1] > pos_x[z] + 1:
                pos_x[z] += 1
                if pos_y[z - 1] > pos_y[z]:
                    pos_y[z] += 1
                if pos_y[z - 1] < pos_y[z]:
                    pos_y[z] -= 1
            if pos_x[z - 1] < pos_x[z] - 1:
                pos_x[z] -= 1
                if pos_y[z - 1] > pos_y[z]:
                    pos_y[z] += 1
                if pos_y[z - 1] < pos_y[z]:
                    pos_y[z] -= 1
            if pos_y[z - 1] > pos_y[z] + 1:
                pos_y[z] += 1
                if pos_x[z - 1] > pos_x[z]:
                    pos_x[z] += 1
                if pos_x[z - 1] < pos_x[z]:
                    pos_x[z] -= 1
            if pos_y[z - 1] < pos_y[z] - 1:
                pos_y[z] -= 1
                if pos_x[z - 1] > pos_x[z]:
                    pos_x[z] += 1
                if pos_x[z - 1] < pos_x[z]:
                    pos_x[z] -= 1
            if z == 9:
                dicta[str(pos_x[z]) + ", " + str(pos_y[z])] += 1

print(dicta)
print(len(dicta))
