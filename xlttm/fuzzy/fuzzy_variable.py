

def angle_normal(angle):
    if angle > 5 and angle <= 20:
        return (20 - angle) / 15.0
    elif angle >= -5 and angle <= 5:
        return 1.0
    elif angle >= -20 and angle <-5:
        return (angle + 20) / 15.0
    else:
        return 0.0

def angle_left(angle):
    if 20 <= angle and angle <= 30:
        return 1.0
    elif 5 <= angle and angle <=20:
        return (angle - 5) / 15.0
    elif 30 <= angle and angle <= 45:
        return (45 - angle) / 10.0
    else:
        return 0.0

def angle_more_left(angle):
    if angle >= 45:
        return 1.0
    elif 35 < angle and angle < 45:
        return (angle - 35) / 10.0
    else:
        return 0.0

def angle_right(angle):
    if -35 <= angle and angle <=-15:
        return 1.0
    elif -15<= angle and angle <=-5:
        return (-angle - 5)/ 10.0
    elif -45 <= angle and angle <= -35:
        return (angle + 45) / 10.0
    else:
        return 0.0

def angle_more_right(angle):
    if angle <= -45:
        return 1.0
    elif -45 < angle and angle <= -35:
        return (-angle - 35) / 10.0
    else:
        return 0.0


def drive_normal(angle):
    if angle > 5 and angle <= 15:
        return (angle - 5) / 10.0
    elif angle >= -5 and angle <= 5:
        return 1.0
    elif angle >= -15 and angle <-5:
        return (angle + 15) / 10.0
    else:
        return 0.0

def drive_right(angle):
    if 15 <= angle and angle <= 35:
        return 1.0
    elif 5 <= angle and angle <=15:
        return (angle - 5) / 10.0
    elif 35 <= angle and angle <= 45:
        return (45 - angle) / 10.0
    else:
        return 0.0

def drive_more_right(angle):
    if angle >= 45:
        return 1.0
    elif 35 < angle and angle < 45:
        return (angle - 35) / 10.0
    else:
        return 0.0

def drive_left(angle):
    if -35 <= angle and angle <=-15:
        return 1.0
    elif -15<= angle and angle <=-5:
        return (-angle - 5)/ 10.0
    elif -45 <= angle and angle <= -35:
        return (angle + 45) / 10.0
    else:
        return 0.0

def drive_more_left(angle):
    if angle <= -45:
        return 1.0
    elif -45 < angle and angle <= -35:
        return (-angle - 35) / 10.0
    else:
        return 0.0

def lamp_yellow(time):
    if -2 <= time and time <= 2:
        return 1.0
    elif 2 <= time and time <= 5:
        return (5 - time) / 3.0
    elif -5 <= time and time <= -2:
        return (time + 5) / 3.0
    else:
        return 0.0

def lamp_green(time):
    if 5 <= time and time <= 7:
        return 1.0
    elif 2 <= time and time <= 5:
        return (time - 2) / 3.0
    elif 7 <= time and time <= 10:
        return (10 - time) / 3.0
    else:
        return 0.0

def lamp_more_green(time):
    if time >= 10:
        return 1.0
    elif 7 <= time and time <= 10:
        return (time - 7) / 3.0
    else:
        return 0.0

def lamp_red(time):
    if -7 <= time and time <= -5:
        return 1.0
    elif -5 <= time and time <= -2:
        return (-time - 2) / 3.0
    elif -10 <= time and time <= -5:
        return (time + 10) / 3.0
    else:
        return 0.0

def lamp_more_red(time):
    if time <= -10:
        return 1.0
    elif -10 <= time and time <= -7:
        return (-time - 7) / 3.0
    else:
        return 0.0

def speed_slow(speed):
    if 0<= speed and speed <= 15:
        return 1.0
    elif 15 <= speed and speed <= 30:
        return (30 - speed) / 15.0
    else:
        return 0.0

def speed_normal(speed):
    if speed == 35:
        return 1.0
    elif 15 <= speed and speed <= 40:
        return (speed - 15) / 25.0
    elif 40 <= speed and speed <= 65:
        return (65 - speed) / 25.0
    else:
        return 0.0

def speed_fast(speed):
    if speed >= 65:
        return 1.0
    elif 40 <= speed and speed <= 65:
        return (speed - 40) / 25.0
    else:
        return 0.0

def distance_near(distance):
    if 0 <= distance and distance <= 10:
        return 1.0
    elif 10 <= distance and distance <= 20:
        return (20 - distance) / 10.0
    else:
        return 0.0

def distance_normal(distance):
    if distance == 30:
        return 1.0
    elif 10 <= distance and distance <= 30:
        return (distance - 10) / 20.0
    elif 30 <= distance and distance <= 50:
        return (50 - distance) / 20.0
    else:
        return 0.0

def distance_far(distance):
    if distance >= 50:
        return 1.0
    elif 30 <= distance and distance <= 50:
        return (distance - 30) / 20.0
    else:
        return 0.0

