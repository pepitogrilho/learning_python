# -*- coding: utf-8 -*-
"""
"""

class Cat:
  def __init__(self, color, legs):
    self.color = color
    self.legs = legs
  def meow(self):
    print("MeEeoOoW")
    
felix = Cat("ginger", 4)
print(type(felix))
print(felix.color)
print(felix.legs)

felix.meow()


