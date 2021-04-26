import numpy as np
import sys,os
sys.path.append(os.pardir)
from dataset.mnist import load_mnist
import task4_1

# 読み込み(初回時のみダウンロードも行います) 
(x_train,t_train),(x_test,t_test) = load_mnist(normalize=True,one_hot_label=True)

net = task4_1.NeuralNetwork(784,500,10,0.1)
batch = 100
epoc = 100
learning_rate = 0.0001
train_size = 100
iter_epoc = max(train_size/batch,1)
train_loss_list =[]
train_acc_list =[]
test_acc_list = []
num = np.random.randint(0, 60000, (100,))

for i in range(epoc):
    batch_mask = np.random.choice(train_size,batch)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]
    print(x_batch.shape)
    print(t_batch.shape)
    grad  = net.backprop(x_batch,t_batch)
    for key in params:
        net.params[key] -= learning_rate * grad[key]
    loss = net.loss(x_batch,t_batch)
    train_loss_list.append(loss)

    if i % iter_epoc ==0:
        train_acc = net.accuracy(x_train,t_train)
        test_acc = net.accuracy(x_test,t_test)
        train_acc_list.append(train_acc)
        test_acc_list.append(test_acc)

