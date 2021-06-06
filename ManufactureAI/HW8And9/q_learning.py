import numpy as np
import numpy.random as nr
import random

total_episode = 50
learning_rate = 0.1
total_reward = 0
epsilon = 0.1

#MAP : HHFFFSFFG
Q = np.ones([7,2]) #7*2형태, value = 1 인 행렬
goal_pos = 6
hole_pos = 0
actions =[0,1] # 0또는 1 의 액션
movement = [-1 , 1]
policy = [0.5, 0.5]
discount_factor = 0.9

POLICY_GREEDY = 1
POILICY_SAMPLING = 2
default_policy = POLICY_GREEDY #Greedy방식 사용
num_sampling = 0
num_exploit = 0
num_explore = 0

def hidden_reward(pos):
    if pos == goal_pos:
        return 1
    if pos == hole_pos:
        return -1
    else:
        return 0
    
for i in range(total_episode):
    curr_pos = 3
    print("-------------- Restart of the game --------------")
    for j in range(50):
        policy[0] = Q[curr_pos][0]/(Q[curr_pos][0]+Q[curr_pos][1])
        policy[1] = Q[curr_pos][1]/(Q[curr_pos][0]+Q[curr_pos][1])
    
        if default_policy == POLICY_GREEDY: #Epsilon greedy
            if nr.rand() < epsilon: #Exploration (Random movement)
                a = random.randrange(0, len(actions))
                num_explore +=1
                print("Exploration choice in Epsilon greedy is ", a)
            else: #Exploitation
                a = np.argmax(policy)
                num_exploit += 1
                print("Exploitation choice in Epsilon greedy is ", a)
        else:
            if nr.rand() < epsilon: #Exploration(Random movement)
                a = random.randrange(0,len(actions))
                num_explore +=1
                print("Exploration choice in Epsilon sampling is ", a)
            else: #sampling
                a = np.random.choice(actions,p=policy)
                num_sampling +=1
                print("Sampling choice in Epsilon sampling is ", a)
        print("Current pos is", curr_pos, ". Selected action is", movement[a])

        next_pos = curr_pos + movement[a]
        print("Now, our agent is at ",next_pos)

        reward = hidden_reward(next_pos)
        print("True reward of the action ", a, " is ", reward)

        np.maximum(Q[next_pos][0], Q[next_pos][1])

        Q[curr_pos][a]  = Q[curr_pos][a] + learning_rate * (reward + discount_factor * \
            np.maximum(Q[next_pos][0], Q[next_pos][1])-Q[curr_pos, a])
        print("Updated Q[curr_pos][a] is ", Q[curr_pos][a])
        print(Q)

        curr_pos = next_pos

        if reward == -1:
            break
        if reward == 1:
            total_reward += reward
            break

print("Total success ratio is ", (total_reward/total_episode))
print("num_sampling: ", num_sampling," , ","num_exploit: ", num_exploit," , ","num_explore: ",num_explore)