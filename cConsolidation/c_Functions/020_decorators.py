# -*- coding: utf-8 -*-
"""
This is ideal when you need to extend/change functions that you don't want to modify
"""

def decor(func):
  def wrap():
    print("............................")
    func() 
    print("............................")
  return wrap

def hello():
  print("hello")
  
decorated=decor(hello)
decorated()