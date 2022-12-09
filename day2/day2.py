import numpy as np
import pandas as pd

# df = pd.read_csv('input.csv', index_col=0)
file1 = open('exampleInput.txt', 'r')
# file1 = open('input.txt', 'r')

lines = file1.readlines()

count = 0
result = np.array([])
i = 0

# A = rock    = X
# b = Paper   = Y
# C = Sciccors= Z
for line in lines:
    line = line.strip()
    if line == "A Y":
        count += (3 + 1)
    if line == "A X":
        count += (0 + 3)
    if line == "A Z":
        count += (6 + 2)
    if line == "B Y":
        count += (3 + 2)
    if line == "B X":
        count += (0 + 1)
    if line == "B Z":
        count += (6 + 3)
    if line == "C Y":
        count += (3 + 3)
    if line == "C X":
        count += (0 + 2)
    if line == "C Z":
        count += (6 + 1)


print(count)
