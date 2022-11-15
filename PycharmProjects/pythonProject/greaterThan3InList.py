listInput = [1, -1, 0, 0, 2, 2, 3, 2, 3, 4, 5, 99, 1, 2, 3, 6, 4, 100]
threshold = 3
counter = 0

for x in listInput:
    if x > threshold:
        counter += 1

print(counter)