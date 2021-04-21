import numpy as np

class layerout:
    def __init__(self,w):
        self.w = w

    def forward(self,x,b):
        result = np.dot(self.w.T,x)
        result = result + b
        return result


x = np.array([1.0, 0.5])
W = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]]) 
b = np.array([0.1, 0.2, 0.3])

w1 = layerout(W)
print(w1.forward(x,b))