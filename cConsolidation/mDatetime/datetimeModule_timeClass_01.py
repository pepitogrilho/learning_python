#Module:datetime / Class:time
from datetime import datetime
import time


secs_from_1970=time.time()
print(secs_from_1970)
print(time.ctime(secs_from_1970))
print(time.gmtime(secs_from_1970))

print(time.ctime(0))
print(time.gmtime(0))


fl_ahora = time.time()
st_ahora = time.ctime(fl_ahora)
dt_ahora = datetime.strptime(st_ahora, "%a %b %d %H:%M:%S %Y")
st_ahora_ii = dt_ahora.strftime("%Y.%m.%d_%H:%M:%S")
print(st_ahora_ii)

#Module:datetime / Class:time
