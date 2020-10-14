#Module:datetime / Class:timedelta
#Classes: datetime, date, time, timedelta

#A timedelta objects holds time between 2 times or 2 dates

from datetime import timedelta


tdOb_01 = timedelta(weeks=2)
print('\n')
print("valor = " + str(tdOb_01) + "// type = " + str(type(tdOb_01)))

tdOb_02 = timedelta(days=367)
print('\n')
print("valor = " + str(tdOb_02) + "// type = " + str(type(tdOb_02)))