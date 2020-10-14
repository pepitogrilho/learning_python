# -*- coding: utf-8 -*-


def mult(x,y):
  return x*y
  
mult_func=mult
print(type(mult_func))

a=4
b=7
c=mult(a,b)

print(type(c))
print(c)

#........................................

def sum(x,y):
  return x+y

def mult(x,y):
  return x*y

sum_func = sum
mul_fun = mult

a=1
b=2
c=3
d=4
e=sum_func(a,b)
f=sum_func(c,d)
g=mult(e,f)
#(1+2)*(3+4)=3*7=21
print(g)  
    
