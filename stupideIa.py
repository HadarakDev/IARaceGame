from utils import *
from predict import *
import sys
import predict
#action : F -> Front -> 0, L -> Left -> 1, R -> Right -> 2


nb_poids = 34
layers = [5, 3, 3]
W = [ x*0.1 for x in range(nb_poids)]
X = [ x*0.1 for x in range(5)]


next_input_must_be("START player")
player = int(input())
next_input_must_be("STOP player")

next_input_must_be("START settings")
line = input()
while line != "STOP settings":
    line = input()

grid = []

while True:
    # Get sensors information
    next_input_must_be("START turn")
    string_sensors = input()
    other_information = input()
    next_input_must_be("STOP turn")

    sensors = getSensorsFromString(string_sensors)
    isCrash, score = parse_other_information(other_information)
    print(isCrash, score, file=sys.stderr)

    # Send decision
    print("START action")
    print(take_decision(layers, W, sensors))
    print("STOP action")
