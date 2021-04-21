

class Perceptron:

    def __init__(self,w1,w2,theta):
        self.w1 = w1
        self.w2 = w2
        self.theta = theta

    def forward(self,x1,x2):
        num = x1*self.w1 + x2*self.w2
        if  num >= self.theta:
           output = 1
        else:
           output = 0
        return output

