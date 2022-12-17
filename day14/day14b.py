import re
import numpy as np
from collections import defaultdict
import math
import ast
import functools

def compare(a, b):
    if a is None and b is None:
        return None
    if a is None and b is not None:
        return True
    if a is not None and b is None:
        return False
    if isinstance(a, int):
        if isinstance(b, int):
            if a == b:
                return 0
            if a < b:
                return -1
            if a > b:
                return 1
        if isinstance(b, list):
            return compare([a], b)
    if isinstance(a, list):
        if isinstance(b, int):
            return compare(a, [b])
        if isinstance(b, list):
            if len(a) == 0 and len(b) == 0:
                return 0
            if len(a) == 0 and len(b) > 0:
                return -1
            if len(a) > 0 and len(b) == 0:
                return 1
            result = compare(a[0], b[0])
            if result == 1:
                return 1
            elif result == -1:
                return -1
            else:
                c = a.copy()
                d = b.copy()
                c.pop(0)
                d.pop(0)
                return compare(c, d)
file1 = open('input.txt', 'r')
# file1 = open('exampleinput.txt', 'r')

mapArray = []
i = 0
loc = (0, 0)
endloc = (0, 0)
result = 0
sortinghat = []

# for x in range(1, 9):
for x in range(1, 151):
    a = file1.readline()
    b = file1.readline()
    file1.readline()
    a = ast.literal_eval(a)
    b = ast.literal_eval(b)
    sortinghat.append(a)
    sortinghat.append(b)

sortinghat.append([[2]])
sortinghat.append([[6]])

sortinghat = sorted(sortinghat, key=functools.cmp_to_key(compare))

result = (sortinghat.index([[2]]) + 1) * (sortinghat.index([[6]]) + 1)
print(result)

