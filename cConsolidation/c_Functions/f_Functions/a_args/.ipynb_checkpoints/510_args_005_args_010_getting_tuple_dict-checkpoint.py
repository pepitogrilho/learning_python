# -*- coding: utf-8 -*-
"""
"""

# getting a TUPLE
def add(*args):
  print(type(args))
  o=0
  for i in args:
      o+=i
  return o
print(add(3,5))


# getting a DICT
def add(**kwargs):
  print(type(kwargs))
  o=0
  for number in kwargs:
      o+=kwargs[number]
  return o      
print(add(x=3,y=5))
