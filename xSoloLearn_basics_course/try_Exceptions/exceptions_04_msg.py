# -*- coding: utf-8 -*-


# Exceptions raised by user with message .................................
def main():

  a=1;b=1
  if (a==b):
    raise ValueError("Wrong values: a= ",a," b= ",b)
  c=4/0; print(c)

main()


# Exceptions raised after being caught ..................................
def main():

 try:
  c=4/0; print(c)
 except:
  print("Error has happend")
  raise
  
main()
