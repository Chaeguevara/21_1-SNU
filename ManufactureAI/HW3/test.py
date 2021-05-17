import numpy as np
import matplotlib.pyplot as plot

input_dim = 10
hidden_dim = 21

w1 =  np.random.normal(0.0, pow(input_dim, -0.5), (input_dim, hidden_dim))
print(w1)
h = np.zeros((1,hidden_dim))
print(h)