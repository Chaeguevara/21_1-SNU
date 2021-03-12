import random

def func(x):
    func = x*(x-1)*(x-2)*(x-4)
    return func

local_minima_y = 100000
local_minima_x = 100000
range_max = 10
center_num = 5

for i in range(100):
    s = range_max*random.uniform(0,1) - center_num

    if local_minima_y > func(s):
        local_minima_y = func(s)
        local_minima_x = s
        print(i, "\t: ", s,"\t: ", local_minima_y)