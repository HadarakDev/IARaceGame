import pygame
import random
from pygame.locals import *
from  data import *
from display import *

def displayTxtMap(gameMap):
    for r in gameMap:
        for cell in r:
            print(cell, end=' ')
        print()

def isMapFull(curY, curX, row, col, gameMap):
    if (curX == col and curY == row) :
        if (gameMap[curY][curX - 1] != "0" and gameMap[curY - 1][curX] != "0"): #check top-left
            return 1
        return 0
    if (curX == 0 and curY == row):
        if (gameMap[curY][curX + 1] != "0" and gameMap[curY - 1][curX] != "0"): #check top-right
            return 1
        return 0
    if (curX == 0 and curY == 0):
        if (gameMap[curY][curX + 1] != "0" and gameMap[curY + 1][curX] != "0"): #check bot-right
            return 1
        return 0
    if (curX == col and curY == 0):
        if (gameMap[curY][curX - 1] != "0" and gameMap[curY + 1][curX] != "0"): #check bot-left
            return 1
        return 0
    if (curY == 0):
        if (gameMap[curY + 1][curX] != "0" and gameMap[curY][curX + 1] != "0" and gameMap[curY][curX -1] != "0"): #check bot-left-right
            return 1
        return 0
    if (curY == row):
        if (gameMap[curY -1][curX] != "0" and gameMap[curY][curX + 1] != "0" and gameMap[curY][curX -1] != "0"): #check top-right-left
            return 1
        return 0
    if (curX == col):
        if (gameMap[curY + 1][curX] != "0" and gameMap[curY - 1][curX] != "0" and gameMap[curY][curX - 1] != "0"): #check top-bot-left
            return 1
        return 0
    if (curX == 0):
        if (gameMap[curY + 1][curX] != "0" and gameMap[curY - 1][curX] != "0" and gameMap[curY ][curX + 1] != "0"): #check top-bot-right
            return 1
        return 0
    if curX > 0 and curX < col and curY > 0 and curY < row:
        if gameMap[curY + 1][curX] != "0" and gameMap[curY - 1][curX] != "0" and gameMap[curY][curX + 1] != "0" and gameMap[curY][curX -1] != "0": #check all
            return 1
        return 0
    return 0

def determineStartDirection(curY, curX, row, col, gameMap, dico):
    #check impossible
    while isMapFull(curY, curX, row, col, gameMap) == 0:
        nb = ["top", "bot", "left", "right"]
        if curX == col and curY == row: # bas droite
            nb  = ["top", "left"]
        elif curX == 0 and curY == row: # bas gauche
            nb  = ["top", "right"]
        elif curX == 0 and curY == 0: # top gauche
            nb  = ["bot", "right"]
        elif curX == col and curY == 0: # top droite
            nb  = ["bot", "left"]
        elif curY == 0: # top
            nb  = ["bot", "right", "left"]
        elif curY == row: # bas
            nb  = ["top", "right", "left"]
        elif curX == col: # droite
            nb  = ["top", "bot", "left"]
        elif curX == 0: # gauche
            nb  = ["top", "bot", "right"]

        direction = random.choice(nb)
        if gameMap[curY + dico[direction]["y"]][curX + dico[direction]["x"]] == "0":
            return direction
    return "error"
        

def addStart(gameMap, rowY, colX, directions):
    coordY = random.randint(0, rowY)
    coordX = random.randint(0, colX)
    direction = determineStartDirection(coordY, coordX, rowY, colX, gameMap, directions)

    if direction == "left":
        gameMap[coordY][coordX] = "L"
    elif direction == "right":
        gameMap[coordY][coordX] = "R"
    elif direction == "top":
        gameMap[coordY][coordX] = "B"
    elif direction == "bot":
        gameMap[coordY][coordX] = "T"
    return gameMap, coordX, coordY, direction

def addEndTile(gameMap, coordY, coordX, direction, directions):
    if direction == "left":
        gameMap[coordY + directions[direction]["y"]][coordX + directions[direction]["x"]] = "l"
    elif direction == "right":
        gameMap[coordY + directions[direction]["y"]][coordX + directions[direction]["x"]] = "r"
    elif direction == "top":
       gameMap[coordY + directions[direction]["y"]][coordX + directions[direction]["x"]] = "t"
    elif direction == "bot":
        gameMap[coordY + directions[direction]["y"]][coordX + directions[direction]["x"]] = "b"
    return gameMap

def generateMap(length, rowY, colX):
    gameMap =  [["0" for x in range(colX)] for y in range(rowY)] 
    directions = declareDirection()
    tiles = declareTiles()
    rowY -= 1
    colX -= 1
    if length > rowY * colX:
        length = rowY * colX - 2
    with open("map.txt", "w") as file:

        gameMap, coordX, coordY, direction = addStart(gameMap, rowY, colX, directions)
        for idx in range(0, length):
            t = random.choice(tiles[direction])
            nextDirection = t["output_" + direction]

            newY = coordY + directions[direction]["y"] + directions[nextDirection]["y"]
            newX = coordX + directions[direction]["x"] + directions[nextDirection]["x"]
            i = 0
            while newX < 0 or newX > colX or newY < 0 or newY > rowY or gameMap[newY][newX] != "0":
                t = random.choice(tiles[direction])
                nextDirection = t["output_" + direction]
                newY = coordY + directions[direction]["y"] + directions[nextDirection]["y"]
                newX = coordX + directions[direction]["x"] + directions[nextDirection]["x"]
                i = i + 1
                if (i > 10):
                    return gameMap, idx
            coordY += directions[direction]["y"]
            coordX += directions[direction]["x"]
            gameMap[coordY][coordX] = t["symbol"]
            direction = nextDirection
            if isMapFull(coordY + directions[direction]["y"], coordX + directions[direction]["x"], rowY, colX, gameMap) == 1:
                gameMap = addEndTile(gameMap, coordY, coordX, direction, directions)
                return gameMap, idx + 1
    gameMap = addEndTile(gameMap, coordY, coordX, direction, directions)
    return gameMap, idx + 1

def generateBackground(gameMap, backY, backX, mapY, mapX):
    grass = pygame.image.load("./gameAsset/Grass_Tile.png").convert()
    backgroundSoil = pygame.image.load("./gameAsset/Soil_Tile.png").convert()
    backgroundSoil1 = pygame.image.load("./gameAsset/Soil_Tile1.png").convert()
    backgroundSoil2 = pygame.image.load("./gameAsset/Soil_Tile2.png").convert()
    backgroundSoil3 = pygame.image.load("./gameAsset/Soil_Tile3.png").convert()
    water = pygame.image.load("./gameAsset/Water_Tile.png").convert()

    background = []
    background.extend((backgroundGrass, backgroundSoil, backgroundSoil, backgroundSoil, backgroundSoil2,  backgroundSoil2,  backgroundSoil1, backgroundSoil3, backgroundSoil3 ))
    backMap =  [[water for x in range(backX)] for y in range(backY)] 
    for y in range (0, mapY):
        for x in range (0, mapX):
            if gameMap[y][x] != "0":
                backMap[y + 2][x + 2] = grass
            else:
                image = random.choice(background)
                backMap[y + 2][x + 2] = image
    return backMap

if __name__ == '__main__':

    screenX = 16
    screenY = 12

    gameMapX = screenX - 4
    gameMapY = screenY - 4

    gameMap, length = generateMap(40, gameMapY, gameMapX)
    while length < 40:
        gameMap, length = generateMap(40, gameMapY, gameMapX)
        print(length)
    backMap = generateBackground(gameMap, screenY, screenX, gameMapY,  gameMapX)    
    display(gameMap, backMap, screenY, screenX, gameMapY, gameMapX)
