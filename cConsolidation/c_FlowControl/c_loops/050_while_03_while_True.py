
#............................WHILE............................
number = 7
output=""
while True:
   user_input = input("Play? (y/n):").lower()
   if user_input == "n":
       print("Bye then!")
       break
   user_number = int(input("Guess a number from 1 to 10:"))
   if user_number == number:
       print("Great!")
   else:
       print("Sorry, wrong")
   


