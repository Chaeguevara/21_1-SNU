"""
Practical programming Chapter 9 Exercise 11

**Instruction**
Inputs are two integers start_i, end_i. (start_i < end_i)
This function sums all integers between start_i and end_i(both inclusive), 
then calculate average of these integers using loop.
Complete P4 function. 

P4(2, 22)
>>> 12

P4(0, 100)
>>> 50

"""

def P4(start_i: int, end_i: int) -> float:
    ##### Write your Code Here #####
    
    #Intialize parameter
    result = 0
    divider = end_i - start_i + 1

    #1. Add all the integers to result
    for i in range(start_i,end_i+1):
        result += i

    #Calculate the average
    result /= divider

    return result
    ##### End of your code #####
