# -*- coding: utf-8 -*-
"""
"""

class Pizza:
  def __init__(self, toppings):
    self.toppings = toppings
  @property
  def pineapple_allowed(self):
    return False

pizza01=Pizza(["cheese", "onions", "spam"])
print(pizza01.pineapple_allowed)
pizza01.pineapple_allowed = True
#> AttributeError: can't set attribute
