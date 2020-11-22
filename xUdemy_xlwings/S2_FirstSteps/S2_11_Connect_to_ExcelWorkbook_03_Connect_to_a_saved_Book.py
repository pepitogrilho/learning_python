# -*- coding: utf-8 -*-
"""
We open a new book
"""
import time
import xlwings as xw

path_01 = r"C:\GitHub\learning_python\xUdemy_xlwings\S2_FirstSteps\Test2.xlsx"

wb = xw.Book(path_01)
time.sleep(5)
wb.close()
