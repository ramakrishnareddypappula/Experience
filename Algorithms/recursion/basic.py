
# This will print first and then do a function call.
def func(a):
    if a == 1:
        return a
    print(a) # 5 4 3 2
    # it starts with a = 5, it's not 1 so it prints 5 and call the function with a = 4
    # it starts with a = 4, it's not 1 so it prints 4 and call the function with a = 3
    # it starts with a = 3, it's not 1 so it prints 3 and call the function with a = 2
    # it starts with a = 2, it's not 1 so it prints 2 and call the function with a = 1
    # function with a = 1, but since there is no return statement, the function exits after printing 2, so it doesn't print 1.
    func(a - 1)

func(5)

print("*" * 10)

# This will print first and then do a function call.
def func(a):
    if a == 1:
        return a
    print(a) # 5 4 3 2 will be printed here. 1 will be printed down.
    # this function will print 5 and call func with reduced to 4.
    # new stack will print 4 and call func with reduced to 3.
    # new stack will print 3 and call func with reduced to 2.
    # new stack will print 2 and call func with reduced to 1.
    # 1 will be returned and in turn this function will be returned and it will be printed.
    return func(a - 1)

print(func(5)) # 1 will be printed here.

print("*" * 10)
def func(a):
    if a == 1:
        return a
    return func(a - 1)

print(func(5)) # 1 . It will be returned by if condition which is returned recursive function which will be printed.


print("*" * 20)

def func(a):
    if a == 1:
        return a
    func(a - 1)
    print(a)  # 2 3 4 5


func(5)

print("*" * 10)

def func(a):
    if a == 1:
        return a
    return func(a - 1)
    print(a)

print(func(5))  # 1
