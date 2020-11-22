# -*- coding: utf-8 -*-
"""
We open a new book
"""

import xlwings as xw
import datetime as dt

path_01 = r"C:\GitHub\learning_python\xUdemy_xlwings\S2_FirstSteps\Test2.xlsx"

wb = xw.Book(path_01)
sheet0= wb.sheets[0]

date01 = dt.datetime(2020, 11, 14, 23, 4, 0)

sheet0.range("A2").value = date01

date02 = sheet0.range("A2").value
print(date02)

sheet0.range("A2").clear_contents() 

#wb.close()
