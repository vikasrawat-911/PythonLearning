import string

s = "Hello World"
s = "Wonderful World"
result = ""
wordLower = ""

for word in s.split(" "):
    wordLower = word.lower()
    print(wordLower)
    result = result + " " + "".join(sorted(wordLower))

print(result.strip())
