"""
Implement a function that takes two dictionaries as arguments
and returns a dictionary that contains only the key/value pairs found in both
of the original dictionaries.


>>>P5({'a': 1, 'b':True, 'c':[1,2]}, {'a':1, 'b':123, 'c':[1,2]})
{'a': 1, 'c': [1, 2]}

>>>P5({'a': 1, 'b':True }, {'c':1, 'd':123, 'e':[1,2]})
{}

>>>P5({}, {'c':1, 'd':123, 'e':[1,2]})
{}

"""
def P5(dct1, dct2):

    return