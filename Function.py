""" 
-The difference between arguments and parameters
-Positional and keyword arguments
-Default arguments
-Variable-length arguments (*args and kwargs)
-Container Unpacking into functional arguments
-Local vs Global arguments
-Parameter passing (by value or by reference)
"""

def func(name):  # Arguments
    print(name)

func("Black-D3vil")

def foo(a, b, c):
    print(a, b, c)

foo(1, 2, 3)
foo(a=1, b=2, c=3)
foo(c=1, b=2, a=3) # Positional Arguments and Keyword arguments


""" ---------------------------------------------------------------- """

def foo(a, b, c, d = 4):
    print(a, b, c, d)

foo(1, b=2, c=3) # default value also get printed



""" ---------------------------------------------------------------- """

def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

foo(5, 6, 3, 4, 7, six=6,eight=8)


""" ---------------------------------------------------------------- """

def foo(a, b, *, c, d):
    print(a, b, c, d)


foo(2, 5, c=7, d=9)


""" ---------------------------------------------------------------- """

def foo(*args, last):
    for arg in args:
        print(arg)
    print(last)

foo(3, 6, 7, last=100)


""" ---------------------------------------------------------------- """

def foo(a, b, c):
    print(a, b, c)

my_list = [0, 1, 2]
foo(*my_list)
my_tuple = (8, 9, 5)
foo(*my_tuple)
my_dict = {'a': 2, 'b': 6, 'c': 9}
foo(*my_dict)
foo(**my_dict)


""" ---------------------------------------------------------------- """

def foo():
    global number
    x = number
    number = 9
    print('number inside function',x)

number = 0
foo()
print(number)


""" ---------------------------------------------------------------- """

def foo():
    # global number
    # x = number
    number = 9
    # print('number inside function', x)

number = 0
foo()
print(number)


""" ---------------------------------------------------------------- """

def foo(x):
    x = 6

var = 10
foo(var)
print(var)


""" ---------------------------------------------------------------- """

def foo(a_list):
    a_list = [200, 300, 400]
    a_list.append(3)
    a_list[0] = -12

my_list = [4, 7, 9]
foo(my_list)
print(my_list)



""" ---------------------------------------------------------------- """

def foo(a_list):
    a_list += [200, 300, 400]
    a_list.append(3)
    a_list[0] = -12

my_list = [4, 7, 9]
foo(my_list)
print(my_list)