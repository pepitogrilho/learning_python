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
  def __len__(self):
    if (self.x != None) & (self.y != None):
        return 2
    elif (self.x == None) & (self.y == None):
        return 0
    else:
        return 1
  def __getitem__(self,index):
    if (index == 0):
        return self.x
    elif (index == 1):
        return self.y
    else:
        return "?"
    
  
v00 = Vector2D(None, None);print(v00.x); print(v00.y); print(len(v00))
print("\n")
v10 = Vector2D(1, None);print(v10.x); print(v10.y); print(len(v10))
print("\n")
v01 = Vector2D(None, 1);print(v01.x); print(v01.y); print(len(v01))
print("\n")
v11 = Vector2D(1, 1);print(v11.x); print(v11.y); print(len(v11))

print("\n")
v23 = Vector2D(2, 3);print(v23[0]); print(v23[1]); print(v23[2])
