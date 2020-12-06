# -*- coding: utf-8 -*-

"""
Updating and appending
"""

#Update the same way as lists: 
ages={"Dave":24, "Mary":42, "John":58}
ages["Dave"]=ages["Dave"]+1
print(ages["Dave"])

for student in ages:
    print(student)
print("\n")    
    
for student in ages:
    print(f"{student}: {ages[student]}")
print("\n")    
    
for student, age in ages.items():
    print(f"{student}: {age}")