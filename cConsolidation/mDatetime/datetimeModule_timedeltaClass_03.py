#Classes: datetime, date, time, timedelta

#A timedelta objects holds time between 2 times or 2 dates


# diff between 2 DATES
from datetime import date
#2 dates
dOb_01 = date(2020, 10, 12)
dOb_02 = date(2020, 10, 9)
#Difference
tdOb_01 = dOb_02 - dOb_01
print('\n')
print("Diferencia : ", str(tdOb_01))
print("DIAS de diferenia: ", str(tdOb_01.days))

# diff between 2 DATETIMES
from datetime import datetime
#2 datestimes
dtOb_01 = datetime(2020, 10, 9, 21, 20, 00)
dtOb_02 = datetime(2020, 10, 12, 21, 20, 10)
#Difference
tdOb_01 = dtOb_02 - dtOb_01
print('\n')
print("Diferencia : ", str(tdOb_01))
