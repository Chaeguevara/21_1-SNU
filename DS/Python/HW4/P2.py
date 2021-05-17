"""
Implement a function that takes a single dictionary as an argument
and returns the number of distinct values it contains.

* Condition: All values are hashable.


>>>P2({'red': 1, 'green': 1, 'blue': 2})
2

>>>P2({(1,2): 'a', 'g': 3, 1: True})
3

>>>P2(dict())
0

>>>P2({'a':True, 'b': True, 'c':True})
1
"""


def P2(dct):
    result = 0
    new_dct = dct.copy()
    value_list = []
    #base case: if dictionary length = 0, return 0
    if len(new_dct) == 0:
        return result
    # extract values of dictionary and put them into list
    for key in new_dct:
        value_list.append(new_dct[key])
    #convert set
    unique_set = set(value_list)    
    #return length of set
    result = len(unique_set)

    return result
