import numpy as np
import numpy.random as nr
import random

#Mentos machine
hidden_param = [0.5, -0.5]

#Agent
actions = [0,1]
policy = [0.5, 0.5]
Q = [0.5,0.5]
learning_rate = 0.1
total_episode = 1
epsilon = 0.1
num_exploit = 0
num_explore = 0

def rewardMentos(arg):
    res = np.random.randn()

    print("res: ", res, ", marm: ", arg)

    if res>arg:
        return 1
    else:
        return 0

for i in range(total_episode):
    if nr.rand() < epsilon: #Exploration
        a = random.randrange(0,len(actions))
        num_explore += 1
        print("Exploration choise is ", a)
    else: #Exploitation
        a = np.argmax(policy)
        num_exploit +=1
        print("Exploitation choice is ", a)
    
    reward = rewardMentos(hidden_param[a])

    print("reward is ", reward)

    Q[a] = Q[a] + learning_rate * (reward - Q[a])

    policy[0] = Q[0] / (Q[0] + Q[1])
    policy[1] = Q[1] / (Q[0] + Q[1])

    print("Q[0], Q[1] = ", Q[0]," : ", Q[1])
    print("p[0], p[1] = ", policy[0], " : ", policy[1])
    print("<=============================================>")
print("num_exploit: ",num_exploit," , ","num_explore: ",num_explore)