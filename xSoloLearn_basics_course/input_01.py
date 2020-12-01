
#
input_01 = input()
print(input_01)

#
input_02 = input("write something:")
print(input_02)

#
input_03 = input("Enter your name:")
print("Hello, "+input_03)

#
input_04 = input("Enter 1, 2 or 3:")
if (input_04 != "1") and (input_04 != "2") and (input_04 != "3"):
   print("\""+input_04+"\" is not a valid number")
else:
   input_04 = int(input_04)
   if (input_04 == 1):
     print("ONE!:"+str(input_04)+"<")    
   else:
     print("Not One:"+str(input_04)+"<")