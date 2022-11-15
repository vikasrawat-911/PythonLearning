import string

s = string.ascii_lowercase
input = "The quick brown fox jumps over the lazy do"
exception = ""
input = input.lower()

print(s)

for i in string.ascii_lowercase:
    if not i in input:
        exception = exception + i

print(exception)

if len(exception) > 0:
    print("False")
else:
    print("True")

