import pygame
from pygame.locals import *
import time
import math

pygame.init()
track = pygame.image.load("resources/images/map4.png")
player = pygame.image.load("resources/images/car5.png")
screen = pygame.display.set_mode((1200,686))
trackx = 0
tracky = 0
xpos = 0
ypos = 520
keys=[False,False,False,False]
direction = 0
forward = 0

running = 1
check = 1

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

        movex=math.cos(direction/57.29)*forward
        movey=math.sin(direction/57.29)*forward
        xpos-=movex

        print("x ", trackx)
        ypos+=movey
        print("y ", tracky)

        playerrot = pygame.transform.rotate(player,direction)
        screen.blit(track, (trackx,tracky))
        screen.blit(playerrot, (xpos,ypos))
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
