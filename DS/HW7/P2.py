def P2(lst):
    """
    two tasks
    prerequistes: length of string is 1~20(including 1,20)
    all strings are lowercase w/o space
    1. create a dictionary. key = string length, value: list of strings
    2. for a key, if there are several values, sort them.
    3. from the smaller key, add values one by one to new list 
    """
    new_list = []
    length_word_dictionary ={}

    #create a dictionary. length : [word list]
    for word in lst:
        length_word_dictionary.setdefault(len(word),[])
        length_word_dictionary[len(word)].append(word)

    #sort the [word list].
    for key_set in length_word_dictionary:
        length_word_dictionary[key_set].sort()


    #now loop with sorted key
    sorted_key = sorted(length_word_dictionary.keys())

    # add one by one to new list
    for key in sorted_key:
        for item in length_word_dictionary[key]:
            new_list.append(item)
    
    
    return new_list
