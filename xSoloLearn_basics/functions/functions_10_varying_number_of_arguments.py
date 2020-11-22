# -*- coding: utf-8 -*-


# the variable number of parameters are a TUPLE

def vectorNdimensions(name, *args):
  print(name)
  print(args)
  for arg in args:
    print(arg)

  
vector1dim=vectorNdimensions("line",1)
vector2dim=vectorNdimensions("plane",1,2)
vector3dim=vectorNdimensions("cube",1,2,3)
