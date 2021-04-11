import numpy as np
def length(col_v):
    result = 0
    result = np.sum(np.power(col_v,2))
    result = np.sqrt(result)
    return result
l = [[1],[2],[3],[4],[5],[6],[1],[2],[9]]
print(length(l))

def normalize(col_v):
    result = np.divide(col_v,length(col_v))
    return result

print(normalize(l))
