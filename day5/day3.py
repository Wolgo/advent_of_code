import re

file1 = open('input.txt', 'r')
# file1 = open('exampleinput.txt', 'r')
lines = file1.readlines()
count = 0

stack = []

phase = 0

for line in lines:

    if phase == 3:
        x = re.findall(r'\d+', line)
        i = 0
        temp = []
        while i < int(x[0]):
            temp.insert(0, (stack[int(x[1]) - 1].pop()))
            i += 1
        i = 0
        while i < int(x[0]):
            stack[int(x[2]) - 1].append(temp[i])
            i += 1
        print(stack)

    if phase == 2:
        phase = 3

    if phase == 1:
        index = 0
        stackindex = 0
        for x in line:
            if int(index) % 4 == 1 and phase != 2:
                if x == "1":
                    phase = 2
                elif x != " ":
                    stack[stackindex].insert(0, x)
                stackindex += 1;
            index += 1

        print(stack)

    if phase == 0:
        index = 0
        for x in line:
            if int(index) % 4 == 1:
                if x != " ":
                    stack.append([x])
                else:
                    stack.append([])
            index += 1

        # print(stack)
        phase += 1


    #
    # a = line.split(",")
    # b = a[0].split("-")
    # c = a[1].split("-")
    #
    #
    # if (int(b[0]) >= int(c[0])) and (int(b[0]) <= int(c[1])):
    #     count += 1
    # else:
    #     if (int(b[1]) >= int(c[0])) and (int(b[1]) <= int(c[1])):
    #         count += 1
    #     else:
    #         if (int(c[1]) >= int(b[0])) and (int(c[1]) <= int(b[1])):
    #             count += 1
    #         else:
    #             if (int(c[0]) >= int(b[0])) and (int(c[0]) <= int(b[1])):
    #                 count += 1

i = 0
string = ""
while i < len(stack):
 string += stack[i].pop();
 i += 1
print(string)




#
# addTen = np.vectorize(add)
# result = addTen(result)


# print(result[0])
# print(np.sum(result[:3]))
