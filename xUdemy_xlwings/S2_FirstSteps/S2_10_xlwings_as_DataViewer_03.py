
import xlwings as xw
import numpy as np
import pandas as pd


df = pd.read_csv("S2_00_Resources_Titanic.csv")
xw.view(df)
