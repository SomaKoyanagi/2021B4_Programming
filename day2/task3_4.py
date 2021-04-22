import numpy as np

x = np.array([[1.0, 0.5], [-0.4, 0.1]])
W = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]]) 
b = np.array([0.1, 0.2, 0.3])

class Affine:
    def __init__(self,w,b):
        self.w = w
        self.b = b
        self.x = None
        self.dw = None
        self.db = None
    
    def forward(self,x):
        self.x = x
        result = np.dot(self.x,self.w) + self.b
        return result

    def backprop(self,dz):
        dx = np.dot(dz,self.w.T)
        self.dw = np.dot(self.x.T,dz)
        self.db = np.sum(dz,axis=0)
        return dx,self.dw,self.db


out = Affine(W,b)
output = out.forward(x)
dz = np.full(output.shape,1.0)
print("順伝播出力:\n",output)
dx,dw,db = out.backprop(dz)
print("逆伝播出力dx:\n",dx)
print("逆伝播出力dw:\n",dw)
print("逆伝播出力db:\n",db)
