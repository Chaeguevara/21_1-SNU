import numpy as np
import matplotlib.pyplot as plt

# Define the plot format 1.9700000e+03 -> 1970.00
float_formatter = "{:.2f}".format
np.set_printoptions(formatter={'float_kind': float_formatter})

#import data
cancer_data = np.genfromtxt('cancer.csv', delimiter=',', dtype="U75")

# Preprocessing
# Drop first column
cancer_data = np.delete(cancer_data, 0, 1)

# process age. Original data is 0-4,5-9 something like
# turn 0-4 -> 2


def processAge(x):
    new_x = x.copy()
    for i, age in np.ndenumerate(new_x):
        new_age = age.split('-')
        if(len(new_age) == 2):
            new_x[i] = (int(new_age[0]) + int(new_age[1])) / 2
        else:
            new_x[i] = new_age[0]
    return new_x

def softmax(x):
    return np.exp(x)/np.sum(np.exp(x))

# print(cancer_data)
x = cancer_data[0]
y = cancer_data[1]
x = processAge(x)

# type cast
x = x.astype(np.float)
y = y.astype(np.float)

# normalize y
x = x/np.max(x)
y = y/np.max(y)
# y = softmax(y)
print(x)

#logisticRegression
def logisticRegression(x, y, m, b, alpha):
    der_CE_over_m, der_CE_over_b = 1, 1
    #stop when both slope is almost flat
    i = 1
    while(abs(der_CE_over_b) >= 0.001) and (abs(der_CE_over_m) >= 0.001):
        logi_Reg = 1/(1+np.exp(m*x+b))
        print(logi_Reg)
        CE_loss = -np.sum(y*np.log(logi_Reg)+(1-y)*np.log(1-logi_Reg))/len(x)
        der_CE_over_m = np.sum(
            -x*(logi_Reg-y)
        ) / len(x)
        der_CE_over_b = np.sum(
            -(logi_Reg-y)
        ) / len(x)
        # by GDA
        m = m - alpha*der_CE_over_m
        b = b - alpha*der_CE_over_b
        print("CE_loss:",CE_loss,"\tm:",m,"\tb",b, "\tDER_M",der_CE_over_m,"\tDER_b",der_CE_over_b,"\tIteration",i)
        i +=1
    return m,b

m,b = logisticRegression(x,y,-15,-1,0.005)

plt.plot(x, y, 'bo')
plt.plot(x, 1/(1+np.exp(m*x+b)),'k--')
plt.ylabel('Liver cancer rate')
plt.xlabel('Age')
plt.legend(['AGE vs Liver cancer rate'])
plt.grid()
plt.show()