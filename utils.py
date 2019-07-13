import math


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