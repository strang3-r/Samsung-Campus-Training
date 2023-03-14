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


""" ------------------- """

def foo(a, b, c, d = 4):
    print(a, b, c, d)

foo(1, b=2, c=3) # default value also get printed


