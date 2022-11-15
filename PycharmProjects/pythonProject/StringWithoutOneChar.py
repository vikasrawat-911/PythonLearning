s = "ABCD1234"
i = 5
new = ""

if len(s) == 0 or i >= len(s):
    print(s)
else:
    for j in range(len(s)):
        if j != i:
            new = new + s[j]
    print(new)
