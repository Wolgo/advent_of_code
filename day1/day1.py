

file1 = open('input.txt', 'r')
lines = file1.readlines()

count = 0
result = []
maxresult = 0
i = 0
maxresultindex = 0

for line in lines:
    if line.strip().isnumeric():
        count += int(line.strip())
    else:
        if count > maxresult:
            maxresult = count
            maxresultindex = i
        result.append(count)
        count = 0
        i += 1



print(maxresult)
print(maxresultindex + 1)

result.sort(reverse=True)
print(result[0] + result[1] + result[2])