import numpy as np

x = np.array([[1.0, 0.5], [-0.4, 0.1]]) 
t = np.array([[1.0, 0.0], [0.0, 1.0]])

class SoftmaxCrossEntropy:
    def __init__(self):
        self.y = None
        self.t = None

    def forward(self,x,t):
        xmax = np.max(x)
        a1 = np.exp(x-xmax)
        a2 = np.sum(a1)
        self.y = a1/a2
        self.y = self.y.reshape(1,self.y.size)
        self.t = t
        self.t = self.t.reshape(1,self.t.size)
        N = self.y.shape[0]
        return np.sum(self.t*-np.log(self.y[np.arange(N)]))/N

    def backprop(self):
        dx = self.y-self.t
        return dx

out = SoftmaxCrossEntropy()
output = out.forward(x,t)
print("順伝播出力:\n",output)

back = out.backprop()
print("逆伝播出力:\n",back)