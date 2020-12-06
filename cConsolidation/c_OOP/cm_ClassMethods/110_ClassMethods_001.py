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


test=ClassTest()

#These next 2 calls have the same result
test.instance_method()
ClassTest.instance_method(test)

#
ClassTest.class_method()
