# Insert Square numbers from 1 to 10 in each index
x = []
for i in range(9):
    y = i*i
    x.append(y)
print(x)

# Pick Even numbers and return them in a list:
myfunc(5,6,7,8)

emptyList = []
def myfunc (*args):
    for x in args:
        if x % 2 == 0:
            emptyList.append(x)
        else:
            pass
    return emptyList