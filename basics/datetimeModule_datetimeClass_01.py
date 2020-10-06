#Module:datetime / Class:datetime
from datetime import datetime

#the 'dtObject_01' object is assigned the current time using the datetime's "now()" function 
print('\n')
dtObject_01 = datetime.now(); print(type(dtObject_01))
print(dtObject_01)
#the 'dtObject_02' object is assigned a defined date from an string
print('\n')
dtString_02 = '2020.10.03'
dtObject_02 = datetime.strptime(dtString_02, "%Y.%m.%d"); print(type(dtObject_02))
print(dtObject_02)

#We get info from our datetime objects (i)
print('\n')
print(str(dtObject_01.year) + '.' + str(dtObject_01.month) + '.' + str(dtObject_01.day))
#We get info from our datetime objects (ii)
#Mon=0, Tue=1, ...
wD = dtObject_01.weekday()
print("WeekDay: " + str(wD))
#We get info from our datetime objects (iii)
import calendar
wDname = calendar.day_name[wD]
wDabbr = calendar.day_abbr[wD]
print("wDname = "+wDname+"   wDabbr = "+wDabbr)
#We get info from our datetime objects (iv)
print('\n')
print(str(dtObject_01.hour) + ':' + str(dtObject_01.minute) + ':' + str(dtObject_01.second))

#From the datetime object we get both: (i) a date object, and (ii) a time object
print('\n')
print(dtObject_01.date())
print(dtObject_01.date().year)
print('\n')
print(dtObject_01.time())
print(dtObject_01.time().hour)
