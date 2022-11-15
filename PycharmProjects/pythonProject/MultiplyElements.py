
listInput = ["a", "b", "c", "d"]
listInput = [3//2,2,3,4]
listNew =[]
factor = 3

for x in listInput:
    if not isinstance(x, str):
        listNew.append(x*factor)
    else:
        s=""
        for i in range(factor):
            s = s+x
        listNew.append(s)

print(listNew)



