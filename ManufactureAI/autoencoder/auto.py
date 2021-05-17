import numpy as np
import matplotlib.pyplot as mp


class Autoencoder:
    def __init__(self, input_dim, hidden_dim, lr=0.01):
        self.w1 = np.random.normal(
            0.0, pow(hidden_dim, -0.5), (input_dim, hidden_dim))
        self.w2 = np.random.normal(
            0.0, pow(hidden_dim, -0.5), (hidden_dim, input_dim))
        self.h = np.zeros((1, hidden_dim))
        self.lr = lr
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.theta = 0

    def sigmoid(self, x):
        return 1/(1+np.exp(-x))

    def feedforward(self, x):
        self.h = self.sigmoid(np.dot(x, self.w1) - self.theta)
        return self.sigmoid(np.dot(self.h, self.w2)-self.theta)

    def feedforward_upto_hidden(self, x):
        return self.sigmoid(np.dot(x, self.w1) - self.theta)

    def bprop_w2(self, g, y):  # target, output
        q = (-2)*(g-y)*y*(1-y)
        return np.dot(self.h.reshape(self.hidden_dim, 1), q.reshape(1, self.input_dim))

    def bprop_w1(self, g, y, x):  # target, output, input
        q1 = (-2)*(g-y)*y*(1-y)
        q2 = np.dot(self.w2, q1)
        return np.dot(x.reshape(self.input_dim, 1), q2*self.h*(1-self.h).reshape(1, self.hidden_dim))

    def training(self, input, target):
        x = np.array(input).T
        y = self.feedforward(x)
        g = np.array(target).T

        self.w1 = self.w1 - self.lr*self.bprop_w1(x, y, x)
        self.w2 = self.w2 - self.lr*self.bprop_w2(x, y)


# Training
input_dim = 784
hidden_dim = 100
epoch = 1

ae = Autoencoder(784, 100, lr=0.1)
training_dataset_file = open("mnist_200.csv", 'r')
training_dataset_list = training_dataset_file.readlines()
training_dataset_file.close()
input_list = list()
for k in range(epoch):
    ae.lr = ae.lr * 0.8  # learning lrate decay
    for i in training_dataset_list:
        all_values = i.split(',')
        inputs = (np.asfarray(all_values[1:])/255.0*0.99)+0.01
        input_list.append(inputs)
        ae.training(inputs, inputs)

# True image (dimension = 784)
im_array = np.asfarray(input_list[1]).reshape((28, 28))

mp.imshow(im_array, cmap='Greys', interpolation='None')
output = ae.feedforward(input_list[1])
im_array = np.asfarray(output).reshape((28, 28))
mp.imshow(im_array, cmap='Greys', interpolation='None')
