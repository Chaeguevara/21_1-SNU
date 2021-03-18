"""
Practical programming Chapter 8 Exercise 10

**Instruction**
Inputs are a nested list having two lists. 
Complete P7 function that returns a list whose elements are as following:
- the list has 2 items
- the first item is the first item of the first inner list of input
- the second item is the last item of the second inner list of input

P7([['km','miles','league'],['kg','pound','stone']])
>>> ['km','stone']

P7([[0,1,2,3],[4,5,6]])
>>> [0,6]

P7([[0,0,0],[1]])
>>> [0,1]
"""


def P7(nested_list: list) -> list:
    ##### Modify code Here #####
    # Assert input as a nested list having two lists(not empty)
    assert (len(nested_list) == 2) and (len(nested_list[0]) != 0) and (
        len(nested_list[1]) != 0), 'Input is not valid'

    # Loop or direct access of the item. Here, I'll go with loop
    # access lists in list
    for i in range(2):
        # access elements in list
        if i == 0:
            nested_list[i] = nested_list[i][0]
        elif i == 1:
            nested_list[i] = nested_list[i][-1]

    return nested_list
    ##### End of your code #####
