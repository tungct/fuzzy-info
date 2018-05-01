

def angle_normal(angle):
    if angle > 5 and angle <= 20:
        return (angle - 5) / 15.0
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

