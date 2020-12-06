# -*- coding: utf-8 -*-
"""
With Polymorfism we use a COMMON INTERFACE for multiple forms (data types).
"""

class Parrot:
    
  def fly(self):
    print("Parrot can fly")

  def swim(self):
    print("Parront CAN'T swim")
    
    
class Penguin:

  def fly(self):
    print("Penguin CAN'T fly")

  def swim(self):
    print("Penquin can swim")


#common interface
def flying_test(bird):
  bird.fly()
  
parrot = Parrot()
penquin = Penguin()

flying_test(parrot)
flying_test(penquin)