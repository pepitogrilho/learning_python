
#while
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