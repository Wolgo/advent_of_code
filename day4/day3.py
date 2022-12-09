file1 = open('input.txt', 'r')
# file1 = open('exampleinput.txt', 'r')
lines = file1.readlines()
count = 0
for line in lines:
    a = line.split(",")
    b = a[0].split("-")
    c = a[1].split("-")


    if (int(b[0]) >= int(c[0])) and (int(b[0]) <= int(c[1])):
        count += 1
    else:
        if (int(b[1]) >= int(c[0])) and (int(b[1]) <= int(c[1])):
            count += 1
        else:
            if (int(c[1]) >= int(b[0])) and (int(c[1]) <= int(b[1])):
                count += 1
            else:
                if (int(c[0]) >= int(b[0])) and (int(c[0]) <= int(b[1])):
                    count += 1

print(count)




#
# addTen = np.vectorize(add)
# result = addTen(result)


# print(result[0])
# print(np.sum(result[:3]))
