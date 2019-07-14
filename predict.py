import numpy
import math


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def predict_next_move(layers, W, X):
    acc = 0
    X.append(1)  # biais
    for i in range(len(layers) - 1):
        
        end = layers[i] * layers[i + 1] + layers[i + 1]
        Wn = W[acc : acc + end]
        acc = acc + end
        res = []
        for x in range(len(X)):
            summ = 0
            for y in range(len(Wn)):
                summ = summ + Wn[y] * X[x]
            res.append(math.tanh(summ))
        X = res
        
    output = X[:-1]

    return numpy.argmax(output)


def take_decision(layers, W, X):

    result = predict_next_move(layers, W, X)

    if result == 0:
        return "F"
    elif result == 1:
        return  "L"
    elif result == 2:
        return "R"




