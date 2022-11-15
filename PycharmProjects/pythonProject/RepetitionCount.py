s = "corp"
new = ""
repeted = ""
count = 0

for c in s:
    if not c in new:
        new = new + c
    elif not c in repeted:
        repeted = repeted + " " +c
        count = count + 1

print(count)
if len(repeted.strip()) == 0:
    print("None")
else:
    print(" ".join(sorted(repeted)).strip())