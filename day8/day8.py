import re
import numpy as np

file1 = open('input.txt', 'r')
# file1 = open('exampleinput.txt', 'r')
lines = file1.readlines()
count = 0

i = 0
list = []
dicta = dict()
count = 0


for line in lines:
    list.append([])
    for x in line.strip():
        list[i].append(int(x))
        count += 1
    i += 1

list = np.array(list)
# print(list)

for x in range(1, len(list)-1):
    for y in range(1, len(list[0])-1):
        # print(list[x,y])
        # print(list[0:x,y])
        if any(num >= list[x, y] for num in list[0:x,y]):
            # print(list[x+1:len(list),y])
            if any(num >= list[x, y] for num in list[x+1:len(list),y]):
                # print(list[x,0:y])
                if any(num >= list[x, y] for num in list[x,0:y]):
                    # print(list[x,y+1:len(list[0])])
                    if any(num >= list[x, y] for num in list[x,y+1:len(list[0])]):
                        # print(x,y,list[x,y])
                        count -= 1
print(count)
