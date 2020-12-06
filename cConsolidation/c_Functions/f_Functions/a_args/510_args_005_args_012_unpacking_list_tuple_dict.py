# -*- coding: utf-8 -*-


#passing parameters from a LIST : >*< + we get a TUPLE
def test(*args):
  print(type(args))
  print(f"x = {args[0]}")
  print(f"y = {args[1]}")
nums=[3,5]
test(*nums)



#passing parameters from a TUPLE : >*< + we get a TUPLE
def test(*args):
  print(type(args))
  print(f"x = {args[0]}")
  print(f"y = {args[1]}")
nums=(3,5)
test(*nums)



#passing parameters from a DICT : >**< + we get a DICT
def test(**kwargs):
  print(type(kwargs))
  print(f"x = {kwargs['x']}")
  print(f"y = {kwargs['y']}")
nums={"x":3, "y":5}
test(**nums)
