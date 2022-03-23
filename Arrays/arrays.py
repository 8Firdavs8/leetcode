# Insert Square numbers from 1 to 10 in each index
x = []
for i in range(9):
    y = i*i
    x.append(y)
print(x)

# Pick Even numbers and return them in a list:

emptyList = []
def myfunc (*args):
    for x in args:
        if x % 2 == 0:
            emptyList.append(x)
        else:
            pass
    return emptyList
print(myfunc(5,6,7,8))


def upperString(string):
    res = []
    for letter in range(len(string)):
        if (letter+1)%2==0:
            res.append(string[letter].upper())
        else:
            res.append(string[letter].lower())
    return ''.join(res)
    
        
print(upperString("firdavs"))


# Q20: Valid Parenthesis

# stack = []
        
#         CloseToOpen = {")":"(", "]":"[", "}":"{" }
        
#         for c in s:
#             if c in CloseToOpen:
#                 if stack and stack[-1] == CloseToOpen[c]:
#                     stack.pop()
#                 else:
#                     return False
#             else:
#                 stack.append(c)
#         return True if not stack else False