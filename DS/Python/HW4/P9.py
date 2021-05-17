"""
Same explanation with P8 (sparse vector)

The dot product of two vectors is the sum of the products of corresponding elements.
For example, the dot product of [1, 2, 3] and [4, 5, 6] is 4+10+18 = 32.
Implement another function that calculates the dot product of two sparse vectors.


>>>P9({0:1, 6:3}, {0:2, 5:2, 6:2, 7:1})
8

>>>P9({0:1, 6:3}, {1:-1, 2:2, 3:2, 4:1})
0

>>>P9({0:1, 6:-3}, {0:-1, 6:3})
-10
"""


def P9(dct1, dct2):
    dct1_new = dct1.copy()
    dct2_new = dct2.copy()

    result = 0
    # base case empty dict(zero vector)
    if (len(dct1_new) == 0) and (len(dct2_new) == 0):
        return result

    if (len(dct1_new) == 0):
        return dct2_new

    if (len(dct2_new) == 0):
        return dct1_new

    # iterate try to find the value from dct1 with the key of dct2
    # In this case, use dict.get(key,0) so that if the key doesn't exist, the product value becomes 0
    for key in dct2_new:
        result += dct1_new.get(key, 0) * dct2_new[key]



    return result