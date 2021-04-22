import numpy as np
import math

x = np.array([-0.5,0.0,1.0,2.0])
e = math.e

class Softmax:
    def __init__(self):
        self.x = None
        self.result = None
    
    def forward(self,x):
        self.result = 1/(1+e**-x)
        return self.result
       

    def backprop(self,dz):
        dx = dz*(1.0-self.result)*self.result
        return dx

out = Softmax()
output = out.forward(x)
print("順伝播出力:",output)
dz = np.full(output.shape,1.0)
back = out.backprop(dz)
print("逆伝播出力:",back)