import re
import numpy as np
from collections import defaultdict
import math
import ast


mapArray = np.empty((200, 800))
i = 0
loc = (0, 0)
endloc = (0, 0)
result = 0
file1 = open('input.txt', 'r')
# file1 = open('exampleinput.txt', 'r')

lines = file1.readlines()
for line in lines:
    divider = re.findall(r'\d+', line)
    for i in range(0, int(len(divider) / 2 - 1)):
        j = i * 2
        if int(divider[j]) == int(divider[j+2]):

            a = min(int(divider[j+1]), int(divider[j+3]))
            b = max(int(divider[j+1]), int(divider[j+3])) + 1
            # print(mapArray[a:b, int(divider[j])])
            mapArray[a:b, int(divider[j])] = 1
        if int(divider[j+1]) == int(divider[j+3]):
            a = min(int(divider[j]), int(divider[j+2]))
            b = max(int(divider[j+2]), int(divider[j])) + 1
            # print(mapArray[int(divider[j+1]), a:b])
            mapArray[int(divider[j+1]), a:b] = 1

mapArray[169,:] = 1
print(mapArray)

Bottom = False
while Bottom is False:
    x = 500
    y = 0
    while True:
        if mapArray[y,x] == 1:
            Bottom = True
            break;
        if mapArray[y+1,x] != 1:
            y += 1
        elif mapArray[y+1,x-1] != 1:
            y += 1
            x -= 1
        elif mapArray[y+1,x+1] != 1:
            y += 1
            x += 1
        else:
            mapArray[y, x] = 1
            break;

    result += 1

print(result - 1)