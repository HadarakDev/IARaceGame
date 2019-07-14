import math
import sys


def deg_to_rad(degrees):
    return degrees / 180.0 * math.pi

def getPosNear(pos, distance):
    x = int(pos[0])
    y = int(pos[1])
    ret = []
    for x in range (x - distance, x + distance + 1):
        for y in range(y - distance, y + distance + 1):
            ret.append((x, y))
    return ret

def isPixelCrash(surface, liste_pos):
    for pos in liste_pos:
        value = surface.get_at(pos)
        if value == (255, 0, 0):
           return True
    return False

def next_input_must_be(value):
    val = input()
    if val != value:
        print("expected input was '%s' instead of '%s'"%(value, val), file=sys.stderr)
        quit()

def getSensorsFromString(input):
    return input.split(";")


# for event in pygame.event.get():
#     if event.type == pygame.QUIT:
#         running = False
#
#     if event.type == pygame.KEYDOWN:
#         None
#
# key = pygame.key.get_pressed()
# if key[pygame.K_LEFT]:
#     vehicles[0].left = True
# if key[pygame.K_RIGHT]:
#     vehicles[0].right = True
# if key[pygame.K_UP]:
#     vehicles[0].forward = True
# if key[pygame.K_DOWN]:
#     vehicles[0].backward = True
# if key[pygame.K_r]:
#     vehicles[0].rect.y, vehicles[0].rect.x,  vehicles[0].angle  = getStart(gameMap, mapY, mapX)
#     vehicles[0].crash, vehicles[0].end = False, False
# if key[pygame.K_ESCAPE]:
#     pygame.quit()