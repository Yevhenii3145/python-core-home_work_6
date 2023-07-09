#print(lamda x,y: x + y)
# add = lamda x,y: x + async
# print(add(3,4))

def add(x, y):
    return x + y
print(add(3, 4))

res = ((lambda x, y: x + y)(5, 12))
print(res)
