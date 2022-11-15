a, b = [int(item) for item in input().split()]
list1 = []
list2 = []
sum1 = 0

for i in range(a):
    list1 = [int(item) for item in input().split()]
    list1.pop(0)
    print(max(list1))
    list2.append(max(list1))

for i in list2:
    sum1 = sum1 + i * i
sum1 = sum1 % b

print(sum1)