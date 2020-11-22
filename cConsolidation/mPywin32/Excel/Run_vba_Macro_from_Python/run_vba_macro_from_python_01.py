# -*- coding: utf-8 -*-
"""
"""

import win32com.client

ExcelFileWithMacro_Path = r"X:\C14F5\MOGLI\09_Apps\99_tests\99_general_tests\pywin32\Excel\run_vba_macro_from_python\run_vba_macro_from_python_01.xlsm"

xl=win32com.client.Dispatch("Excel.Application")
xl.Workbooks.Open(Filename=ExcelFileWithMacro_Path,ReadOnly=1)
xl.Application.Run("SayHello.SayHello")
xl.Workbooks(1).Close(SaveChanges=0)
xl.Application.Quit()
xl=0