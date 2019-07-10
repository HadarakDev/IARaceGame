import pygame
import random
from pygame.locals import *

def displayMap(gameMap, screen, mapY, mapX):
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

    xPos = 0
    yPos = 0
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
                screen.blit(horizontalBEnd, (xPos, yPos))
            elif gameMap[y][x] == "t":
                screen.blit(horizontalTEnd, (xPos, yPos))
            xPos += 100
        xPos = 0
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

def display(gameMap, backMap, screenY, screenX, mapY, mapX):
         # Initialise screen
    pygame.init()

    screen = pygame.display.set_mode((screenX * 100, screenY * 100))
    pygame.display.set_caption('IA RACE GAME')

    displayBackground(screenY, screenX, screen)
    displayMap(gameMap, screen, mapY, mapX)
    pygame.display.flip()

    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        displayBackground(screenY, screenX, screen)
        displayMap(gameMap, screen, mapY, mapX)
        pygame.display.flip()