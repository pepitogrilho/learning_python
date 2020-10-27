# -*- coding: utf-8 -*-

# Common exceptions:
#
# - ImportError        , an import fails
# - IndexError         , a list is indexed with an out-of-range number
# - NameError          , an unknown variable is used
# - SyntaxError        , the code can't be parsed
# - TypeError          , a function is called on a value of an inappropriate type
# - ValueError         , a function is called on a value of correct type, but wrong value
# - ZeroDivisionError  , a function is called on a value of correct type, but wrong value



#...................... No error is caught ..............................
def main():
  print(2+"2")

main()
#............... All errors are caught by the same except ...............
def main():
 try:
  print(2+"2")
  #c=4/0; print(c)

 except:
  print("Error caught !!!")

main()
#................ Errors are caught by type .............................
def main():
 try:
  print(2+"2")
  #c=4/0; print(c)

 except(TypeError, ValueError):
  print("TypeError or ValueError !!")
 except ZeroDivisionError:
  print("ZeroDivisionError!!")

 print("done")
main()
#........................................................................
