
import numpy as np
import matplotlib.pyplot as plt

# Define the plot format 1.9700000e+03 -> 1970.00
float_formatter = "{:.2f}".format
np.set_printoptions(formatter={'float_kind':float_formatter})

#import data
air_data = np.genfromtxt('ManufactureAI/Hw1/air_passenger.csv',delimiter=',' )
electricity_data = np.genfromtxt('ManufactureAI/Hw1/Electricity.csv',delimiter=',')
GDP_data = np.genfromtxt('ManufactureAI/Hw1/GDP.csv',delimiter=',')
print(air_data)
print(electricity_data)

#Preprocessing
# if '-' -> nan
x = np.arange(1,11)
print(x)

#plot data
plt.title("Air Vs GDP")