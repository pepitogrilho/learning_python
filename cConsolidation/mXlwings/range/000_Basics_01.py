# -*- coding: utf-8 -*-
"""
We open a new book
"""

import xlwings as xw

app = xw.apps.active
wb = xw.Book()
sh = wb.sheets[0]

################## CLEAR ###########################
sh.range("A1:D4").clear()
################## CLEAR ###########################

############### RANGE NAME ########################
sh.range("A1").name = "celdaA1"
print(sh.range("A1").name)
sh.range("celdaA1").value = "esta es la celda A1"
print(sh.range("A1").name)
############### RANGE NAME ########################

############### RANGE NAME ########################
sh["A2"].value = 666
print(sh["A2"].value)
############### RANGE NAME ########################




#wb.close()
