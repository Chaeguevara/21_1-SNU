"""
A balanced color is one whose red, green, and blue values add up to 1.0. 
Implement a function that takes a dictionary whose keys are 'R', 'G', and 'B' 
and whose values are between 0 and 1 as input and that returns True 
if they represent a balanced color.


>>>P4({'R': 0.2, 'G': 0.3, 'B': 0.5})
True

>>>P4({'R': 0.2, 'G': 0.3, 'B': 0.6})
False

>>>P4({'R': 0.1, 'G': 0.1, 'B': 0.1})
False
"""


def P4(dct):
    result = False
    value_sum = 0
    # sum value
    for key in dct:
        value_sum += dct[key]
    
    # check
    if value_sum == 1:
        result = True
    return result
