# -*- coding: utf-8 -*-
"""
"""

import win32com.client

testFilePath = r"X:\C14F5\MOGLI\09_Apps\99_tests\99_general_tests\pywin32\Excel\Exploring_COM_in_Excel"
testFileName = "Exploring_COM_in_Excel.xlsx"
testFileRef = testFilePath + "\\" + testFileName
testSheet01 = "Sheet01"
testRange01 = "A1:D4"

#...............................xlApp..............................
xlApp=win32com.client.Dispatch("Excel.Application")
xlApp.Visible = 1
#...............................xlWBook..............................
xlWBook = xlApp.Workbooks.Open(testFileRef)   #; print(xlWBook.Name)
xlWBook.Activate
xlApp.Workbooks(testFileName).Activate
#...............................xlSheet..............................
xlSheet = xlWBook.Sheets(testSheet01)         #; print(xlSheet.Name)
xlSheet.Activate
#...............................xlRange..............................
xlRRange = xlSheet.Range(testRange01)
xlRRange.Value = "Python Rules!!"
xlSheet.Cells(5,5).Value = "Python Rules!!"