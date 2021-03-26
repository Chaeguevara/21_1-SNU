
import numpy as np
import matplotlib.pyplot as plt

# Define the plot format 1.9700000e+03 -> 1970.00
float_formatter = "{:.2f}".format
np.set_printoptions(formatter={'float_kind': float_formatter})

#import data
electricity_data = np.genfromtxt('Electricity.csv', delimiter=',')
GDP_data = np.genfromtxt('GDP.csv', delimiter=',')

# Preprocessing
# Drop first column
GDP_data = np.delete(GDP_data, 0, 1)
electricity_data = np.delete(electricity_data, 0, 1)


def matchYear(normList, otherList):
    """
    Match the year records and return matched data.
    Either normList or otherList can be shortened as result

    return : two numpy array in a tuple
    """
    norm = normList.copy()
    other = otherList.copy()
    result1 = []
    result2 = []
    norm_years = set(norm[0].flatten())
    other_years = set(other[0].flatten())

    # common years
    years = norm_years.intersection(other_years)
    years = sorted(list(years))

    # select common years from np array
    for year in years:
        for j, other_year in np.ndenumerate(other[0]):
            if year == other_year:
                result2.append(other[:, j[0]])
                break
        for k, norm_year in np.ndenumerate(norm[0]):
            if year == norm_year:
                result1.append(norm[:, k[0]])
                break
    # for i,year in np.ndenumerate(norm[0]):
    #     for j,other_year in np.ndenumerate(other[0]):
    #         if year == other_year:
    #             result.append(other[:,j[0]])
    #             break
    # result = np.transpose(result)
    # concantenate list
    result1 = np.transpose(result1)
    result2 = np.transpose(result2)
    return result1, result2


matched_elect, matched_GDP = matchYear(electricity_data, GDP_data)
# print(matched_elect)
# print(matched_GDP)

# get the X and Y for LR

x = matched_GDP[1, :]
y = matched_elect[1, :]
# normalize x
x = x/(np.max(x))

print(type(x))
# print(x)
# print(y)
"""
preprocessing finished
"""

"""
Data visualization
"""

# construct scatter chart
# plt.plot(x,y,'bo')
# plt.ylabel('Electricity consumption(kwh per capita')
# plt.xlabel('GDP')
# plt.legend(['GDP vs Electricity'])
# plt.grid()
# plt.show()

# LR


def linearRegresssionAffine(x, y, w, alpha, b):
    """
    x,y: numpy array
    w = initial slope, float
    alpha = step, int
    """
    # stop when slope is almost flat
    derivative = 1
    delta_w, delta_b = 0, 0
    i = 0
    der_b = 1
    while((abs(derivative) > 0.01) and (abs(der_b) > 0.01)):
        # print w and loss, iteration
        second_der = np.sum(x**2)
        second_der_b = 1*len(x)
        w_old = w
        b_old = b
        i += 1
        derivative = np.sum(x*(w*x+b-y))
        loss = np.sum((w*x+b-y)**2)/(2*len(x))
        der_b = np.sum(w*x+b-y)
        print(w, b, loss, i)
        w = w - alpha*(derivative+second_der*delta_w/2)/len(x)
        b = b - alpha*(der_b+second_der_b*delta_b/2)/len(x)
        delta_w = w - w_old
        delta_b = b-b_old
    return w, b

# def linearRegresssionAffine(x, y, w, alpha, b):
#     """
#     x,y: numpy array
#     w = initial slope, float
#     alpha = step, int
#     """
#     # stop when slope is almost flat
#     derivative = 1
#     delta_w, delta_b = 0, 0
#     i = 0
#     der_b = 1
#     u = 0.9
#     while((abs(derivative) > 0.01) and (abs(der_b) > 0.01)):
#         # print w and loss, iteration
#         second_der = np.sum(x**2)
#         second_der_b = 1*len(x)
#         w_old = w
#         b_old = b
#         i += 1
#         derivative = np.sum(x*(w*x+b-y))
#         loss = np.sum((w*x+b-y)**2)/(2*len(x))
#         der_b = np.sum(w*x+b-y)
#         print(w, b, loss, i)
#         w = w - alpha*derivative+u*delta_w
#         w /= len(x)
#         b = b - alpha*der_b+u*delta_b
#         w /= len(x)
#         delta_w = w - w_old
#         delta_b = b-b_old
#     return w, b

# plot linear fit
# plt.plot(x, y, 'bo')
# plt.plot(x, slope*x, '-')
# plt.ylabel('Electricity consumption(kwh per capita')
# plt.xlabel('GDP')
# plt.legend(['GDP vs Electricity'])
# plt.grid()
# plt.show()
# Affine function regression
new_slope, b = linearRegresssionAffine(x, y, 1, 0.05, 1)

# visualize
plt.plot(x, y, 'bo', label='GDP vs Elec Consumption')
plt.plot(x, new_slope*x+b, '-', label='Affine Function Regression')
plt.ylabel('Electricity consumption(kwh per capita')
plt.xlabel('GDP')

plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
           ncol=2, mode="expand", borderaxespad=0.)
plt.grid()
plt.show()
