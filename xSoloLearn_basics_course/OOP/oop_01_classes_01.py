# -*- coding: utf-8 -*-
"""
Class = "Cat"
Attributes = [color(string), legs(int)]
"""

class Cat:
  def __init__(self, color, legs):
    self.color = color
    self.legs = legs
    
felix = Cat("ginger", 4)
print(type(felix))
print(felix.color)
print(felix.legs)


