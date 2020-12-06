# -*- coding: utf-8 -*-
"""
the variable number of parameters are a TUPLE
"""


def vector(name, *args):
  p_name = name                 ; print(f"p_name = {p_name}")
  print(type(args))             ; print(args)
  ps = [arg for arg in args]    ; print(ps)
vector1dim=vector("line",1)
vector2dim=vector("plane",1,2)
vector3dim=vector("cube",1,2,3)
