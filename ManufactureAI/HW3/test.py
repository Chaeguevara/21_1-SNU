import numpy as np
import matplotlib.pyplot as plot

input_dim = 10
hidden_dim = 2

w1 =  np.random.normal(0.0, pow(input_dim, -0.5), (input_dim, hidden_dim))
print(w1)