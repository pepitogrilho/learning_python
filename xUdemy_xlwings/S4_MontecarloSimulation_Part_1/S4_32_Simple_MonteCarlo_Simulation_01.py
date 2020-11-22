# -*- coding: utf-8 -*-
"""
"""

import xlwings as xw
import numpy as np
import matplotlib.pyplot as plt


app = xw.apps.active
#Open workbook
wb = xw.Book("real_estate.xlsx")
inp = wb.sheets[0]

#Define ranges
inp["D20"].name = "cpi"
inp["D25"].name = "ppf"
inp["D40"].name = "cost"
#inp["G24:G25"].name = "performance"
inp["G24"].name = "performance_multiple"
inp["G25"].name = "performance_IRR"

#Number of simulations
sims = 100

#CPI: Probability Distribution (normal)
cpi_exp = 0.02
cpi_std = 0.01
cpi_pd = np.random.normal(cpi_exp, cpi_std, sims)
plt.hist(cpi_pd, bins = 100)
plt.show()

#PPF: Probability Distribution (normal)
ppf_exp = 23
ppf_std = 3
ppf_pd = np.random.normal(ppf_exp, ppf_std, sims)
plt.hist(ppf_pd, bins = 100)
plt.show()

#COST: Probability Distribution (normal)
cost_exp = 250000
cost_std = 50000
cost_pd = np.random.normal(cost_exp, cost_std, sims)
plt.hist(cost_pd, bins = 100)
plt.show()

#PERFORMANCE
results=[]
for i in range(sims):
    inp["cpi"].value = np.random.normal(cpi_exp, cpi_std)
    inp["ppf"].value = np.random.normal(ppf_exp, ppf_std)
    inp["cost"].value = np.random.normal(cost_exp, cost_std)
    results.append(inp["performance_multiple"].value)

plt.hist(results, bins = 100)
plt.show()


    
##############   2:09/14:33


wb.close()
