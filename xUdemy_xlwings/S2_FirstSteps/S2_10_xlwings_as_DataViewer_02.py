
import xlwings as xw
import numpy as np
import pandas as pd


data21 = np.random.randint(1, 100, 100).reshape(10, 10)
xw.view(data21)
xw.view(data21, sheet = xw.sheets.active)