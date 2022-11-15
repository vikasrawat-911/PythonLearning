listInput = [1, 1, 1, 2, 3, 4, 1, 2, 5, 6, 7, 2, 2, 3, 8, 9, 10]
listTemp = []

print(list(set(listInput)))

for x in listInput:
    if not x in listTemp:
        listTemp.append(x)

listInput = listTemp
print(listInput)