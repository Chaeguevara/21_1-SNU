def func(x):
    func = x*(x-1)*(x-2)*(x-4)
    return func


def derivative_of_func(x):
    derivative_of_func = (x-1)*(x-2)*(x-4) + x*(x-2) * \
        (x-4) + x*(x-1)*(x-4) + x*(x-1)*(x-2)
    return derivative_of_func


x = -5
step = 0.01

for i in range(50):
    x = x-step*derivative_of_func(x)
    print(i, "\t: ", x, "\t: ", func(x))
