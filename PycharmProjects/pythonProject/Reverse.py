s = "Hello World"
s= "Python is Awesome"

count = len(s)
new_String = ""

for x in s.split(" "):
    new = ""
    for i in range(len(x)):
        if x[i].islower():
            new = x[i].upper() + new
        else:
            new = x[i].lower() + new

    new_String = new_String + " " + new

print(new_String.strip())
