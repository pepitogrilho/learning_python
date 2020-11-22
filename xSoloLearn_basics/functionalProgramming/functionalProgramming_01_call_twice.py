# -*- coding: utf-8 -*-

"""
"""


def x2(x):
  return x*x

def call_twice(func,x):
  return func(func(x))
  
x4 = call_twice(x2,2)
print(x4)