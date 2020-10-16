#Module:datetime / Classes: timedelta+datetime
#Classes: datetime, date, time, timedelta

#A datetime object 
#A timedelta objects holds time between 2 times or 2 dates

from datetime import datetime, timedelta

#NOW
dtOb_01 = datetime.now()
print('\n')
print("hoy es, y estamos a las : ", str(dtOb_01))

#1 day delay
tdOb_01 = timedelta(days=1)
print('\n')
print("valor = " + str(tdOb_01) + "// type = " + str(type(tdOb_01)))
#NOW + 1 day delay
dtOb_02 = dtOb_01 + tdOb_01
print('\n')
print("mañana por estas horas : " + str(dtOb_02))

#1 week delay
tdOb_02 = timedelta(weeks=1)
print('\n')
print("valor = " + str(tdOb_02) + "// type = " + str(type(tdOb_02)))
#NOW + 1 week delay
dtOb_03 = dtOb_01 + tdOb_02
print('\n')
print("dentro de una semana por estas horas : " + str(dtOb_03))

