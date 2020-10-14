# -*- coding: utf-8 -*-

def hello_world():
  print("hello world")
  
hello_world()

#----------------------------------------

def hello(to):
  print("hello " + to)
  
hello("world")

#----------------------------------------

def hello(to):
  print("hello " + to)
  return
  
hello("world")

#----------------------------------------

def mul(x, y):
  return x*y
  #Once you return a value from a function, the execution stops
  print("eeeeeeeeeeoooooooooooooo")

z = mul(7,4)
print("z = ", z)


#----------------------------------------

def shout(word):
    """
    Print a word with an exclamation mark

    Parameters
    ----------
    word : string
        Word to be shouted.

    Returns
    -------
    The shouted word.

    """
    return word + "!!!!!!"

shout("Basta")
