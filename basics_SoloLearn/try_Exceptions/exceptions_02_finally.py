# -*- coding: utf-8 -*-

# "finally" ensures some code runs no matter what errors occur
def main():

 try:
  print(2+"2")
  c=4/0; print(c)

 except:
  print("Error caught !!!")

 finally:
  print("This code will run no matter what")   

main()