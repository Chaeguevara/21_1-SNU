def P4(nums):
    '''
    nums: list
    '''
    # n
    num_set = set(nums)

    # n dictionary
    num_dict = {}
    for items in nums:
        # in case same value twice
        num_dict.setdefault(items, 1)
    biggest = 0
    sub_sum = 1

    for key in num_dict.keys():
        left_key = key
        right_key = key
        if num_dict.get(key, -1) == 1:
            num_dict[key] = 0
            while num_dict.get(left_key-1, -1) == 1:
                left_key -= 1
                num_dict[left_key] = 0
                sub_sum += 1
            while num_dict.get(right_key+1, -1) == 1:
                right_key += 1
                num_dict[right_key] = 0
                sub_sum += 1
            if sub_sum > biggest:
                biggest = sub_sum
        else:
            sub_sum = 1

    return biggest

