import pygame
import random
from pygame.locals import *
import numpy as np
import math
from Car import *
from utils import *
import time

rep = "game"

def generateBackground(gameMap, backY, backX, mapY, mapX):
    backgroundSoil = pygame.image.load("./gameAsset/%s/Soil_Tile.png" % rep).convert()
    backgroundSoil1 = pygame.image.load("./gameAsset/%s/Soil_Tile1.png" % rep).convert()
    backgroundSoil2 = pygame.image.load("./gameAsset/%s/Soil_Tile2.png" % rep).convert()
    backgroundSoil3 = pygame.image.load("./gameAsset/%s/Soil_Tile3.png" % rep).convert()
    backgroundSoil4 = pygame.image.load("./gameAsset/%s/Soil_Tile4.png" % rep).convert()
    backgroundSoil5 = pygame.image.load("./gameAsset/%s/Soil_Tile5.png" % rep).convert()
    water = pygame.image.load("./gameAsset/%s/Water_Tile.png" % rep).convert()

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
    cornerTL = pygame.image.load("./gameAsset/%s/cornerTL.png" % rep).convert_alpha()
    cornerTR = pygame.image.load("./gameAsset/%s/cornerTR.png" % rep).convert_alpha()
    cornerBL = pygame.image.load("./gameAsset/%s/cornerBL.png" % rep).convert_alpha()
    cornerBR = pygame.image.load("./gameAsset/%s/cornerBR.png" % rep).convert_alpha()
    horizontal = pygame.image.load("./gameAsset/%s/horizontal.png" % rep).convert()
    vertical = pygame.image.load("./gameAsset/%s/vertical.png" % rep).convert()

    verticalLStart = pygame.image.load("./gameAsset/%s/verticalLStart.png" % rep).convert()
    verticalRStart = pygame.image.load("./gameAsset/%s/verticalRStart.png" % rep).convert()
    horizontalBStart = pygame.image.load("./gameAsset/%s/horizontalBStart.png" % rep).convert()
    horizontalTStart = pygame.image.load("./gameAsset/%s/horizontalTStart.png" % rep).convert()

    verticalLEnd = pygame.image.load("./gameAsset/%s/verticalLEnd.png" % rep).convert()
    verticalREnd = pygame.image.load("./gameAsset/%s/verticalREnd.png" % rep).convert()
    horizontalBEnd = pygame.image.load("./gameAsset/%s/horizontalBEnd.png" % rep).convert()
    horizontalTEnd = pygame.image.load("./gameAsset/%s/horizontalTEnd.png" % rep).convert()

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
    def display_all(main_surface, display_list):

        displayBackground(backMap, screenY, screenX, screen)
        displayMap(gameMap, screen, mapY, mapX, margin)

        for element in display_list:
            element.display(main_surface)

    def update_all(update_list):
        for element in update_list:
            element.update(screen)

    # Initialisation
    pygame.font.init()

    clock = pygame.time.Clock()
    clock.tick(30)

    font = pygame.font.SysFont("", 20)

    pygame.init()
    margin = 200
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption('IA RACE GAME')
    backMap = generateBackground(gameMap, screenY, screenX, mapY, mapX)
    displayBackground(backMap, screenY, screenX, screen)
    displayMap(gameMap, screen, mapY, mapX, margin)
    pygame.display.flip()

    # Params position initiale voiture
    carPosY, carPosX, baseDegree = getStart(gameMap, mapY, mapX)


    # read number of players
    next_input_must_be("START players")
    number_players = int(input())
    next_input_must_be("STOP players")
    # print("number_players", number_players)

    print("START settings")
    print("Nothing")
    print("STOP settings")


    vehicles = []
    for id_player in range(1, number_players + 1):
        vehicles.append(Car(id_player, carPosX, carPosY, baseDegree))

    # GAME
    running = True
    turn = 1
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE]:
                pygame.quit()
        #recopier ici les touches joueurs

        for id_player in range(1, number_players + 1):
            print("START turn %d %d" % (turn, id_player))
            sensors = vehicles[id_player - 1].getSensorsToString(screen)
            print(sensors)

            print("STOP turn %d %d" % (turn, id_player))
            next_input_must_be("START actions %d %d" % (turn, id_player))
            action = input()
            if action == "R":
                vehicles[id_player - 1].right = True
            elif action == "L":
                vehicles[id_player - 1].left = True
            elif action == "F":
                vehicles[id_player - 1].forward = True
            next_input_must_be("STOP actions %d %d" % (turn, id_player))

        to_update = vehicles
        to_display = vehicles

        update_all(to_update)
        display_all(screen, to_display)
        pygame.display.flip()

        turn += 1
