x = 50

def test(x):
    print(f"x is: {x}")
    x = 33
    print("x is changed to: ",x)

test(x)
print("x is still:",x)