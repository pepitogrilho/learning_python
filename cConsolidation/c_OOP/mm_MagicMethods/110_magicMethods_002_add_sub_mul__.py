# -*- coding: utf-8 -*-
"""
__magicMethods__ OPERATOR OVERLOADING:
__add__ for +
__sub__ for -
__mul__ for *
__truediv__ for /
__floordiv__ for //
__mod__ for %
__pow__ for **
__and__ for &
__or__ for |
__xor__ for ^
"""

class Vector2D:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def __add__(self, other):
    return Vector2D(self.x + other.x, self.y + other.y)
  def __sub__(self, other):
    return Vector2D(self.x - other.x, self.y - other.y)
  def __mul__(self, other):
    return Vector2D(self.x * other.x, self.y * other.y)
    
v_5_7 = Vector2D(5, 7)
v_3_9 = Vector2D(3, 9)

v_add = v_5_7 + v_3_9; print(v_add.x); print(v_add.y)
v_sub = v_5_7 - v_3_9; print(v_sub.x); print(v_sub.y)
v_mul = v_5_7 * v_3_9; print(v_mul.x); print(v_mul.y)




