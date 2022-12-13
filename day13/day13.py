import re
import numpy as np
from collections import defaultdict
import math
import ast

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
                return None
            if a < b:
                return True
            if a > b:
                return False
        if isinstance(b, list):
            return compare([a], b)
    if isinstance(a, list):
        if isinstance(b, int):
            return compare(a, [b])
        if isinstance(b, list):
            if len(a) == 0 and len(b) == 0:
                return None
            if len(a) == 0 and len(b) > 0:
                return True
            if len(a) > 0 and len(b) == 0:
                return False
            result = compare(a[0], b[0])
            if result == False:
                return False
            elif result == True:
                return True
            else:
                a.pop(0)
                b.pop(0)
                return compare(a, b)
file1 = open('input.txt', 'r')
# file1 = open('exampleinput.txt', 'r')

mapArray = []
i = 0
loc = (0, 0)
endloc = (0, 0)
result = 0

for x in range(1, 151):
    a = file1.readline()
    b = file1.readline()
    file1.readline()
    a = ast.literal_eval(a)
    b = ast.literal_eval(b)
    if compare(a, b):
        print(x)
        result += x

print(result)
