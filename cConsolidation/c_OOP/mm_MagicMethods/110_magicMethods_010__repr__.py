# -*- coding: utf-8 -*-
"""
__magicMethods__ are special methods = dunders

__repr_ for giving an unique representation of the object
"""

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  #def __str__(self):
  #  return f"Person '{self.name}', {self.age} years old"
  def __repr__(self):
    return f"<Person '{self.name}', {self.age} years old>"
    
bob = Person("Bob", 35)
print(bob)