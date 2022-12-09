import re

file1 = open('input.txt', 'r')
# file1 = open('exampleinput.txt', 'r')
lines = file1.readlines()
count = 0

i = 0
list = []
location = []
dicta = dict()

for line in lines:
    if re.match('(\$ cd ).+', line) != None:
        x = line[5:].strip()
        if x != "..":
            location.append("." + x)
            dicta[''.join(location)] = 0
        if x == "..":
            location.pop()
        # print(location)
    if re.match('\d', line) != None:
        x = re.findall(r'\d+', line)
        if(''.join(location)) in dicta.keys():
            dicta[''.join(location)] += int(x[0])

print(dicta)
resultDic = dict()

for x in sorted(dicta.keys()):
    for y in dicta.keys():
        if x == y:
            resultDic[x] = int(dicta[y])
        if x != y:
            if y.startswith(x):
                resultDic[x] += int(dicta[y])

print(resultDic)
result = 0
print(resultDic.values())
for x in resultDic.values():
    if int(x) <= 100000:
        result += int(x)

print(result)
print(30000000 - (70000000 - resultDic["./"]))
print("---")
for x in sorted(resultDic.values()):
    if int(x) >= (30000000 - (70000000 - resultDic["./"])):
        print(x)