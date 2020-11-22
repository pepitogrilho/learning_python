
"""
The code within else is called if the loop finishes normally
(when a break statement does not cause an exit from the loop)
"""

# The loop ends calling the else code
for i in range(10):
    if i == 999:
        print("if..."+str(i))
        break
else:
    print("else..."+str(i))

# The loop ends normally (break)
for i in range(10):
    if i == 5:
        print("if..."+str(i))
        break
else:
    print("else..."+str(i))
