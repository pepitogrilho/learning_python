# -*- coding: utf-8 -*-


#else code is run if no error ocurrs in the try statement 
def exFunc(a,b):
 try:
  print(a/b)
 except ZeroDivisionError:
  print("ZeroDivisionError")
 else:
  print("else")
  
exFunc(1,1)
print("\n")
exFunc(1,0)
