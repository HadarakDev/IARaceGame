from utils import *
#action : F -> Front, L -> Left, R -> Right

next_input_must_be("START player")
player = int(input())
next_input_must_be("STOP player")

next_input_must_be("START settings")
line = input()
while line != "STOP settings":
    line = input()

grid = []

while True:
    next_input_must_be("START turn")
    sensors = input()
    next_input_must_be("STOP turn")
    print("START action")
    print("F")
    print("STOP action")
