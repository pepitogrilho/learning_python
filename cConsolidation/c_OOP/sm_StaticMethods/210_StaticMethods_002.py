# -*- coding: utf-8 -*-
"""
- Instance Methods receive the OBJECT as argument
- Class Methods receive the CLASS as argument
- Static Methods don't receive neither the OBJECT, nor the CLASS
"""

class Pizza:
  def __init__(self, toppings):
    self.toppings = toppings
  @staticmethod
  def validate_topping(topping):
    if topping == "pineapple":
      raise ValueError("No pineapples!!!")
    else:
      return True

def createPizza(ingredients):
  for ingredient in ingredients:
    Pizza.validate_topping(ingredient)
  for ingredient in ingredients:
    print(ingredient)    
  new_pizza=Pizza(ingredients)
  return new_pizza  

pizza01=createPizza(["cheese", "onions", "spam"])
print(type(pizza01))

pizza02=createPizza(["cheese", "onions", "pineapple"])
print(type(pizza02))