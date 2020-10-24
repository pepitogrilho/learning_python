# -*- coding: utf-8 -*-
"""
Class Methods are called by a class, which is passed to the ...
.... cls parameter
A common use of these are factory 
"""

class Vector2D:
  def __init__(self, x, y):
    if x > 0:
       self.x = x
    else:
       self.x = 0
    if y > 0:
       self.y = y
    else:
       self.y = 0
  def area(self):
    return self.x * self.y
  @classmethod
  def newVector2D(cls,coord):
    return cls(coord, coord)    
  
v01 = Vector2D.newVector2D(4)
print(v01.area())