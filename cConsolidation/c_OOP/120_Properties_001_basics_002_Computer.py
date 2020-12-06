# -*- coding: utf-8 -*-
"""
"""

class Computer:
    
  def __init__(self):
    self._maxprice = 100

  def get_maxprice(self):
    return self._maxprice

  def set_maxprice(self, value):
    self._maxprice = value    
      
c = Computer()       ;print(c.get_maxprice())
c.set_maxprice(200)  ;print(c.get_maxprice())