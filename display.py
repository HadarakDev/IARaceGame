import pygame
import random
from pygame.locals import *
import numpy as np
import math
from Car import *
from utils import *
import time


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
                return y * 100 +250 , x * 100 + 250, 180
            elif gameMap[y][x] == "B":
                return y * 100 +250 , x * 100 + 250, 0
            elif gameMap[y][x] == "R":
                return y * 100 +250 , x * 100 + 250, 270
            elif gameMap[y][x] == "L":
                return y * 100 +250 , x * 100 + 250, 90

def display(gameMap, screenY, screenX, mapY, mapX):

    pygame.font.init()

    clock = pygame.time.Clock()
    font = pygame.font.SysFont("", 20)

    pygame.init()
    margin = 200
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption('IA RACE GAME')
    backMap = generateBackground(gameMap, screenY, screenX, mapY,  mapX)
    displayBackground(backMap, screenY, screenX, screen)
    displayMap(gameMap, screen, mapY, mapX, margin)
    pygame.display.flip()

    # Params position initiale voiture
    carPosY, carPosX, baseDegree = getStart(gameMap, mapY, mapX)


    vehicles = []
    for id_car in range(1):
        vehicles.append(Car(1, carPosX, carPosY, baseDegree))

    def display_all(main_surface, display_list, text_list):

        displayBackground(backMap, screenY, screenX, screen)
        displayMap(gameMap, screen, mapY, mapX, margin)

        for element in display_list:
            element.display(main_surface)
        for element_val in range(0, len(text_list)):
            main_surface.blit(font.render(str(text_list[element_val]), True, (0, 255, 0)), (10, 10 + (10 * element_val)))

    def update_all(update_list):
        for element in update_list:
            element.update(screen)

    running = True
    while running:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                None

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            vehicles[0].left = True
        if key[pygame.K_RIGHT]:
            vehicles[0].right = True
        if key[pygame.K_UP]:
            vehicles[0].forward = True
        if key[pygame.K_DOWN]:
            vehicles[0].backward = True
        if key[pygame.K_r]:
            vehicles[0].rect.y, vehicles[0].rect.x,  vehicles[0].angle  = getStart(gameMap, mapY, mapX)
            vehicles[0].crash, vehicles[0].end = False, False
        if key[pygame.K_ESCAPE]:
            pygame.quit()

        to_update = vehicles
        to_display = vehicles
        to_text = []
        # to_text = [clock.get_fps(),
        #             vehicle.angle,
        #             vehicle.current_speed,
        #             vehicle.move_x,
        #             vehicle.move_y,
        #             "F " + str(vehicle.forward),
        #             "L " + str(vehicle.left),
        #             "R " + str(vehicle.right)]


        update_all(to_update)
        display_all(screen, to_display, to_text)
        pygame.display.flip()
