#Module:datetime / Class:datetime
#Classes: datetime, date, time, timedelta
from datetime import datetime

diaObjetivo_datetime = datetime.today()
print(type(diaObjetivo_datetime))
print(diaObjetivo_datetime)

diaObjetivo_string = diaObjetivo_datetime.strftime("%Y.%m.%d")
print(type(diaObjetivo_string))
print(diaObjetivo_string)

