n = int(input())
lis1 = [int(item) for item in input().split()]

firstMax = 0
for x in lis1:
    if x > firstMax:
        firstMax = x

secondMax = 0
for x in lis1:
    if x > secondMax and x != firstMax:
        secondMax = x

print(secondMax)