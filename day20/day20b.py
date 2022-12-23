import re
from itertools import cycle

file1 = open('input.txt', 'r')
# file1 = open('exampleinput.txt', 'r')

org_list = []
mixed_list = []
i = 0

lines = file1.readlines()
key = 811589153



for line in lines:
    flow = re.findall(r'-?\d+', line)
    org_list.append([int(flow[0]) * key, i])
    mixed_list.append([int(flow[0]) * key, i])
    i += 1


# print(mixed_list)
for i_1 in range(10):
    for x in org_list:
        j = mixed_list.index(x)
        mixed_list.remove(x)
        new_index = (j + x[0]) % len(mixed_list)
        mixed_list.insert(new_index, x)
        # print(mixed_list)
    print(i_1)

iterator = cycle(mixed_list)
j = 0
found_zero = False
result = 0
while True:
    current = iterator.__next__()
    # print(current)
    if found_zero:
        j += 1
        if j % 1000 == 0:
            result += current[0]
            print(current[0])
        if j == 3000:
            print(result)
            exit()
    if current[0] == 0:
        found_zero = True


