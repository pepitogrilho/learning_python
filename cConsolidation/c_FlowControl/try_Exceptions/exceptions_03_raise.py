# -*- coding: utf-8 -*-

# User can raise exceptions ....................................
def main():

 try:
  a=1;b=1
  if (a==b):
    raise ValueError
  c=4/0; print(c)

 except ValueError:
  print("ValueError caught !!!")

main()


# User can raise exceptions ....................................
def main():

 try:
  a=1;b=1
  if (a==b):
    raise ValueError("Wrong value: ")
  c=4/0; print(c)

 except ValueError:
  print("ValueError caught !!!")

main()


