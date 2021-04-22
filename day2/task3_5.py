import numpy as np

x = np.array([[1.0, 0.5], [-0.4, 0.1]]) 
t = np.array([[1.0, 0.0], [0.0, 1.0]])

class SoftmaxCrossEntropy:
    def __init__(self):
        self.y = None
        self.t = None

    def forward(self,x,t):
        self.y =  np.exp(x) / np.sum(np.exp(x), axis = 1)
        self.t = t
        return  -np.sum(self.t * np.log(self.y))/len(x)

    def backprop(self):
        dx = self.y - self.t
        return dx

out = SoftmaxCrossEntropy()
output = out.forward(x,t)
print("順伝播出力:\n",output)

back = out.backprop()
print("逆伝播出力:\n",back)