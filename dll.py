from ctypes import *
from ctypes.wintypes import *
import ctypes as ct
import os
from collections.abc import Iterable

dll_name = "pyProject.dll"
dllabspath = os.path.dirname(os.path.abspath(__file__)) + os.path.sep + dll_name
myDll = CDLL(dllabspath)

# predict
myDll.predict.argtypes = [ct.c_void_p,
                          ct.c_void_p, ct.c_int, ct.c_int, ct.c_void_p]
myDll.predict.restype = POINTER(ct.c_double)

# loadModel
myDll.loadModel.argtypes = [ct.c_void_p, ct.c_int, ct.c_int, ct.c_void_p]
myDll.loadModel.restype = ct.c_void_p


def predict(W, pyLayers, pyLayer_count, pyInputCountPerSample, pyX):
    layers = (ct.c_int * len(pyLayers))(*pyLayers)
    layer_count = ct.c_int(pyLayer_count)
    X = (ct.c_double * len(pyX))(*pyX)
    inputCountPerSample = ct.c_int(pyInputCountPerSample)
    res = myDll.predict(
        W, layers, layer_count, inputCountPerSample, X
    )
    # print("here", res)
    l = [res[i] for i in range(pyLayers[-1] + 1)]
    return l


def loadModel(pyLayers, pyLayer_count,  pyInputCountPerSample, pyW):
    layers = (ct.c_int * len(pyLayers))(*pyLayers)
    layer_count = ct.c_int(pyLayer_count)
    W = (ct.c_double * len(pyW))(*pyW)
    inputCountPerSample = ct.c_int(pyInputCountPerSample)
    return myDll.loadModel(layers, layer_count, inputCountPerSample, W)