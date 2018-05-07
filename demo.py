import pygame
from pygame.locals import *
import time
import math
import random
import datetime

pygame.init()
track = pygame.image.load("resources/images/map4.png")
player = pygame.image.load("resources/images/car5.png")
tflamp = pygame.image.load("resources/images/green.png")
tflamp2 = pygame.image.load("resources/images/yellow.png")
tflamp3 = pygame.image.load("resources/images/red.png")
stone = pygame.image.load("resources/images/stone.png")
screen = pygame.display.set_mode((1200,686))
trackx = 0
tracky = 0
xpos = 0
ypos = 520
xlamp = 250
ylamp = 475
xlamp2 = 550
ylamp2 = 350
xlamp3 = 950
ylamp3 = 220
keys=[False,False,False,False]
direction = 0
forward = 0
xstone, ystone = 0, 0

running = 1
check = 1

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
        timeLamp = 15
    return lampNow, timeLamp

timeLamp1 = initTimeLamp()
timeLamp2 = initTimeLamp()
timeLamp3 = initTimeLamp()
lamp1 = "green"
lamp2 = "green"
lamp3 = "red"
dt_started = datetime.datetime.utcnow()

while running:
    pygame.display.set_caption('driving')
    screen.fill(0)
    if check == 1:
        if keys[0]==True:
            direction+= 2
        if keys[1]==True:
            direction-= 2
        if keys[2]==True:
            forward-= 0.2
        if keys[3]==True and forward <= 0:
            forward+= 0.2
        print("forward : ", forward, "direction : ", direction)

        movex=math.cos(direction/57.29)*forward
        movey=math.sin(direction/57.29)*forward
        xpos-=movex
        ypos+=movey
        # print("forward : ", forward)
        # print("angle : ", direction)
        # print("xpos : ", movex, "ypos : ", movey)

        playerrot = pygame.transform.rotate(player,direction)
        screen.blit(track, (trackx,tracky))
        screen.blit(playerrot, (xpos,ypos))
        screen.blit(stone, (xstone, ystone))

        dt_ended = datetime.datetime.utcnow()
        if ((dt_ended - dt_started).total_seconds() > 1.0) and ((dt_ended - dt_started).total_seconds() < 1.2):
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
        screen.blit(label, (275, 500))
        label2 = lamp_font.render(str(timeLamp2), 1, (255, 255, 255))
        screen.blit(label2, (525, 375))
        label3 = lamp_font.render(str(timeLamp3), 1, (255, 255, 255))
        screen.blit(label3, (975, 225))

        pygame.display.flip()
    # if -100 < trackx + 3500 < 200 or -150 < tracky + 1550 < 100 or trackx > 100 or tracky > 350:
    #     check = 0
    # time.sleep(0.015)


    for event in pygame.event.get():
    # check if the event is the X button
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)

        if event.type == pygame.KEYDOWN:
            if event.key==K_LEFT:
                keys[0]=True
            elif event.key==K_RIGHT:
                keys[1]=True
            elif event.key==K_UP:
                keys[2]=True
            elif event.key==K_DOWN:
                keys[3]=True

        if event.type == pygame.KEYUP:
            if event.key==pygame.K_LEFT:
                keys[0]=False
            elif event.key==pygame.K_RIGHT:
                keys[1]=False
            elif event.key==pygame.K_UP:
                keys[2]=False
            elif event.key==pygame.K_DOWN:
                keys[3]=False

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print(pos)
            xstone = pos[0]
            ystone = pos[1]
