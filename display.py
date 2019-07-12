import pygame
import random
from pygame.locals import *
import numpy as np
import math

def generateBackground(gameMap, backY, backX, mapY, mapX):
    backgroundSoil = pygame.image.load("./gameAsset/Soil_Tile.png").convert()
    backgroundSoil1 = pygame.image.load("./gameAsset/Soil_Tile1.png").convert()
    backgroundSoil2 = pygame.image.load("./gameAsset/Soil_Tile2.png").convert()
    backgroundSoil3 = pygame.image.load("./gameAsset/Soil_Tile3.png").convert()
    backgroundSoil4 = pygame.image.load("./gameAsset/Soil_Tile4.png").convert()
    backgroundSoil5 = pygame.image.load("./gameAsset/Soil_Tile5.png").convert()
    water = pygame.image.load("./gameAsset/Water_Tile.png").convert()

    # background = []
    background = [ backgroundSoil,  backgroundSoil1,  backgroundSoil2, backgroundSoil3, backgroundSoil4 , backgroundSoil5 ]
    backMap =  [[np.random.choice(background, 1, p=[0.4, 0.01, 0.19, 0.19, 0.01, 0.20])[0] for x in range(backX)] for y in range(backY)] 
    
    for y in range (0, mapY):
        for x in range (0, mapX):
            if gameMap[y][x] != "0":
                backMap[y + 2][x + 2] = backgroundSoil
            else:
                image = np.random.choice(background, 1, p=[0.3, 0.01, 0.19, 0.19, 0.01, 0.30])[0]
                backMap[y + 2][x + 2] = image
    return backMap

def displayMap(gameMap, screen, mapY, mapX, margin):
    cornerTL = pygame.image.load("./gameAsset/cornerTL.png").convert_alpha()
    cornerTR = pygame.image.load("./gameAsset/cornerTR.png").convert_alpha()
    cornerBL = pygame.image.load("./gameAsset/cornerBL.png").convert_alpha()
    cornerBR = pygame.image.load("./gameAsset/cornerBR.png").convert_alpha()
    horizontal = pygame.image.load("./gameAsset/horizontal.png").convert()
    vertical = pygame.image.load("./gameAsset/vertical.png").convert()

    verticalLStart = pygame.image.load("./gameAsset/verticalLStart.png").convert()
    verticalRStart = pygame.image.load("./gameAsset/verticalRStart.png").convert()
    horizontalBStart = pygame.image.load("./gameAsset/horizontalBStart.png").convert()
    horizontalTStart = pygame.image.load("./gameAsset/horizontalTStart.png").convert()

    verticalLEnd = pygame.image.load("./gameAsset/verticalLEnd.png").convert()
    verticalREnd = pygame.image.load("./gameAsset/verticalREnd.png").convert()
    horizontalBEnd = pygame.image.load("./gameAsset/horizontalBEnd.png").convert()
    horizontalTEnd = pygame.image.load("./gameAsset/horizontalTEnd.png").convert()

    xPos = margin
    yPos = margin
    for y in range(0, mapY):
        for x in range(0, mapX):
            if gameMap[y][x] == "/":
                screen.blit(cornerTL, (xPos, yPos))
            elif gameMap[y][x] == "\\":
                screen.blit(cornerTR, (xPos, yPos))
            elif gameMap[y][x] == "(":
                screen.blit(cornerBL, (xPos, yPos))
            elif gameMap[y][x] == ")":
                screen.blit(cornerBR, (xPos, yPos))
            elif gameMap[y][x] == "=":
                screen.blit(horizontal, (xPos, yPos))
            elif gameMap[y][x] == "|":
                screen.blit(vertical, (xPos, yPos))
            elif gameMap[y][x] == "L":
                screen.blit(verticalLStart, (xPos, yPos))
            elif gameMap[y][x] == "R":
                screen.blit(verticalRStart, (xPos, yPos))
            elif gameMap[y][x] == "B":
                screen.blit(horizontalBStart, (xPos, yPos))
            elif gameMap[y][x] == "T":
                screen.blit(horizontalTStart, (xPos, yPos))
            elif gameMap[y][x] == "l":
                screen.blit(verticalLEnd, (xPos, yPos))
            elif gameMap[y][x] == "r":
                screen.blit(verticalREnd, (xPos, yPos))
            elif gameMap[y][x] == "b":
                screen.blit(horizontalTEnd, (xPos, yPos))
            elif gameMap[y][x] == "t":
                screen.blit(horizontalBEnd, (xPos, yPos))
            xPos += 100
        xPos = margin
        yPos += 100

def displayBackground(backMap, screenY, screenX, screen):
    xPos = 0
    yPos = 0
    for y in range (0, screenY):
        for x in range (0, screenX):
            screen.blit(backMap[y][x], (xPos, yPos))
            xPos += 100
        xPos = 0
        yPos += 100

def getStart(gameMap, mapY, mapX):
    for y in range(0, mapY):
        for x in range(0, mapX):
            if gameMap[y][x] == "T":
                return y, x, 180
            elif gameMap[y][x] == "B":
                return y, x, 0
            elif gameMap[y][x] == "R":
                return y, x, -90
            elif gameMap[y][x] == "L":
                return y, x, 90

def display(gameMap, screenY, screenX, mapY, mapX):
         # Initialise screen
    pygame.init()
    margin = 200
    mainClock = pygame.time.Clock()
    screen = pygame.display.set_mode((screenX * 100, screenY * 100))
    pygame.display.set_caption('IA RACE GAME')
    backMap = generateBackground(gameMap, screenY, screenX, mapY,  mapX)  
    displayBackground(backMap, screenY, screenX, screen)
    displayMap(gameMap, screen, mapY, mapX, margin)
    pygame.display.flip()
    
    left = False
    right = False
    forward = False
    backward = False

    carPosY, carPosX, baseDegree = getStart(gameMap, mapY, mapX)
    car = pygame.transform.rotate(car, baseDegree)
    degree = 0
    print(carPosY)
    carPosY = margin + 35 + carPosY * 100
    carPosX = margin + 35 + carPosX * 100
    speed = 1
    # Event loop
    while 1:
        degree = 0
        print(baseDegree)
        if right: # don't need == True
            degree -= 2
            while degree < 0:
                degree += 360
        elif left: # don't need == True
            degree += 2
            while degree > 359:
                degree -= 360

        dx = math.cos(math.radians(baseDegree + degree))
        dy = math.sin(math.radians(baseDegree + degree))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                elif event.key == K_a: # use constants K_a
                    left = True
                elif event.key == K_d: # use constants K_d
                    right = True
                elif event.key == K_w: # use constants K_w
                    forward = True
                elif event.key == K_s: # use constants K_s
                    backward = True

            if event.type == KEYUP:
                if event.key == K_a: # use constants K_a
                    left = False
                elif event.key == K_d: # use constants K_d
                    right = False
                elif event.key == K_w: # use constants K_w
                    forward = False
                elif event.key == K_s: # use constants K_s
                    backward = False

        baseDegree += degree
        if (baseDegree > 360 or baseDegree < 360):
            baseDegree = 0
        if forward:
            carPosY -= int(speed * dx)
            carPosX -= int(speed * dy)
        elif backward:
            carPosY += int(speed * dx)
            carPosX += int(speed * dy)
        

        # if forward:
        #     if baseDegree == 0
        #         carPosY += 1 
        #     carPosX += 0
        car = pygame.transform.rotate(car, degree)
        displayBackground(backMap, screenY, screenX, screen)
        displayMap(gameMap, screen, mapY, mapX, margin)
        screen.blit(car, (carPosX, carPosY))
        pygame.display.flip()
        mainClock.tick(10)