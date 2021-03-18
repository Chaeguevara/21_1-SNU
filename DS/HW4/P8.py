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

    
    return