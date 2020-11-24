#Module:datetime / Class:datetime
#Classes: datetime, date, time, timedelta
from datetime import datetime

diaObjetivo_string = '24/11/2020'

diaObjetivo_datetime = datetime.strptime(diaObjetivo_string, '%d/%m/%Y')
print(type(diaObjetivo_datetime))
print(diaObjetivo_datetime)

diaObjetivo_date = diaObjetivo_datetime.date()
print(type(diaObjetivo_date))
print(diaObjetivo_date)
