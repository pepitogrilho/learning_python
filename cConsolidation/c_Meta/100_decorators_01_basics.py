# -*- coding: utf-8 -*-
"""
This is ideal when you need to extend/change functions that you don't want to modify
"""

def pretty(func):
  def wrap():
    print("............................")
    func() 
    print("............................")
  return wrap

def ordinary():
  print("hello")

ordinary()
  
pretty=pretty(ordinary)
pretty()