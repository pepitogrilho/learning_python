#Module:datetime / Class:datetime

#Way 1: import the whole datetime module, including classes: (i)datetime, (ii)date, (iii)time
import datetime
print('\n')
dtObject_01 = datetime.datetime.now(); print(type(dtObject_01))
print(dtObject_01)

#Way 2: import from the datetime module the datetime class
from datetime import datetime
print('\n')
dtObject_01 = datetime.now(); print(type(dtObject_01))
print(dtObject_01)

