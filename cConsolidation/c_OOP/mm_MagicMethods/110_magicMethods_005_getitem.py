# -*- coding: utf-8 -*-
"""
__magicMethods__ CONTAINERS-LIKE FUNCTIONS OVERLOADING:
__len__ for len()
__getitem__ for indexing, like list01[x]
__setitem__ for assingning to indexed values
__delitem__ for deleting indexed values
__iter__ for iteration over objects (e.g. in for loops)
__contais__ for in
"""

class Vector2D:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def __getitem__(self,index):
    if (index == 0):
        return self.x
    elif (index == 1):
        return self.y
    else:
        return "?"
    


v23 = Vector2D(2, 3);print(v23[0]); print(v23[1]); print(v23[2])
