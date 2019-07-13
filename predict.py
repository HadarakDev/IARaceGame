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

    print(numpy.argmax(output))
    return numpy.argmax(output)



layers = [2, 3, 3, 2]
acc = 0
for i in range(len(layers) - 1):
    acc = acc + layers[i] * layers[i + 1] + layers[i + 1]
W = []

w = 0
for i in range(acc):
    W.append(w)
    w = w + 1

X = []
for i in range(layers[0]):
    X.append(i + 10)

print("DATA")
print(layers)
print(W)
print(X)
print("FEED FORWARD")
predict_next_move(layers, W, X)
