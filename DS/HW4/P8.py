"""
A sparse vector is a vector whose entries are almost all zero, like [1, 0, 0, 0, 0, 0, 3, 0, 0, 0]. 
Storing all those zeros in a list wastes memory, so programmers often use dictionaries instead 
to keep track of just the nonzero entries. For example, the vector shown earlier would be 
represented as {0:1, 6:3}, because the vector it is meant to represent has 
the value 1 at index 0 and the value 3 at index 6.

The sum of two vectors is just the element-wise sum of their elements.
For example, the sum of [1, 2, 3] and [4, 5, 6] is [5, 7, 9]. Implement a function
that takes two sparse vectors stored as dictionaries and returns a new dictionary representing their sum.

* Condition: All entries of vector are integers.


>>>P8({0:1, 6:3}, {0:2, 5:2, 6:2, 7:1})
{0:3, 5:2, 6:5, 7:1}

>>>P8({0:1, 6:3}, {0:-1, 5:2, 6:2, 7:1})
{6: 5, 5: 2, 7: 1}

>>>P8({0:1, 6:3}, {0:-1, 1:1, 2:2, 6:-3})
{1: 1, 2: 2}

>>>P8({0:1, 6:-3}, {0:-1, 6:3})
{}
"""


def P8(dct1, dct2):
    dct1_new = dct1.copy()
    dct2_new = dct2.copy()

    result = {}
    check_zero = 0
    # base case empty dict(zero vector)
    if (len(dct1_new) == 0) and (len(dct2_new) == 0):
        return result

    if (len(dct1_new) == 0):
        return dct2_new

    if (len(dct2_new) == 0):
        return dct1_new

    # iterate to construct a dictionary
    # dct1 then dct2. Try to get the value in case it already exists
    for key in dct1_new:
        result[key] = result.get(key, 0) + dct1_new[key]

    # dct2
    for key in dct2_new:
        result[key] = result.get(key, 0) + dct2_new[key]
    
    # if all values are 0, return empty

    for key in result:
        if result[key] == 0:
            check_zero +=1
    
    if check_zero == len(result):
        result = {}


    return result

print(P8({0:1, 6:-3}, {0:-1, 6:3}))