# -*- coding: utf-8 -*-
"""
__magicMethods__ are special methods = dunders
> implement functionality that CAN'T be in NORMAL methdos
> __init__ : for the class CONSTRUCTOR
> __add__ : for OPERATOR OVERLOADING
"""

class Vector2D:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def __add__(self, other):
    return Vector2D(self.x + other.x, self.y + other.y)

    
vector_5_7 = Vector2D(5, 7)
vector_3_9 = Vector2D(3, 9)

vector_addition_01 = vector_5_7 + vector_3_9
print(vector_addition_01.x)
print(vector_addition_01.y)




