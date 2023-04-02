# -*- coding: utf-8 -*-
"""
We change the function "ordinary"
"""


def pretty(func):
  def wrap():
    print("............................")
    func() 
    print("............................")
  return wrap


# way 1  ..........................................

def ordinary():
  print("hello")
ordinary=pretty(ordinary)
ordinary()
# way 1  ..........................................


# way 2  ..........................................
@pretty
def ordinary():
  print("hello")
ordinary()
# way 2  ..........................................


