# Python program for Dijkstra's single source shortest
# path algorithm. The program is for adjacency matrix
# representation of the graph

import cv2
import sys
import numpy as np
import pygame
import time
import random
import datetime
import math
import xlttm.calc_drive
import xlttm.calc_lamp
import xlttm.calc_stone

PI = math.pi
np.set_printoptions(threshold='nan')

map_distance = {}
parent_node = {}
dead_node = {}
listXY = []


def grayscale(file):
    image = cv2.imread(file)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('./gray_image/gray_image.png', gray_image)
    return gray_image


def Convert():
    a_matrix = grayscale("./image/map28.png")
    for i in range(len(a_matrix)):
        for j in range(len(a_matrix[i])):
            if a_matrix[i][j] == 255:
                temp = []
                temp.append(j)
                temp.append(i)
                listXY.append(temp)
            else:
                a_matrix[i][j] = 0  # black
    temp_list = bubbleSort(listXY,0)
    temp_list_1 = bubbleSort(listXY,1)
    final_node = []
    i = 0
    while i < len(temp_list):
        if (temp_list[i][0] + 4) % 5 == 0:
            final_node.append(temp_list[i])
        i+=1
    j = 0    
    while j < len(temp_list_1):
        if (temp_list_1[j][1] + 1) % 2 == 0 and CheckList(temp_list_1[j],final_node) == False:
            final_node.append(temp_list_1[j])
        j+=1    
    print(len(final_node) )
    return final_node

def bubbleSort(alist,index):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i][index]>alist[i+1][index]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    return alist

def CompareXY(x, y):
    if (x[0] == y[0]) & (x[1] == y[1]):
        return True
    else:
        return False


def CheckList(x, list):
    for i in range(len(list)):
        if CompareXY(x, list[i]):
            return True
    return False


def neighbor(x, y):
    if (x[0] == y[0]) and ((x[1] == y[1] + 1) or (x[1] == y[1] - 1)):
        return True
    if (x[1] == y[1]) and ((x[0] == y[0] + 1) or x[0] == y[0] - 1):
        return True
    if (x[0] == y[0] + 1) and ((x[1] == y[1] + 1) or (x[1] == y[1] - 1)):
        return True
    if (x[0] == y[0] - 1) and ((x[1] == y[1] + 1) or (x[1] == y[1] - 1)):
        return True
    else:
        return False


def init(x, list_node):
    map_distance[tuple(x)] = 0
    parent_node[tuple(x)] = x
    dead_node[tuple(x)] = False
    for i in range(len(list_node)):
        if CompareXY(x, list_node[i]) == False:
            map_distance[tuple(list_node[i])] = 10000
            parent_node[tuple(list_node[i])] = []
            dead_node[tuple(list_node[i])] = False


def getParentNode(x):
    return parent_node[tuple(x)]


def getDistance(x):
    return map_distance[tuple(x)]


def getStatus(x):
    return dead_node[tuple(x)]


def updateDistance(x, d):
    map_distance[tuple(x)] = d


def updateParent(x, p):
    parent_node[tuple(x)] = p


def updateStatus(x, status):
    dead_node[tuple(x)] = status


def dijkstra(x, y, list_node):
    init(x, list_node)
    current = x
    count = []
    index = []
    d = 0
    count_node = 0
    while current != y:
        for i in range(len(list_node)):
            # if neighbor(current,list_node[i]):
            temp_node = list_node[i]
            dist = math.hypot(temp_node[0] - current[0], temp_node[1] - current[1])
            if dist >= 5 and dist <= 7:
                d = getDistance(current) + 1
                if d < getDistance(list_node[i]):
                    updateDistance(list_node[i], d)
                    updateParent(list_node[i], current)
                    count.append(d)
                    index.append(i)
            updateStatus(current, True)
            temp = 10000
        if d == 0:
            print("Wrong path!")
            sys.exit(0)
        for i in range(len(count)):
            if count[i] < temp and getStatus(list_node[index[i]]) == False:
                temp = count[i]
                current = list_node[index[i]]
                count_node += 1
    return count_node


def reverse_list(list_node):
    arr = []
    for i in range(len(list_node) - 1, 0, -1):
        arr.append(list_node[i])
    arr.append(list_node[0])
    return arr


def getPath(x, y, list_node):
    if (CheckList(x, list_node) and CheckList(y, list_node)) == False:
        print("Wrong path!!")
        sys.exit(0)
    start = time.time()
    count = dijkstra(x, y, list_node)
    path = []
    path.append(y)
    k = y
    while k != x:
        path.append(getParentNode(k))
        k = getParentNode(k)
    end = time.time()
    print("Time process : %0.2fs" % (end - start))
    i = len(path) - 1
    print("Number of node in path : %d" % i)
    print("Number node scan per second : %0.0f" % (count / (end - start)))
    return reverse_list(path)


list_node = Convert()

def compareCoord(x, y):
    xp = x
    yp = y
    for i in range(len(list_node)):
        disx = abs(x - list_node[i][0])
        disy = abs(y - list_node[i][1])
        if disx < 30 and disy < 30:
            xp = list_node[i][0]
            yp = list_node[i][1]
            break
    return xp, yp

def distanceCoord(x1,y1,x2,y2):
    dist = math.hypot(x2 - x1, y2 - y1)
    return dist

def calculate_angle(point_x, point_y, target_x, target_y):
    neg_dir = math.atan2(point_y - target_y, target_x - point_x) * 180 / PI
    return neg_dir



pygame.init()
track = pygame.image.load("./im/map4.png")
player = pygame.image.load("./im/car5.png")
dotbegin = pygame.image.load("./im/loc.png")
dotend = pygame.image.load("./im/loc.png")
tflamp = pygame.image.load("./im/green.png")
tflamp2 = pygame.image.load("./im/yellow.png")
tflamp3 = pygame.image.load("./im/red.png")
stone = pygame.image.load("./im/stone.png")
# dot = []
# for i in range(50):
#     temp = pygame.image.load("./im/loc.png")
#     dot.append(temp)
screen = pygame.display.set_mode((1200,686))

trackx = 0
tracky = 0
xpos = 0
ypos = 520
xx = 0
yy = 0
xbegin = 0
ybegin = 0
xend = 0
yend = 0
xstone, ystone = 0, 0
check_stone = 0
direction = 0
running = 1
check = 1
i = 0
# xlamp = 250
# ylamp = 475
xlamp = 200
ylamp = 500
# xlamp2 = 550
# ylamp2 = 350
xlamp2 = 400
ylamp2 = 350
xlamp3 = 950
ylamp3 = 220

def initTimeLamp():
    time = random.randrange(0, 15)
    return time

def displayLamp(lampNow, timeLamp):
    if lampNow == "red" and timeLamp == 0:
        lampNow = "green"
        timeLamp = 15
    elif lampNow == "green" and timeLamp == 0:
        lampNow = "yellow"
        timeLamp = 3
    elif lampNow == "yellow" and timeLamp == 0:
        lampNow = "red"
        timeLamp = 10
    return lampNow, timeLamp

screen.blit(track, (trackx,tracky))
pygame.display.flip()
count = 0
while running:
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)

        if event.type == pygame.MOUSEBUTTONUP:
            count = count + 1
            pos = pygame.mouse.get_pos()
            # print(pos)
            xx = pos[0]
            yy = pos[1]
            if count == 1:
                xbegin, ybegin = compareCoord(xx, yy)
                xpos, ypos = xbegin, ybegin
                screen.blit(track, (trackx, tracky))
                screen.blit(dotbegin, (xbegin, ybegin))
                pygame.display.flip()
            elif count == 2:
                xend , yend = compareCoord(xx, yy)
                screen.blit(track, (trackx, tracky))
                screen.blit(dotbegin, (xbegin, ybegin))
                screen.blit(dotend, (xend, yend))
                pygame.display.flip()
                running = 0
                break


pathDriver = getPath([xbegin,ybegin],[xend, yend],list_node)
pathNode = []

for k in range(len(pathDriver) - 1):
    if k%15 == 0:
        pathNode.append(pathDriver[k])
timeLamp1 = initTimeLamp()
timeLamp2 = initTimeLamp()
timeLamp3 = initTimeLamp()
lamp1 = "green"
lamp2 = "green"
lamp3 = "red"
dt_started = datetime.datetime.utcnow()
running = 1
i = 1
dir = 0
j = 15
angle = 0
angle_past = 0
t1 = 0
flag = 0
if pathNode[0][0] > pathNode[1][0]:
    flag = 1
if (pathNode[0][0] > pathNode[len(pathNode) - 1][0]):
    flag = 2
if (pathNode[0][1] < pathNode[len(pathNode)-1][1]):
    flag = 3
print("flag : ", flag)
def convert_speed(speed):
    return speed / 15.0

while running:
    pygame.display.set_caption('driving')
    screen.fill(0)

    if check == 1:
        # get nextNode in path
        dis_temp = distanceCoord(xpos, ypos, pathNode[i][0], pathNode[i][1])
        for j in range(len(pathNode)):

            if flag == 1:
                if angle < -90:
                    print("< - 90")
                    if ypos < pathNode[j][1]:
                        i = j
                        break
                elif angle > 90:
                    print("> 90")
                    if ypos > pathNode[j][1]:
                        i = j
                        break
                else:
                    "else"
                    if dis_temp > 0 and dis_temp < 2:
                        i = i + 1
                        break
            elif flag == 2:
                if angle < -90:
                    if ypos < pathNode[j][1]:
                        i = i
                        break
                elif angle > 90:
                    if ypos > pathNode[j][1]:
                        i = j
                        break
                else:
                    if dis_temp > 0 and dis_temp < 3:
                        i = i + 1
                        break
            elif flag == 3:
                if angle < -90:
                    if ypos < pathNode[j][1]:
                        i = i
                        break
                elif angle > 90:
                    if ypos > pathNode[j][1]:
                        i = j
                        break
                else:
                    print("else 2")
                    if dis_temp > 0 and dis_temp < 3:
                        i = i + 1
                        break
            else:
                if xpos <= pathNode[j][0]:
                    i = j
                    break
        dis_end = distanceCoord(xpos, ypos, pathNode[len(pathNode) -1][0], pathNode[len(pathNode)-1][1])
        if dis_end >= 0 and dis_end <1:
            break

        angle = calculate_angle(xpos, ypos, pathNode[i][0], pathNode[i][1])
        # if angle > 90:
        #     angle = angle - 180
        dir = xlttm.calc_drive.calc_drive(angle_past - angle)
        print("angle : ", angle, " dir : ", dir, " angle_past : ", angle_past)

        if xstone == 0 and ystone == 0:
            if xpos < xlamp - 7:
                # dis = distanceCoord(xpos, ypos, 235, 450)
                dis = distanceCoord(xpos, ypos, 175, 475)
                if lamp1 == "red":
                    t1 = - timeLamp1
                elif lamp1 == "green":
                    t1 = timeLamp1
                elif lamp1 == "yellow":
                    t1 = timeLamp1 - 1.5
                sp = xlttm.calc_lamp.calc_speed_lamp(angle_past - angle, t1, dis)
                speed = convert_speed(sp)
                print(" time : ", t1, " angle : ", -dir, " dis : ", dis, " speed : ", sp)

                movex = - math.cos(angle / 57.29) * speed
                movey = - math.sin(angle / 57.29) * speed
            elif xpos > xlamp and xpos < xlamp2 - 5 and distanceCoord(xpos, ypos, 400, 425) < 200:
                # dis = distanceCoord(xpos, ypos, 550, 425)
                dis = distanceCoord(xpos, ypos, 400, 425)
                if lamp2 == "red":
                    t1 = - timeLamp2
                elif lamp2 == "green":
                    t1 = timeLamp2
                elif lamp2 == "yellow":
                    t1 = timeLamp2 - 1.5
                sp = xlttm.calc_lamp.calc_speed_lamp(angle_past - angle, t1, dis)
                speed = convert_speed(sp)
                print(" time : ", t1, " angle : ", -dir, " dis : ", dis, " speed : ", sp)

                movex = - math.cos(angle / 57.29) * speed
                movey = - math.sin(angle / 57.29) * speed
            elif xpos > xlamp2 and xpos < xlamp3 - 5 and distanceCoord(xpos, ypos, 950, 300) < 200:
                dis = distanceCoord(xpos, ypos, 950, 300)
                if lamp3 == "red":
                    t1 = - timeLamp3
                elif lamp3 == "green":
                    t1 = timeLamp3
                elif lamp3 == "yellow":
                    t1 = timeLamp3 - 1.5
                sp = xlttm.calc_lamp.calc_speed_lamp(angle_past - angle, t1, dis)
                speed = convert_speed(sp)
                print(" time : ", t1, " angle : ", -dir, " dis : ", dis, " speed : ", sp)

                movex = - math.cos(angle / 57.29) * speed
                movey = - math.sin(angle / 57.29) * speed
            else:
                movex = - math.cos(angle / 57.29) * 1.5
                movey = - math.sin(angle / 57.29) * 1.5
        elif xstone != 0 and ystone != 0:
            if xpos < xlamp and xlamp < xstone :
                # dis = distanceCoord(xpos, ypos, 235, 450)
                dis = distanceCoord(xpos, ypos, 175, 475)
                if lamp1 == "red":
                    t1 = - timeLamp1
                elif lamp1 == "green":
                    t1 = timeLamp1
                elif lamp1 == "yellow":
                    t1 = timeLamp1 - 2
                sp = xlttm.calc_lamp.calc_speed_lamp(angle_past - angle, t1, dis)
                speed = convert_speed(sp)
                # print("i : ", i, " time : ", t1, " angle : ", -dir, " dis : ", dis, " speed : ", sp)

                movex = - math.cos(angle / 57.29) * speed
                movey = - math.sin(angle / 57.29) * speed
            elif xpos > xlamp and xpos < xlamp2 and xlamp2 < xstone:
                # dis = distanceCoord(xpos, ypos, 550, 425)
                dis = distanceCoord(xpos, ypos, 400, 425)
                if lamp2 == "red":
                    t1 = - timeLamp2
                elif lamp2 == "green":
                    t1 = timeLamp2
                elif lamp2 == "yellow":
                    t1 = timeLamp2 - 2
                sp = xlttm.calc_lamp.calc_speed_lamp(angle_past -angle, t1, dis)
                speed = convert_speed(sp)
                # print("i : ", i, " time : ", t1, " angle : ", -dir, " dis : ", dis, " speed : ", sp)

                movex = - math.cos(angle / 57.29) * speed
                movey = - math.sin(angle / 57.29) * speed
            elif xpos > xlamp2 and xpos < xlamp3 and xlamp3 < xstone:
                dis = distanceCoord(xpos, ypos, 950, 300)
                if lamp3 == "red":
                    t1 = - timeLamp3
                elif lamp3 == "green":
                    t1 = timeLamp3
                elif lamp3 == "yellow":
                    t1 = timeLamp3 - 2
                sp = xlttm.calc_lamp.calc_speed_lamp(angle_past -angle, t1, dis)
                speed = convert_speed(sp)
                # print("i : ", i, " time : ", t1, " angle : ", -dir, " dis : ", dis, " speed : ", sp)

                movex = - math.cos(angle / 57.29) * speed
                movey = - math.sin(angle / 57.29) * speed
            elif distanceCoord(xpos, ypos, xstone, ystone) < 150:
                dis = distanceCoord(xpos, ypos, xstone - 20, ystone)
                sp = xlttm.calc_stone.calc_speed_stone(dis -20, -dir)
                speed = convert_speed(sp)
                # print("i : ", i , " angle : ", -dir, " dis : ", dis, " speed : ", sp)

                movex = - math.cos(angle / 57.29) * speed
                movey = - math.sin(angle / 57.29) * speed
            else:
                movex = - math.cos(-dir / 57.29) * 1.0
                movey = - math.sin(-dir / 57.29) * 1.0
        xpos = xpos - movex
        ypos = ypos + movey
        print("x : ", xpos, "y : ", ypos, pathNode[i])


        playerrot = pygame.transform.rotate(player,angle_past + dir)
        angle_past = angle_past + dir
        screen.blit(track, (trackx,tracky))
        screen.blit(dotbegin, (xbegin, ybegin))
        screen.blit(dotend, (xend, yend))
        if xstone != 0 and ystone != 0:
            screen.blit(stone, (xstone, ystone -20))

        screen.blit(playerrot, (xpos - 10,ypos - 15))
        dt_ended = datetime.datetime.utcnow()
        if ((dt_ended - dt_started).total_seconds() > 1.0) and ((dt_ended - dt_started).total_seconds() < 1.1):
            dt_started = dt_ended
            timeLamp1 = timeLamp1 - 1
            timeLamp2 = timeLamp2 - 1
            timeLamp3 = timeLamp3 - 1
        lamp1, timeLamp1 = displayLamp(lamp1, timeLamp1)
        lamp2, timeLamp2 = displayLamp(lamp2, timeLamp2)
        lamp3, timeLamp3 = displayLamp(lamp3, timeLamp3)
        if lamp1 == "green":
            screen.blit(tflamp, (xlamp, ylamp))
        elif lamp1 == "yellow":
            screen.blit(tflamp2, (xlamp, ylamp))
        elif lamp1 == "red":
            screen.blit(tflamp3, (xlamp, ylamp))

        if lamp2 == "green":
            screen.blit(tflamp, (xlamp2, ylamp2))
        elif lamp2 == "yellow":
            screen.blit(tflamp2, (xlamp2, ylamp2))
        elif lamp2 == "red":
            screen.blit(tflamp3, (xlamp2, ylamp2))

        if lamp3 == "green":
            screen.blit(tflamp, (xlamp3, ylamp3))
        elif lamp3 == "yellow":
            screen.blit(tflamp2, (xlamp3, ylamp3))
        elif lamp3 == "red":
            screen.blit(tflamp3, (xlamp3, ylamp3))
        lamp_font = pygame.font.SysFont(None, 25)
        # render text
        label = lamp_font.render(str(timeLamp1), 1, (255, 255, 255))
        screen.blit(label, (225, 500))
        label2 = lamp_font.render(str(timeLamp2), 1, (255, 255, 255))
        screen.blit(label2, (450, 375))
        label3 = lamp_font.render(str(timeLamp3), 1, (255, 255, 255))
        screen.blit(label3, (975, 225))
        pygame.display.flip()

        for event in pygame.event.get():
        # check if the event is the X button
            if event.type==pygame.QUIT:
                # if it is quit the game
                pygame.quit()
                exit(0)

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if check_stone == 0:
                    xstone, ystone = compareCoord(pos[0], pos[1])
                    check_stone = 1
                else:
                    check_stone = 0
                    xstone = 0
                    ystone = 0