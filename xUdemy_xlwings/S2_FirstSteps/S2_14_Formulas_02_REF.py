# -*- coding: utf-8 -*-
"""
We open a new book
"""

import xlwings as xw

path_01 = r"C:\GitHub\learning_python\xUdemy_xlwings\S2_FirstSteps\Test2.xlsx"

wb = xw.Book(path_01)
sheet0= wb.sheets[0]

sheet0.range("E1").value = "EEEEOOOOO"
sheet0.range("F1").formula = "=E1"

f1_value = sheet0.range("F1").value
print(f1_value)

#wb.close()
