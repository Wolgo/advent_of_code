import re
import numpy as np
from collections import defaultdict


def def_value():
    return 0


file1 = open('input.txt', 'r')
# file1 = open('exampleinput.txt', 'r')
count = 0

max_monkey = 8

monkeys = []

for i in range(0, max_monkey):
    line = file1.readline()

    line = file1.readline()
    items = re.findall(r'-?\d+', line)
    curr_monkey = items

    line = file1.readline()
    functionText = re.findall(r'old.+', line)
    exec("def monkey_inspect" + str(i) + "(old): return " + functionText[0])

    line = file1.readline()
    divider = re.findall(r'-?\d+', line)

    line = file1.readline()
    true = re.findall(r'-?\d+', line)
    # print(true[0])

    line = file1.readline()
    false = re.findall(r'-?\d+', line)
    # print(false[0])
    exec("def monkey_decide" + str(i) + "(item): \n if item % "+ str(divider[0])+" == 0: monkeys[ "+str(true[0])+"].append(item) \n else: monkeys["+ str(false[0])+"].append(item)")

    # Skip empty line
    line = file1.readline()
    monkeys.append(curr_monkey)

print(monkeys)
count = [0, 0, 0, 0, 0, 0, 0, 0]
prev_count = [0, 0, 0, 0, 0, 0, 0, 0]

for i in range(0, 10000):
    for j in range(0, max_monkey):
        temp_list = monkeys[j]
        inspect = globals()["monkey_inspect" + str(j)]
        decide = globals()["monkey_decide" + str(j)]
        count[j] += len(temp_list)
        for itemx in temp_list:
            itemx = inspect(int(itemx))
            itemx = itemx % 9699690
            decide(int(itemx))
        monkeys[j] = []
    # print(count)
    # print(prev_count)
    # change = [a - b for a, b in zip(count, prev_count)]
    # print(change)
    # prev_count = count.copy()

    print(i)

print(sorted(count, reverse=True)[0] * sorted(count, reverse=True)[1])
