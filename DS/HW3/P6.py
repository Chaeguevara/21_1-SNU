"""
Practical programming Chapter 8 Exercise 4

**Instruction**
Complete P6 function that changes input list as following
a. Remove 3382 from the list.
b. Extend the list by adding [5566, 1830] to it.
c. Sort the list in ascending order.
Assume 3382 is always included in the input list and each element of input list is always number.
Assume there is only one 3382 in the input list.

P6([4353, 2314, 2956, 3382, 9362, 3900])
>>> [1830, 2314, 2956, 3900, 4353, 5566, 9362]
"""
from typing import List
def P6(num_list: List[float]) -> List[float]: 
    ##### Modify code Here #####
    add_list = [5566,1830]

    #Remove 3382
    num_list.remove(3382)

    #Add [5566,1830]
    num_list += add_list

    #Sort
    num_list.sort()

    return num_list
    ##### End of your code #####