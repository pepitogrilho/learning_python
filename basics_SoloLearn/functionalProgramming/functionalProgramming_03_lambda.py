# -*- coding: utf-8 -*-
"""
"""

def function_runner(f,arg):
    return f(arg)

y=function_runner(lambda x: 2*x*x, 5)
print(y)