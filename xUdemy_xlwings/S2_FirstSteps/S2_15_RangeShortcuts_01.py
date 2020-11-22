# -*- coding: utf-8 -*-
"""
"""

import xlwings as xw

path_01 = r"C:\GitHub\learning_python\xUdemy_xlwings\S2_FirstSteps\Test2.xlsx"

wb = xw.Book(path_01)
sheet0= wb.sheets[0]

sheet0.range("A2").value = 100
print(sheet0.range("A2").value)

sheet0["A2"].value = 100
print(sheet0["A2"].value)

#wb.close()
