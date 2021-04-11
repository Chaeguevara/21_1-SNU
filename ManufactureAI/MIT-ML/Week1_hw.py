import numpy as np
def signed_dist(x,th,th0):
    theta_length = np.linalg.norm(th)
    theta_x = np.dot(th.T,x)

    return (theta_x + th0)/theta_length
#solution
# x is dimension d by 1
# th is dimension d by 1
# th0 is a scalar
# return 1 by 1 matrix of signed distance
def signed_dist_sol(x, th, th0):
   return ((th.T@x) + th0) / np.linalg.norm(th)


x = np.array([[0,0,0]]).T
th = np.array([[3,4,5]]).T
th0 = -1


print(signed_dist(x,th,th0))

import numpy as np
def positive(x, th, th0):
    f = th.T@x + th0
    length = np.linalg.norm(f)
    if length == 0:
        return np.array([[0]])
    f = f/length
    return f

#solution
# x is dimension d by 1
# th is dimension d by 1
# th0 is dimension 1 by 1
# return 1 by 1 matrix of +1, 0, -1
def positive_sol(x, th, th0):
   return np.sign(np.dot(np.transpose(th), x) + th0)
