# -*- coding: utf-8 -*-
"""
Python Anonymous/Lambda Functions
-> Defined without a name
-> lambda arguments: expression
-> We use lambda functions when we need a nameless function for a short period of time
"""



def function_caller(f,arg):
    return f(arg)

y=function_caller(lambda x: x * 2, 3)
print(y)