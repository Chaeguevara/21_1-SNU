"""
Practical programming Chapter 9 Exercise 9

**Instruction**
You are given two integers, start_i and end_i(start_i < end_i)
Complete P10 function to return a list that contains all integers in the range start_i to end_i(inclusive)
in ascending order

P10(33, 49)
>>> [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]

P10(-10, -7)
>>> [-10, -9, -8, -7]

P10(10, 11)
>>> [10, 11]
"""


def P10(start_i: int, end_i: int) -> list:
    ##### Modify code Here #####
    # Initilize output
    result = []

    for i in range(start_i,end_i +1):
        result.append(i)
    return result
    ##### End of your code #####