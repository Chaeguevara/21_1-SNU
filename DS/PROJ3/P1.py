def P1(nums, k):
    '''
    nums: list, k: int
    '''
    '''
    Key idea : get modulus
    construct modulo : length dict
    if key == 0, check whether it's even or not
    else
    check a key and other key which makes a dividable by sum
    and compare length
    '''
    modulo_dict = {}
    # n
    for item in nums:
        modulo_dict.setdefault(item % k, 0)
        modulo_dict[item % k] +=1

    print(modulo_dict)
    #base case
    if k == 2:
        if (modulo_dict[0] % 2 == 0) and (modulo_dict[1] % 2 == 0):
            return True
    # n
    for keys in modulo_dict:
        # do for half
        if keys <= k/2:
            # base case when key == 0
            if (keys == 0) and not (modulo_dict[keys] % 2 == 0):
                return False
            # base case when key == k / 2
            if (keys == k / 2) and not (modulo_dict[keys] % 2 == 0):
                return False
            # get the length of opposite key
            opp_key_length = modulo_dict.get(k-keys, 0)
            if modulo_dict.keys != opp_key_length:
                return False
        else:
            break
    return True
