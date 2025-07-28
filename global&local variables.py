#local variable
Var=9
loop=True
def func(x):
    newVar=7
    print(newVar)
    if x ==5:
        return newVar

func(2)

#global variable

Var=9
loop=True
def func2(x):
    global loop
    loop=7
    if x ==5:
        return newVar
def other_func(x):
    newVar=10
    print(newVar)

other_func(7)
print(loop)