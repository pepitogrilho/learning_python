# -*- coding: utf-8 -*-
"""
"""

class Pizza:
  def __init__(self, toppings):
    self.toppings = toppings
    self._pineapple_allowed = False

  @property
  def pineapple_allowed(self):
    return self._pineapple_allowed

  @pineapple_allowed.setter 
  def pineapple_allowed(self, value):
    self._pineapple_allowed = value    
      
pizza01=Pizza(["cheese", "onions", "spam"])
print(pizza01.pineapple_allowed)
pizza01.pineapple_allowed = True
print(pizza01.pineapple_allowed)