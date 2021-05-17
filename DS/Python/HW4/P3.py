"""
Implement a function that takes a dictionary as an argument
and returns the number of values that appear two or more times.

* Condition: All values are hashable.


>>>P3({'red': 1, 'green': 1, 'blue': 2})
1

>>>P3({'r': 'a', 'g': 'b', 'b': 'c'})
0

>>>P3(dict())
0

>>>P3({'a':True, 'b': True, 'c':2, 'd':2})
2
"""

def P3(dct):
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

    #calcualte the length of 'value_list' and 'unique set' length
    l_length = len(value_list)
    s_length = len(unique_set)
    # if the set of lenth is same, return 0
    if l_length == s_length:
        return result
    
    # delete the each value once, if the value was duplicated it will still remain
    for unique in unique_set:
        if unique in value_list:
            value_list.remove(unique)
            pass

    # get the lenght of new set
    result = len(set(value_list))

    return result

