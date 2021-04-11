import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_deriv(x):
    return sigmoid(x) * (1-sigmoid(x))

def forward(x,w1,w2,predict = False):
    
    a = np.matmul(x,w1)
    z = sigmoid(a)
    bias = np.ones((len(z),1))
    z = np.concatenate((bias, z), axis = 1)
    a_ = np.matmul(z, w2)
    z_ = sigmoid(a_)

    if predict:
        return z_
    return a, z, a_, z_

def backward(a_, z0, z, z_, y):

    delta_ = z_ - y
    Delta_ = np.matmul(z.T, delta_)
    delta = (delta_.dot(w2[1:,:].T)) * sigmoid_deriv(a)
    Delta = np.matmul(z0.T, delta)

    return delta_, Delta, Delta_

# Training Data 
x = np.array([[1,1,0],[1,0,1],[1,0,0],[1,1,1]])
y = np.array([[1],[1],[0],[0]])
learningrate = 0.01
epoch = 15000
costs = []
m = len(x)

# weights
w1 = np.random.randn(3,5)
w2 = np.random.randn(6,1)


# Train Model
for i in range(epoch):

    a, z, a_, z_ = forward(x,w1,w2)
    delta_, Delta, Delta_ = backward(a_, x, z, z_, y)
    w1 = w1 - (learningrate * (1/m) * Delta)
    w2 = w2 - (learningrate * (1/m) * Delta_)

    addcost_ = np.mean(np.abs(delta_))
    costs.append(addcost_)

    if i % 1000 == 0:
        print(f"Iteration: {i}, Error: {addcost_}")

# Test
z__ = forward(x, w1, w2, True)
print ("Percentage: ")
print (z__)
print ("Prediction: ")
print (np.round(z__))

# Plot Model

plt.figure()
plt.title("Cost Plot of the 2-Layer Perceptron Network for the XOR Gate")
x_axis = np.arange(0, epoch, 1)
plt.plot(x_axis, costs)
plt.xlabel("epoch")
plt.ylabel("costs")
plt.show()