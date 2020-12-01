

#............................FOR............................
print("\n")
output=""
for i in range(5): 
  output=output+str(i+1)+"@"
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