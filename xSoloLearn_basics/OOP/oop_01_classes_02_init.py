# -*- coding: utf-8 -*-
"""
The init method 
- is called when an object is created
- has "self" as the first parameter
"""

class Cat:
  def __init__(self, color, legs):
    self.color = color
    self.legs = legs
    
felix = Cat("ginger", 4)
print(type(felix))
print(felix.color)
print(felix.legs)


