import datetime
import time
import datetime
import math
dt_started = datetime.datetime.utcnow()

# do some stuff
# time.sleep(1)
dt_ended = datetime.datetime.utcnow()
print((dt_ended - dt_started).total_seconds())
if (dt_ended - dt_started).total_seconds() > 1.0 and ((dt_ended - dt_started).total_seconds() < 1.002):
    print("HELLO")

def compareCoord(x, y, x2, y2):
    dist = math.hypot(x2 - x, y2 - y)
    return dist

print(compareCoord(100,100, 100.01, 100.01))
print(math.cos(math.radians(26)))

angle = ['more_right', 'right', 'mormal', 'left', 'more_left']
drive = ['more_right', 'right', 'mormal', 'left', 'more_left']
distance = ['near', 'normal', 'far']
speed = ['slow', 'normal', 'fast']
lamp = ['more_red', 'red', 'yellow', 'green', 'more_green']
count = 0

# for i in range(len(drive)):
#     for j in range(len(lamp)):
#         for k in range(len(distance)):
#             count = count + 1
#             print(count , angle[i] + " - " + lamp[j] + " - " + distance[k])

def distanceC(x1,y1,x2,y2):
    dist = math.hypot(x2 - x1, y2 - y1)
    return dist

xlamp = 250
ylamp = 475
xlamp2 = 550
ylamp2 = 350
xlamp3 = 950
ylamp3 = 220
# 235 -450
# 1 - 30
# 2 - 75
# 3 - 70
print(distanceC(950,275,950,220))
