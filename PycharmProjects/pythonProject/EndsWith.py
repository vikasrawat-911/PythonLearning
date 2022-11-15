import string

s = "Jai Shri Ram"
suffix = "Ram"

print(s[-len(suffix):] == suffix)

print(s.endswith(suffix))

print(s[-3:])