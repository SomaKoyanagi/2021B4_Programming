import numpy as np
from collections import OrderedDict
import task3_2
import task3_3
import task3_4
import task3_5

class NeuralNetwork:
    def __init__(self,input,hidden,output,weight,bias):
        self.params = {}
        self.params['W1'] = weight * np.random.randn(input,hidden)
        self.params['b1'] = np.zeros(hidden)
        self.params['W2'] = weight * np.random.randn(input,hidden)
        self.params['b2'] = np.zeros(output)
        self.layers = OrderedDict()
        self.layers['Affine1'] = task3_4.Affine(self.params['W1'],self.params['b1'])
        self.layers['Relu'] = task3_2.Relu()
        self.layers['Affine2'] = task3_4.Affine(self.params['W1'],self.params['b1'])
        self.lastLayer = task3_5.SoftmaxCrossEntropy()

    
    def forward(self,x):
        for l in self.layers.values():
            x = l.forward(x)
        return x
    
    def loss(self,x,t):
        y = self.forward(x)
        return self.lastLayer.forward(y,t)
    
    def accuracy(self,x,t):
        y = self.forward(x)
        y = np.argmax(y,axis=1)
        if t.ndim != 1 :t = np.argmax(t,axis=1)
        accuracy = np.sum(y == t) /float(x.shape[0])
        return accuracy


    def backprop(self,x,t):
        self.loss(x,t)
        d = self.lastLayer.backprop(1)
        layers = list(self.layers.values())
        layers.reverse()
        for l in layers:
            d  = layer.backprop(d)
        grads={}
        grads['W2'] = self.layers['Affine1'].dW
        grads['b2'] = self.layers['Affine1'].db
        grads['W1'] = self.layers['Affine2'].dW
        grads['b2'] = self.layers['Affine2'].db
        return grads

    def sgd(self,x,t,learning_rate):
        self.backprop(x,t)
        for key in self.params.keys():
            self.params[key] -= learning_rate * self.grads[key]


