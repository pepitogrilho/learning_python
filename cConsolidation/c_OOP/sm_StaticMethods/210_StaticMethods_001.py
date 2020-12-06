# -*- coding: utf-8 -*-
"""
- Instance Methods receive the OBJECT as argument
- Class Methods receive the CLASS as argument
- Static Methods don't receive neither the OBJECT, nor the CLASS
"""

class ClassTest:
  def instance_method(self):
    print(f"Called instance_method of {self}")
  
  @classmethod
  def class_method(cls):
    print(f"Called class_method of {cls}")

  @staticmethod
  def static_method():
    print("Called static_method.")

test=ClassTest()

test.instance_method()

#Static methods can be called in 2 ways:
test.static_method()
ClassTest.static_method()