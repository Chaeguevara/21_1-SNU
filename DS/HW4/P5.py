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
    new_dct1 = dct1.copy()
    new_dct2 = dct2.copy()
    result = {}
    #Base case if one of the dictionary is empty, return empty
    if (len(new_dct1) == 0) or (len(new_dct2) == 0):
        return result
    #Get the keys and turn into set
    key_set1 = set(new_dct1.keys())
    key_set2 = set(new_dct2.keys())

    #intersect keys
    key_intersect = key_set1.intersection(key_set2)

    #if the length of intersect == 0, return empty
    if len(key_intersect) == 0:
        return result
    #check the values and add to result
    for key in key_intersect:
        if (new_dct1[key]) == (new_dct2[key]):
            result[key] = new_dct1[key]

    return result

print(P5({'a': 1, 'b':True, 'c':[1,2]}, {'a':1, 'b':123, 'c':[1,2]}))
    