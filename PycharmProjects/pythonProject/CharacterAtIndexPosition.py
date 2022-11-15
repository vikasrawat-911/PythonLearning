
s = "Vikas Rawat"
#s = ""
i = 2

if i > len(s):
    print("i is out of range")
elif len(s) == 0:
    print("Empty String")
else:
    print(s[i])

if not s:
    print("nothing String")

print ("".join(reversed(s)))
