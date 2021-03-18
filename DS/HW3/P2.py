"""
Practical programming Chapter 8 Exercise 8

**Instruction**
Return True if and only if the length of L1 is longer than the length of L2.
Assume inputs are always 2 lists(No input validity check is necessary)
>>> P2([1, 2, 3], [4, 5])
True
>>> P2(['abcdef'], ['ab', 'cd', 'ef'])
False
>>> P2(['a', 'b', 'c'], [1, 2, 3]
False

Complete P2 function
"""

def P2(L1: list, L2: list) -> bool:
    ##### Write your Code Here #####
    #Initialize parameter
    length1 = len(L1)
    length2 = len(L2)
    result = False

    #Compare length and 
    if length1 > length2:
        result = True


  
    return result
    ##### End of your code #####

