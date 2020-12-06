# -*- coding: utf-8 -*-

#
def hello_world():
  print("hello world")
  
hello_world()

# PARAMETER vs ARGUMENT
def hello(to):
  #"to" is the PARAMETER
  print("hello " + to)
  
#"world" is the ARGUMENT
hello("world")

#
def hello(to):
  print("hello " + to)
  return
  
hello("world")

#
def mul(x, y):
  return x*y
  #Once you return a value from a function, the execution stops
  print("eeeeeeeeeeoooooooooooooo")

z = mul(7,4)
print("z = ", z)

