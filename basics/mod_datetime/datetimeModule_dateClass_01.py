#Module:datetime / Class:datetime
#Classes: datetime, date, time, timedelta
from datetime import date

d=date.today()
print(d.isoformat())
print(d.strftime("%d/%m/%y"))



