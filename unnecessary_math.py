'''
Module showing how doctests can be included with source code
Each '>>>' line is run as if in a python shell, and counts as a test.
The next line, if not '>>>' is the expected output of the previous line.
If anything doesn't match exactly (including trailing spaces), the test fails.
'''
 
def multiply(a, b):
    return a * b

# some comment 
def myFun(a, b):
    return a + b


def perryFun(a):
    return a
