# -*- coding: utf-8 -*-
"""
Class = "Student"
Attributes = [name(string), grades(tuple(int))]
"""

class Student:
  def __init__(self, name, grades):
    self.name = name
    self.grades = grades
  def average(self):
    return sum(self.grades)/len(self.grades)
    
stu_rolf = Student("Rolf", (90,90,93,78,90))
print(type(stu_rolf))
print(stu_rolf.name)
print(stu_rolf.grades)
print(stu_rolf.average())

