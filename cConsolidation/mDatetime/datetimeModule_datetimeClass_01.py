#Module:datetime / Class:datetime
#Classes: datetime, date, time, timedelta
from datetime import datetime

#the 'dtO_01' object is assigned the current time using the datetime's "now()" function 
print('\n')
dtO_01 = datetime.now(); print(type(dtO_01))
print(dtO_01)
#the 'dtO_02' object is assigned a defined date from an string
print('\n')
dtString_02 = '2020.10.03'
dtO_02 = datetime.strptime(dtString_02, "%Y.%m.%d"); print(type(dtO_02))
print(dtO_02)

#From the datetime object we get both: (i) a DATE object, and (ii) a TIME object
print('\n')
print(dtO_01.date())
print(dtO_01.date().year)
print('\n')
print(dtO_01.time())
print(dtO_01.time().hour)

#We get DATE-info from our datetime objects (i)
print('\n')
print(str(dtO_01.year) + '.' + str(dtO_01.month) + '.' + str(dtO_01.day))
#We get DATE-info from our datetime objects (ii)
#Mon=0, Tue=1, ...
wD = dtO_01.weekday()
print('\n')
print("WeekDay: " + str(wD))
#We get DATE-info from our datetime objects (iii)
import calendar
wDname = calendar.day_name[wD]
wDabbr = calendar.day_abbr[wD]
print("wDname = "+wDname+"   wDabbr = "+wDabbr)
#We get DATE-info from our datetime objects (iv)
print('\n')
print(dtO_01.isocalendar())
print('year: '+str(dtO_01.isocalendar()[0]))
print('week in year: '+str(dtO_01.isocalendar()[1]))
print('day in week: '+str(dtO_01.isocalendar()[2]))

#We get TIME-info from our datetime objects (i)
print('\n')
print(str(dtO_01.hour) + ':' + str(dtO_01.minute) + ':' + str(dtO_01.second))


