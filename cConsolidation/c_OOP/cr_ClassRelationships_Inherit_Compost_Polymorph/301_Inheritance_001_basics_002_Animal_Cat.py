# -*- coding: utf-8 -*-
"""
"""

class Animal:
  def __init__(self, name, color):
    self.name = name
    self.color = color
  def IamAnAnimal(self):
    print("I am an Animal")

class Cat(Animal):
  def meow(self):
    print("MeEeoOoW")
  def IamACat(self):
    print("I am a Cat")

class PersianCat(Cat):
  def IamAPersianCat(self):
    print("I am a Persian Cat")
    
felix = PersianCat("Zoe", "ginger")
print(type(felix))
print(felix.name)
print(felix.color)

felix.IamAnAnimal()
felix.IamACat()
felix.meow()
felix.IamAPersianCat()





