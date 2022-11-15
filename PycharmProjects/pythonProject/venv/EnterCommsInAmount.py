strAmount = input("Enter Any Amount = ")
outTemp = ""
i = len(strAmount)
while i > 0:
    i = i - 1
    outTemp = outTemp + strAmount[i]

i = 0
strAmount = ""
while i < len(outTemp):
    if i == 0:
        strAmount = outTemp[i]
    elif i % 3 == 0:
        strAmount = outTemp[i] +"," + strAmount
    else:
        strAmount = outTemp[i] + strAmount
    i += 1

print("Amount with Commas - "+strAmount)




