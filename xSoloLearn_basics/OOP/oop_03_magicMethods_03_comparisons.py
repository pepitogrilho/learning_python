# -*- coding: utf-8 -*-
"""
__magicMethods__ COMPARATORS OVERLOADING:
__lt__ for <
__le__ for <=
__eq__ for ==
__ne__ for !=
__gt__ for >
__ge__ for >=
"""

class Vector2D:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def __lt__(self, other):
    if (self.x < other.x) & (self.y < other.y):
        return True
    else:
        return False
    
v_5_7 = Vector2D(5, 7); v_3_9 = Vector2D(3, 9); print(v_5_7 < v_3_9)
v_3_5 = Vector2D(3, 5); v_4_6 = Vector2D(4, 6); print(v_3_5 < v_4_6)


