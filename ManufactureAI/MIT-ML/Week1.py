# Provide an expression that sets A to be a 2*3 numpy array (2 rows by 3 columns), containing any values you wish.
import numpy as np

A = np.zeros((2,3))
B = np.array([[1,2,3],[4,5,6]])
print(A)
print(B)

#Transpose
def tp(A):
    return A.T

print(tp(B))

#list to row Row vector
def rv(value_list):
    return np.array([value_list])

print(rv([1,2,3,4,5,6]))

# Column vector. By using rv
def cv(value_list):
    return np.transpose(rv(value_list))

print (cv([1,2,3,4,5,6,7,8]))

# Vector's Euclidean length. W/O loop
def length(col_v):
    result = 0
    # sum and power
    result = np.sum(np.power(col_v,2))
    # root
    result = np.sqrt(result)
    return result

print (length([1,1,1,1,1,-1,4,4,3,5,9]))

#Normalize. No loop. use length() procedure
def normalize(col_v):
    result = np.divide(col_v,length(col_v))
    return result

print (normalize([1,2,3,4,4,3,3,7]))

# indexing 
# Last column A[:,-1]
# splice and preserve the dimension? -> A[:,-1:]
def index_final_col(A):

    return A[:,-1:]


print(index_final_col(B))

data = [['Weight', 'height'],[150,5.8],[130,5.5],[120,5.3]] #your code here
data = np.array(data)
print(data)

#list to array