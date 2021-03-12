import numpy as np

def softmax(x):
    return np.exp(x) / np.sum(np.exp(x))


x  = [3.0, 2.0, 1.0]
print(softmax(x))