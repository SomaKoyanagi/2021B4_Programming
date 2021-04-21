x1_list = [1,1,0,0]
x2_list = [1,0,1,0]

class Perceptron:

    def __init__(self,w1,w2,theta):
        self.w1 = w1
        self.w2 = w2
        self.theta = theta

    def forward(self,x1,x2):
        num = x1*self.w1 + x2*self.w2
        output = -1
        if  num >= self.theta:
           output = 1
        else:
           output = 0
        return output

#インスタンスの生成
AND = Perceptron(1,1,2)
NAND = Perceptron(-1,-1,-1)
OR = Perceptron(1,1,1)

def XOR(x1,x2):
    out1 = NAND.forward(x1,x2)
    out2 = NAND.forward(x1,out1)
    out3 = NAND.forward(out1,x2)
    return NAND.forward(out2,out3)


for i in range(len(x1_list)):
    x1 = x1_list[i]
    x2 = x2_list[i]
    print('XOR(',x1,',',x2,') = ',XOR(x1,x2))
