# -*- coding: utf-8 -*-
"""
We open a new book
"""

import xlwings as xw

path_01 = r"C:\GitHub\learning_python\xUdemy_xlwings\S2_FirstSteps\Test2.xlsx"

wb = xw.Book(path_01)
sheet0= wb.sheets[0]

#..............SUM.........................
f_ini=2
f=f_ini
c=4
n=10

while f < f_ini+n:
  sheet0.range(f,c).value = f
  f+=1

sheet0.range("D1").formula = "=SUM(D2:D11)"

formula01 = sheet0.range("D1").formula
print(formula01)
#..............SUM.........................

#wb.close()
