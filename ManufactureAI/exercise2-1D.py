def func(x):
    temp = (4 - x **2)
    return temp*temp

def derivative_of_func(x):
    derivative_of_func = 4*(x**3) -16*x
    return derivative_of_func

x = 1
step = 0.01

for i in range(50):
    x = x - step*derivative_of_func(x)
    print(i,"\t: ",x,"\t: ",func(x))