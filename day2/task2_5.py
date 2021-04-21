import numpy as np

# 各層のユニット数は[2, 3, 2, 2]、バッチサイズは4
x = np.array([[1.0, 0.5], [-0.3, -0.2], [0.0, 0.8], [0.3, -0.4]])
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
b1 = np.array([0.1, 0.2, 0.3])
W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
b2 = np.array([0.1, 0.2])
W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
b3 = np.array([0.1, 0.2])

def relu(x):
    return np.maximum(0,x)

def softmax(x):
    xmax = max(x)
    a1 = np.exp(x-xmax)
    a2 = np.sum(a1)
    return a1/a2
    
class MLP_3Layer:
    def __init__(self,w1,w2,w3,b1,b2,b3):
        self.w1 = w1
        self.w2 = w2
        self.w3 = w3
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3

    def forward(self,x):
        a1 = self.w1.T.dot(x) + self.b1
        result1= relu(a1)

        a2 = self.w2.T.dot(result1) + self.b2
        result2 = relu(a2)

        a3 = self.w3.T.dot(result2) + self.b2
        result3 = softmax(a3)

        return result3

parameters= MLP_3Layer(W1,W2,W3,b1,b2,b3)
num = -1
y = []
for i in x:
    num += 1
    y.append(parameters.forward(x[num]))
output = np.array(y)
print(output)



