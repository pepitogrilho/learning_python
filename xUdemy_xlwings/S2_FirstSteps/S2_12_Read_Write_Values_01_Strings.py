# -*- coding: utf-8 -*-
"""
We open a new book
"""

import xlwings as xw

path_01 = r"C:\GitHub\learning_python\xUdemy_xlwings\S2_FirstSteps\Test2.xlsx"

wb = xw.Book(path_01)
sheet0= wb.sheets[0]

sheet0.range("A2").value = "Hello World!"

valueA1 = sheet0.range("A1").value
print(valueA1)

valueA2 = sheet0.range(2,1).value
print(valueA2)

valueB1 = sheet0.range(1,2).value
print(valueB1)

#wb.close()
