"""
Practical programming Chapter 9 Exercise 12

**Instruction**
When P5([1, 2, 3, -3, 6, -1, -3, 1]) is executed, it produces [1, 2, 3, 6, -3, 1].
The for loop traverses the elements of the list, and when a negative value
(like -3 at position 3) is reached, it is removed, shifting the subsequent
values one position earlier in the list (so 6 moves into position 3). The
loop then continues on to process the next item, skipping over the value
that moved into the removed item’s position. If there are two negative
numbers in a row (like -1 and -3), then the second one won’t be removed.
Rewrite the code to avoid this problem.
Assume each element of input list is always number.

Remove the negative numbers from the list num_list.
>>> numbers = [-5, 1, -3, 2]
>>> P5(numbers)
>>> numbers
[1, 2]
  
"""
from typing import List
def P5(num_list: List[float]) -> List[float]:
    ##### Modify code Here #####
    #iterate over copied list
    test = num_list.copy()
    for item in test:
      if item < 0:
        num_list.remove(item)
    return num_list
    ##### End of your code #####

print(P5([1,2,3,-3,6,-1,-3,1]))
print(P5([-5, 1, -3, 2]))