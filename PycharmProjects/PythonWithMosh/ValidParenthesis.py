
stackList = []
s = "()"
for i in range(len(s)):
        if s[i] in ["(", "{", "["]:
            stackList.append(s[i])
        else:
            if len(stackList) == 0:
                print(False)
            if stackList[-1]+s[i] in ["()", "{}", "[]"]:
                stackList = stackList[:-1]
                print(stackList[-1]+s[i])
            else:
                print(False)
                break

print(True)