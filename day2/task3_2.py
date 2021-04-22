import numpy as np

x = np.array([-0.5,0.0,1.0,2.0])

class Relu:
    def __init__(self):
        self.x = None
        self.mask = None
    
    def forward(self,x):
        self.mask = (x<=0)
        out = x.copy()
        out[self.mask] = 0
        return out

    def backprop(self,dy):
        dy[self.mask] = 0
        dx = dy
        return dx
    
out = Relu()
output = out.forward(x)
print("順伝播出力:",output)
dy = np.full(output.shape,1.0)
back = out.backprop(dy)
print("逆伝播出力:",back)
