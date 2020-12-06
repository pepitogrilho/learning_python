# -*- coding: utf-8 -*-


def mult(x,y):
  return x*y
  #Once you return a value from a function, the execution stops
  print("eeeeeeeeeeoooooooooooooo")
  
mult_func=mult
print(type(mult_func))

a,b=4,7
c=mult(a,b)
d=mult_func(a,b)

print(type(c));print(c)
print(type(d));print(d)
