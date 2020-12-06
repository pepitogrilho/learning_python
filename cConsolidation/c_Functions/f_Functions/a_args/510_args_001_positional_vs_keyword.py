# -*- coding: utf-8 -*-


#POSITIONAL: parametere takes the arguments value depending on their POSITION
def suma(x,y):
  return x+y
z=suma(1,2)
print(z)

#KEYWORD(named): parametere takes the arguments value depending on the KEYWORD(named) ARGUMENTS
def suma(x,y):
  return x+y
z=suma(y=2, x=1)
print(z)

# POSITIONAL + KEYWORD: in 1st place POSITIONAL
def suma(x,y):
  return x+y
#this works....................
z=suma(1,y=2)
print(z)
#this does not work............
#z=suma(x=1,2)