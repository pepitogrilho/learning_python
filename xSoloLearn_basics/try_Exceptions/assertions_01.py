# -*- coding: utf-8 -*-

# An assertion in a sanity-check that you can turn off when finished testing
# If the condition checked is false an exception is raised

#...................................................

def square(x):
  assert (type(x)==int or type(x)==float)
  return x*x

def test(func,x):
  print(func(x))
  
test(square,"2")

#...................................................

def square(x):
  assert (type(x)==int or type(x)==float), "not valid type: "
  return x*x

def test(func,x):
  print(func(x))
  
test(square,"2")