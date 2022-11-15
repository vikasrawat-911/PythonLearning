
listInput = [1, 2, 3, 4, 5, 6, 7]
#listInput = []
i =0

if len(listInput) > 0:
    for x in listInput:
        print(x, end=" ")
        print(i)
        i += 1
else:
    print("\"Empty List\"")
print("-----------------------------------------------------")
if len(listInput) > 0:
    for i in range(len(listInput)):
        print(listInput[i], end=" ")
        print(i)
else:
    print("\"Empty List\"")