
intTemp = int(input("Enter any Integer = "))
strBinary = ""
originalTemp = intTemp

while intTemp != 0:
    strBinary = str(intTemp % 2) + strBinary
    intTemp = intTemp // 2

print(f"binary representation of {originalTemp} is - {strBinary}")

