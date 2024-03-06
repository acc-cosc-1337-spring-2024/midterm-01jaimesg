
x = 10

def use_global():
    print(x)


def change_global():
    global x 
    x = 5
    print(x)
