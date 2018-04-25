# Python program for Dijkstra's single source shortest
# path algorithm. The program is for adjacency matrix
# representation of the graph

from collections import defaultdict
import cv2
import sys, time, math
import numpy as np
import pygame
from pygame.locals import *
import time
import math
from matplotlib import pyplot as plt

np.set_printoptions(threshold='nan')
# a_matrix = [[0,0,0,255,0,255,0,255,0],
#           [0,0,255,0,0,255,0,0,255],
#           [255,255,0,0,0,0,0,0,0],
#           [0,0,255,255,255,0,0,255,0],
#           [0,0,0,0,255,255,255,0,0]]
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
    a_matrix = grayscale("./image/1.png")
    for i in range(len(a_matrix)):
        for j in range(len(a_matrix[i])):
            if a_matrix[i][j] == 255:
                temp = []
                temp.append(j)
                temp.append(i)
                listXY.append(temp)
            else:
                a_matrix[i][j] = 0  # black
    cur = listXY[0]
    final_node = []
    final_node.append(cur)
    for i in range(1, len(listXY), 1):
        d = math.hypot(listXY[i][0] - cur[0], listXY[i][1] - cur[1])
        if d >= 5 and d <= 7:
            final_node.append(listXY[i])
            cur = listXY[i]
    return final_node


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
        print("Wrong path!")
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
    arr_x = []
    arr_y = []
    # while i >= 0:
    #     arr_x.append(path[i][0])
    #     arr_y.append(path[i][1])
    #     i-=1
    # plt.plot(arr_x,arr_y, 'ro')
    # plt.axis([0, 1500, 0, 1500])
    # plt.show()
    return reverse_list(path)


list_node = Convert()
print(list_node)

# [1154, 384] [1106, 2]

def compareCoord(x, y):
    minDis = 1000
    count = 0
    xp = x
    yp = y
    print("x,y : ", x, y)
    for i in range(len(list_node)):
        disx = abs(x - list_node[i][0])
        disy = abs(y - list_node[i][1])
        if disx < 100 and disy < 100:
            xp = list_node[i][0]
            yp = list_node[i][1]
            break
    print("compare : ", (xp,yp))
    return xp, yp


pygame.init()
track = pygame.image.load("./im/map4.png")
player = pygame.image.load("./im/car5.png")
dotbegin = pygame.image.load("./im/loc.png")
dotend = pygame.image.load("./im/loc.png")
screen = pygame.display.set_mode((1200, 686))

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
direction = 0
running = 1
check = 1
i = 0

screen.blit(track, (trackx, tracky))
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
            print(pos)
            xx = pos[0]
            yy = pos[1]

            if count == 1:
                xbegin, ybegin = compareCoord(xx, yy)
                screen.blit(track, (trackx, tracky))
                screen.blit(dotbegin, (xbegin, ybegin))
                pygame.display.flip()
            elif count == 2:
                xend, yend = compareCoord(xx, yy)
                screen.blit(track, (trackx, tracky))
                screen.blit(dotbegin, (xbegin, ybegin))
                screen.blit(dotend, (xend, yend))
                pygame.display.flip()
                running = 0
                break

pathDriver = getPath([xbegin, ybegin], [xend, yend], list_node)

running = 1
while running:
    pygame.display.set_caption('driving')
    screen.fill(0)
    if check == 1:
        xpos = pathDriver[i][0] - 20
        ypos = pathDriver[i][1]
        playerrot = pygame.transform.rotate(player, direction)
        screen.blit(track, (trackx, tracky))
        screen.blit(dotbegin, (xbegin, ybegin))
        screen.blit(dotend, (xend, yend))
        screen.blit(playerrot, (xpos, ypos))
        pygame.display.flip()
        i = i + 1

    for event in pygame.event.get():
        # check if the event is the X button
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print(pos)
            xx = pos[0]
            yy = pos[1]


