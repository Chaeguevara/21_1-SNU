def func(x):
    func = x**2
    return func

def derivative_of_func(x):
    derivative_of_func = 2*x
    return derivative_of_func

x = -5
step = 0.1

for i in range(20):
    x = x -step*derivative_of_func(x)
    print(i,"\t: ", x, "\t:", func(x))