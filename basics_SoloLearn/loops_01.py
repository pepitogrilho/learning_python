
#............................WHILE............................
i = 0
while i <=10:
   i += 1
   if i == 3:
      print("Let's skip 3")
      #the "continue" statement stops the current iteration and continue with the next one
      continue
   elif i == 5:
      print("Let's break at 5",end='')
      #the "break" statement stops the loop
      break
   else :
      print(i,end='')   
   print(" while_loop_end")
   
print("Finished!")



#............................WHILE............................
print("\n")
words = ["hello", "world", "spam", "eggs"]
counter = 0
max_index = len(words) - 1
output=""
while counter <= max_index:
   output += words[counter]+"@"
   counter = counter + 1
   
print(output)


#............................FOR............................
print("\n")
output=""
words = ["hello", "world", "spam", "eggs"]
for word in words:
   output += word+"@"
   
print(output)

#............................FOR............................
print("\n")
str="testing for loops"
counted_Ts = 0
for s in str:
   if (s == 't'):
     counted_Ts += 1       
   
print("\"", str, "\" has ", counted_Ts, " Ts")