
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
words = ["hello", "world", "spam", "eggs"]
counter = 0
max_index = len(words) - 1

while counter <= max_index:
   word = words[counter]
   print(word + "!")
   counter = counter + 1