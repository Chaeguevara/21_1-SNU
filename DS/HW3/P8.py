"""
Practical programming Chapter 9 Exercise 8

**Instruction**
You are given two lists, rat_1 and rat_2, that contain the daily weights of
two rats over a period of ten days. Assume the rats never have exactly
the same weight. 
Complete P8 function to return True if the weight of rat 1 is greater than rat2 on day n,
return False if the weight of rat 1 is less than rat2 on day n.
Assume 1 <= n <= 10

rat_1 = [5, 6, 7, 6, 7, 8, 10, 9, 8, 10]
rat_2 = [7, 8, 6, 7, 8, 10, 9, 8, 10, 11]

P8(rat_1, rat_2, 1)
>>> False

P8(rat_1, rat_2, 5)
>>> False

P8(rat_1, rat_2, 3)
>>> True
"""


def P8(rat_1: list, rat_2: list, measure_day: int) -> bool:
    ##### Modify code Here #####

    # Initialize result
    result = False
    index = measure_day-1

    # compare item at index
    if(rat_1[index] > rat_2[index]):
        result = True

    return result
    ##### End of your code #####
