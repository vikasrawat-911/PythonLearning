
s = "Good Morning"
prefix = "Good Mornin"

if len(prefix) > len(s):
    print(False)
elif prefix == s[:len(prefix)]:
    print(True)
else:
    print(False)