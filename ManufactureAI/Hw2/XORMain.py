import numpy as np
import matplotlib.pyplot as plt


def sigmoid(x):
    return 1/(1+np.exp(-x))


def back_prop_w(g, y, x1):
    return (-2)*(g-y)*y*(1-y)*x1


def back_prop_theta(g, y):
    return 2*(g-y)*y*(1-y)


def feedforward(x1, x2, w1, w2, theta):
    return sigmoid(x1*w1 + x2*w2 - theta)


w1_1_1 = 0.5
w1_1_2 = 0.5
w1_2_1 = 0.5
w1_2_2 = 0.5
w2_1 = 0.5
w2_2 = 0.5

theta1 = 0.5
theta2 = 0.5
theta = 0.5

lr = 0.1
epoch = 4000
wb1_1_1 = list()
wb1_1_2 = list()
wb1_2_1 = list()
wb1_2_2 = list()
wb2_1 = list()
wb2_2 = list()

thetab1 = list()
thetab2 = list()
thetab3 = list()

loss1 = []
loss2 = []
loss3 = []
# And
# Or
# And
for i in range(epoch):
    if i % 4 == 0:
        x1 = 0
        x2 = 0
        g1 = 0
        g2 = 0
        g = 0
    elif i % 4 == 1:
        x1 = 1
        x2 = 0
        g1 = 0
        g2 = 1
        g = 1
    elif i % 4 == 2:
        x1 = 0
        x2 = 1
        g1 = 0
        g2 = 1
        g = 1
    elif i % 4 == 3:
        x1 = 1
        x2 = 1
        g1 = 1
        g2 = 1
        g = 0

    y1 = feedforward(x1, x2, w1_1_1, w1_1_2, theta1)
    y2 = feedforward(x1, x2, w1_2_1, w1_2_2, theta2)
    y = feedforward(y1, y2, w2_1, w2_2, theta)
    w1_1_1 = w1_1_1 - lr*back_prop_w(g1, y1, x1)
    w1_1_2 = w1_1_2 - lr*back_prop_w(g1, y1, x2)
    w1_2_1 = w1_2_1 - lr*back_prop_w(g2, y2, x1)
    w1_2_2 = w1_2_2 - lr*back_prop_w(g2, y2, x2)
    w2_1 = w2_1 - lr*back_prop_w(g, y, y1)
    w2_2 = w2_2 - lr*back_prop_w(g, y, y2)

    theta1 = theta1 - lr*back_prop_theta(g1, y1)
    theta2 = theta2 - lr*back_prop_theta(g2, y2)
    theta = theta - lr*back_prop_theta(g, y)

    # print("y1\t:", y1, "g1\t:", g1, "g1-y1\t:",
    #       g1-y1, "x1\t:", x1, "x2\t:", x2)
    # print("w1_1_1\t:", w1_1_1, "w1_1_2\t:", w1_1_2, "theta1\t:", theta1)
    # print("y2\t:", y2, "g2\t:", g2, "g2-y2\t:",
    #       g2-y2, "x1\t:", x1, "x2\t:", x2)
    # print("w1_2_1\t:", w1_2_1, "w1_2_2\t:", w1_2_2, "theta2\t:", theta2)
    # print("y\t:", y, "g\t:", g, "g-y\t:",
    #       g-y, "x1\t:", x1, "x2\t:", x2)
    # print("w2_1\t:", w2_1, "w2_2\t:", w2_2, "theta\t:", theta)

    # print("-------------------------------------------------")

    wb1_1_1.append(w1_1_1)
    wb1_1_2.append(w1_1_2)
    wb1_2_1.append(w1_2_1)
    wb1_2_2.append(w1_2_2)
    wb2_1.append(w2_1)
    wb2_2.append(w2_2)

    thetab1.append(theta1)
    thetab2.append(theta2)
    thetab3.append(theta)

    loss1.append((y1-g1)**2)
    loss2.append((y2-g2)**2)
    loss3.append((y-g)**2)

x = np.arange(1, epoch, 1)
# print(x)

# plt.figure(1)
# plt.plot(x, wb1_1_1[1:epoch], 'k',label="epoch vs w11")
# plt.figure(2)
# plt.plot(x, wb1_1_2[1:epoch], 'k',label="epoch vs w12")
# plt.figure(3)
# plt.plot(x, wb1_2_1[1:epoch], 'k',label="epoch vs w21")
# plt.figure(4)
# plt.plot(x, wb1_2_2[1:epoch], 'k',label="epoch vs w22")
# plt.figure(5)
# plt.plot(x, wb2_1[1:epoch], 'k',label="epoch vs w1")
# plt.figure(6)
# plt.plot(x, wb2_2[1:epoch], 'k',label="epoch vs w2")
# plt.plot(x,thetab3[1:epoch],'k',label="epoch vs theta")

# plt.ylabel('theta')
# plt.xlabel('Epoch')


# plt.show()

# plt.figure(1)
# plt.plot(x,loss1[1:epoch],'-',label ="epoch vs loss1")

# plt.figure(2)
# plt.plot(x,loss2[1:epoch],'-',label ="epoch vs loss2")

plt.figure(3)
plt.plot(x,loss3[1:epoch],'-',label ="epoch vs loss")

plt.ylabel('Loss')
plt.xlabel('Epoch')


plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
           ncol=2, mode="expand", borderaxespad=0.)

plt.show()