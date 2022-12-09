import re

file1 = open('input.txt', 'r')
# file1 = open('exampleinput.txt', 'r')
lines = file1.readlines()
count = 0

i = 0
list = []

def all_unique(item):
    return len(set(item)) == len(item)

for line in lines:
    for x in line:
        i+=1
        list.append(x)
        if(len(list) > 14):
            del list[0]
        if all_unique(list):
            print(i)



