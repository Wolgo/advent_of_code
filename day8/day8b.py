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
    i += 1

list = np.array(list)
print(list)

for x in range(1, len(list)-1):
    for y in range(1, len(list[0])-1):
        # print(x,y, list[x,y])
        # print(list[0:x,y])
        # print(list[0:x,y])
        a = 0
        for num in reversed(list[0:x,y]):
            a += 1
            if(num >= list[x,y]):
                break
        b = 0
        # print( list[x+1:len(list),y])
        for num in list[x+1:len(list),y]:
            b += 1
            if(num >= list[x,y]):
                break
        # print(list[x,0:y])
        c = 0
        for num in reversed(list[x,0:y]):
            c += 1
            if(num >= list[x,y]):
                break
        # print(list[x,y+1:len(list[0])])
        d = 0
        for num in list[x,y+1:len(list[0])]:
            d += 1
            if(num >= list[x,y]):
                break
        if(a * b * c * d > count):
          # print(x,y,list[x,y])
          # print(a, b, c, d)
          count = (a * b * c * d)
print(count)
