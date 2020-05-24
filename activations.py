import numpy as np

def str2act(name):
    if name == 'sigmoid':
        return sigmoid
    elif name == 'relu':
        return relu
    else:
        return None

def sigmoid():
    return 1

def relu():
    return 1


