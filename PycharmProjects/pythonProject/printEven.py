
s = "Vikas Rawat"
new = ""
i = 0

if len(s) < 2:
    print(s)
else:
    while i < len(s):
        if i % 2 == 0:
            new = new + s[i]
        i = i + 1

print(new)