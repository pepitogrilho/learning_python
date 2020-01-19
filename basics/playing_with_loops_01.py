
#............................WHILE............................
i = 0
while i <=10:
   i += 1
   if i == 3:
      print("Let's skip 3")
      continue
   elif i == 5:
      print("Let's break at 5")
      break
   else :
      print(i)
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