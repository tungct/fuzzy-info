import datetime
import time
import datetime
dt_started = datetime.datetime.utcnow()

# do some stuff
time.sleep(1)
dt_ended = datetime.datetime.utcnow()
print((dt_ended - dt_started).total_seconds())
if (dt_ended - dt_started).total_seconds() > 1.0 and ((dt_ended - dt_started).total_seconds() < 1.002):
    print("HELLO")