import numpy as np
import math
import sys


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def predict_next_move(layers, W, X):

    #normalize

    X = [ (x - 0) / 16 for x in X ]

    acc = 0
    X.append(1)  # biais
    for i in range(len(layers) - 1):
        
        end = layers[i] * layers[i + 1] + layers[i + 1]
        Wn = W[acc : acc + end]
        # print("HERE", Wn, file=sys.stderr)
        acc = acc + end
        res = []
        for x in range(layers[i + 1]):
            for j in range(layers[i]):
                res.append(np.dot(Wn[x], X[j]))

        X = res
        print(i, len(X), X, file=sys.stderr)

    res = []
    for x in range(layers[-1:][0]):
        for j in range(layers[-2:-1][0]):
            res.append(np.dot(Wn[x], X[j]))

    X = res
    output = X[:-1]

    return np.argmax(output)


def take_decision(layers, W, X):


    result = predict_next_move(layers, W, X)

    if result == 0:
        return "F"
    elif result == 1:
        return "L"
    elif result == 2:
        return "R"




