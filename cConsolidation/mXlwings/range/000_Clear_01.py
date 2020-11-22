# -*- coding: utf-8 -*-
"""
We open a new book
"""

import xlwings as xw
import datetime as dt

path_01 = r"C:\GitHub\learning_python\xUdemy_xlwings\S2_FirstSteps\Test2.xlsx"

wb = xw.Book(path_01)
sheet0= wb.sheets[0]
sheet0.range("A1").name = "celdaA1"
print(sheet0.range("A1").name)

sheet0.range("celdaA1").value = "esta es la celda A1"


#wb.close()
