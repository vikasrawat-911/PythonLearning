
listInput = [1, 2, 3, 2, 4, 2, 6, 7]
#listInput = []
elem_to_remove = 2

if len(listInput) == 0:
    print("Empty List")
elif not elem_to_remove in listInput:
    print("Not Found")
else:
    for i in range(len(listInput)):
        if elem_to_remove in listInput:
            listInput.remove(elem_to_remove)
    print(listInput)