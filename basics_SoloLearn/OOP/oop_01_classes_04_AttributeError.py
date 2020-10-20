# -*- coding: utf-8 -*-
"""
Trying to 
- access an attribute of an instance that isn't defined 
- call an undefined method 
>> causes an AttributeError
"""

class Cat:
  def __init__(self, color, legs):
    self.color = color
    self.legs = legs

    
felix = Cat("ginger", 4)
print(type(felix))
print(felix.color)
print(felix.legs)
print(felix.tail)



