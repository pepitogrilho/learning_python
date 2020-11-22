
import xlwings as xw
import numpy as np
#import pandas as pd

data1 = np.random.randint(1, 100, 10000)
print(data1.shape)
xw.view(data1)


data2 = data1.reshape(100, 100)
print(data2.shape)
xw.view(data2)