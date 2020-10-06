#Module:datetime / Class:datetime
#Classes: datetime, date, time
from datetime import time


secs_from_1970=time.time()
print(secs_from_1970)
print(time.ctime(secs_from_1970))
print(time.gmtime(secs_from_1970))

print(time.ctime(0))
print(time.gmtime(0))


#Module:datetime / Class:time
