# -*- coding: utf-8 -*-
"""
We change the function "ordinary"
"""




# way 1  ..........................................

def divide(a,b):
  return a/b

def smart_divide(func):
  def divide_wrapper(a,b):
    if b == 0:
      return f"cannot operate {a}/{b}"
    return func(a,b)
  return divide_wrapper
#Change definition of function
divide=smart_divide(divide)

#Run re-defined function
out=divide(4,1); print(out)
out=divide(4,0); print(out)

# way 1  ..........................................


# way 2  ..........................................

def smart_divide(func):
  def divide_wrapper(a,b):
    if b == 0:
      return f"cannto operate {a}/{b}"
    return func(a,b)
  return divide_wrapper

#Change definition of function
@smart_divide
def divide(a,b):
  return a/b

#Run re-defined function
out=divide(4,1); print(out)
out=divide(4,0); print(out)

# way 2  ..........................................
