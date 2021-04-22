import numpy as np

a = 2
b = 3
c = 4

class Multiply():
    def __init__(self):
        self.x = None
        self.y = None
    
    def forward(self,x,y):
        self.x = x
        self.y = y
        z = x * y
        return z

    
    def backprop(self,dz):
        dx = dz * self.y
        dy = dz * self.x
        return dx, dy


class Add():
    def __init__(self):
        self.x = None
        self.y = None
    
    def forward(self,x,y):
        self.x = x
        self.y = y
        z = x + y
        return z

    def backprop(self,dz):
        dx = dz*1
        dy = dz*1
        return dx, dy


ab = Add()
add = ab.forward(a,b)
abc = Multiply()
mul = abc.forward(add,c)
print("順伝播出力:",mul)

dz = 1
da_b,dc = abc.backprop(dz)
da,db = ab.backprop(da_b)
print("逆伝播出力 da:",da,"db:",db,"dc:",dc)
