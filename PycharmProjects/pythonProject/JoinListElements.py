
listInput = [1, 2, 3, 4]

#print(" ".join(listInput))

for x in listInput:
    print(x, end=" ")

print("")


print(*listInput, sep=" ")
