import numpy as np
import math
import sys
from dll import *


def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def predict_next_move(layers, W, X):

    #normalize

    X = [ (x - 0) / 16 for x in X ]

    acc = 0
    X.append(1)  # biais
    for l in range(1, len(layers)):
        
        end = layers[i] * layers[i + 1] + layers[i + 1]
        Wn = W[acc : acc + end]
        # print("HERE", Wn, file=sys.stderr)
        acc = acc + end
        res = 0
        Xn = []
        for j in range(1, layers[l] + 1):
            for i in range(layers[l - 1] + 1):
                res = res + Wn[i], X[j]
            if l == len(layers) - 1:
                Xn.append(res)
            else:
                Xn.append(math.tanh(res)) 
        X = Xn
        print(i, len(X), X, file=sys.stderr)

    output = X[:-1]

    return np.argmax(output)


def take_decision(layers, W, X):

    # normalize
    X = [(x - 0) / 16 for x in X]

    myWC = loadModel(layers, len(layers),  layers[0], W)

    result = predict(myWC, layers, len(layers), layers[0], X)

    result.pop(0)
    result = np.argmax(np.array(result))

    if result == 0:
        return "F"
    elif result == 1:
        return "L"
    elif result == 2:
        return "R"




