# -*- coding: utf-8 -*-

"""
Dictionaries are like lists, but with explicit key
(List's key is it's index: 0,1,2,3,...)
"""

#My first dictionary
ages={"Dave":24, "Mary":42, "John":58}
print(ages)
print(ages["Dave"])
print(ages["Mary"])

#My second dictionary
student={'name':'John', 'age':25, 'courses': ['Math', 'CompSci']}
print(student)
print(student['name']+" has"+str(student['age'])+" years old")

#KeyError vs None
print(student['name'])
print(student['surname'])
print(student.get('name'))
print(student.get('surname'))

