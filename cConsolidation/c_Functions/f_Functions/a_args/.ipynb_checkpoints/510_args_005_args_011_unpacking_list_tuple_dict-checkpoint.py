# -*- coding: utf-8 -*-


#passing parameters from a LIST : >*<
def add(x, y):
  return x+y
nums=[3,5]
print(add(*nums))

#passing parameters from a LIST : >*< + we get a TUPLE
def add(*args):
  print(type(args))
  o=0
  for i in args:
      o+=i
  return o
nums=[3,5]
print(add(*nums))



#passing parameters from a TUPLE : >*<
def add(x, y):
  return x+y
nums=(3,5)
print(add(*nums))

#passing parameters from a TUPLE : >*< + we get a TUPLE
def add(*args):
  print(type(args))
  o=0
  for i in args:
      o+=i
  return o
nums=(3,5)
print(add(*nums))



#passing parameters from a DICT : >**<
def add(x, y):
  return x+y
nums={"x":3, "y":5}
print(add(**nums))

#passing parameters from a DICT : >**< + we get a DICT
def add(**kwargs):
  print(type(kwargs))
  o=0
  for number in kwargs:
      o+=kwargs[number]
  return o     
nums={"x":3, "y":5}
print(add(**nums))
