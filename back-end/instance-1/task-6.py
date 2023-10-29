e_list = [5, 6, 3, [], [], 9]
copyArr = []
index = 0

while index < len(e_list):
    if e_list[index] != []:
        copyArr.append(e_list[index])
    index += 1

print(copyArr)