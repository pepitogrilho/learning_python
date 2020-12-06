# -*- coding: utf-8 -*-
"""
* Pure Functions are like math functions. E.G. cos(x): for the same value of x cos(x)has the same value
  (Functional programming seeks to use Pure Functions.)
* Impure Functions ...  
"""

#Pure: it has always the same result 
def pure_function(x,y):
    return (x+2*y)/(2*x+y)



#Impure: the result depends on external conditions
    
list_01 = []

def impure_function(arg):
    list_01.append(arg)
    
impure_function("kk")

print(list_01)