"""
Implement a function that takes a list of integers as its input argument 
and returns a set of those integers occurring two or more times in the list.


>>>P1([1,2,3,1])
{1}

>>>P1([1,2,3,4])
set()

>>>P1([])
set()

>>> P1([1,2,3,1,4,2])
set({1,2})
"""


def P1(lst):
    new_list = lst.copy()
    lst_to_set = set(lst)  
    # check if item is duplicated by comparing length
    l_length = len(lst)
    s_length = len(lst_to_set)
    if l_length == s_length:
        return set()

    # Delete duplicated item 
    for unique in lst_to_set:
        if unique in new_list:
            new_list.remove(unique)
            pass

    #turn new_list into set
    result = set(new_list)

    return result
